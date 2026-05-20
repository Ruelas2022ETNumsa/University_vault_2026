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
REM    MySQL 8.0 instalado con el instalador oficial:
set "MYSQL_BIN=C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe"
REM    Fallback: si pusiste MySQL en c:\mariadb\ siguiendo el PDF del docente
if not exist "%MYSQL_BIN%" set "MYSQL_BIN=C:\mariadb\bin\mysql.exe"
REM    Ultimo recurso: que este en PATH
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
echo.
echo ┌──────────────────────────────────────────────────────────┐
echo │  SCRIPT 1: tomar_muestra.bat                             │
echo │  Hace ping a los 10 enlaces y guarda en archivo TXT      │
echo └──────────────────────────────────────────────────────────┘
echo.
type "%SCRIPTS%\tomar_muestra.bat"
echo.
echo ┌──────────────────────────────────────────────────────────┐
echo │  SCRIPT 2: cargar_bd.bat                                 │
echo │  Lee el archivo TXT e inserta las muestras en la BD      │
echo └──────────────────────────────────────────────────────────┘
echo.
type "%SCRIPTS%\cargar_bd.bat"
echo.
pause
goto MENU

REM ════════════════════════════════════════════════════════════
REM  OPCION 2 - Activar/desactivar tareas con Task Scheduler
REM ════════════════════════════════════════════════════════════
:GESTIONAR_CRON
cls
echo ══ OPCION 2: Activar monitoreo automatico (Task Scheduler) ══
echo.
echo   Se programaran dos tareas:
echo   - Cada 5 minutos: tomar_muestra.bat  (guarda en archivo TXT)
echo   - Cada 1 hora   : cargar_bd.bat      (inserta 12 muestras en BD)
echo.
echo   1) Activar tareas (crear en Task Scheduler)
echo   2) Ver tareas actuales
echo   3) Desactivar tareas (eliminar de Task Scheduler)
echo   0) Volver al menu principal
echo.
set /p "SUB=  Elige una opcion: "

if "%SUB%"=="1" (
    echo.
    echo   Creando tareas en el Task Scheduler...
    echo   (Corren con tu usuario actual: %USERNAME%, sin pedir contrasena)
    echo.

    REM Sin /RU ni /RP: schtasks usa el usuario actual y no pide contrasena.
    REM La tarea corre cuando estas logueado (que es el caso siempre).
    schtasks /Create /SC MINUTE /MO 1 /TN "MonitoreoRed_Muestra" /TR "\"%SCRIPTS%\tomar_muestra.bat\"" /F
    if !errorlevel! equ 0 (
        echo   [OK] Tarea de muestreo creada ^(cada 5 minutos^)
    ) else (
        echo   [ERROR] No se pudo crear la tarea de muestreo
        echo          Asegurate de ejecutar este menu como Administrador.
    )
    schtasks /Create /SC MINUTE /MO 2 /TN "MonitoreoRed_Carga" /TR "\"%SCRIPTS%\cargar_bd.bat\"" /F
    if !errorlevel! equ 0 (
        echo   [OK] Tarea de carga creada ^(cada hora^)
    ) else (
        echo   [ERROR] No se pudo crear la tarea de carga
    )
    echo.
    echo   IMPORTANTE: Las tareas de Task Scheduler tienen por defecto
    echo   la condicion "solo correr si esta enchufada a corriente AC".
    echo   Si tu laptop esta a bateria, las tareas NO se disparan.
    echo   Tenes dos opciones:
    echo     1^) Dejar la laptop enchufada cuando este monitoreando.
    echo     2^) Abrir Task Scheduler ^(taskschd.msc^), buscar las dos
    echo        tareas, click derecho -^> Properties -^> Conditions,
    echo        y desmarcar la opcion de "AC power".
    echo.
    echo   Para probar la tarea ahora sin esperar 5 min:
    echo     schtasks /Run /TN "MonitoreoRed_Muestra"
)
if "%SUB%"=="2" (
    echo.
    echo   Tareas actuales:
    echo   ──────────────────────────────────────────────────────
    schtasks /Query /TN "MonitoreoRed_Muestra" 2>nul || echo   (Tarea de muestreo no existe)
    echo.
    schtasks /Query /TN "MonitoreoRed_Carga" 2>nul || echo   (Tarea de carga no existe)
    echo   ──────────────────────────────────────────────────────
)
if "%SUB%"=="3" (
    schtasks /Delete /TN "MonitoreoRed_Muestra" /F 2>nul
    schtasks /Delete /TN "MonitoreoRed_Carga" /F 2>nul
    echo   [OK] Tareas eliminadas del Task Scheduler.
)
if "%SUB%"=="0" goto MENU
echo.
pause
goto MENU

