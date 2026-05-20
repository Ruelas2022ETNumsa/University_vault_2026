# proywin

Proyecto: Sistema de Monitoreo de Enlaces TCP/IP
ETN921 — Teoría de Sistemas Operativos
Plataforma: Windows 10 + IIS + MySQL 8.0.46 + PHP 7.1.11

---

## Estructura del proyecto

```
proyecto_monitoreo_windows\
  menu.bat
  scripts\
    tomar_muestra.bat
    cargar_bd.bat
    muestras_temp.txt
    muestras_procesadas.txt
  sql\
    crear_bd.sql
    fix_auth_php71.sql
    prueba.txt
  web\
    enlaces.txt
    enlaces.php
    ping_web.bat
    ping_helper.php
    index.php
    ping_online.php
    ping_manual.php
    estado_enlaces.php
    gestionar_enlaces.php
    reporte.php
    comparar.php
    estilos.css
```

---

## menu.bat

> Menú principal de administración del sistema.
> Requiere ejecución como Administrador.
> Llama a [[tomar_muestra.bat]] y [[cargar_bd.bat]] (opción 1 — visualización).
> Crea tareas en Task Scheduler que ejecutan [[tomar_muestra.bat]] cada 5 min y [[cargar_bd.bat]] cada hora (opción 2).
> Ejecuta [[crear_bd.sql]] y [[fix_auth_php71.sql]] contra MySQL (opción 3).
> Copia la carpeta `web\` a IIS y aplica permisos (opción 4).
> Edita [[enlaces.txt]] y sincroniza con la copia en `wwwroot` (opción 8).

```batch
@echo off
REM ============================================================
REM  SISTEMA DE MONITOREO DE ENLACES TCP/IP - Windows 10 + IIS
REM  ETN921 - Teoria de Sistemas Operativos
REM  menu.bat - Menu principal de administracion
REM
REM  REQUISITOS (segun PDF del docente):
REM    - IIS instalado con CGI habilitado
REM    - PHP 7.1.11 NTS en c:\php (registrado en IIS via FastCGI)
REM    - MySQL Server 8.0.46 instalado
REM    - PATH incluye c:\php y la carpeta bin de MySQL
REM ============================================================

setlocal enabledelayedexpansion
chcp 65001 >nul 2>&1

REM ── Detectar directorio donde vive este script ──────────────
set "DIR=%~dp0"
if "%DIR:~-1%"=="\" set "DIR=%DIR:~0,-1%"
set "SCRIPTS=%DIR%\scripts"
set "SQL=%DIR%\sql"
set "WEB_DEST=C:\inetpub\wwwroot\monitoreo"

REM ── Credenciales de MySQL (ajusta aqui si cambian) ──────────
set "DB_USER=root"
set "DB_PASS=Mamacita.com921"

REM ── Ruta al cliente mysql.exe ───────────────────────────────
set "MYSQL_BIN=C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe"
if not exist "%MYSQL_BIN%" set "MYSQL_BIN=C:\mariadb\bin\mysql.exe"
if not exist "%MYSQL_BIN%" set "MYSQL_BIN=mysql.exe"

:MENU
cls
echo ============================================================
echo      SISTEMA DE MONITOREO DE ENLACES TCP/IP  v1.0
echo                ETN921 - Teoria de S.O.
echo               Plataforma: Windows 10 + IIS
echo         Carpeta del proyecto: %DIR%
echo ============================================================
echo.
echo   1) Ver scripts de monitoreo           (tomar_muestra.bat y cargar_bd.bat)
echo   2) Activar/desactivar Task Scheduler  (cada 5 min y cada hora)
echo   3) Gestionar Base de Datos            (ver SQL, crear BD, limpiar tabla)
echo   4) Instalar interfaz web en IIS       (copiar a inetpub\wwwroot\monitoreo)
echo   5) Prueba manual de ping              (ping a cualquier direccion)
echo   6) Resetear todo el sistema           (borrar BD + web + tareas)
echo   7) Subir archivo a la BD              (cargar sql\prueba.txt)
echo   8) Gestionar enlaces                  (agregar/quitar enlaces a monitorear)
echo   0) Salir
echo.
set /p "OPT=  Elige una opcion [0-8]: "

if "%OPT%"=="1" goto VER_SCRIPTS
if "%OPT%"=="2" goto GESTIONAR_CRON
if "%OPT%"=="3" goto GESTIONAR_BD
if "%OPT%"=="4" goto INSTALAR_WEB
if "%OPT%"=="5" goto PING_MANUAL
if "%OPT%"=="6" goto RESETEAR
if "%OPT%"=="7" goto SUBIR_ARCHIVO
if "%OPT%"=="8" goto GESTIONAR_ENLACES
if "%OPT%"=="0" goto SALIR
echo   Opcion invalida.
pause
goto MENU

REM ════════════════════════════════════════════════════════════
REM  OPCION 1 - Ver los scripts de monitoreo
REM ════════════════════════════════════════════════════════════
:VER_SCRIPTS
cls
echo ══ OPCION 1: Scripts de recoleccion de datos ══
type "%SCRIPTS%\tomar_muestra.bat"
type "%SCRIPTS%\cargar_bd.bat"
pause
goto MENU

REM ════════════════════════════════════════════════════════════
REM  OPCION 2 - Activar/desactivar tareas con Task Scheduler
REM ════════════════════════════════════════════════════════════
:GESTIONAR_CRON
cls
echo ══ OPCION 2: Activar monitoreo automatico (Task Scheduler) ══
echo   1) Activar tareas (crear en Task Scheduler)
echo   2) Ver tareas actuales
echo   3) Desactivar tareas (eliminar de Task Scheduler)
echo   0) Volver al menu principal
set /p "SUB=  Elige una opcion: "

if "%SUB%"=="1" (
    schtasks /Create /SC MINUTE /MO 1 /TN "MonitoreoRed_Muestra" /TR "\"%SCRIPTS%\tomar_muestra.bat\"" /F
    schtasks /Create /SC MINUTE /MO 2 /TN "MonitoreoRed_Carga"   /TR "\"%SCRIPTS%\cargar_bd.bat\""    /F
)
if "%SUB%"=="2" (
    schtasks /Query /TN "MonitoreoRed_Muestra" 2>nul || echo   (Tarea de muestreo no existe)
    schtasks /Query /TN "MonitoreoRed_Carga"   2>nul || echo   (Tarea de carga no existe)
)
if "%SUB%"=="3" (
    schtasks /Delete /TN "MonitoreoRed_Muestra" /F 2>nul
    schtasks /Delete /TN "MonitoreoRed_Carga"   /F 2>nul
    echo   [OK] Tareas eliminadas del Task Scheduler.
)
if "%SUB%"=="0" goto MENU
pause
goto MENU

REM ════════════════════════════════════════════════════════════
REM  OPCION 3 - Gestionar base de datos
REM ════════════════════════════════════════════════════════════
:GESTIONAR_BD
cls
echo ══ OPCION 3: Base de datos MySQL ══
echo   1) CREAR BASE DE DATOS (ejecutar el script SQL)
echo   2) Verificar si la BD ya existe
echo   3) Borrar tabla muestras (para pruebas)
echo   4) Fix auth MySQL 8 <-> PHP 7.1
echo   0) Volver al menu principal
set /p "SUB=  Elige una opcion: "

if "%SUB%"=="1" (
    "%MYSQL_BIN%" -u %DB_USER% -p%DB_PASS% < "%SQL%\crear_bd.sql"
)
if "%SUB%"=="2" (
    "%MYSQL_BIN%" -u %DB_USER% -p%DB_PASS% -e "SHOW DATABASES LIKE 'monitoreo_red';"
)
if "%SUB%"=="3" (
    "%MYSQL_BIN%" -u %DB_USER% -p%DB_PASS% monitoreo_red -e "TRUNCATE TABLE muestras;"
)
if "%SUB%"=="4" (
    "%MYSQL_BIN%" -u %DB_USER% -p%DB_PASS% < "%SQL%\fix_auth_php71.sql"
)
if "%SUB%"=="0" goto MENU
pause
goto MENU

REM ════════════════════════════════════════════════════════════
REM  OPCION 4 - Instalar archivos web en IIS
REM ════════════════════════════════════════════════════════════
:INSTALAR_WEB
cls
echo ══ OPCION 4: Instalar interfaz web en IIS ══
echo   1) Instalar / actualizar archivos web
echo   2) Ver estado de IIS
echo   0) Volver al menu principal
set /p "SUB=  Elige una opcion: "

if "%SUB%"=="1" (
    if not exist "%WEB_DEST%"          mkdir "%WEB_DEST%"
    if not exist "%WEB_DEST%\reportWEB" mkdir "%WEB_DEST%\reportWEB"
    xcopy /Y /E "%DIR%\web\*" "%WEB_DEST%\" >nul
    icacls "%WEB_DEST%"              /grant "IIS_IUSRS:(OI)(CI)RX" /T >nul 2>&1
    icacls "%WEB_DEST%\reportWEB"    /grant "IIS_IUSRS:(OI)(CI)M"  /T >nul 2>&1
    icacls "%WEB_DEST%\enlaces.txt"  /grant "IIS_IUSRS:M"              >nul 2>&1
    echo   [OK] Archivos web instalados. Abre: http://localhost/monitoreo/
)
if "%SUB%"=="2" (
    sc query W3SVC 2>nul | findstr "STATE"
)
if "%SUB%"=="0" goto MENU
pause
goto MENU

