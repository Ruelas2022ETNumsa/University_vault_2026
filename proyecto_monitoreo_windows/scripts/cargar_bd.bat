@echo off
REM ============================================================
REM  cargar_bd.bat  (Windows 10)
REM  Lee muestras_temp.txt e inserta los datos en MySQL
REM  Programado por Task Scheduler cada 1 hora (~12 muestras)
REM ============================================================

setlocal enabledelayedexpansion

set "DIR=%~dp0"
if "%DIR:~-1%"=="\" set "DIR=%DIR:~0,-1%"
set "ARCHIVO_TXT=%DIR%\muestras_temp.txt"
set "ARCHIVO_PROC=%DIR%\muestras_procesadas.txt"

REM ── Credenciales de la base de datos ────────────────────────
set "DB_USER=root"
set "DB_PASS=Mamacita.com921"
set "DB_NAME=monitoreo_red"

REM ── Ruta al cliente mysql.exe ───────────────────────────────
set "MYSQL_BIN=C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe"
if not exist "%MYSQL_BIN%" set "MYSQL_BIN=C:\mariadb\bin\mysql.exe"
if not exist "%MYSQL_BIN%" set "MYSQL_BIN=mysql.exe"

REM ── Verificar que el archivo de muestras existe ─────────────
if not exist "%ARCHIVO_TXT%" exit /b 0

REM ── Leer cada linea e insertar en la BD ─────────────────────
for /f "usebackq tokens=1,2,3,4 delims=|" %%A in ("%ARCHIVO_TXT%") do (
    if not "%%A"=="" (
        "%MYSQL_BIN%" -u %DB_USER% -p%DB_PASS% %DB_NAME% -e "INSERT INTO muestras (enlace, fecha, hora, rtt_max) VALUES ('%%C', '%%A', '%%B', '%%D');" 2>nul
    )
)

REM ── Mover el archivo procesado a historico y limpiar TXT ────
type "%ARCHIVO_TXT%" >> "%ARCHIVO_PROC%"
type nul > "%ARCHIVO_TXT%"

endlocal
exit /b 0
