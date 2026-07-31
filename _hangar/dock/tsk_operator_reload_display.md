---
galaxy_body: ship
project: "operator reload display"
date: 2026-07-31
status: docked
fleet:
blocked_by:
---

## Handoff

**Última sesión:** —
**Retomar desde:** inicio
**Completado esta sesión:** —
**Próximo paso:** iniciar análisis
**Preguntas de cierre:** —

---

## Resumen y objetivo

Agregar campo `reload: "HH:MM"` al YAML de los operators y mostrarlo visualmente — ya sea via Supercharged Links (CSS con `attr()`) o via DataView en el logbook del hangar.

**Próximo paso:** implementar via DataView en `logbook.md` del hangar — más simple y sin limitaciones de CSS (1ro por logbook, dataview esta desavilitado)

---

## Decisiones

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
| 2026-07-31 | Ship creado, análisis pendiente | El campo `reload` es dinámico — CSS puro tiene limitaciones con `attr()` en Electron/Obsidian |

> [!note]- Descartadas
> —

---

## Flujo de pasos

1. Agregar `reload: "HH:MM"` al YAML de los 7 operators
2. Evaluar soporte de `attr()` en `::before`/`::after` en Obsidian (Electron renderer)
3. Si `attr()` funciona → agregar selector CSS en `supercharged-links.css`
4. Si no → implementar vista DataView en `logbook.md` del hangar con columna `reload`
5. Documentar resultado en `supercharged_guide.md` o beacon DataView según corresponda

---

## Tareas

- [ ] Agregar `reload:` a los 7 operators
- [ ] Testear `attr()` en CSS de Supercharged Links
- [ ] Implementar solución (CSS o DataView)
- [ ] Documentar

---

## Preguntas abiertas

- ¿Obsidian soporta `content: attr(data-link-reload)` en `::before`/`::after`?
- ¿Se prefiere mostrar en el explorador (CSS) o en el logbook (DataView)?

---

## Recursos

- `E:\University_vault_2026\_hangar\` — operators a editar
- `E:\University_vault_2026\.obsidian\snippets\supercharged-links.css`
- `E:\University_vault_2026\_app\_appnotes\supercharged_guide.md`
- https://github.com/mdelobelle/obsidian_supercharged_links
