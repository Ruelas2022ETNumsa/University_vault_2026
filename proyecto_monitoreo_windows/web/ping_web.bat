@echo off
REM ============================================================
REM  ping_web.bat
REM
REM  Llamado desde PHP (Componente 2 del proyecto ETN921) via
REM  shell_exec(). Esto cumple con la arquitectura pedida en
REM  la especificacion:
REM
REM      navegador --GET--^> PHP --shell_exec--^> .bat --^> ping
REM
REM  Uso:    ping_web.bat ^<direccion^>
REM  Ej:     ping_web.bat www.rfi.fr
REM
REM  Devuelve la salida del comando ping por stdout, que PHP
REM  captura y muestra al usuario.
REM ============================================================

setlocal

set "DESTINO=%~1"

REM Validacion basica de entrada
if "%DESTINO%"=="" (
    echo ERROR: No se proporciono direccion.
    exit /b 1
)

REM Ping con 3 paquetes (rapido para respuesta web)
REM En Windows:  -n = numero de paquetes,  -w = timeout en ms
ping -n 3 -w 5000 %DESTINO%

REM El parseo del RTT maximo lo hace PHP (ping_helper.php)
REM porque maneja mejor el formato espanol/ingles.

endlocal
exit /b 0
