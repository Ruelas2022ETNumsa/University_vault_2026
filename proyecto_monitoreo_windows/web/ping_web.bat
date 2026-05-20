@echo off
REM ping_web.bat
REM Ejecuta ping desde Windows y devuelve el resultado a PHP.
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

REM PHP procesa la salida y calcula el RTT maximo

endlocal
exit /b 0