REM ════════════════════════════════════════════════════════════
REM  OPCION 3 - Ver script SQL y crear la base de datos
REM ════════════════════════════════════════════════════════════
:GESTIONAR_BD
cls
echo ══ OPCION 3: Base de datos MySQL ══
echo.
echo   Cliente MySQL: %MYSQL_BIN%
echo   Script SQL  : %SQL%\crear_bd.sql
echo.
type "%SQL%\crear_bd.sql"
echo.
echo   1) CREAR BASE DE DATOS (ejecutar el script SQL)
echo   2) Verificar si la BD ya existe
echo   3) Borrar tabla muestras (para pruebas)
echo   4) Fix auth MySQL 8 ^<-^> PHP 7.1  (IMPORTANTE: ejecutar 1 vez ANTES de crear la BD)
echo   0) Volver al menu principal
echo.
set /p "SUB=  Elige una opcion: "

if "%SUB%"=="1" (
    echo.
    echo   Ejecutando script SQL con usuario: %DB_USER%
    "%MYSQL_BIN%" -u %DB_USER% -p%DB_PASS% < "%SQL%\crear_bd.sql"
    if !errorlevel! equ 0 (
        echo   [OK] Base de datos y tabla creadas correctamente.
    ) else (
        echo   [ERROR] Verifica:
        echo          - Que mysql.exe exista en: %MYSQL_BIN%
        echo          - Que la contrasena sea correcta
        echo          - Que el servicio MySQL este corriendo
    )
)
if "%SUB%"=="2" (
    "%MYSQL_BIN%" -u %DB_USER% -p%DB_PASS% -e "SHOW DATABASES LIKE 'monitoreo_red';"
)
if "%SUB%"=="3" (
    "%MYSQL_BIN%" -u %DB_USER% -p%DB_PASS% monitoreo_red -e "TRUNCATE TABLE muestras;"
    echo   [OK] Tabla vaciada.
)
if "%SUB%"=="4" (
    echo.
    echo   Ejecutando fix de autenticacion para MySQL 8 + PHP 7.1...
    "%MYSQL_BIN%" -u %DB_USER% -p%DB_PASS% < "%SQL%\fix_auth_php71.sql"
    if !errorlevel! equ 0 (
        echo   [OK] Usuario root ahora usa mysql_native_password.
        echo   PHP 7.1 podra conectar sin problemas.
    ) else (
        echo   [ERROR] No se pudo aplicar el fix.
    )
)
if "%SUB%"=="0" goto MENU
echo.
pause
goto MENU

REM ════════════════════════════════════════════════════════════
REM  OPCION 4 - Instalar archivos web en IIS (inetpub\wwwroot)
REM ════════════════════════════════════════════════════════════
:INSTALAR_WEB
cls
echo ══ OPCION 4: Instalar interfaz web en IIS ══
echo.
echo   Los archivos PHP/HTML/BAT se copiaran a:
echo   %WEB_DEST%
echo.
echo   Tambien se creara la subcarpeta reportWEB
echo.
echo   1) Instalar / actualizar archivos web
echo   2) Ver estado de IIS
echo   0) Volver al menu principal
echo.
set /p "SUB=  Elige una opcion: "

