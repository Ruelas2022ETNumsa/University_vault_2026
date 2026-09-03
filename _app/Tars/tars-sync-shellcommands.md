---
galaxy_body: blueprint
status: evaluando
priority: media
date: 2026-09-03
---

# TARS Sync — Shell Commands desde Obsidian

> **Relación:** Comando en Obsidian que toma el archivo activo y lo copia a la carpeta del Connectivity Kit (CASE o TARS), reemplazando el drag & drop manual. Sin scripts externos ni dependencias.

---

## Concepto central

- [ ] Dos comandos en Shell Commands — uno por calculadora
- [ ] Un solo Ctrl+P → alias → copia instantánea, sin salir de Obsidian
- [ ] Sin script externo, sin PowerShell, sin Python — solo xcopy nativo de Windows
- [ ] Aplica a cualquier archivo abierto en Obsidian: .hpprgm, .py, .hpnote, cualquier extensión

---

## Herramienta

- [ ] Shell Commands (Taitava) — Community plugin de Obsidian
  - Variable clave: {{file_path:absolute}} — ruta absoluta del archivo activo
  - Shell a usar: CMD.EXE (no PowerShell — evita problemas con caracteres no-ASCII)
  - Repo: https://github.com/taitava/obsidian-shellcommands
  - Instalacion: Settings → Community plugins → buscar "Shell commands"

---

## Comandos a configurar en Shell Commands

Alias: TARS: Enviar a CASE
Comando: xcopy /Y "{{file_path:absolute}}" "C:\Users\USUARIO\Documents\HP Connectivity Kit\Calculadoras\CASE\"

Alias: TARS: Enviar a TARS
Comando: xcopy /Y "{{file_path:absolute}}" "C:\Users\USUARIO\Documents\HP Connectivity Kit\Calculadoras\TARS\"

USUARIO = reemplazar con el nombre real del usuario de Windows antes de configurar.
/Y = sobreescribe sin pedir confirmacion si el archivo ya existe.

---

## Rutas de destino (confirmadas 2026-09-03)

| Destino | Ruta |
|---|---|
| CASE | C:\Users\USUARIO\Documents\HP Connectivity Kit\Calculadoras\CASE\ |
| TARS | C:\Users\USUARIO\Documents\HP Connectivity Kit\Calculadoras\TARS\ |

Los .hpprgm van directo en la raiz de cada carpeta — sin subcarpetas.
Carpeta en espanol: Calculadoras (confirmar que xcopy maneja el acento sin problema).

---

## Descartado

- Script .ps1 (PowerShell) — requiere ajustar ExecutionPolicy en Windows, dependencia externa innecesaria para una copia simple.
- Script .py (Python) — depende de que Python este en el PATH, innecesario.
- Menu interactivo CASE/TARS — dos comandos separados es mas simple y directo.

---

## Flujo final

Archivo activo en Obsidian (ej. KMH_CONV.hpprgm)
        |
Ctrl+P → "TARS: Enviar a CASE"
        |
xcopy copia el archivo a Calculadoras\CASE\
        |
Kit lo detecta al abrirse (o al refrescar si ya esta abierto)

---

## A depurar antes de implementar

- [ ] Confirmar nombre real del usuario de Windows para hardcodear la ruta
- [ ] Testear que xcopy maneja correctamente la tilde en Calculadoras — si falla, usar ruta corta o alias de Windows
- [ ] Configurar output de Shell Commands como notification en Obsidian para confirmar exito visualmente
- [ ] Testear primero con KMH_CONV.hpprgm (ya probado en CASE) antes de usar con otros archivos

---

## Referencias

- Shell Commands plugin: https://github.com/taitava/obsidian-shellcommands
- Variable file_path:absolute: https://publish.obsidian.md/shellcommands/Variables/Variables+-+general+principles
- Guia TARS: _app/Tars/HP_Prime_guide.md