REM ════════════════════════════════════════════════════════════
REM  OPCION 5 - Prueba manual de ping
REM ════════════════════════════════════════════════════════════
:PING_MANUAL
cls
set /p "DEST=  Direccion (ej: www.google.com): "
ping -n 5 %DEST%
pause
goto MENU

REM ════════════════════════════════════════════════════════════
REM  OPCION 6 - Resetear todo
REM ════════════════════════════════════════════════════════════
:RESETEAR
cls
set /p "CONFIRM=  Estas SEGURO? Escribe 'SI' para confirmar: "
if /I not "%CONFIRM%"=="SI" goto MENU
"%MYSQL_BIN%" -u %DB_USER% -p%DB_PASS% -e "DROP DATABASE IF EXISTS monitoreo_red;" 2>nul
if exist "%WEB_DEST%" rmdir /S /Q "%WEB_DEST%"
schtasks /Delete /TN "MonitoreoRed_Muestra" /F 2>nul
schtasks /Delete /TN "MonitoreoRed_Carga"   /F 2>nul
type nul > "%SCRIPTS%\muestras_temp.txt"      2>nul
type nul > "%SCRIPTS%\muestras_procesadas.txt" 2>nul
echo   [OK] Reseteo completo.
pause
goto MENU

REM ════════════════════════════════════════════════════════════
REM  OPCION 7 - Subir archivo de prueba a la BD
REM ════════════════════════════════════════════════════════════
:SUBIR_ARCHIVO
cls
set "ARCHIVO_PRUEBA=%SQL%\prueba.txt"
echo   1) Subir este archivo a la BD ahora
echo   2) Editar el archivo (Notepad)
echo   0) Volver al menu principal
set /p "SUB=  Elige una opcion: "
if "%SUB%"=="1" (
    for /f "usebackq tokens=1,2,3,4 delims=|" %%A in ("%ARCHIVO_PRUEBA%") do (
        if not "%%A"=="" (
            "%MYSQL_BIN%" -u %DB_USER% -p%DB_PASS% monitoreo_red -e "INSERT INTO muestras (enlace, fecha, hora, rtt_max) VALUES ('%%C', '%%A', '%%B', '%%D');" 2>nul
        )
    )
    echo   [OK] Datos insertados.
)
if "%SUB%"=="2" notepad "%ARCHIVO_PRUEBA%"
if "%SUB%"=="0" goto MENU
pause
goto MENU

REM ════════════════════════════════════════════════════════════
REM  OPCION 8 - Gestionar lista de enlaces
REM ════════════════════════════════════════════════════════════
:GESTIONAR_ENLACES
cls
set "ARCHIVO_ENLACES=%DIR%\web\enlaces.txt"
echo   1) Agregar un enlace nuevo
echo   2) Quitar un enlace
echo   3) Editar manualmente (Notepad)
echo   4) Restaurar lista original de 10 enlaces
echo   0) Volver al menu principal
set /p "SUB=  Elige una opcion: "

if "%SUB%"=="1" goto AGREGAR_ENLACE
if "%SUB%"=="2" goto QUITAR_ENLACE
if "%SUB%"=="3" (
    notepad "%ARCHIVO_ENLACES%"
    call :SINCRONIZAR_WEB
    goto GESTIONAR_ENLACES
)
if "%SUB%"=="4" (
    (
        echo # Lista de enlaces a monitorear
        echo www.google.com
        echo www.youtube.com
        echo www.facebook.com
        echo www.wikipedia.org
        echo www.rfi.fr
        echo www.bbc.com
        echo www.amazon.com
        echo www.microsoft.com
        echo www.cloudflare.com
        echo www.github.com
    ) > "%ARCHIVO_ENLACES%"
    call :SINCRONIZAR_WEB
    echo   [OK] Lista original restaurada.
    pause
    goto GESTIONAR_ENLACES
)
if "%SUB%"=="0" goto MENU
goto GESTIONAR_ENLACES

:AGREGAR_ENLACE
set /p "NUEVO=  Dominio o IP a agregar: "
echo !NUEVO!>> "%ARCHIVO_ENLACES%"
call :SINCRONIZAR_WEB
echo   [OK] Agregado: !NUEVO!
pause
goto GESTIONAR_ENLACES

:QUITAR_ENLACE
set /p "QUITAR=  Dominio exacto a quitar: "
set "TMP_FILE=%ARCHIVO_ENLACES%.tmp"
for /f "usebackq delims=" %%L in ("%ARCHIVO_ENLACES%") do (
    set "LINEA=%%L"
    if /I not "!LINEA!"=="!QUITAR!" echo !LINEA!>> "%TMP_FILE%"
)
move /Y "%TMP_FILE%" "%ARCHIVO_ENLACES%" >nul
call :SINCRONIZAR_WEB
echo   [OK] Removido: !QUITAR!
pause
goto GESTIONAR_ENLACES

:SINCRONIZAR_WEB
if exist "%WEB_DEST%\enlaces.txt" (
    copy /Y "%ARCHIVO_ENLACES%" "%WEB_DEST%\enlaces.txt" >nul
)
exit /b 0

:SALIR
endlocal
exit /b 0
```

---

## scripts\tomar_muestra.bat

> Ejecutado automáticamente por el Task Scheduler cada 5 minutos.
> Lee la lista de dominios desde [[enlaces.txt]] (primero busca la copia en IIS, luego la del proyecto).
> Usa `Test-Connection` de PowerShell para hacer ping a cada enlace.
> Escribe los resultados en `muestras_temp.txt` con formato `FECHA|HORA|ENLACE|RTT_MAX`.
> El archivo resultante es leído por [[cargar_bd.bat]].

```batch
@echo off
REM ============================================================
REM  tomar_muestra.bat  (Windows 10)
REM  Hace ping a los enlaces listados en ..\web\enlaces.txt
REM  y guarda en muestras_temp.txt.
REM  Programado por Task Scheduler cada 5 minutos.
REM ============================================================

setlocal enabledelayedexpansion

set "DIR=%~dp0"
if "%DIR:~-1%"=="\" set "DIR=%DIR:~0,-1%"
set "ARCHIVO_TXT=%DIR%\muestras_temp.txt"
set "ARCHIVO_RTT=%DIR%\_rtt_tmp.txt"

REM ── Buscar enlaces.txt (misma fuente que la web) ─────────────
set "ARCHIVO_ENLACES=C:\inetpub\wwwroot\monitoreo\enlaces.txt"
if not exist "%ARCHIVO_ENLACES%" set "ARCHIVO_ENLACES=%DIR%\..\web\enlaces.txt"
if not exist "%ARCHIVO_ENLACES%" exit /b 1

REM ── Fecha y hora con PowerShell ──────────────────────────────
for /f "delims=" %%D in ('powershell -NoProfile -Command "Get-Date -Format 'yyyy-MM-dd'"') do set "FECHA=%%D"
for /f "delims=" %%H in ('powershell -NoProfile -Command "Get-Date -Format 'HH:mm:ss'"') do set "HORA=%%H"

REM ── Leer cada linea de enlaces.txt y hacer ping ──────────────
REM    eol=# ignora lineas de comentario
for /f "usebackq tokens=* eol=#" %%E in ("%ARCHIVO_ENLACES%") do (
    if not "%%E"=="" (
        set "RTT_MAX=-1"
        if exist "!ARCHIVO_RTT!" del "!ARCHIVO_RTT!" 2>nul

        powershell -NoProfile -ExecutionPolicy Bypass -Command ^
          "try { $r = Test-Connection -ComputerName '%%E' -Count 5 -ErrorAction Stop; ^
          ($r | Measure-Object -Property ResponseTime -Maximum).Maximum } ^
          catch { -1 }" > "!ARCHIVO_RTT!" 2>nul

        if exist "!ARCHIVO_RTT!" (
            set /p RTT_MAX=<"!ARCHIVO_RTT!"
            for /f "tokens=* delims= " %%T in ("!RTT_MAX!") do set "RTT_MAX=%%T"
        )
        if "!RTT_MAX!"=="" set "RTT_MAX=-1"

        REM Formato de salida: FECHA|HORA|ENLACE|RTT_MAX
        echo !FECHA!^|!HORA!^|%%E^|!RTT_MAX!>> "%ARCHIVO_TXT%"
    )
)

if exist "!ARCHIVO_RTT!" del "!ARCHIVO_RTT!" 2>nul
endlocal
exit /b 0
```

---

## scripts\cargar_bd.bat

> Ejecutado automáticamente por el Task Scheduler cada hora.
> Lee `muestras_temp.txt` línea por línea (generado por [[tomar_muestra.bat]]).
> Inserta cada registro en la tabla `muestras` de MySQL.
> Mueve el contenido procesado a `muestras_procesadas.txt` y vacía el archivo temporal.

```batch
@echo off
REM ============================================================
REM  cargar_bd.bat  (Windows 10)
REM  Lee muestras_temp.txt e inserta los datos en MySQL.
REM  Programado por Task Scheduler cada 1 hora.
REM ============================================================

setlocal enabledelayedexpansion

set "DIR=%~dp0"
if "%DIR:~-1%"=="\" set "DIR=%DIR:~0,-1%"
set "ARCHIVO_TXT=%DIR%\muestras_temp.txt"
set "ARCHIVO_PROC=%DIR%\muestras_procesadas.txt"

