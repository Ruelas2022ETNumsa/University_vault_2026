---
project: "memory-matter"
date: 2026-07-30
status: nueva
---

## Handoff

**Última sesión:** 2026-07-30
**Retomar desde:** Sección "Preguntas abiertas" — ninguna decisión tomada aún
**Completado esta sesión:** Discusión inicial de la idea, comparación con archivos existentes, búsqueda web de antecedentes
**Próximo paso:** Leer más contexto del sistema galaxy antes de diseñar estructura
**Preguntas de cierre:** ¿Dónde vive el archivo — beacon, MOC, o raíz de materia?

---

## Resumen y objetivo

Explorar si tiene sentido un archivo de contexto/estado por materia (ej. `MAT101_mem.md`) que centralice información específica de esa galaxia: progreso de transcripciones, libros subidos a NotebookLM, fechas de exámenes, tareas y proyectos activos. Ninguna decisión tomada — idea en fase de revisión y diseño.

## Decisiones

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
|       |          |        |

> [!note]- Descartadas
> —

---

## Planificación

Idea aún sin diseño formal. Lo discutido hasta ahora:

**Problema que resuelve:** `_galaxy-system.md` y `_claude-boot.md` son extensos y no son específicos por materia. No existe un lugar único que junte estado académico (exámenes, notas) con estado del vault (qué se transcribió, qué se subió a NotebookLM) para una materia concreta.

**Lo que NO es:** no reemplaza la memoria automática de Claude.ai ni duplica los skills existentes. No es infraestructura del vault (eso es `_galaxy-system`). No es handoff de tarea (eso es `tlp_worker`).

**Lo que SÍ podría ser:** un dashboard de materia — estado actual, progreso y pendientes específicos de esa galaxia. Portable, versionable, bajo control del usuario.

**Contenido tentativo discutido:**
- Estado general: semestre, parcial actual, fecha próximo examen
- Apuntes: qué clases están transcriptas, cuáles pendientes
- Libros / NotebookLM: qué fuentes están subidas, cuáles faltan
- Proyectos activos vinculados a la materia (ships en dock/)
- Fórmulas clave del parcial actual (las que no conviene buscar cada vez)

**Pendiente de definir antes de diseñar:**
- Leer más contexto del sistema galaxy (archivos no leídos aún)
- Decidir `galaxy_body` apropiado o si queda fuera del sistema galaxy
- Decidir ubicación: `_app/_config/` (beacon), `MOC/`, o raíz de `Semesters/Sem_NN/ETNXXX/`
- Decidir nombre: `MAT101_mem.md`, `MAT101_boot.md`, u otro

---

## Sugerencias

**Antecedentes web encontrados (2026-07-30):**

- **CLAUDE.md pattern** — la comunidad de Claude Code usa archivos `.md` por proyecto para darle contexto persistente a Claude. El principio es el mismo: contexto específico cargado bajo demanda, no global. Fuente: docs.claude.ai + varios posts.
- **ai-memory-vault (jaredrhod)** — vault completo de Obsidian como memoria de AI. Diferencia: apunta a memoria personal general, no a contexto académico por materia.
- **obsidian-memory-for-ai (jrcruciani)** — memoria en markdown plano, versionable con Git. Enfoque similar al propuesto pero genérico.
- **Conclusión de la búsqueda:** no se encontró un antecedente específico de "contexto por materia universitaria en vault Obsidian". La idea es genuinamente específica del sistema galaxy.

---

## Flujo de pasos

- [ ] Leer archivos de contexto adicionales del vault que no se leyeron en esta sesión
- [ ] Definir si el archivo tiene `galaxy_body` o queda fuera del sistema galaxy
- [ ] Definir ubicación dentro del vault
- [ ] Definir nombre y convención de nombres para todas las materias
- [ ] Diseñar estructura del archivo con secciones concretas
- [ ] Validar contra un caso real (MAT101 u otra materia activa)
- [ ] Decidir si se crea uno por materia o se prototipa solo con una primero

---

## Tareas

- [ ] Leer `_claude-boot.md` para entender qué contexto ya carga al inicio
- [ ] Leer `_notebooklm-system.md` para entender cómo se integra NotebookLM
- [ ] Leer `_TABnote-system.md` para entender el ciclo de transcripción
- [ ] Leer `_projects_system.md` para entender cómo los ships se vinculan a materias
- [ ] Leer MOC de alguna materia activa para ver qué información ya existe ahí
- [ ] Proponer borrador de estructura y discutir

---

## Preguntas abiertas

- ¿Dónde vive el archivo dentro del vault?
- ¿Tiene `galaxy_body` propio o es un archivo operativo sin tipo galaxy?
- ¿Cómo se llama — `mem`, `boot`, `dashboard`, `context`?
- ¿Una por materia desde el inicio o solo para materias activas?
- ¿Quién la actualiza — el usuario manualmente, Claude al cerrar sesión, o ambos?
- ¿Se integra con el skill `_claude-close.md` para actualización automática al cerrar?

---

## Recursos

- `E:\University_vault_2026\_app\_config\_galaxy-system.md` — sistema completo del vault
- `E:\University_vault_2026\_hagar\tlp_worker.md` — plantilla de worker (referencia de diseño)
- `E:\University_vault_2026\_skills\_claude-plan.md` — skill activo esta sesión
- Archivos pendientes de leer: `_claude-boot.md`, `_notebooklm-system.md`, `_TABnote-system.md`, `_projects_system.md`