if "%SUB%"=="1" (
    if not exist "%WEB_DEST%" mkdir "%WEB_DEST%"
    if not exist "%WEB_DEST%\reportWEB" mkdir "%WEB_DEST%\reportWEB"

    REM Si ya existe una copia "viva" de enlaces.txt en IIS (porque
    REM el usuario edito enlaces desde la web), la preservamos.
    set "PRESERVAR_ENLACES=0"
    if exist "%WEB_DEST%\enlaces.txt" (
        copy /Y "%WEB_DEST%\enlaces.txt" "%TEMP%\enlaces_backup.txt" >nul
        set "PRESERVAR_ENLACES=1"
    )

    xcopy /Y /E "%DIR%\web\*" "%WEB_DEST%\" >nul
    if !errorlevel! equ 0 (
        echo   [OK] Archivos web instalados en %WEB_DEST%

        REM Restaurar enlaces.txt editado por el usuario si existia
        if "!PRESERVAR_ENLACES!"=="1" (
            copy /Y "%TEMP%\enlaces_backup.txt" "%WEB_DEST%\enlaces.txt" >nul
            del "%TEMP%\enlaces_backup.txt" >nul 2>&1
            echo   [OK] Lista de enlaces editada por el usuario preservada.
        )

        REM Dar permisos a IIS (IIS_IUSRS) sobre la carpeta del proyecto.
        REM Sobre reportWEB damos permiso de ESCRITURA tambien (para los .bat).
        REM Sobre enlaces.txt damos permiso de MODIFICACION para que
        REM gestionar_enlaces.php pueda agregar/quitar enlaces desde la web.
        echo   Configurando permisos para IIS_IUSRS...
        icacls "%WEB_DEST%" /grant "IIS_IUSRS:(OI)(CI)RX" /T >nul 2>&1
        icacls "%WEB_DEST%\reportWEB" /grant "IIS_IUSRS:(OI)(CI)M" /T >nul 2>&1
        icacls "%WEB_DEST%\enlaces.txt" /grant "IIS_IUSRS:M" >nul 2>&1
        echo   [OK] Permisos asignados.

        echo.
        echo   Abre tu navegador en: http://localhost/monitoreo/
        echo.
        echo   IMPORTANTE: Si IIS no encuentra index.php, agregalo como
        echo   Default Document desde el IIS Manager ^(ver paso 9 del PDF
        echo   de instalacion^).
    ) else (
        echo   [ERROR] No se pudieron copiar los archivos.
        echo   Ejecuta este menu como Administrador.
    )
)
if "%SUB%"=="2" (
    echo.
    echo   Servicio W3SVC ^(IIS^):
    sc query W3SVC 2>nul | findstr "STATE"
    echo.
    echo   Si IIS no esta corriendo, abre "Internet Information Services (IIS) Manager"
    echo   o ejecuta:   iisreset /start
)
if "%SUB%"=="0" goto MENU
echo.
pause
goto MENU

REM ════════════════════════════════════════════════════════════
REM  OPCION 5 - Prueba manual de ping
REM ════════════════════════════════════════════════════════════
:PING_MANUAL
cls
echo ══ OPCION 5: Prueba manual de ping ══
echo.
set /p "DEST=  Direccion (ej: www.google.com): "
echo.
if "%DEST%"=="" (
    echo   No ingresaste ninguna direccion.
) else (
    echo   Haciendo ping a %DEST% ^(5 paquetes^)...
    echo   ──────────────────────────────────────────────────────
    ping -n 5 %DEST%
    echo   ──────────────────────────────────────────────────────
)
echo.
pause
goto MENU

REM ════════════════════════════════════════════════════════════
REM  OPCION 6 - Resetear todo
REM ════════════════════════════════════════════════════════════
:RESETEAR
cls
echo ══ OPCION 6: Resetear el sistema completo ══
echo.
echo   Esta opcion hara LO SIGUIENTE (irreversible):
echo     - Eliminar la base de datos 'monitoreo_red' completa
echo     - Borrar los archivos web de %WEB_DEST%
echo     - Desactivar las tareas del Task Scheduler
echo     - Vaciar el archivo de muestras temporales
echo.
set /p "CONFIRM=  Estas SEGURO? Escribe 'SI' para confirmar: "

if /I not "%CONFIRM%"=="SI" (
    echo.
    echo   Operacion cancelada. No se borro nada.
    pause
    goto MENU
)

echo.
echo   Ejecutando reseteo...
echo.
echo   [1/4] Eliminando base de datos monitoreo_red...
"%MYSQL_BIN%" -u %DB_USER% -p%DB_PASS% -e "DROP DATABASE IF EXISTS monitoreo_red;" 2>nul

echo   [2/4] Borrando archivos web en %WEB_DEST%...
if exist "%WEB_DEST%" rmdir /S /Q "%WEB_DEST%"

