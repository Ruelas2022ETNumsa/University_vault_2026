---
galaxy_body: ship
project: "ETN607 T1 — Complementos"
date: 2026-08-20
status: in-orbit
fleet: ETN607
blocked_by:
---

## Handoff

**Última sesión:** 2026-08-20
**Retomar desde:** `E:\University_vault_2026\Semesters\Sem_04\ETN607\Partial_1\ETN607-T01-P1-Conceptos generales 1.md`
**Completado esta sesión:** Transcripción T1 completa · Complemento versores cilíndricas (Nivel C) ya insertado · Lista de complementos pendientes definida
**Próximo paso:** Generar complementos en NotebookLM usando BCv4i o BCv4ii según sección · Insertar en el archivo de notas
**Preguntas de cierre:** ¿El complemento de d/e/f Parabólicas/Hiperbólicas/Otros se limita a ecuaciones de transformación o incluye figura?

---

## Resumen y objetivo

Añadir complementos nivel B y C a las secciones del T1 que quedaron sin respaldo de libro tras la transcripción del apunte. Meta: que cada sección tenga definición formal + figura o ejercicio donde corresponda, usando los libros del stack de ETN607.

---

## Decisiones

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
| 2026-08-20 | Usar BCv4ii para complementos que no dependen del apunte | El docente no sigue el índice linealmente — BCv4ii trabaja solo desde el library |
| 2026-08-20 | Versores cilíndricas ya complementado (Nivel C) | Resuelto en sesión — bloque ad-note insertado después del `>[!summary]` de cilíndricas |
| 2026-08-20 | d/e/f Parabólicas·Hiperbólicas·Otros → Nivel B mínimo | El docente no las desarrolló — solo ecuaciones de transformación si existen en los libros |

> [!note]- Descartadas
> TikZJax en complemento de versores cilíndricas — se mantiene por decisión del usuario aunque tikz-3dplot no está en la lista estándar del prompt.

---

## Planificación

Fuentes por sección según `_library_ETN607.md`:
- T1 teoría → Taylor Cap. 1 (1ª opción) · Goldstein Cap. 1 (2ª opción)
- T1 ejercicios → Nelson Schaum's Dynamics Cap. 11–12 · Wells Cap. 1

Prompt a usar:
- **BCv4ii** — para secciones sin apunte cargado (complemento por índice)
- **BCv4i** — si se quiere complementar una sección específica con el apunte como contexto

Archivo destino del blueprint: `E:\University_vault_2026\Semesters\Sem_04\ETN607\Partial_1\complementos para 607 T1.md`

---

## Flujo de pasos

1. Abrir NotebookLM con los libros del T1 cargados (Taylor Cap.1, Goldstein Cap.1, Nelson Cap.11-12)
2. Para cada complemento pendiente: lanzar mensaje BCv4ii correspondiente
3. Pegar output en el blueprint `complementos para 607 T1.md`
4. Revisar nivel (B/C), figura, ejercicio
5. Insertar bloque `ad-note` en la posición indicada del archivo de notas
6. Marcar tarea como completada aquí

---

## Tareas

- [x] Complemento versores cilíndricas (Nivel C) — insertado
- [ ] **Objetivo** — Nivel B · fuerzas de ligadura, por qué las elimina Lagrange · Taylor Cap. 1
- [ ] **Newton (§a Métodos)** — Nivel C · condiciones del método + ejercicio péndulo cilíndricas · Nelson Cap. 11
- [ ] **Condiciones (Masa, Velocidad, Tiempo)** — Nivel B · justificación de cada límite + definición mecánica clásica · Taylor Cap. 1
- [ ] **Sistemas de coordenadas (intro)** — Nivel B · independencia y completitud de un sistema · Taylor Cap. 1 / Alonso
- [ ] **Esférico (§c Sistemas coord.)** — Nivel C · ejercicio conversión de coordenadas · Nelson Cap. 12
- [ ] **d) Parabólicas Cilíndricas** — Nivel B mínimo · ecuaciones de transformación · Taylor / Alonso
- [ ] **e) Hiperbólicas Cilíndricas** — Nivel B mínimo · ecuaciones de transformación · Taylor / Alonso
- [ ] **f) Otros** — Nivel B mínimo · referencia a otros sistemas existentes · Taylor / Alonso
- [ ] **Rotacion y traslacion (intro)** — Nivel B · motivación geométrica de la rotación de ejes · Taylor Cap. 1 / Goldstein Cap. 1
- [ ] **Grados de libertad DOF** — Nivel C · fórmula $N = 3n - k$ + ejemplo sistema multi-pieza · Wells Cap. 1 / Taylor

---

## Preguntas abiertas

- ¿El complemento de `### c) Rotacion Z γ` (sección agregada, no dictada) necesita complemento o se deja como está?
- ¿El `>[!note] Corrección` de coordenadas cilíndricas se borra en esta sesión o en la próxima?

---

## Recursos

- Notas T1: `E:\University_vault_2026\Semesters\Sem_04\ETN607\Partial_1\ETN607-T01-P1-Conceptos generales 1.md`
- Blueprint complementos: `E:\University_vault_2026\Semesters\Sem_04\ETN607\Partial_1\complementos para 607 T1.md`
- Prompts NotebookLM:
  - `E:\University_vault_2026\_app\notebooklm\prompts\ETN607\ETN607-transcription_BCv4i.md`
  - `E:\University_vault_2026\_app\notebooklm\prompts\ETN607\ETN607-transcription_BCv4ii.md`
- Library: `E:\University_vault_2026\Semesters\Sem_04\ETN607\_library_ETN607.md`
