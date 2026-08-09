---
galaxy_body: carrier
project: "Anki Galaxy — Sistema completo operativo"
date: 2026-08-02
status: delayed
fleet: anki
blocked_by: "tsk_marginalia_anki, tsk_flashcards, tsk_obsidian_to_anki — las 3 opciones deben estar probadas, funcionando y documentadas"
---

## Handoff

**Ultima sesion:** 2026-08-02
**Retomar desde:** verificar estado de los 3 tsk individuales antes de avanzar aqui
**Completado esta sesion:** carrier creado. 3 tsk individuales creados (A, B, C). Decisiones A vs B tomadas. Scripts 2 y 3 implementados.
**Proximo paso:** cuando los 3 tsk individuales esten en status delivered — volver aqui y completar tareas de integracion y documentacion final.
**Preguntas de cierre:** —

---

## Resumen y objetivo

Coordinar y verificar que el sistema Anki Galaxy completo este operativo: las 3 opciones funcionando juntas sin conflictos, todos los scripts documentados, y la documentacion final integrada al vault.

---

## Decisiones

| Fecha | Decision | Motivo |
| ----- | -------- | ------ |
| 2026-08-02 | Opcion A principal para planet/moon/comet | Marginalia invisible, Script 2 resuelve LaTeX, mantenimiento activo |
| 2026-08-02 | Opcion B complemento para dwarf/formularios T00 | Cloze y reversed utiles en notas de repaso puro, carpeta = deck automatico |
| 2026-08-02 | Opcion C exclusiva para Image Occlusion | Unico plugin que soporta Image Occlusion Enhanced desde Excalidraw |
| 2026-07-28 | AnkiSync+ descartado | Creaba decks pero no tarjetas |
| 2026-07-28 | Opcion D descartada | Complejidad innecesaria |

> [!note]- Descartadas
> - AnkiSync+ (RochaG07): creaba mazos pero no tarjetas. Sin fix, sin mantenimiento.
> - Opcion D (Obsidian-Anki-Sync debanjandhar12): sintaxis de cloze en LaTeX muy compleja.
> - TrillStones Image Occlusion: genera 2 PNG separados, no compatible con Image Occlusion Enhanced.

---

## Tareas

### Prerequisitos — completar antes de avanzar aqui
- [ ] `tsk_marginalia_anki` entregado — Opcion A probada con Script 2 en notas reales
- [ ] `tsk_flashcards` entregado — Opcion B activada y probada, compatibilidad con C verificada
- [ ] `tsk_obsidian_to_anki` entregado — Opcion C completa y probada

### Integracion
- [ ] Verificar que A + B + C coexisten sin conflictos
- [ ] Probar flujo completo en nota real: A (planet) + B (dwarf) + C (excalidraw) en misma sesion de Anki
- [ ] Verificar sync AnkiDroid con las 3 opciones activas

### Documentacion final
- [ ] Integrar `Obsidian_to_anki.md` a documentacion definitiva del vault
- [ ] Actualizar `anki_galaxy_guide.md` con estado final de las 3 opciones
- [ ] Verificar que todos los scripts tienen su `shellcmd_*.md` documentado
- [ ] Actualizar galaxy-links en todos los archivos relacionados

### Scripts
- [x] Script 2 — `latex_to_mathjax/main.py` creado y documentado
- [x] Script 3 — `occlusion_actions/main.py` creado y documentado
- [ ] Script 1 — conversor Marginalia -> Flashcards (baja prioridad, solo si surge necesidad)
- [ ] Script 4 — limpiar `<!--ID-->` de Image-Occlusions (pendiente, cubierto parcialmente por accion B del Script 3)

---

## Archivos del carrier

| Archivo | Tipo | Estado | Descripcion |
| ------- | ---- | ------ | ----------- |
| `tsk_anki.md` | carrier | delayed | Este archivo — coordinador general |
| `tsk_marginalia_anki.md` | ship | in-orbit | Opcion A — validacion con Script 2 |
| `tsk_flashcards.md` | ship | in-orbit | Opcion B — activacion y pruebas |
| `tsk_obsidian_to_anki.md` | ship | in-orbit | Opcion C — Image Occlusion completo |
| `anki_galaxy_guide.md` | beacon | activo | Guia maestra del sistema Anki |
| `anki-opcionA-marginalia.md` | beacon | activo | Documentacion Opcion A |
| `anki-opcionB-flashcards.md` | beacon | activo | Documentacion Opcion B |
| `anki-opcionC-obsidian-to-anki.md` | beacon | activo | Documentacion Opcion C |
| `Obsidian_to_anki.md` | beacon | activo | Flujo Image Occlusion — pendiente integracion |
| `opA_vs_opB.md` | beacon | activo | Comparativa y veredicto A vs B |

---

## Recursos

**Scripts:**
- `.obsidian/scripts/python/latex_to_mathjax/main.py` — Script 2
- `.obsidian/scripts/python/occlusion_actions/main.py` — Script 3
- `.obsidian/scripts/python/image_occlusion_reset/main.py` — legacy

**Documentacion shell commands:**
- `_app/shellcommands/shellcmd_latex_mathjax.md`
- `_app/shellcommands/shellcmd_occlusion_actions.md`

**Plugins:**
- Cornell Marginalia: https://github.com/Anna-Thomas/cornell-marginalia
- Flashcards reuseman: https://github.com/reuseman/flashcards-obsidian
- Obsidian_to_Anki: https://github.com/ObsidianToAnki/Obsidian_to_Anki
- AnkiConnect addon: codigo `2055492159`
- Image Occlusion Enhanced addon: codigo `1374772155`
