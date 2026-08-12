---
galaxy_body: ship
project: "Biblioteca ETN1015 — Stack de libros"
date: 2026-08-11
status: delivered
fleet: ETN1015
blocked_by:
---

## Handoff

**Última sesión:** 2026-08-11
**Retomar desde:** no aplica — proyecto entregado
**Completado esta sesión:** stack construido, evaluado y documentado completo
**Próximo paso:** actualizar si el docente cambia de libro base, o cuando haya temario oficial
**Preguntas de cierre:** ninguna

---

## Resumen y objetivo

Construir el stack de libros óptimo para ETN1015 — Procesamiento Digital de Señales, partiendo del libro base del docente (Rao) y sin temario oficial disponible. El objetivo fue cubrir todos los roles del stack (teoría, problemas, puente lingüístico) sin redundancia, y documentarlo en el vault.

---

## Decisiones

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
| 2026-08-11 | Libro base: Rao — Signals and Systems — Birkhäuser 2018 | Libro que sigue el docente |
| 2026-08-11 | Teoría rigurosa: Oppenheim 2da ed. (EN) | Referencia estándar mundial para la materia |
| 2026-08-11 | Puente lingüístico: Oppenheim 2da ed. (ES) | Versión Pearson Educación en español de calidad decente |
| 2026-08-11 | Problemas estándar: Hsu Schaum 1995 | Cubre exactamente los temas del curso con soluciones paso a paso |
| 2026-08-11 | DSP puro: Hayes Schaum DSP 1999 | Condicionado — solo para caps. 6–8 de Rao |
| 2026-08-11 | Complemento avanzado: Phillips, Parr & Riskin 4ta ed. | Transformadas y análisis avanzado |
| 2026-08-11 | Solutions Manual de Mani agregado al stack | Soluciones oficiales de los ejercicios del Oppenheim |
| 2026-08-11 | Oppenheim EN y ES divididos en 1to5 y 6to11 | Límite de 500K palabras/200MB por fuente en NotebookLM |

> [!note]- Descartadas
> Ninguna — stack construido desde cero sin libros previos que descartar.

---

## Planificación

Sin temario oficial. El docente dicta siguiendo Rao capítulo a capítulo. El stack se organizó tomando el índice completo de Rao (8 capítulos) como estructura base, y asignando un libro complementario por rol para cada capítulo. Restricción clave: los libros debían ser los que el usuario ya tenía conseguidos — no se recomendaron libros adicionales salvo el Solutions Manual de Mani.

---

## Sugerencias

No aplica — proyecto de selección y documentación interna, sin búsqueda web de antecedentes.

---

## Flujo de pasos

1. Leer `_library-system.md` para activar el protocolo
2. Recibir inputs: sin temario, nivel ingeniería, libro base Rao
3. Evaluar libro base (Rao) → ✅ visto bueno
4. Construir stack recomendado con roles cubiertos
5. Evaluar libros conseguidos por el usuario uno a uno
6. Incorporar Solutions Manual de Mani al stack
7. Confirmar stack final con usuario
8. Crear `_library_ETN1015.md` en la raíz del vault
9. Agregar callout de advertencia sobre cambio de libro base
10. Documentar archivos divididos (Oppenheim 1to5 y 6to11)
11. Actualizar tabla "Qué usar por tema" con rutas de archivos divididos
12. Crear este ship

---

## Tareas

- [x] Leer `_library-system.md`
- [x] Evaluar libro base del docente (Rao)
- [x] Construir stack recomendado
- [x] Evaluar lista de libros conseguidos por el usuario
- [x] Incorporar Solutions Manual de Mani
- [x] Confirmar stack final
- [x] Crear `_library_ETN1015.md`
- [x] Agregar callout de advertencia libro base provisional
- [x] Documentar división de Oppenheim EN y ES (1to5 / 6to11)
- [x] Actualizar tabla por capítulo con archivos divididos
- [x] Crear ship

---

## Preguntas abiertas

Ninguna.

---

## Recursos

**Archivo principal:**
- `E:\University_vault_2026\Semesters\Sem_08\ETN1015\_library_ETN1015.md`

**Referencia de protocolo:**
- `E:\University_vault_2026\_app\_config\_library-system.md`

**Template usado:**
- `E:\University_vault_2026\_hangar\template\tpl_ship.md`

**Stack final documentado:**

| Archivo | Rol |
|---|---|
| K. Deergha Rao — Signals and Systems — Birkhäuser 2018 | Teoría principal |
| Oppenheim EN (1to5) | Teoría rigurosa caps. 1–5 |
| Oppenheim EN (6to11) | Teoría rigurosa caps. 6–11 |
| Oppenheim ES (1to5) | Puente lingüístico caps. 1–5 |
| Oppenheim ES (6to11) | Puente lingüístico caps. 6–11 |
| Mani et al. — Solutions Manual | Soluciones oficiales Oppenheim |
| Hsu — Schaum's Signals and Systems 1995 | Problemas estándar |
| Hayes — Schaum's DSP 1999 | DSP puro (caps. 6–8 de Rao) |
| Phillips, Parr & Riskin — 4ta ed. | Transformadas avanzadas |
