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

echo.
pause
