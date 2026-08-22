---
galaxy_body: ship
project: "ETN607 T1 — Ejercicios NotebookLM"
date: 2026-08-20
status: docked
fleet: ETN607
blocked_by:
---

## Handoff

**Última sesión:** 2026-08-20
**Retomar desde:** Lista de tareas — lanzar mensajes a NotebookLM por sección
**Completado esta sesión:** Definición del plan de ejercicios · Ship creado
**Próximo paso:** Lanzar consultas a NotebookLM por sección usando el mensaje BCv4ii Mensaje 2
**Preguntas de cierre:** —

---

## Resumen y objetivo

Obtener ejercicios resueltos de los libros del stack para cada sección del T1 que los admita. Los ejercicios van como complemento Nivel C dentro del archivo de notas, dentro del bloque `ad-note` correspondiente a cada sección.

---

## Decisiones

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
| 2026-08-20 | Usar BCv4ii Mensaje 2 para consultas puntuales de ejercicios | No requiere apunte cargado — consulta directa al libro |
| 2026-08-20 | Fuente principal T1 ejercicios: Nelson Cap. 11–12 | Según `_library_ETN607.md` — Wells asume demasiado en T1 |
| 2026-08-20 | Fuente secundaria: Wells Cap. 1 | Para ejercicios de coordenadas generalizadas y DOF |

> [!note]- Descartadas
> Lim World Scientific para T1 — nivel demasiado alto para conceptos básicos.

---

## Planificación

Mensaje a usar en NotebookLM (BCv4ii Mensaje 2):
```
Complemento nivel B/C: [nombre del concepto o subtítulo]
```

Libros a tener cargados en NotebookLM:
- `Nelson & Best & McLean-schaums Statics and dynamics.pdf` — Cap. 11–12
- `Dare A. Wells-SCHAUM'S Lagrangian Dynamics-McGraw-Hill.pdf` — Cap. 1
- `John R. Taylor-Classical mechanics-eng-1to9.pdf` — Cap. 1

Insertar los ejercicios obtenidos en:
`E:\University_vault_2026\Semesters\Sem_04\ETN607\Partial_1\ETN607-T01-P1-Conceptos generales 1.md`

---

## Flujo de pasos

1. Abrir NotebookLM con Nelson Cap.11-12, Wells Cap.1 y Taylor Cap.1 cargados
2. Lanzar mensaje BCv4ii Mensaje 2 para cada sección pendiente
3. Revisar output: nivel correcto, fuente confirmada, ejercicio aplicable
4. Insertar dentro del `ad-note` correspondiente en el archivo de notas
5. Marcar tarea como completada

---

## Tareas

- [ ] **Newton — péndulo en cilíndricas** · `Complemento nivel B/C: aplicación de Newton en coordenadas cilíndricas — péndulo simple` · Nelson Cap. 11
- [ ] **Sistemas de coordenadas — conversión** · `Complemento nivel B/C: conversión entre sistemas de coordenadas rectangular, cilíndrico y esférico` · Nelson Cap. 12
- [ ] **Coordenadas No Lineales (A, θ, Z)** · `Complemento nivel B/C: ejercicio de conversión en coordenadas no lineales` · Nelson Cap. 12 / Taylor Cap. 1
- [ ] **Velocidad escalar — coordenadas cilíndricas** · `Complemento nivel B/C: velocidad escalar en coordenadas cilíndricas — ejercicio resuelto` · Nelson Cap. 12
- [ ] **Velocidad escalar — coordenadas esféricas** · `Complemento nivel B/C: velocidad escalar en coordenadas esféricas — ejercicio resuelto` · Nelson Cap. 12
- [ ] **Grados de libertad DOF** · `Complemento nivel B/C: grados de libertad — fórmula general y ejercicio sistema multi-pieza` · Wells Cap. 1 / Taylor Cap. 1
- [ ] **Rotaciones sucesivas** · `Complemento nivel B/C: rotaciones sucesivas de ejes cartesianos — ejercicio numérico` · Taylor Cap. 1

---

## Preguntas abiertas

- ¿Los ejercicios de Lagrange y Conservación de energía (métodos b y c) necesitan ejercicio adicional o el del apunte ya es suficiente?
- ¿Se añaden ejercicios de DOF para sistemas con bisagra + rótula combinados o solo los básicos?

---

## Recursos

- Notas T1: `E:\University_vault_2026\Semesters\Sem_04\ETN607\Partial_1\ETN607-T01-P1-Conceptos generales 1.md`
- Ship complementos: `E:\University_vault_2026\Semesters\Sem_04\ETN607\Partial_1\ETN607-T01-complementos.md`
- Prompt BCv4ii: `E:\University_vault_2026\_app\notebooklm\prompts\ETN607\ETN607-transcription_BCv4ii.md`
- Library: `E:\University_vault_2026\Semesters\Sem_04\ETN607\_library_ETN607.md`
