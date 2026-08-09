---
galaxy_body: dropship
carrier: "[[_hangar/anki/tsk_anki.md]]"
scope: opcion-B
status: activo
date: 2026-08-02
---

## Handoff

**Ultima sesion:** 2026-08-02
**Retomar desde:** activar plugin Flashcards y probar coexistencia con Opciones A y C
**Completado esta sesion:** decision A vs B tomada y documentada. Rol de Opcion B definido.
**Proximo paso:** activar Flashcards en Obsidian, configurar segun guia, probar en notas dwarf/formularios T00.
**Preguntas de cierre:** —

---

## Resumen y objetivo

Activar y dejar operativa la Opcion B (Flashcards reuseman) como complemento de Opcion A y C en el sistema Galaxy. Su rol esta definido: notas dedicadas a flashcards (dwarf, formularios T00) donde cloze y reversed agregan valor. No reemplaza Opcion A en notas de contenido (planet, moon, comet).

---

## Decisiones

| Fecha | Decision | Motivo |
| ----- | -------- | ------ |
| 2026-08-02 | Opcion B como complemento, no sustituto | Galaxy usa notas de contenido puro — Marginalia respeta eso, Flashcards agrega ruido sintactico (`#card`) |
| 2026-08-02 | Rol especifico: dwarf y formularios T00 | Cloze y reversed encajan en notas de repaso puro. Carpeta = deck automatico |
| 2026-08-02 | Opcion A principal para planet/moon/comet | Marginalia invisible, Script 2 resuelve LaTeX, mantenimiento activo |

> [!note]- Descartadas
> Opcion B como plugin principal — descartada porque `#card` visible en el body rompe la legibilidad de notas galaxy de contenido.

---

## Planificacion

Activar Flashcards con cuidado — verificar que no genere conflictos con Opcion C (Image Occlusion). Configurar segun guia `anki-opcionB-flashcards.md`. Probar los casos de uso definidos.

**Restricciones:**
- No usar en notas planet/moon/comet — esas van con Opcion A
- Verificar compatibilidad con Opcion C al activar

---

## Flujo de pasos

1. Activar plugin Flashcards en Obsidian
2. Verificar que Opcion C (Image Occlusion) sigue funcionando correctamente
3. Configurar Flashcards segun `anki-opcionB-flashcards.md` seccion 2
4. Probar tarjeta basica `#card` en nota dwarf de prueba
5. Probar inline `::`, cloze `==highlight==`, reversed `#card-reverse`
6. Probar LaTeX `$...$` directo
7. Probar Excalidraw SVG embebido (con Auto-export SVG activo)
8. Probar deck automatico por carpeta
9. Documentar resultados y actualizar `anki-opcionB-flashcards.md`
10. Actualizar `anki_galaxy_guide.md` con estado final

---

## Tareas

- [ ] Activar plugin Flashcards en Obsidian
- [ ] Verificar que Opcion C sigue operativa tras activar Flashcards
- [ ] Configurar Flashcards (context-aware OFF, folder deck ON, default deck Galaxy::General)
- [ ] Probar tarjeta basica `#card`
- [ ] Probar inline `::`
- [ ] Probar cloze `==highlight==`
- [ ] Probar reversed `#card-reverse`
- [ ] Probar LaTeX `$...$` directo
- [ ] Probar Excalidraw SVG embebido
- [ ] Probar deck automatico por carpeta
- [ ] Documentar resultados en `anki-opcionB-flashcards.md`
- [ ] Actualizar `anki_galaxy_guide.md`
- [ ] Evaluar Script 1 (conversor Marginalia -> Flashcards) si surge necesidad real

---

## Preguntas abiertas

- Al activar Flashcards, ¿genera conflictos con Image Occlusion o con el scan de Opcion C?

---

## Recursos

**Documentacion:**
- `_hangar/anki/anki-opcionB-flashcards.md` — guia completa Opcion B
- `_hangar/anki/opA_vs_opB.md` — comparativa y veredicto
- `_hangar/anki/anki_galaxy_guide.md` — guia maestra del sistema

**Plugin:**
- Flashcards reuseman: https://github.com/reuseman/flashcards-obsidian
- Disponible en Community Plugins — instalacion directa desde Obsidian

**Script pendiente relacionado:**
- Script 1 — conversor Marginalia -> Flashcards (pendiente, baja prioridad)