set "DB_USER=root"
set "DB_PASS=Mamacita.com921"
set "DB_NAME=monitoreo_red"

set "MYSQL_BIN=C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe"
if not exist "%MYSQL_BIN%" set "MYSQL_BIN=C:\mariadb\bin\mysql.exe"
if not exist "%MYSQL_BIN%" set "MYSQL_BIN=mysql.exe"

if not exist "%ARCHIVO_TXT%" exit /b 0

REM ── Insertar cada linea en la BD ────────────────────────────
for /f "usebackq tokens=1,2,3,4 delims=|" %%A in ("%ARCHIVO_TXT%") do (
    if not "%%A"=="" (
        "%MYSQL_BIN%" -u %DB_USER% -p%DB_PASS% %DB_NAME% ^
          -e "INSERT INTO muestras (enlace, fecha, hora, rtt_max) VALUES ('%%C', '%%A', '%%B', '%%D');" 2>nul
    )
)

REM ── Rotar archivo: anexar al historico y vaciar temporal ─────
type "%ARCHIVO_TXT%" >> "%ARCHIVO_PROC%"
type nul > "%ARCHIVO_TXT%"

endlocal
exit /b 0
```

---

## sql\crear_bd.sql

> Ejecutado una sola vez desde la opción 3→1 de [[menu.bat]].
> Crea la base de datos `monitoreo_red` y la tabla `muestras`.
> La tabla es leída y escrita por [[cargar_bd.bat]], [[estado_enlaces.php]], [[reporte.php]] y [[comparar.php]].

```sql
-- ============================================================
--  crear_bd.sql — ETN921
--  Crea la base de datos y tabla para el sistema de monitoreo
-- ============================================================

CREATE DATABASE IF NOT EXISTS monitoreo_red
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE monitoreo_red;