echo   [3/4] Desactivando tareas del Task Scheduler...
schtasks /Delete /TN "MonitoreoRed_Muestra" /F 2>nul
schtasks /Delete /TN "MonitoreoRed_Carga" /F 2>nul

echo   [4/4] Limpiando archivos de muestras temporales...
type nul > "%SCRIPTS%\muestras_temp.txt" 2>nul
type nul > "%SCRIPTS%\muestras_procesadas.txt" 2>nul

echo.
echo   [OK] Reseteo completo. El sistema quedo limpio.
echo.
pause
goto MENU

REM ════════════════════════════════════════════════════════════
REM  OPCION 7 - Subir archivo de prueba a la BD
REM ════════════════════════════════════════════════════════════
:SUBIR_ARCHIVO
cls
echo ══ OPCION 7: Subir archivo de datos a la BD ══
echo.
set "ARCHIVO_PRUEBA=%SQL%\prueba.txt"

echo   Formato del archivo sql\prueba.txt:
echo   ──────────────────────────────────────────────────────────
echo     FECHA^|HORA^|ENLACE^|RTT_MAX
echo     2025-04-07^|08:00:00^|www.google.com^|12.345
echo     2025-04-07^|08:00:00^|www.google.com^|-1   (usa -1 si no hubo respuesta)
echo   ──────────────────────────────────────────────────────────
echo.

if not exist "%ARCHIVO_PRUEBA%" (
    echo   [WARN] No se encontro %ARCHIVO_PRUEBA%
    echo   Asegurate de que exista o copialo desde el zip original.
    pause
    goto MENU
)

echo   Contenido actual de prueba.txt:
echo   ──────────────────────────────────────────────────────────
type "%ARCHIVO_PRUEBA%"
echo   ──────────────────────────────────────────────────────────
echo.
echo   1) Subir este archivo a la BD ahora
echo   2) Editar el archivo (Notepad)
echo   0) Volver al menu principal
echo.
set /p "SUB=  Elige una opcion: "

if "%SUB%"=="1" (
    echo.
    echo   Insertando datos en la BD...
    set "INSERTADOS=0"
    set "ERRORES=0"
    for /f "usebackq tokens=1,2,3,4 delims=|" %%A in ("%ARCHIVO_PRUEBA%") do (
        if not "%%A"=="" (
            "%MYSQL_BIN%" -u %DB_USER% -p%DB_PASS% monitoreo_red -e "INSERT INTO muestras (enlace, fecha, hora, rtt_max) VALUES ('%%C', '%%A', '%%B', '%%D');" 2>nul
            if !errorlevel! equ 0 (
                set /a INSERTADOS+=1
            ) else (
                set /a ERRORES+=1
            )
        )
    )
    echo.
    echo   [OK] Insertados: !INSERTADOS! registros
    if !ERRORES! gtr 0 echo   [ERR] Errores:   !ERRORES! registros ^(verifica que la BD existe^)
    echo.
    echo   Ahora abre la pagina web para ver los datos y las graficas.
)
if "%SUB%"=="2" (
    notepad "%ARCHIVO_PRUEBA%"
)
if "%SUB%"=="0" goto MENU
echo.
pause
goto MENU

REM ════════════════════════════════════════════════════════════
REM  OPCION 8 - Gestionar lista de enlaces
REM ════════════════════════════════════════════════════════════
:GESTIONAR_ENLACES
cls
echo ══ OPCION 8: Gestionar lista de enlaces a monitorear ══
echo.
set "ARCHIVO_ENLACES=%DIR%\web\enlaces.txt"

if not exist "%ARCHIVO_ENLACES%" (
    echo   [ERROR] No se encuentra %ARCHIVO_ENLACES%
    pause
    goto MENU
)

REM Mostrar enlaces actuales numerados (ignorando comentarios y vacios)
echo   Enlaces actuales:
echo   ──────────────────────────────────────────────
set "COUNT=0"
for /f "usebackq eol=# tokens=*" %%E in ("%ARCHIVO_ENLACES%") do (
    if not "%%E"=="" (
        set /a COUNT+=1
        if !COUNT! lss 10 (
            echo     0!COUNT!^) %%E
        ) else (
            echo     !COUNT!^) %%E
        )
    )
)
echo   ──────────────────────────────────────────────
echo   Total: !COUNT! enlaces
echo.
echo   1) Agregar un enlace nuevo
echo   2) Quitar un enlace
echo   3) Editar manualmente (Notepad)
echo   4) Restaurar lista original de 10 enlaces
echo   0) Volver al menu principal
echo.
set /p "SUB=  Elige una opcion: "

