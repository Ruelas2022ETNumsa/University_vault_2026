# tars-sync

Comandos de Shell Commands para copiar el archivo activo en Obsidian a la carpeta del HP Connectivity Kit.

## Tipo
xcopy nativo de CMD — sin script externo, sin Python, sin dependencias.

## Comandos registrados en Shell Commands

### TARS: Enviar a CASE
- **Shell:** cmd.exe
- **Comando:**
  ```
  xcopy /Y "{{file_path:absolute}}" "C:\Users\USUARIO\Documents\HP Connectivity Kit\Calculadoras\CASE\"
  ```
- **stdout:** Notification balloon
- **stderr:** Notification balloon

### TARS: Enviar a TARS
- **Shell:** cmd.exe
- **Comando:**
  ```
  xcopy /Y "{{file_path:absolute}}" "C:\Users\USUARIO\Documents\HP Connectivity Kit\Calculadoras\TARS\"
  ```
- **stdout:** Notification balloon
- **stderr:** Notification balloon

## Trigger
Manual — Ctrl+P → alias → ejecución instantánea.
Futuro: botones via Commander.

## Notas
- /Y sobreescribe sin pedir confirmación si el archivo ya existe.
- Aplica a cualquier extensión: .hpprgm, .py, .hpnote, etc.
- Testear que xcopy maneja correctamente el acento en "Calculadoras" — si falla, evaluar ruta corta o mklink.
- Usuario de Windows confirmado: USUARIO
