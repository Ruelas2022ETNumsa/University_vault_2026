@echo off
:: ==============================================================================
:: patch-obsidian.bat
:: Lanzador del patcher para Tags Routes - Obsidian
:: Coloca este archivo junto a patch-obsidian.ps1
:: Ejecutar con Obsidian CERRADO
:: ==============================================================================

title Tags Routes Patcher

echo.
echo  Asegurate de que Obsidian este CERRADO antes de continuar.
echo.
pause

powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0patch-obsidian.ps1"

if %ERRORLEVEL% EQU 0 (
    echo.
    echo  Todo salio bien. Cerrando en 3 segundos...
    timeout /t 3 /nobreak >nul
) else (
    echo.
    echo  Hubo un error. Revisa los mensajes anteriores.
    pause
)