if "%SUB%"=="1" goto AGREGAR_ENLACE
if "%SUB%"=="2" goto QUITAR_ENLACE
if "%SUB%"=="3" goto EDITAR_ENLACES
if "%SUB%"=="4" goto RESTAURAR_ENLACES
if "%SUB%"=="0" goto MENU
echo   Opcion invalida.
pause
goto GESTIONAR_ENLACES

:AGREGAR_ENLACE
echo.
set /p "NUEVO=  Dominio o IP a agregar (ej: www.umsa.bo): "
if "!NUEVO!"=="" (
    echo   Cancelado.
    pause
    goto GESTIONAR_ENLACES
)
REM Verificar si ya existe
findstr /B /I /C:"!NUEVO!" "%ARCHIVO_ENLACES%" >nul 2>&1
if !errorlevel! equ 0 (
    echo   [WARN] El enlace "!NUEVO!" ya esta en la lista.
    pause
    goto GESTIONAR_ENLACES
)
echo !NUEVO!>> "%ARCHIVO_ENLACES%"
echo   [OK] Agregado: !NUEVO!
call :SINCRONIZAR_WEB
pause
goto GESTIONAR_ENLACES

:QUITAR_ENLACE
echo.
set /p "QUITAR=  Dominio exacto a quitar (ej: www.google.com): "
if "!QUITAR!"=="" (
    echo   Cancelado.
    pause
    goto GESTIONAR_ENLACES
)
REM Verificar si existe
findstr /B /I /C:"!QUITAR!" "%ARCHIVO_ENLACES%" >nul 2>&1
if !errorlevel! neq 0 (
    echo   [WARN] El enlace "!QUITAR!" no esta en la lista.
    pause
    goto GESTIONAR_ENLACES
)
REM Generar archivo nuevo sin la linea a quitar
set "TMP_FILE=%ARCHIVO_ENLACES%.tmp"
if exist "%TMP_FILE%" del "%TMP_FILE%"
for /f "usebackq delims=" %%L in ("%ARCHIVO_ENLACES%") do (
    set "LINEA=%%L"
    REM No escribir la linea a quitar (compara con espacios tambien)
    if /I not "!LINEA!"=="!QUITAR!" (
        echo !LINEA!>> "%TMP_FILE%"
    )
)
move /Y "%TMP_FILE%" "%ARCHIVO_ENLACES%" >nul
echo   [OK] Removido: !QUITAR!
call :SINCRONIZAR_WEB
pause
goto GESTIONAR_ENLACES

:EDITAR_ENLACES
notepad "%ARCHIVO_ENLACES%"
echo   Si hiciste cambios, sincronizando con la web...
call :SINCRONIZAR_WEB
goto GESTIONAR_ENLACES

:RESTAURAR_ENLACES
echo.
set /p "CONF=  Esto sobrescribira tu lista actual. Continuar? (S/N): "
if /I not "!CONF!"=="S" (
    echo   Cancelado.
    pause
    goto GESTIONAR_ENLACES
)
(
    echo # Lista de enlaces a monitorear ^(uno por linea^)
    echo # Lineas que empiezan con # son comentarios
    echo.
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
echo   [OK] Lista original restaurada (10 enlaces).
call :SINCRONIZAR_WEB
pause
goto GESTIONAR_ENLACES

REM ── Sincronizar enlaces.txt con la copia en wwwroot ─────────
:SINCRONIZAR_WEB
if exist "%WEB_DEST%\enlaces.txt" (
    copy /Y "%ARCHIVO_ENLACES%" "%WEB_DEST%\enlaces.txt" >nul
    echo   [OK] Sincronizado con %WEB_DEST%\enlaces.txt
)
exit /b 0

REM ════════════════════════════════════════════════════════════
:SALIR
echo.
echo   Hasta luego!
echo.
endlocal
exit /b 0
