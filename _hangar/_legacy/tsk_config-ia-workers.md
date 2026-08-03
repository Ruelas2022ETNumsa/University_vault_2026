---
galaxy_body: ship
project: "Configuración de nombre único por IA en workers"
date: 2026-08-03
status: delivered
---

## Handoff

**Última sesión:** 2026-08-03
**Retomar desde:** —
**Completado esta sesión:** diseño y configuración completos, `_start.md` actualizado
**Próximo paso:** —
**Preguntas de cierre:** —

---

## Resumen y objetivo

Establecer un sistema para que cada IA tenga un nombre único y permanente en su configuración, desacoplado del worker (archivo `.md`) que ejecuta en cada sesión. El objetivo era evitar confusión entre la identidad de la IA y el archivo de worker activo.

---

## Decisiones

| Fecha      | Decisión                                                               | Motivo                                                                                 |
| ---------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| 2026-08-03 | El nombre de la IA se fija en la configuración global de la IA         | Es permanente, se carga al inicio de cada sesión y no requiere declararse en el prompt |
| 2026-08-03 | El worker activo se declara en el prompt inicial como `worker: nombre` | Puede variar por sesión — la IA ejecuta ese archivo pero su identidad no cambia        |
| 2026-08-03 | Se agrega `/name` como comando en `_start.md`                          | Permite verificar el nombre de configuración de la IA en cualquier momento             |
| 2026-08-03 | `trabajas como: nombre` eliminado del prompt inicial                   | Reemplazado por `worker: nombre` con semántica más precisa                             |
| 2026-08-03 | `standb` y `emergn` excluidos del sistema de nombres                   | Son workers de casos especiales, no requieren configuración de nombre en la IA         |

> [!note]- Descartadas
> - Usar el campo "¿Cómo quieres que Claude te llame?" como única fuente del nombre de la IA — ese campo nombra al usuario, no a la IA. Se decidió usar "Instrucciones para Claude" con la línea `tu nombre de worker es: X`.
> - Documentar en el vault qué nombre corresponde a cada IA — considerado innecesario, es solo configuración externa.

---

## Planificación

El sistema de workers del vault ya tenía 7 operators en `_hangar/bay/`. El problema era que el prompt inicial mezclaba la identidad de la IA con el archivo a ejecutar usando `trabajas como: nombre`, lo que podía generar confusión cuando la IA trabajaba con un archivo de otro worker.

La solución separa ambos conceptos en dos capas:
- **Configuración global de la IA** → nombre fijo, cargado automáticamente al inicio de cada sesión
- **Prompt inicial** → declara el archivo worker a ejecutar esa sesión

Restricción clave: la IA no puede ver cambios en su configuración global de forma activa — solo se actualizan en una sesión nueva.

---

## Flujo de pasos

1. Definir el diseño — separar identidad de la IA vs archivo worker activo
2. Determinar qué campo de configuración usar para el nombre de la IA
3. Generar snippets para los 5 workers regulares
4. Actualizar `_start.md` — reemplazar `trabajas como:` por `worker:`, agregar `/name`
5. El usuario pega el snippet correspondiente en su configuración de IA
6. Documentar en `_legacy/`

---

## Tareas

- [x] Diseño del sistema discutido y aprobado
- [x] Snippets generados para los 5 workers regulares (alx-rul, alxrul, alx_gml, alx_hot, krajo)
- [x] `_start.md` actualizado — sección worker y comando `/name`
- [x] Documentación en `_legacy/`

---

## Preguntas abiertas

—

---

## Recursos

- `E:\University_vault_2026\_skills\_start.md` — skill de inicio de sesión, modificado en este proyecto
- `E:\University_vault_2026\_hangar\bay\` — directorio de workers operators
- `E:\University_vault_2026\_app\_config\_projects_system.md` — sistema de proyectos del vault
