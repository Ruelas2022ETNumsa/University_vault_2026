---
galaxy_body: operator
project: "Script 3 — Image Occlusion Reset"
date: 2026-08-01
status: busy
---

## Handoff

**Última sesión:** 2026-08-01
**Retomar desde:** implementar Script 3 — diseño aprobado, listo para codear
**Completado esta sesión:** diseño completo del script discutido y aprobado
**Próximo paso:** crear `main.py` en `.obsidian/scripts/python/image_occlusion_reset/` y configurar en Shell Commands
**Preguntas de cierre:** —

---

## Ship activo

**Ship:** Script 3 — borrar carpetas antiguas de Image Occlusion y notas en Anki
**Origen:** flujo Image Occlusion Excalidraw → Anki, necesidad de re-exportar tras editar excalidraw
**Bloqueado por:** —

---

## Diseño aprobado

### Prompt (Shell Commands — Preactions)
- Campo prellenado con `{{title}}` (nombre del archivo activo)
- Editable por el usuario antes de ejecutar
- Ejemplo: `Prueba_anki.excalidraw`

### Lógica del script

**Paso 1 — Input**
Recibe nombre base del excalidraw (ej. `Prueba_anki.excalidraw`) vía argumento desde Shell Commands.

**Paso 2 — Buscar carpetas**
Busca en `Excalidraw/Image-Occlusions/` todas las carpetas cuyo nombre empiece con ese nombre base.
Formato de carpetas: `NombreBase__YYYY-MM-DD HH.MM.SS`

**Paso 3 — Lógica de selección (cuál conservar)**
- **Caso A:** si alguna carpeta tiene `.md` sin `<!--ID:-->` → esa es la nueva (aún no exportada), conservarla. Borrar todas las demás.
- **Caso B:** si todas las carpetas tienen ID (todas exportadas) → conservar la más reciente por timestamp de carpeta. Borrar todas las demás.

**Paso 4 — Borrar de Anki**
Para cada carpeta a borrar:
- Leer los `TIMESTAMP.md` (excluir `batch-marker.md`)
- Extraer `<!--ID: NNNNNNNNNNNNN-->` de cada uno
- Llamar a AnkiConnect `deleteNotes` con esos IDs
- Endpoint: `http://127.0.0.1:8765` — sin API key (configuración default)

**Paso 5 — Borrar carpeta del vault**
Borrar la carpeta completa del filesystem.

**Paso 6 — Output**
Notificación con resumen: cuántas carpetas borradas, cuántas notas eliminadas de Anki, cuál carpeta se conservó.

### Casos edge a manejar
- Anki no está abierto → error claro: "Anki debe estar abierto con AnkiConnect activo"
- Solo hay una carpeta → notificar al usuario, no borrar nada
- Carpeta sin ningún `.md` con ID y sin `.md` sin ID → tratar como Caso B

---

## Configuración Shell Commands

| Campo | Valor |
|---|---|
| Alias | `image-occlusion-reset` |
| Comando | `"C:\Users\USUARIO\AppData\Local\Programs\Python\Python313\python.exe" "{{vault_path}}\.obsidian\scripts\python\image_occlusion_reset\main.py" "{{_excalidraw_name}}" "{{vault_path}}"` |
| Shell | PowerShell 5 |
| stdout | Notification balloon |
| stderr | Notification balloon |
| Output mode | Wait until finished |

**Prompt (Preactions):**
- Título: `Image Occlusion Reset`
- Campo: `Nombre del excalidraw`
- Variable custom: `{{_excalidraw_name}}`
- Valor por defecto: `{{title}}`

---

## Tareas

- [ ] Crear `.obsidian/scripts/python/image_occlusion_reset/main.py`
- [ ] Probar Caso A — carpeta nueva sin ID + carpeta vieja con ID
- [ ] Probar Caso B — todas las carpetas con ID
- [ ] Probar edge: Anki cerrado
- [ ] Probar edge: una sola carpeta
- [ ] Configurar en Shell Commands con Prompt
- [ ] Agregar botón al ribbon via Commander
- [ ] Documentar en `Obsidian_to_anki.md` — Parte 2

---

## Recursos

- `E:\University_vault_2026\_hangar\anki\Obsidian_to_anki.md` — buffer de documentación
- `E:\University_vault_2026\_hangar\anki\anki-opcionC-obsidian-to-anki.md` — doc Opción C
- `E:\University_vault_2026\_app\shellcommands\shellcmd_scripting_guide.md`
- `E:\University_vault_2026\_app\shellcommands\shellcmd_latex_mathjax.md` — referencia Script 2
- AnkiConnect endpoint: `http://127.0.0.1:8765`
- AnkiConnect action: `deleteNotes` — params: `{ "notes": [ID1, ID2, ...] }`
- Carpeta de oclusiones: `Excalidraw/Image-Occlusions/`
