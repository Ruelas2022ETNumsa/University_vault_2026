@echo off
REM ============================================================
REM  tomar_muestra.bat  (Windows 10)
REM  Hace ping a los enlaces listados en ..\web\enlaces.txt
REM  y guarda en muestras_temp.txt.
REM
REM  Programado por Task Scheduler cada 5 minutos.
REM
REM  Pingea uno por uno (secuencial) usando Test-Connection
REM  de PowerShell. Tiempo total aproximado: 20 segundos.
REM ============================================================

setlocal enabledelayedexpansion

REM ── Directorio donde vive este script ────────────────────────
set "DIR=%~dp0"
if "%DIR:~-1%"=="\" set "DIR=%DIR:~0,-1%"
set "ARCHIVO_TXT=%DIR%\muestras_temp.txt"
set "ARCHIVO_RTT=%DIR%\_rtt_tmp.txt"

REM ── Buscar enlaces.txt (misma fuente que la web) ─────────────
REM    Primero la copia "viva" en IIS (si la web esta instalada),
REM    sino la copia del proyecto.
set "ARCHIVO_ENLACES=C:\inetpub\wwwroot\monitoreo\enlaces.txt"
if not exist "%ARCHIVO_ENLACES%" set "ARCHIVO_ENLACES=%DIR%\..\web\enlaces.txt"
if not exist "%ARCHIVO_ENLACES%" exit /b 1

REM ── Fecha y hora (usa PowerShell, mas confiable que wmic) ────
for /f "delims=" %%D in ('powershell -NoProfile -Command "Get-Date -Format 'yyyy-MM-dd'"') do set "FECHA=%%D"
for /f "delims=" %%H in ('powershell -NoProfile -Command "Get-Date -Format 'HH:mm:ss'"') do set "HORA=%%H"

REM ── Leer cada linea de enlaces.txt y hacer ping ──────────────
REM    eol=# ignora lineas de comentario que empiecen con #
for /f "usebackq tokens=* eol=#" %%E in ("%ARCHIVO_ENLACES%") do (
    if not "%%E"=="" (
        set "RTT_MAX=-1"

        REM Borrar archivo temporal previo si existe
        if exist "!ARCHIVO_RTT!" del "!ARCHIVO_RTT!" 2>nul

        REM Test-Connection envia 5 paquetes ICMP y devuelve el RTT maximo.
        REM Si todos fallan -> -1. Salida redirigida a archivo temporal,
        REM lo cual es mas confiable que "for /f" con pipes anidados.
        powershell -NoProfile -ExecutionPolicy Bypass -Command "try { $r = Test-Connection -ComputerName '%%E' -Count 5 -ErrorAction Stop; ($r | Measure-Object -Property ResponseTime -Maximum).Maximum } catch { -1 }" > "!ARCHIVO_RTT!" 2>nul

        REM Leer el archivo temporal (linea unica con el numero)
        if exist "!ARCHIVO_RTT!" (
            set /p RTT_MAX=<"!ARCHIVO_RTT!"
            for /f "tokens=* delims= " %%T in ("!RTT_MAX!") do set "RTT_MAX=%%T"
        )
        if "!RTT_MAX!"=="" set "RTT_MAX=-1"

        REM Escribir linea en archivo de muestras: FECHA|HORA|ENLACE|RTT_MAX
        echo !FECHA!^|!HORA!^|%%E^|!RTT_MAX!>> "%ARCHIVO_TXT%"
    )
)

REM Limpiar archivo temporal
if exist "!ARCHIVO_RTT!" del "!ARCHIVO_RTT!" 2>nul

endlocal
exit /b 0
