---
galaxy_body: ship
project: "ETN607 T1 — Ejercicios tipo examen"
date: 2026-08-20
status: docked
fleet: ETN607
blocked_by:
---

## Handoff

**Última sesión:** 2026-08-20
**Retomar desde:** Lista de tareas — lanzar mensajes a NotebookLM por tema
**Completado esta sesión:** Definición del plan · Ship creado
**Próximo paso:** Lanzar consultas a NotebookLM usando Lim como fuente principal
**Preguntas de cierre:** —

---

## Resumen y objetivo

Obtener ejercicios de dificultad examen para el T1. Problemas que integren varios conceptos del tema (coordenadas, velocidad, DOF, transformaciones) y que el docente podría colocar en una prueba parcial. No son ejercicios de práctica — son ejercicios de cierre de tema.

---

## Decisiones

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
| 2026-08-20 | Fuente principal: Lim World Scientific | Nivel examen — problemas integradores con solución |
| 2026-08-20 | Fuente secundaria: Wells Cap. 1–2 | Problemas de coordenadas generalizadas y DOF con resolución paso a paso |
| 2026-08-20 | No usar Nelson para este ship | Nelson cubre práctica estándar — ya está en el ship de ejercicios |

> [!note]- Descartadas
> Taylor Instructor's Manual — ejercicios de T1 demasiado conceptuales, poco calculísticos para examen de este tipo.

---

## Planificación

Mensaje a usar en NotebookLM (BCv4ii Mensaje 2):
```
Complemento nivel B/C: [concepto] — ejercicio tipo examen
```

Libros a tener cargados en NotebookLM:
- `LimYung-kuo-Problems and Solutions on Mechanics-1994.pdf`
- `Dare A. Wells-SCHAUM'S Lagrangian Dynamics-McGraw-Hill.pdf` — Cap. 1–2
- `John R. Taylor-Instructor's Manual to accompany Classical Mechanics-2005.pdf`

Output: guardar en nota de práctica independiente o en el blueprint según volumen.

---

## Flujo de pasos

1. Abrir NotebookLM con Lim, Wells Cap.1-2 y Taylor Instructor's Manual cargados
2. Lanzar mensaje BCv4ii Mensaje 2 para cada tarea pendiente
3. Verificar que el ejercicio sea nivel examen: integra más de un concepto, varias etapas de resolución
4. Guardar output en el archivo destino
5. Marcar tarea como completada

---

## Tareas

- [ ] **Conversión entre los 4 sistemas** · `Complemento nivel B/C: conversión entre coordenadas cartesianas, cilíndricas, esféricas y no lineales — ejercicio tipo examen` · Lim
- [ ] **Velocidad en curvilíneas** · `Complemento nivel B/C: velocidad escalar y vectorial en coordenadas cilíndricas y esféricas — ejercicio tipo examen` · Lim / Wells Cap. 2
- [ ] **Aceleración en cilíndricas** · `Complemento nivel B/C: aceleración en coordenadas cilíndricas — ejercicio tipo examen` · Lim / Wells Cap. 2
- [ ] **Rotaciones sucesivas** · `Complemento nivel B/C: rotaciones sucesivas de ejes cartesianos con ángulos dados — ejercicio tipo examen` · Wells Cap. 1
- [ ] **DOF sistema complejo** · `Complemento nivel B/C: grados de libertad de un sistema mecánico con múltiples cuerpos y restricciones combinadas — ejercicio tipo examen` · Wells Cap. 1 / Lim
- [ ] **Problema integrador T1** · `Complemento nivel B/C: problema que combine sistemas de coordenadas, velocidad escalar y DOF — ejercicio tipo examen` · Lim

---

## Preguntas abiertas

- ¿Los ejercicios tipo examen van en el archivo de notas T1 o en una nota de práctica separada?
- ¿Se incluyen ejercicios de los 4 métodos (Newton, Lagrange, Conservación, Simulink) o solo coordenadas y DOF?

---

## Recursos

- Notas T1: `E:\University_vault_2026\Semesters\Sem_04\ETN607\Partial_1\ETN607-T01-P1-Conceptos generales 1.md`
- Ship complementos: `E:\University_vault_2026\Semesters\Sem_04\ETN607\Partial_1\ETN607-T01-complementos.md`
- Ship ejercicios práctica: `E:\University_vault_2026\Semesters\Sem_04\ETN607\Partial_1\ETN607-T01-ejercicios.md`
- Prompt BCv4ii: `E:\University_vault_2026\_app\notebooklm\prompts\ETN607\ETN607-transcription_BCv4ii.md`
- Library: `E:\University_vault_2026\Semesters\Sem_04\ETN607\_library_ETN607.md`