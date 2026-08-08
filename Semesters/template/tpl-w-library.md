---
title: "_library_ETNXXX"
galaxy_body: workshop
subject: ETNXXX
semester: N
tags: [ETNXXX, workshop, library]
date_created: YYYY-MM-DD
date_updated: YYYY-MM-DD
status: activo
---

%%
# Instrucciones de uso
Antes de arrancar la búsqueda, Claude debe leer:
  - `E:\University_vault_2026\_app\_config\_library-system.md` ← protocolo de búsqueda y roles del stack

Flujo completo de incorporación de materia nueva:
  Paso 1 — Búsqueda de libros (este archivo) → stack aprobado
  Paso 2 — Subir PDFs a NLM → extraer índices verificados
  Paso 3 — Crear ETNXXX_library.md en guides/ETNXXX/ (fuente técnica para NLM)
  Paso 4 — Crear ETNXXX-study.md en prompts/ETNXXX/ (prompt de estudio)
  Ver flujo completo: `_app/_config/_notebooklm-system.md`

1. Completar YAML: subject, semester, tags, dates
2. Completar ## Objetivo de la materia
3. Pegar el temario completo en ## Temario oficial
4. Ejecutar búsqueda de libros con Claude (leer _library-system.md)
5. Llenar ## Bibliografía del docente si el docente la provee
6. Completar ## Stack completo al cerrar la búsqueda
7. Completar tablas "Qué usar por tema" con capítulos exactos
8. Mover archivo a raíz del vault como _library_ETNXXX.md al terminar

Libros puente (español):
- Incluir siempre una versión en español del libro principal si existe
- Rol: "Puente lingüístico" — mismo contenido, terminología en español para NLM
- Útil cuando el libro principal está en inglés y se necesita vocabulario técnico en español
- Ejemplo: Taylor inglés → Taylor Reverté como puente

Archivos divididos:
- Si un libro supera el límite de NLM, dividirlo por rangos de capítulos
- Registrar el rango exacto de cada parte en ## Archivos divididos
- Usar nombre de archivo descriptivo: Autor-titulo-idioma-CAPinicio_to_CAPfin.pdf
%%

---

## Objetivo de la materia

%%
2-4 líneas describiendo el objetivo general de la materia.
¿Qué métodos, herramientas o conocimientos desarrolla el estudiante?
%%

---

## Temario oficial

%%
Pegar el temario completo dividido por temas.
Usar ### TN — NOMBRE DEL TEMA como encabezado.
Incluir todos los subtemas con guion o lista.
%%

### T1 —

### T2 —

---

## Bibliografía del docente

%%
Lista de libros recomendados por el docente (si los provee).
Formato: - Título. Autor. Editorial.
Se evalúan en la búsqueda — pueden quedar en el stack o ser descartados.
%%

-

---

## Stack completo

%%
Llenar al cerrar la búsqueda de libros con Claude.
Incluir nombre exacto del archivo PDF tal como se carga en NLM.
%%

| Libro | Autor(es) | Edición / Año | Editorial | Rol | Archivo NLM | Idioma |
|---|---|---|---|---|---|---|
| | | | | Teoría principal | `` | |
| | | | | Puente lingüístico | `` | Español |
| | | | | Teoría rigurosa | `` | |
| | | | | Problemas resueltos | `` | |
| | | | | Problemas difíciles | `` | |

### Archivos divididos

%%
Solo si algún libro está dividido en partes para NLM.
%%

```
[Libro] — [Autor]
  caps. X–Y  → nombre-archivo-1.pdf
  caps. Z–W  → nombre-archivo-2.pdf
```

---

## Flujo de uso

```
Tema nuevo                → [libro de teoría principal]
No entiendo el fondo      → [libro riguroso]
Terminología en español   → [puente lingüístico]
Empezar a practicar       → [problemas estándar]
Práctica seria            → [problemas difíciles]
```

---

## Qué usar por tema — Teoría

| Tema | 1ª opción | 2ª opción |
|---|---|---|
| T1 — | | |
| T2 — | | |

---

## Qué usar por tema — Ejercicios

| Tema | 1ª opción | 2ª opción |
|---|---|---|
| T1 — | | |
| T2 — | | |

---

## Libros descartados

%%
Registrar libros evaluados y descartados durante la búsqueda.
%%

| Libro | Autor(es) | Razón |
|---|---|---|
| | | |

---

%%
# galaxy-links
[[_app/_config/_library-system.md]]
[[_app/_config/_notebooklm-system.md]]
%%