CREATE TABLE IF NOT EXISTS muestras (
    id        INT AUTO_INCREMENT PRIMARY KEY,
    enlace    VARCHAR(100)   NOT NULL COMMENT 'Dominio monitoreado',
    fecha     DATE           NOT NULL COMMENT 'Fecha de la muestra',
    hora      TIME           NOT NULL COMMENT 'Hora de la muestra',
    rtt_max   FLOAT          NOT NULL COMMENT 'RTT maximo en ms (-1 si no responde)',
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Indice compuesto para acelerar consultas por enlace y fecha
ALTER TABLE muestras ADD INDEX idx_enlace_fecha (enlace, fecha);

SELECT 'Base de datos monitoreo_red creada correctamente.' AS resultado;
```

---

## sql\fix_auth_php71.sql

> Ejecutado una sola vez desde la opción 3→4 de [[menu.bat]].
> Resuelve la incompatibilidad entre MySQL 8 (`caching_sha2_password`) y PHP 7.1 (que no lo soporta).
> Sin este fix, [[reporte.php]], [[comparar.php]] y [[estado_enlaces.php]] no pueden conectar a la BD.

```sql
-- ============================================================
--  fix_auth_php71.sql
--  Cambia el plugin de autenticacion de root a
--  mysql_native_password, compatible con PHP 7.1.
-- ============================================================

ALTER USER 'root'@'localhost'
    IDENTIFIED WITH mysql_native_password BY 'Mamacita.com921';

FLUSH PRIVILEGES;

SELECT 'Usuario root ahora usa mysql_native_password. PHP 7.1 puede conectar.' AS resultado;
```

---

## sql\prueba.txt

> Datos de ejemplo cargados desde la opción 7 de [[menu.bat]].
> Formato: `FECHA|HORA|ENLACE|RTT_MAX`
> Procesado por el `for /f` del mismo [[menu.bat]] (opción 7) con INSERT directo a MySQL.
> Permite ver gráficos en [[reporte.php]] y [[comparar.php]] sin esperar al monitoreo automático.

```
# Archivo de prueba — Sistema de Monitoreo ETN921
# Formato: FECHA|HORA|ENLACE|RTT_MAX
2025-04-07|08:00:00|www.google.com|12.345
2025-04-07|08:00:00|www.youtube.com|25.678
2025-04-07|08:00:00|www.facebook.com|18.901
2025-04-07|08:00:00|www.wikipedia.org|45.123
2025-04-07|08:00:00|www.rfi.fr|110.456
2025-04-07|08:00:00|www.bbc.com|98.234
2025-04-07|08:00:00|www.amazon.com|67.890
2025-04-07|08:00:00|www.microsoft.com|33.445
2025-04-07|08:00:00|www.cloudflare.com|8.901
2025-04-07|08:00:00|www.github.com|55.678
2025-04-07|08:05:00|www.google.com|11.222
2025-04-07|08:05:00|www.youtube.com|28.999
2025-04-07|08:05:00|www.facebook.com|-1
2025-04-07|08:05:00|www.wikipedia.org|41.001
2025-04-07|08:05:00|www.rfi.fr|115.333
2025-04-07|08:05:00|www.bbc.com|95.111
2025-04-07|08:05:00|www.amazon.com|70.222
2025-04-07|08:05:00|www.microsoft.com|30.555
2025-04-07|08:05:00|www.cloudflare.com|9.123
2025-04-07|08:05:00|www.github.com|52.444
```

---

## web\enlaces.txt

> Fuente de verdad única de la lista de dominios monitoreados.
> Leída por [[tomar_muestra.bat]] en cada ejecución automática.
> Leída por [[enlaces.php]] en cada petición web.
> Editada desde consola vía opción 8 de [[menu.bat]] o desde el navegador vía [[gestionar_enlaces.php]].

```
# ============================================================
#  enlaces.txt - Lista de enlaces a monitorear
# ============================================================
#  - Un dominio (o IP) por linea
#  - Las lineas que empiezan con # son comentarios (se ignoran)
#  - Las lineas vacias se ignoran
# ============================================================

www.google.com
www.youtube.com
www.facebook.com
www.wikipedia.org
www.rfi.fr
www.bbc.com
www.amazon.com
www.microsoft.com
www.cloudflare.com
www.github.com
```

---

## web\enlaces.php

> Helper PHP incluido con `require_once` por [[index.php]], [[ping_online.php]], [[estado_enlaces.php]] y [[gestionar_enlaces.php]].
> Lee [[enlaces.txt]] y devuelve los dominios válidos como array PHP.
> `obtener_enlaces_numerados()` devuelve claves 1..N para que coincidan con `?Equipo=N` de [[ping_online.php]].

```php
<?php
// enlaces.php
// Carga y procesa la lista de enlaces desde enlaces.txt

function obtener_enlaces() {
    $archivo = __DIR__ . '/enlaces.txt';
    $resultado = [];

    if (!file_exists($archivo)) {
        return $resultado;
    }

    // Lee líneas ignorando vacías
    $lineas = file($archivo, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
    foreach ($lineas as $linea) {
        $linea = trim($linea);
        // Ignorar comentarios
        if ($linea === '' || $linea[0] === '#') {
            continue;
        }
        // Solo caracteres válidos de dominio/IP
        $linea = preg_replace('/[^a-zA-Z0-9.\-]/', '', $linea);
        if ($linea !== '') {
            $resultado[] = $linea;
        }
    }
    return $resultado;
}

// Devuelve enlaces numerados desde 1 (para ?Equipo=N)
function obtener_enlaces_numerados() {
    $enlaces = obtener_enlaces();
    $numerados = [];
    foreach ($enlaces as $i => $e) {
        $numerados[$i + 1] = $e;
    }
    return $numerados;
}
```

---

## web\ping_web.bat

> Invocado desde PHP mediante `shell_exec()` en [[ping_helper.php]].
> Cumple la cadena obligatoria de la especificación: Navegador → PHP → .bat → ping.
> Recibe el dominio como argumento `%~1` y ejecuta `ping -n 3`.
> La salida es capturada por [[ping_helper.php]] para extraer el RTT máximo.

```batch
@echo off
REM ping_web.bat
REM Ejecuta ping desde Windows y devuelve el resultado a PHP.
REM Cadena: navegador -> PHP -> este .bat -> ping

setlocal

REM Obtiene la direccion recibida desde PHP
set "DESTINO=%~1"

REM Verifica que exista una direccion
if "%DESTINO%"=="" (
    echo ERROR: No se proporciono direccion.
    exit /b 1
)

REM Ejecuta 3 paquetes ping con timeout de 5 segundos
ping -n 3 -w 5000 %DESTINO%

REM PHP (ping_helper.php) procesa la salida y calcula el RTT maximo

endlocal
exit /b 0
```

---

## web\ping_helper.php

> Helper compartido incluido por [[ping_online.php]] y [[ping_manual.php]].
> Llama a [[ping_web.bat]] via `shell_exec()` para cumplir la arquitectura Navegador → PHP → .bat → ping.
> Parsea la salida con regex bilingüe (español: `tiempo=15ms` / inglés: `time=15ms`).
> Devuelve `['salida' => string, 'rtt_max' => float]` (-1 si no hay respuesta).

```php
<?php
// ping_helper.php
// Ejecuta pings en Windows usando ping_web.bat

function hacer_ping($destino) {
    // Filtra caracteres no válidos (previene inyección de comandos)
    $destino_limpio = preg_replace('/[^a-zA-Z0-9.\-]/', '', $destino);
    if ($destino_limpio === '') {
        return ['salida' => 'ERROR: Direccion invalida.', 'rtt_max' => -1];
    }

    // Ruta absoluta al .bat en la misma carpeta
    $bat = __DIR__ . DIRECTORY_SEPARATOR . 'ping_web.bat';
    if (!file_exists($bat)) {
        return ['salida' => 'ERROR: No se encontro ping_web.bat en ' . __DIR__,
                'rtt_max' => -1];
    }

    // Invoca el .bat y captura su salida completa
    $cmd   = '"' . $bat . '" ' . escapeshellarg($destino_limpio) . ' 2>&1';
    $salida = shell_exec($cmd);

    if ($salida === null) {
        return ['salida' => 'ERROR: shell_exec devolvio null.',
                'rtt_max' => -1];
    }

    // Regex bilingüe: acepta "tiempo=15ms" (es) y "time=15ms" (en)
    // También acepta coma o punto como separador decimal
    $rtt_max = -1;
    if (preg_match_all('/(?:tiempo|time)\s*[=<]\s*(\d+(?:[.,]\d+)?)\s*ms/i', $salida, $matches)) {
        $tiempos = [];
        foreach ($matches[1] as $t) {
            $tiempos[] = (float) str_replace(',', '.', $t);
        }
        if (!empty($tiempos)) {
            $rtt_max = max($tiempos);
        }
    }

    return ['salida' => $salida, 'rtt_max' => $rtt_max];
}
```

---

## web\index.php

> Página principal del sistema. Accesible en `http://localhost/monitoreo/`.
> Incluye [[enlaces.php]] para generar botones dinámicos hacia [[ping_online.php]].
> Incluye [[estado_enlaces.php]] al final de la página (tabla de estado actual).
> El formulario POST apunta a [[reporte.php]]; el formulario GET de comparación apunta a [[comparar.php]].
> El formulario GET manual apunta a [[ping_manual.php]].
> El enlace de gestión apunta a [[gestionar_enlaces.php]].

```php
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Monitor de Red - ETN921</title>
    <link rel="stylesheet" href="estilos.css">
</head>
<body>
    <header>
        <div class="header-inner">
            <h1>&#9001; Monitor de Enlaces TCP/IP &#9002;</h1>
            <p class="subtitulo">ETN921 &mdash; Teoría de Sistemas Operativos</p>
        </div>
    </header>

    <main>
        <!-- Componente 2: Ping en tiempo real (GET) -->
        <section class="tarjeta">
            <h2>&#9654; Ping en tiempo real</h2>
            <p>Selecciona un enlace o escribe una dirección para hacer ping ahora mismo.</p>

            <div class="grid-enlaces">
                <?php
                require_once 'enlaces.php';
                $enlaces = obtener_enlaces();
                foreach ($enlaces as $i => $e) {
                    // Genera un botón por cada enlace -> ping_online.php?Equipo=N
                    echo "<a href='ping_online.php?Equipo=" . ($i+1) . "' class='btn-enlace'>$e</a>";
                }
                ?>
            </div>

            <!-- Ping manual via GET -> ping_manual.php -->
            <form method="GET" action="ping_manual.php" class="form-inline">
                <input type="text" name="direccion" placeholder="Escribe una dirección (ej: www.nasa.gov)" required>
                <button type="submit">Ping manual</button>
            </form>

            <p style="margin-top:1rem; font-size:0.85rem; text-align:right;">
                <a href="gestionar_enlaces.php" style="color:var(--acento); text-decoration:none;">
                    &#9881; Agregar o quitar enlaces de la lista &rarr;
                </a>
            </p>
        </section>

        <!-- Componente 3: Reportes gráficos (POST) -> reporte.php -->
        <section class="tarjeta">
            <h2>&#9998; Generar reporte gráfico</h2>
            <form method="POST" action="reporte.php" class="form-reporte">
                <div class="fila-form">
                    <label>Enlace:</label>
                    <select name="enlace" required>
                        <option value="">-- Selecciona --</option>
                        <?php foreach ($enlaces as $e) echo "<option value='$e'>$e</option>"; ?>
                    </select>
                </div>
                <div class="fila-form">
                    <label>Fecha:</label>
                    <input type="date" name="fecha" value="<?php echo date('Y-m-d'); ?>" required>
                </div>
                <div class="fila-form">
                    <label>Hora inicio:</label>
                    <input type="time" name="hora_inicio" value="00:00" required>
                </div>
                <div class="fila-form">
                    <label>Hora fin:</label>
                    <input type="time" name="hora_fin" value="23:59" required>
                </div>
                <button type="submit" class="btn-reporte">Generar reporte</button>
            </form>
        </section>

        <!-- Comparación: Diagrama de quesos -> comparar.php -->
        <section class="tarjeta">
            <h2>&#9685; Comparar los 10 enlaces (diagrama de quesos)</h2>
            <form method="GET" action="comparar.php" class="form-reporte">
                <div class="fila-form">
                    <label>Fecha:</label>
                    <input type="date" name="fecha" value="<?php echo date('Y-m-d'); ?>" required>
                </div>
                <div class="fila-form">
                    <label>Hora inicio:</label>
                    <input type="time" name="hora_inicio" value="00:00" required>
                </div>
                <div class="fila-form">
                    <label>Hora fin:</label>
                    <input type="time" name="hora_fin" value="23:59" required>
                </div>
                <button type="submit" class="btn-reporte" style="background:#7c3aed;">Ver comparación</button>
            </form>
        </section>

        <!-- Estado actual de los 10 enlaces (include de estado_enlaces.php) -->
        <section class="tarjeta">
            <h2>&#9632; Estado actual de los 10 enlaces</h2>
            <?php include 'estado_enlaces.php'; ?>
        </section>
    </main>

    <footer>
        <p>Sistema de Monitoreo TCP/IP &mdash; ETN921 &mdash; <?php echo date('Y'); ?></p>
    </footer>
</body>
</html>
```

---

## web\ping_online.php

> Componente 2 — método GET.
> Recibe `?Equipo=N`, resuelve el dominio usando [[enlaces.php]], y llama a [[ping_helper.php]] → [[ping_web.bat]] → ping.
> Redirige a [[index.php]] si el número de equipo no es válido.

```php
<?php
// ping_online.php — Componente 2 (método GET)
// Flujo: GET ?Equipo=N -> PHP -> ping_helper -> ping_web.bat -> ping

require_once __DIR__ . '/ping_helper.php';
require_once __DIR__ . '/enlaces.php';

// Lista numerada desde 1 para coincidir con ?Equipo=N
$enlaces = obtener_enlaces_numerados();
$equipo  = isset($_GET['Equipo']) ? (int)$_GET['Equipo'] : 0;

// Validar que el índice exista
if (!array_key_exists($equipo, $enlaces)) {
    header("Location: index.php");
    exit;
}

$destino = $enlaces[$equipo];

// Ejecutar ping via ping_helper.php -> ping_web.bat -> ping
$ping    = hacer_ping($destino);
$resultado = $ping['salida'];
$rtt_max   = $ping['rtt_max'] >= 0 ? $ping['rtt_max'] . " ms" : "Sin respuesta";
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Ping a <?php echo htmlspecialchars($destino); ?> - ETN921</title>
    <link rel="stylesheet" href="estilos.css">
</head>
<body>
<header>
    <div class="header-inner">
        <h1>&#9001; Resultado de Ping &#9002;</h1>
        <p class="subtitulo">ETN921 &mdash; Ping en tiempo real (GET)</p>
    </div>
</header>
<main>
    <section class="tarjeta">
        <h2>Ping a: <span class="resaltado"><?php echo htmlspecialchars($destino); ?></span></h2>
        <div class="resultado-ping">
            <div class="rtt-badge">RTT Max: <?php echo htmlspecialchars($rtt_max); ?></div>
            <pre><?php echo htmlspecialchars($resultado); ?></pre>
        </div>
        <a href="index.php" class="btn-volver">&#8592; Volver al menu</a>
    </section>
</main>
<footer>
    <p>Sistema de Monitoreo TCP/IP &mdash; ETN921 &mdash; <?php echo date('Y'); ?></p>
</footer>
</body>
</html>
```

---

## web\ping_manual.php

> Variante de [[ping_online.php]] para dominios escritos por el usuario.
> Recibe `?direccion=dominio` por GET desde el formulario de [[index.php]].
> Llama a [[ping_helper.php]] → [[ping_web.bat]] → ping.
> Redirige a [[index.php]] si la dirección queda vacía tras sanitizar.

```php
<?php
// ping_manual.php — Ping a dirección escrita por el usuario
// Flujo: GET ?direccion=X -> PHP -> ping_helper -> ping_web.bat -> ping

require_once __DIR__ . '/ping_helper.php';

$direccion_raw = isset($_GET['direccion']) ? $_GET['direccion'] : '';

// Sanitizar: solo caracteres válidos de dominio o IP
$destino = preg_replace('/[^a-zA-Z0-9.\-]/', '', $direccion_raw);

if (empty($destino)) {
    header("Location: index.php");
    exit;
}

// Ejecutar ping via ping_helper -> ping_web.bat -> ping
$ping      = hacer_ping($destino);
$resultado = $ping['salida'];
$rtt_max   = $ping['rtt_max'] >= 0 ? $ping['rtt_max'] . " ms" : "Sin respuesta";
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Ping manual - ETN921</title>
    <link rel="stylesheet" href="estilos.css">
</head>
<body>
<header>
    <div class="header-inner">
        <h1>&#9001; Ping Manual &#9002;</h1>
        <p class="subtitulo">ETN921 &mdash; Direccion personalizada (GET)</p>
    </div>
</header>
<main>
    <section class="tarjeta">
        <h2>Ping a: <span class="resaltado"><?php echo htmlspecialchars($destino); ?></span></h2>
        <div class="resultado-ping">
            <div class="rtt-badge">RTT Max: <?php echo htmlspecialchars($rtt_max); ?></div>
            <pre><?php echo htmlspecialchars($resultado); ?></pre>
        </div>
        <form method="GET" action="ping_manual.php" class="form-inline" style="margin-top:1rem;">
            <input type="text" name="direccion" placeholder="Otra direccion..."
                   value="<?php echo htmlspecialchars($destino); ?>">
            <button type="submit">Ping</button>
        </form>
        <a href="index.php" class="btn-volver">&#8592; Volver al menu</a>
    </section>
</main>
<footer>
    <p>Sistema de Monitoreo TCP/IP &mdash; ETN921 &mdash; <?php echo date('Y'); ?></p>
</footer>
</body>
</html>
```

---

## web\estado_enlaces.php

> Incluido directamente en [[index.php]] con `include`.
> Usa [[enlaces.php]] para obtener la lista de dominios.
> Consulta la BD (tabla `muestras` creada por [[crear_bd.sql]]) para obtener el último RTT de cada enlace.
> Clasifica el estado en OK / Lento / Muy lento / Sin respuesta con clases CSS de [[estilos.css]].

```php
<?php
// estado_enlaces.php — Incluido en index.php
// Muestra la última muestra de cada enlace desde la BD

$conn = @new mysqli("localhost", "root", "Mamacita.com921", "monitoreo_red");

if ($conn->connect_error) {
    echo "<p class='aviso'>Base de datos no disponible. Ejecuta primero la Opción 3 del menú.</p>";
    return;
}

require_once __DIR__ . '/enlaces.php';
$enlaces = obtener_enlaces();

echo "<table class='tabla-estado'>";
echo "<thead><tr>
        <th>#</th><th>Enlace</th><th>Última muestra</th>
        <th>Hora</th><th>RTT Máx (ms)</th><th>Estado</th>
      </tr></thead>";
echo "<tbody>";

foreach ($enlaces as $i => $enlace) {
    // Última muestra de este enlace (fecha y hora DESC, LIMIT 1)
    $stmt = $conn->prepare(
        "SELECT fecha, hora, rtt_max FROM muestras
         WHERE enlace = ? ORDER BY fecha DESC, hora DESC LIMIT 1"
    );
    $stmt->bind_param("s", $enlace);
    $stmt->execute();
    $fila = $stmt->get_result()->fetch_assoc();

    if ($fila) {
        $rtt = $fila['rtt_max'];
        // Clasificación del RTT en rangos
        if ($rtt < 0)        { $clase = "estado-error"; $texto = "Sin respuesta"; }
        elseif ($rtt < 100)  { $clase = "estado-ok";    $texto = "OK"; }
        elseif ($rtt < 300)  { $clase = "estado-warn";  $texto = "Lento"; }
        else                 { $clase = "estado-error";  $texto = "Muy lento"; }

        echo "<tr>
            <td>" . ($i+1) . "</td>
            <td><a href='ping_online.php?Equipo=" . ($i+1) . "'>$enlace</a></td>
            <td>{$fila['fecha']}</td>
            <td>{$fila['hora']}</td>
            <td>{$rtt}</td>
            <td class='$clase'>$texto</td>
          </tr>";
    } else {
        echo "<tr>
            <td>" . ($i+1) . "</td>
            <td><a href='ping_online.php?Equipo=" . ($i+1) . "'>$enlace</a></td>
            <td colspan='3'>Sin datos aún</td>
            <td class='estado-warn'>Esperando</td>
          </tr>";
    }
}

echo "</tbody></table>";
$conn->close();
?>
```

---

## web\gestionar_enlaces.php

> Equivalente web de la opción 8 de [[menu.bat]].
> Incluye [[enlaces.php]] para leer y modificar [[enlaces.txt]].
> Acciones POST: `agregar` (append al array + `guardar_lista()`) y `quitar` (`array_filter()` + `guardar_lista()`).
> Los cambios se reflejan en [[tomar_muestra.bat]] en la próxima ejecución automática.
> Usa estilos de [[estilos.css]].

```php
<?php
// gestionar_enlaces.php
// Pantalla web para agregar o quitar enlaces de enlaces.txt.
// Equivalente web de la Opción 8 del menu.bat.

require_once __DIR__ . '/enlaces.php';

$archivo  = __DIR__ . '/enlaces.txt';
$mensaje  = '';
$tipo_msg = '';

// Reescribe el archivo con la lista actualizada
function guardar_lista($archivo, $lista) {
    $contenido  = "# enlaces.txt - Editado desde gestionar_enlaces.php\n\n";
    foreach ($lista as $e) {
        $e = trim($e);
        if ($e !== '' && preg_match('/^[a-zA-Z0-9.\-]+$/', $e)) {
            $contenido .= $e . "\n";
        }
    }
    return @file_put_contents($archivo, $contenido) !== false;
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $accion       = isset($_POST['accion']) ? $_POST['accion'] : '';
    $lista_actual = obtener_enlaces();

    // AGREGAR
    if ($accion === 'agregar') {
        $nuevo = preg_replace('/[^a-zA-Z0-9.\-]/', '', trim($_POST['enlace'] ?? ''));
        if ($nuevo === '') {
            $mensaje = 'Dirección vacía o inválida.'; $tipo_msg = 'err';
        } elseif (in_array($nuevo, $lista_actual)) {
            $mensaje = "El enlace '$nuevo' ya está en la lista."; $tipo_msg = 'err';
        } else {
            $lista_actual[] = $nuevo;
            if (guardar_lista($archivo, $lista_actual)) {
                $mensaje = "Enlace '$nuevo' agregado."; $tipo_msg = 'ok';
            } else {
                $mensaje = "No se pudo escribir enlaces.txt. Verifica permisos."; $tipo_msg = 'err';
            }
        }
    }

    // QUITAR
    if ($accion === 'quitar') {
        $a_quitar = $_POST['enlace'] ?? '';
        $nueva    = array_values(array_filter($lista_actual, function($x) use ($a_quitar) {
            return $x !== $a_quitar;
        }));
        if (guardar_lista($archivo, $nueva)) {
            $mensaje = "Enlace '$a_quitar' eliminado."; $tipo_msg = 'ok';
        } else {
            $mensaje = "No se pudo escribir enlaces.txt."; $tipo_msg = 'err';
        }
    }
}

$enlaces = obtener_enlaces();
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Gestionar enlaces - ETN921</title>
    <link rel="stylesheet" href="estilos.css">
</head>
<body>
<header>
    <div class="header-inner">
        <h1>&#9881; Gestionar Enlaces Monitoreados</h1>
        <p class="subtitulo">ETN921 &mdash; Agregar o quitar dominios de la lista</p>
    </div>
</header>
<main>
    <section class="tarjeta">
        <?php if ($mensaje): ?>
            <div class="msg msg-<?php echo $tipo_msg; ?>"><?php echo htmlspecialchars($mensaje); ?></div>
        <?php endif; ?>

        <h2>&#43; Agregar enlace</h2>
        <form method="POST" action="gestionar_enlaces.php" style="display:flex;gap:0.5rem;margin:1rem 0;">
            <input type="hidden" name="accion" value="agregar">
            <input type="text" name="enlace" placeholder="Ejemplo: www.umsa.bo"
                   pattern="[a-zA-Z0-9.\-]+" required>
            <button type="submit">Agregar</button>
        </form>

        <h2>&#9776; Enlaces actuales</h2>
        <ul style="list-style:none;padding:0;">
            <?php foreach ($enlaces as $i => $e): ?>
            <li style="display:flex;justify-content:space-between;padding:0.6rem 0.8rem;border-bottom:1px solid var(--borde);">
                <span style="font-family:var(--mono);color:var(--acento);"><?php echo ($i+1) . '. ' . htmlspecialchars($e); ?></span>
                <form method="POST" action="gestionar_enlaces.php" style="margin:0;"
                      onsubmit="return confirm('Quitar <?php echo htmlspecialchars($e); ?>?');">
                    <input type="hidden" name="accion" value="quitar">
                    <input type="hidden" name="enlace" value="<?php echo htmlspecialchars($e); ?>">
                    <button type="submit" style="background:rgba(239,68,68,0.15);color:#ef4444;border:1px solid rgba(239,68,68,0.3);padding:0.3rem 0.8rem;border-radius:4px;cursor:pointer;">Quitar</button>
                </form>
            </li>
            <?php endforeach; ?>
        </ul>

        <a href="index.php" class="btn-volver">&#8592; Volver al menu</a>
    </section>
</main>
<footer>
    <p>Sistema de Monitoreo TCP/IP &mdash; ETN921 &mdash; <?php echo date('Y'); ?></p>
</footer>
</body>
</html>
```

---

## web\reporte.php

> Componente 3 — método POST.
> Recibe enlace, fecha y rango horario desde el formulario de [[index.php]].
> Consulta 1: estadísticas agregadas con `AVG`, `MAX`, `MIN`, `STDDEV`, `COUNT`, `SUM(IF())`, `CASE WHEN` sobre la tabla creada por [[crear_bd.sql]].
> Consulta 2: detalle muestra a muestra con `DATE_FORMAT` e `IF()` anidados para el gráfico.
> Renderiza gráfico de línea con Chart.js (datos inyectados como JSON desde PHP).
> Fix PHP 7.1: `match()` reemplazado por `switch` (match existe desde PHP 8.0).
> Usa estilos de [[estilos.css]].

```php
<?php
// reporte.php — Componente 3 (método POST) — PHP 7.1
// Estadísticas con: AVG, MAX, MIN, COUNT, STDDEV, IF, CASE, DATE_FORMAT

if ($_SERVER['REQUEST_METHOD'] !== 'POST' && !isset($_GET['descargar'])) {
    header("Location: index.php");
    exit;
}

$DB_USER = "root";
$DB_PASS = "Mamacita.com921";
$DB_NAME = "monitoreo_red";

$enlace      = $_POST['enlace']      ?? ($_GET['enlace']      ?? '');
$fecha       = $_POST['fecha']       ?? ($_GET['fecha']       ?? date('Y-m-d'));
$hora_inicio = $_POST['hora_inicio'] ?? ($_GET['hora_inicio'] ?? '00:00');
$hora_fin    = $_POST['hora_fin']    ?? ($_GET['hora_fin']    ?? '23:59');
$formato_dl  = $_GET['descargar']    ?? '';

$conn = new mysqli("localhost", $DB_USER, $DB_PASS, $DB_NAME);
if ($conn->connect_error) {
    die("<p style='color:red'>Error de conexion: " . $conn->connect_error . "</p>");
}

$hora_fin_completo = $hora_fin . ":59";

// ── CONSULTA 1: Estadísticas agregadas (todo calculado en MySQL) ──────────
$stmt_stats = $conn->prepare(
    "SELECT
        ROUND(AVG(rtt_max), 3)      AS promedio,
        ROUND(MAX(rtt_max), 3)      AS maximo,
        ROUND(MIN(rtt_max), 3)      AS minimo,
        COUNT(*)                     AS total_muestras,
        SUM(IF(rtt_max >= 0, 1, 0)) AS pings_exitosos,
        SUM(IF(rtt_max <  0, 1, 0)) AS pings_fallidos,
        ROUND(STDDEV(rtt_max), 3)   AS desviacion_std,
        CASE
            WHEN AVG(rtt_max) < 50  THEN 'Excelente'
            WHEN AVG(rtt_max) < 100 THEN 'Bueno'
            WHEN AVG(rtt_max) < 200 THEN 'Regular'
            ELSE 'Malo'
        END AS calidad
     FROM muestras
     WHERE enlace = ? AND fecha = ?
       AND hora BETWEEN ? AND ?
       AND rtt_max >= 0"
);
$stmt_stats->bind_param("ssss", $enlace, $fecha, $hora_inicio, $hora_fin_completo);
$stmt_stats->execute();
$stats = $stmt_stats->get_result()->fetch_assoc();

$promedio       = $stats['promedio']       ?? 0;
$maximo         = $stats['maximo']         ?? 0;
$minimo         = $stats['minimo']         ?? 0;
$total_muestras = $stats['total_muestras'] ?? 0;
$pings_ok       = $stats['pings_exitosos'] ?? 0;
$pings_fail     = $stats['pings_fallidos'] ?? 0;
$stddev         = $stats['desviacion_std'] ?? 0;
$calidad        = $stats['calidad']        ?? 'Sin datos';

// ── CONSULTA 2: Detalle para el gráfico (DATE_FORMAT + IF anidados) ───────
$stmt_datos = $conn->prepare(
    "SELECT
        DATE_FORMAT(hora, '%H:%i') AS hora_fmt,
        ROUND(rtt_max, 3)          AS rtt,
        IF(rtt_max < 0, 'Sin respuesta',
           IF(rtt_max < 100, 'OK',
              IF(rtt_max < 200, 'Lento', 'Muy lento')
           )
        ) AS estado
     FROM muestras
     WHERE enlace = ? AND fecha = ?
       AND hora BETWEEN ? AND ?
     ORDER BY hora ASC"
);
$stmt_datos->bind_param("ssss", $enlace, $fecha, $hora_inicio, $hora_fin_completo);
$stmt_datos->execute();
$res_datos = $stmt_datos->get_result();

$filas = $horas_json_arr = $valores_json_arr = [];
while ($f = $res_datos->fetch_assoc()) {
    $filas[] = $f;
    if ($f['rtt'] >= 0) {
        $horas_json_arr[]   = $f['hora_fmt'];
        $valores_json_arr[] = (float)$f['rtt'];
    }
}
$cnt        = count($valores_json_arr);
$conn->close();

$horas_json   = json_encode($horas_json_arr);
$valores_json = json_encode($valores_json_arr);
$params_dl    = http_build_query(compact('enlace','fecha','hora_inicio','hora_fin'));

// Descarga TXT
if ($formato_dl === 'txt') {
    header('Content-Type: text/plain; charset=utf-8');
    header('Content-Disposition: attachment; filename="reporte_' . preg_replace('/[^a-z0-9]/i','_',$enlace) . '_' . $fecha . '.txt"');
    echo "REPORTE DE MONITOREO - ETN921\n=====================================\n";
    echo "Enlace: $enlace | Fecha: $fecha | Rango: $hora_inicio - $hora_fin\n";
    echo "AVG: $promedio ms | MAX: $maximo ms | MIN: $minimo ms | STDDEV: $stddev ms\n";
    echo "Calidad: $calidad | Exitosos: $pings_ok | Fallidos: $pings_fail\n\n";
    foreach ($filas as $f) echo "{$f['hora_fmt']} | {$f['rtt']} ms | {$f['estado']}\n";
    exit;
}

// Descarga CSV
if ($formato_dl === 'excel') {
    header('Content-Type: text/csv; charset=utf-8');
    header('Content-Disposition: attachment; filename="reporte_' . preg_replace('/[^a-z0-9]/i','_',$enlace) . '_' . $fecha . '.csv"');
    echo "\xEF\xBB\xBF";
    echo "Enlace;Fecha;Hora;RTT (ms);Estado\n";
    foreach ($filas as $f) echo "$enlace;$fecha;{$f['hora_fmt']};{$f['rtt']};{$f['estado']}\n";
    exit;
}

// Fix PHP 7.1: match() es PHP 8.0+, se usa switch
switch ($calidad) {
    case 'Excelente': $calidad_color = '#10b981'; break;
    case 'Bueno':     $calidad_color = '#3b82f6'; break;
    case 'Regular':   $calidad_color = '#f59e0b'; break;
    case 'Malo':      $calidad_color = '#ef4444'; break;
    default:          $calidad_color = '#6b7280';
}
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Reporte: <?php echo htmlspecialchars($enlace); ?></title>
    <link rel="stylesheet" href="estilos.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
</head>
<body>
<header>
    <div class="header-inner">
        <h1>&#9001; Reporte Grafico &#9002;</h1>
        <p class="subtitulo">ETN921 &mdash; Historial de RTT — Estadísticas calculadas con MySQL</p>
    </div>
</header>
<main>
    <section class="tarjeta">
        <h2>Enlace: <span class="resaltado"><?php echo htmlspecialchars($enlace); ?></span>
            <span style="float:right;background:<?php echo $calidad_color;?>;color:#000;font-size:0.75rem;padding:3px 12px;border-radius:20px;">
                <?php echo $calidad; ?>
            </span>
        </h2>
        <p>Fecha: <strong><?php echo $fecha; ?></strong> | Rango: <strong><?php echo $hora_inicio; ?> – <?php echo $hora_fin; ?></strong></p>

        <!-- Tarjetas de estadísticas (calculadas 100% en MySQL) -->
        <div class="stats-grid">
            <div class="stat"><span class="stat-num"><?php echo $maximo; ?></span><span class="stat-lbl">MAX() ms</span></div>
            <div class="stat"><span class="stat-num"><?php echo $promedio; ?></span><span class="stat-lbl">AVG() ms</span></div>
            <div class="stat"><span class="stat-num"><?php echo $minimo; ?></span><span class="stat-lbl">MIN() ms</span></div>
            <div class="stat"><span class="stat-num"><?php echo $stddev; ?></span><span class="stat-lbl">STDDEV() ms</span></div>
            <div class="stat"><span class="stat-num"><?php echo $pings_ok; ?></span><span class="stat-lbl">COUNT exitosos</span></div>
            <div class="stat"><span class="stat-num"><?php echo $pings_fail; ?></span><span class="stat-lbl">COUNT fallidos</span></div>
        </div>

        <!-- Botones de descarga -->
        <div class="botones-descarga">
            <a href="reporte.php?descargar=txt&<?php echo $params_dl; ?>" class="btn-dl btn-txt">&#8595; Descargar TXT</a>
            <a href="reporte.php?descargar=excel&<?php echo $params_dl; ?>" class="btn-dl btn-excel">&#8595; Descargar Excel (.csv)</a>
        </div>

        <?php if ($cnt > 0): ?>
        <!-- Gráfico de línea con Chart.js — datos inyectados como JSON desde PHP -->
        <div class="grafico-contenedor">
            <canvas id="grafico"></canvas>
        </div>
        <script>
        new Chart(document.getElementById('grafico').getContext('2d'), {
            type: 'line',
            data: {
                labels: <?php echo $horas_json; ?>,
                datasets: [{
                    label: 'RTT Maximo (ms) — <?php echo htmlspecialchars($enlace); ?>',
                    data: <?php echo $valores_json; ?>,
                    borderColor: '#00e5ff',
                    backgroundColor: 'rgba(0,229,255,0.10)',
                    borderWidth: 2, pointRadius: 4, tension: 0.3, fill: true
                }, {
                    label: 'Promedio AVG() = <?php echo $promedio; ?> ms',
                    data: Array(<?php echo $cnt; ?>).fill(<?php echo $promedio; ?>),
                    borderColor: '#f59e0b', borderWidth: 1,
                    borderDash: [6,4], pointRadius: 0, fill: false
                }]
            },
            options: {
                responsive: true,
                scales: {
                    x: { ticks:{color:'#aaa'}, grid:{color:'#2a2a2a'} },
                    y: { beginAtZero:true, ticks:{color:'#aaa', callback: function(v){ return v+' ms'; }}, grid:{color:'#2a2a2a'} }
                }
            }
        });
        </script>

        <!-- Tabla detalle con estado calculado por IF() de MySQL -->
        <table class="tabla-estado" style="margin-top:1.5rem;">
            <thead><tr><th>#</th><th>Hora (DATE_FORMAT)</th><th>RTT (ms)</th><th>Estado (IF)</th></tr></thead>
            <tbody>
            <?php foreach ($filas as $i => $f):
                $c = $f['rtt'] < 0 ? 'estado-error' : ($f['rtt'] < 100 ? 'estado-ok' : ($f['rtt'] < 200 ? 'estado-warn' : 'estado-error'));
            ?>
            <tr>
                <td><?php echo $i+1; ?></td>
                <td><?php echo $f['hora_fmt']; ?></td>
                <td><?php echo $f['rtt']; ?></td>
                <td class="<?php echo $c; ?>"><?php echo $f['estado']; ?></td>
            </tr>
            <?php endforeach; ?>
            </tbody>
        </table>
        <?php else: ?>
        <div class="sin-datos">Sin datos para este rango.</div>
        <?php endif; ?>

        <a href="index.php" class="btn-volver">&#8592; Nuevo reporte</a>
    </section>
</main>
<footer><p>Sistema de Monitoreo TCP/IP &mdash; ETN921 &mdash; <?php echo date('Y'); ?></p></footer>
</body>
</html>
```

---

## web\comparar.php

> Componente 3 — comparación de todos los enlaces.
> Recibe fecha y rango horario desde el formulario de [[index.php]].
> Consulta única con `GROUP BY enlace`, `AVG`, `MIN`, `MAX`, `STDDEV`, `COUNT`, `SUM(IF())`, `CASE`, `HAVING`, `ORDER BY promedio ASC` sobre la tabla de [[crear_bd.sql]].
> Renderiza diagrama de quesos (pie chart) y barras horizontal con Chart.js.
> Fix PHP 7.1: arrow functions `fn()` reemplazadas por `function(){}` (fn existe desde PHP 7.4).
> Fix PHP 7.1: `match()` reemplazado por `switch` para las medallas.
> Usa estilos de [[estilos.css]].

```php
<?php
// comparar.php — Comparación de los 10 enlaces — PHP 7.1
// Usa: AVG, MIN, MAX, STDDEV, COUNT, GROUP BY, HAVING, ORDER BY, IF, CASE

$DB_USER = "root";
$DB_PASS = "Mamacita.com921";
$DB_NAME = "monitoreo_red";

$fecha       = $_POST['fecha']       ?? ($_GET['fecha']       ?? date('Y-m-d'));
$hora_inicio = $_POST['hora_inicio'] ?? ($_GET['hora_inicio'] ?? '00:00');
$hora_fin    = $_POST['hora_fin']    ?? ($_GET['hora_fin']    ?? '23:59');
$enviado     = isset($_POST['fecha']) || isset($_GET['fecha']);

$datos_grafico = [];
$error_msg     = '';

if ($enviado) {
    $conn = new mysqli("localhost", $DB_USER, $DB_PASS, $DB_NAME);
    if ($conn->connect_error) {
        $error_msg = "Error de conexion: " . $conn->connect_error;
    } else {
        $hora_fin_completo = $hora_fin . ":59";

        // ── CONSULTA PRINCIPAL con GROUP BY ──────────────────────────────
        $stmt = $conn->prepare(
            "SELECT
                enlace,
                ROUND(AVG(rtt_max), 2)    AS promedio,
                ROUND(MIN(rtt_max), 2)    AS minimo,
                ROUND(MAX(rtt_max), 2)    AS maximo,
                ROUND(STDDEV(rtt_max), 2) AS desviacion,
                COUNT(*)                   AS total,
                SUM(IF(rtt_max >= 0, 1, 0)) AS exitosos,
                SUM(IF(rtt_max  < 0, 1, 0)) AS fallidos,
                CASE
                    WHEN AVG(rtt_max) < 50  THEN 'Excelente'
                    WHEN AVG(rtt_max) < 100 THEN 'Bueno'
                    WHEN AVG(rtt_max) < 200 THEN 'Regular'
                    ELSE 'Malo'
                END AS calidad
             FROM muestras
             WHERE fecha = ?
               AND hora BETWEEN ? AND ?
               AND rtt_max >= 0
             GROUP BY enlace
             HAVING COUNT(*) > 0
             ORDER BY promedio ASC"
        );
        $stmt->bind_param("sss", $fecha, $hora_inicio, $hora_fin_completo);
        $stmt->execute();
        $res = $stmt->get_result();
        while ($f = $res->fetch_assoc()) $datos_grafico[] = $f;
        $conn->close();

        if (empty($datos_grafico))
            $error_msg = "No hay datos para esa fecha y rango de horas.";
    }
}

$labels    = array_column($datos_grafico, 'enlace');
$promedios = array_column($datos_grafico, 'promedio');

$colores = [
    'rgba(0,229,255,0.85)',  'rgba(124,58,237,0.85)',
    'rgba(16,185,129,0.85)', 'rgba(245,158,11,0.85)',
    'rgba(239,68,68,0.85)',  'rgba(59,130,246,0.85)',
    'rgba(236,72,153,0.85)', 'rgba(132,204,22,0.85)',
    'rgba(249,115,22,0.85)', 'rgba(20,184,166,0.85)',
];

// Fix PHP 7.1: fn() existe desde PHP 7.4 — se usa function() normal
$borders = array_map(function($c) { return str_replace('0.85', '1', $c); }, $colores);

$labels_json    = json_encode($labels);
$promedios_json = json_encode($promedios);
$colores_json   = json_encode(array_slice($colores, 0, count($labels)));
$borders_json   = json_encode(array_slice($borders, 0, count($labels)));
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Comparacion de enlaces — ETN921</title>
    <link rel="stylesheet" href="estilos.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
</head>
<body>
<header>
    <div class="header-inner">
        <h1>&#9685; Comparacion de los 10 enlaces</h1>
        <p class="subtitulo">ETN921 &mdash; Diagrama de quesos con AVG() + GROUP BY de MySQL</p>
    </div>
</header>
<main>
    <!-- Formulario de filtro -->
    <section class="tarjeta">
        <h2>&#9998; Seleccionar rango para comparar</h2>
        <form method="POST" action="comparar.php" class="form-reporte">
            <div class="fila-form">
                <label>Fecha:</label>
                <input type="date" name="fecha" value="<?php echo htmlspecialchars($fecha); ?>" required>
            </div>
            <div class="fila-form">
                <label>Hora inicio:</label>
                <input type="time" name="hora_inicio" value="<?php echo htmlspecialchars($hora_inicio); ?>" required>
            </div>
            <div class="fila-form">
                <label>Hora fin:</label>
                <input type="time" name="hora_fin" value="<?php echo htmlspecialchars($hora_fin); ?>" required>
            </div>
            <button type="submit" class="btn-reporte">Generar comparacion</button>
        </form>
    </section>

    <?php if (!empty($error_msg)): ?>
    <section class="tarjeta">
        <div class="sin-datos"><?php echo htmlspecialchars($error_msg); ?></div>
    </section>

    <?php elseif (!empty($datos_grafico)): ?>
    <!-- Gráficos -->
    <section class="tarjeta">
        <h2>&#9685; Diagrama de quesos — Promedio RTT por enlace</h2>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;">
            <div><canvas id="pieChart"></canvas></div>
            <div><canvas id="barChart" style="max-height:340px;"></canvas></div>
        </div>
        <script>
        var labels    = <?php echo $labels_json; ?>;
        var promedios = <?php echo $promedios_json; ?>;
        var colores   = <?php echo $colores_json; ?>;
        var borders   = <?php echo $borders_json; ?>;

        new Chart(document.getElementById('pieChart').getContext('2d'), {
            type: 'pie',
            data: { labels: labels, datasets: [{ data: promedios, backgroundColor: colores, borderColor: borders, borderWidth: 1.5 }] },
            options: { responsive: true, plugins: { legend: { position:'bottom', labels:{ color:'#ccc', font:{size:11} } } } }
        });

        new Chart(document.getElementById('barChart').getContext('2d'), {
            type: 'bar',
            data: { labels: labels, datasets: [{ label:'RTT Promedio AVG() ms', data: promedios, backgroundColor: colores, borderColor: borders, borderWidth:1 }] },
            options: { indexAxis:'y', responsive:true, plugins:{ legend:{display:false} },
                       scales:{ x:{ beginAtZero:true, ticks:{color:'#aaa', callback:function(v){return v+' ms';}}, grid:{color:'#2a2a2a'} },
                                y:{ ticks:{color:'#ccc'}, grid:{color:'#1a1a2a'} } } }
        });
        </script>
    </section>

    <!-- Tabla de ranking -->
    <section class="tarjeta">
        <h2>&#127942; Ranking de rendimiento — resultados de MySQL</h2>
        <table class="tabla-estado" style="font-size:0.82rem;">
            <thead>
                <tr>
                    <th>Pos.</th><th>Enlace</th><th>AVG() ms</th><th>MIN() ms</th>
                    <th>MAX() ms</th><th>STDDEV() ms</th><th>COUNT(*)</th><th>Fallidos</th><th>Calidad</th>
                </tr>
            </thead>
            <tbody>
            <?php foreach ($datos_grafico as $i => $d):
                // Fix PHP 7.1: match() es PHP 8.0+, se usa switch
                switch ($i) {
                    case 0:  $medal = '🥇'; break;
                    case 1:  $medal = '🥈'; break;
                    case 2:  $medal = '🥉'; break;
                    default: $medal = ($i + 1) . '.';
                }
            ?>
            <tr>
                <td><?php echo $medal; ?></td>
                <td style="font-family:var(--mono);color:var(--acento);"><?php echo htmlspecialchars($d['enlace']); ?></td>
                <td><strong><?php echo $d['promedio']; ?></strong></td>
                <td class="estado-ok"><?php echo $d['minimo']; ?></td>
                <td class="estado-error"><?php echo $d['maximo']; ?></td>
                <td style="color:#f59e0b;"><?php echo $d['desviacion']; ?></td>
                <td><?php echo $d['exitosos']; ?></td>
                <td class="<?php echo $d['fallidos']>0?'estado-error':'estado-ok'; ?>"><?php echo $d['fallidos']; ?></td>
                <td><?php echo $d['calidad']; ?></td>
            </tr>
            <?php endforeach; ?>
            </tbody>
        </table>
    </section>
    <?php endif; ?>

    <div style="text-align:center;margin-top:0.5rem;">
        <a href="index.php" class="btn-volver">&#8592; Volver al menu principal</a>
    </div>
</main>
<footer><p>Sistema de Monitoreo TCP/IP &mdash; ETN921 &mdash; <?php echo date('Y'); ?></p></footer>
</body>
</html>
```

---

## web\estilos.css

> Hoja de estilos compartida por todas las páginas PHP.
> Define variables CSS (tema oscuro, colores semánticos OK/warn/error, tipografías).
> Usada por [[index.php]], [[ping_online.php]], [[ping_manual.php]], [[reporte.php]], [[comparar.php]] y [[gestionar_enlaces.php]].

```css
/* ============================================================
   estilos.css — Sistema de Monitoreo TCP/IP — ETN921
   ============================================================ */

@import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Exo+2:wght@300;500;700&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
    --fondo:      #0a0f1a;
    --superficie: #111827;
    --borde:      #1e3a5f;
    --acento:     #00e5ff;
    --acento2:    #7c3aed;
    --texto:      #d1d5db;
    --texto-dim:  #6b7280;
    --ok:         #10b981;
    --warn:       #f59e0b;
    --error:      #ef4444;
    --mono:       'Share Tech Mono', monospace;
    --sans:       'Exo 2', sans-serif;
}

body {
    font-family: var(--sans);
    background: var(--fondo);
    color: var(--texto);
    min-height: 100vh;
    background-image:
        radial-gradient(ellipse at 20% 0%, rgba(0,229,255,0.05) 0%, transparent 60%),
        radial-gradient(ellipse at 80% 100%, rgba(124,58,237,0.05) 0%, transparent 60%);
}

header {
    border-bottom: 1px solid var(--borde);
    background: rgba(0,0,0,0.4);
    backdrop-filter: blur(8px);
    padding: 1.5rem 2rem;
}
.header-inner { max-width: 1100px; margin: 0 auto; }
header h1 {
    font-size: 1.8rem; font-weight: 700;
    color: var(--acento); letter-spacing: 2px;
    font-family: var(--mono);
}
.subtitulo { color: var(--texto-dim); font-size: 0.85rem; margin-top: 0.2rem; }

main {
    max-width: 1100px; margin: 2rem auto;
    padding: 0 1.5rem;
    display: flex; flex-direction: column; gap: 1.5rem;
}

.tarjeta {
    background: var(--superficie);
    border: 1px solid var(--borde);
    border-radius: 12px;
    padding: 1.8rem 2rem;
}
.tarjeta h2 {
    font-size: 1.1rem; font-weight: 500;
    color: var(--acento);
    border-left: 3px solid var(--acento);
    padding-left: 0.7rem; margin-bottom: 1rem;
    font-family: var(--mono);
}

.grid-enlaces {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
    gap: 0.6rem; margin-bottom: 1.2rem;
}
.btn-enlace {
    display: block;
    background: rgba(0,229,255,0.07);
    border: 1px solid var(--borde);
    border-radius: 8px; padding: 0.6rem 0.8rem;
    color: var(--acento); text-decoration: none;
    font-size: 0.8rem; font-family: var(--mono);
    text-align: center;
    transition: background 0.2s, border-color 0.2s;
}
.btn-enlace:hover { background: rgba(0,229,255,0.18); border-color: var(--acento); }

button, .btn-reporte {
    background: var(--acento); color: #000;
    border: none; border-radius: 8px;
    padding: 0.55rem 1.4rem;
    font-weight: 700; font-family: var(--sans);
    font-size: 0.9rem; cursor: pointer;
    transition: opacity 0.2s;
}
button:hover, .btn-reporte:hover { opacity: 0.85; }

.resultado-ping {
    background: #050a12;
    border: 1px solid var(--borde);
    border-radius: 8px; padding: 1rem 1.2rem; margin: 0.8rem 0;
}
.resultado-ping pre {
    font-family: var(--mono); font-size: 0.82rem;
    color: #7dd3fc; white-space: pre-wrap; line-height: 1.6;
}
.rtt-badge {
    display: inline-block;
    background: rgba(0,229,255,0.12);
    color: var(--acento); border: 1px solid var(--acento);
    border-radius: 20px; padding: 0.25rem 1rem;
    font-family: var(--mono); font-size: 0.85rem; margin-bottom: 0.8rem;
}

.tabla-estado { width: 100%; border-collapse: collapse; font-size: 0.85rem; }
.tabla-estado th {
    background: rgba(0,229,255,0.07); color: var(--acento);
    padding: 0.6rem 0.8rem; text-align: left;
    border-bottom: 1px solid var(--borde); font-family: var(--mono);
}
.tabla-estado td { padding: 0.55rem 0.8rem; border-bottom: 1px solid rgba(30,58,95,0.5); }

.estado-ok    { color: var(--ok);    font-weight: 500; }
.estado-warn  { color: var(--warn);  font-weight: 500; }
.estado-error { color: var(--error); font-weight: 500; }

.stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(130px, 1fr));
    gap: 0.8rem; margin: 1rem 0;
}
.stat {
    background: rgba(0,229,255,0.05);
    border: 1px solid var(--borde);
    border-radius: 8px; padding: 0.8rem 1rem; text-align: center;
}
.stat-num { display: block; font-size: 1.4rem; color: var(--acento); font-family: var(--mono); }
.stat-lbl { display: block; font-size: 0.75rem; color: var(--texto-dim); margin-top: 0.2rem; }

.grafico-contenedor {
    background: #050a12;
    border: 1px solid var(--borde);
    border-radius: 8px; padding: 1rem; margin-top: 0.5rem;
}

.botones-descarga { display: flex; gap: 0.7rem; flex-wrap: wrap; margin: 0.8rem 0 1.2rem; }
.btn-dl {
    display: inline-flex; align-items: center; gap: 0.4rem;
    padding: 0.5rem 1.2rem; border-radius: 8px;
    font-size: 0.85rem; font-family: var(--mono);
    text-decoration: none; font-weight: 500;
    transition: opacity 0.2s; border: 1px solid;
}
.btn-txt   { background: rgba(16,185,129,0.12); color: var(--ok);   border-color: var(--ok); }
.btn-excel { background: rgba(245,158,11,0.12);  color: var(--warn); border-color: var(--warn); }

.sin-datos {
    background: rgba(245,158,11,0.08);
    border: 1px solid rgba(245,158,11,0.3);
    border-radius: 8px; color: var(--warn);
    padding: 1rem; font-size: 0.88rem; margin-top: 0.5rem;
}

footer {
    text-align: center; color: var(--texto-dim);
    font-size: 0.78rem; padding: 2rem;
    border-top: 1px solid var(--borde); margin-top: 2rem;
}

@media (max-width: 600px) {
    header h1 { font-size: 1.2rem; }
    .tarjeta  { padding: 1.2rem; }
    .grid-enlaces { grid-template-columns: repeat(2, 1fr); }
}
```
