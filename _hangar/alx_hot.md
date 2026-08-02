---
galaxy_body: operator
project: "Template Anki Excalidraw"
date: 2026-08-01
status: busy
---

## Handoff

**Última sesión:** 2026-08-02
**Retomar desde:** `E:\University_vault_2026\.obsidian\scripts\python\occlusion_actions\main.py` — fix legacy: archivo fuente .excalidraw no se mueve a legacy + carpeta legacy no debe incluir extensión en su nombre
**Completado esta sesión:** Script `occlusion_actions/main.py` creado desde cero. Acción B funcional (borra carpetas, notas Anki, decks vacíos, tags huérfanos). Acción S parcial (mueve carpetas timestamp con IDs, bloquea sin export, sobreescribe en legacy — falta mover archivo fuente .excalidraw). Acción Z funcional. Prompt Shell Commands configurado con variables `{{_excalidraw_name}}` y `{{_occlusion_action}}`. Template `tpl-Anki_excalidraw.md` editado para agregar `.excalidraw` al nombre. Botón ribbon creado en Commander.
**Próximo paso:** Fix S — (1) encontrar y mover archivo fuente `.excalidraw.md` a legacy correctamente, (2) evitar que el nombre capturado por `{{title}}` incluya la extensión `.excalidraw` en el prompt, (3) carpeta legacy no debe tener extensión en su nombre.
**Preguntas de cierre:** ¿El archivo fuente queda como `nombre.excalidraw.md` tras usar la plantilla corregida, o sigue sin extensión?

---

## Ship activo

**Ship:** Rediseño `image_occlusion_reset/main.py` — acciones B/S/Z
**Origen:** flujo Image Occlusion — necesidad de borrar, archivar y restaurar tarjetas desde Obsidian
**Bloqueado por:** —

---

## Worker — `occlusion_actions/main.py` fixes pendientes

**Ruta:** `E:\University_vault_2026\.obsidian\scripts\python\occlusion_actions\main.py`
**BKs disponibles:** `mainv2.py.bk`, `mainv3.py.bk`, `mainv4.py.bk`

**Fix 1 — Carpeta legacy sin extensión:**
El nombre capturado por `{{title}}` incluye `.excalidraw` cuando el archivo fuente tiene esa extensión. La carpeta en legacy queda como `nombre.excalidraw/` en vez de `nombre/`. Solucionar stripeando `.excalidraw` del `excalidraw_name` al armar `destino_base` en acción S y Z.

**Fix 2 — Archivo fuente no se mueve a legacy:**
`find_excalidraw_file` busca `nombre + ".excalidraw.md"` pero el archivo puede estar con otro nombre o ruta. Verificar nombre exacto del archivo fuente tras usar plantilla corregida y ajustar búsqueda.

**Fix 3 — Prompt muestra extensión:**
Cuando el archivo activo es `nombre.excalidraw.md`, `{{title}}` devuelve `nombre.excalidraw`. Evaluar stripear en el script o ajustar variable en Shell Commands.

---

## Tareas

- [x] Crear `.obsidian/scripts/python/image_occlusion_reset/main.py`
- [x] Probar Caso A — carpeta nueva sin ID + carpeta vieja con ID
- [x] Probar Caso B — todas las carpetas con ID
- [x] Probar edge: Anki cerrado
- [x] Probar edge: una sola carpeta
- [x] Configurar en Shell Commands con Prompt
- [x] Documentar en `Obsidian_to_anki.md` — Parte 2
- [x] Agregar botón al ribbon via Commander (opcional — baja prioridad)
- [x] Crear `tpl-Anki_excalidraw.md` en `_templates/` con prompt de nombre y carpeta destino
- [x] Editar script `Image Occlusion.md` — agregar prompt de deck y tag al generar cartas
- [x] Editar `tpl-excalidraw_occlusion.md` — agregar línea `FILE TAGS`
- [x] Implementar rediseño `main.py` — acciones B/S/Z (nuevo script `occlusion_actions/main.py`)
- [x] Reconfigurar Shell Commands — agregar tercer argumento de acción
- [x] Verificar que el tag llegue correctamente a Anki
- [x] Acción B funcional — borra carpetas, notas Anki, decks vacíos, tags huérfanos
- [x] Acción Z funcional — restaura desde legacy
- [ ] Fix acción S — mover archivo fuente `.excalidraw.md` a legacy
- [ ] Fix nombre capturado por `{{title}}` — evitar que incluya extensión `.excalidraw`
- [ ] Fix carpeta legacy — no debe incluir extensión en su nombre
- [ ] Probar S completo tras fixes
- [ ] Actualizar cabecera de `main.py` con ejemplo correcto (sin extensión en argumento)

---

## Recursos

- `E:\University_vault_2026\Excalidraw\template\Template.excalidraw.md` — base para el nuevo template
- `E:\University_vault_2026\_hangar\anki\Obsidian_to_anki.md` — documentación del flujo
