---
title: "DOC — ETN607 Study Prompt"
galaxy_body: beacon
scope: vault
audience: [usuario, claude]
tags: [beacon, notebooklm, ETN607, infraestructura, prompts, study, ejercicios]
date_created: 2026-09-20
date_updated: 2026-09-20
reviewed: 2026-09-20
status: activo
---

# DOC — ETN607 Study Prompt

Documentación del prompt de estudio y resolución de ejercicios para ETN607 (Mecánica Clásica / Lagrange) en NotebookLM.

---

## Archivos activos

| Archivo | Rol | Estado |
|---|---|---|
| *(pendiente)* | Prompt de estudio + resolución — Parcial 2 | por crear |

> Los prompts de Parcial 1 (`ETN607-study.md`, `ETN607-study-NLMv2.md`, `ETN607-study-NLMv3.md`) son **legacy** — conservados como referencia en `legacy/`. No usar.

---

## Para qué sirve este prompt

El prompt de study cubre dos funciones:

### Función 1 — Consulta de concepto puntual
Dado un nombre de concepto o subtítulo del temario, NLM busca en los libros fuente y entrega un bloque con definición formal + complemento nivel B o C.

**Mensajes disponibles (todas las versiones):**
- **M1 / Concepto** — consulta de un subtítulo del temario
- **M2 / Resolver** — resolución de enunciado propio paso a paso
- **M3 / Enunciado** *(desde v2)* — recibe enunciado pulido desde Claude y lo resuelve

### Función 2 — Resolución de ejercicios
El prompt recibe un enunciado (propio o externo) y lo resuelve con desarrollo algebraico completo, sin saltear pasos. Usa los ejercicios resueltos del parcial como referencia de nivel y formato.

---

## Historial de versiones — legacy

| Versión | Archivo | Fecha aprox. | Cambios clave |
|---|---|---|---|
| v1 | `ETN607-study.md` | anterior a 2026-08 | Versión base. M1 (concepto) + M2 (resolver). Ejercicios de referencia: P1-E1 a E11. TikZJax opcional sin reglas estrictas. Formato array con `$$\begin{array}`. |
| v2 | `ETN607-study-NLMv2.md` | 2026-08 | Agrega M3 (enunciado externo desde Claude). Ejercicios de referencia ampliados: P1-E1 a E23 con descripciones completas. Formato de ejercicio resuelto cambia a pasos con título descriptivo (`**Paso N — nombre**`). |
| v3 | `ETN607-study-NLMv3.md` | 2026-08 | Fork de v2. Agrega sección TikZJax con regla `\begin{tikzpicture}` obligatorio. Figura va después del enunciado y antes de la resolución. Sin otros cambios. |

---

## Diferencias clave entre versiones

### Formato de ejercicio resuelto

**v1** — array LaTeX compacto:
```
$$
\begin{array}{rcl}
\text{paso 1} & = & \text{expresión} \\[4pt]
\therefore\quad \color{orange}{\text{resultado}}
\end{array}
$$
```

**v2 / v3** — pasos con título descriptivo:
```
**Paso 1 — [nombre del paso]**
[explicación breve]
\[ expresión \]
```

### TikZJax

- **v1**: reglas mínimas, sin `\begin{tikzpicture}` explícito
- **v2**: sin sección TikZJax
- **v3**: sección TikZJax dedicada — `\begin{tikzpicture}` obligatorio dentro de `\begin{document}`

### Ejercicios de referencia cargados

- **v1**: P1-E1 a P1-E11 (incluyendo E10-1 y E10-2)
- **v2 / v3**: P1-E1 a P1-E23 con descripción de cada ejercicio

---

## Alcance temático cubierto — Parcial 1

Todos los prompts legacy cubrían exclusivamente **T1 y T2**:

| Tema | Contenido |
|---|---|
| T1 — Conceptos básicos I | Validez Newton · tipos de problemas · metodología dinámica |
| T2 — Conceptos básicos II | Coordenadas (rect/cil/esf) · GDL · restricciones · velocidad · T · aceleración |

Fuentes de teoría: Taylor Cap.1–2 · Alonso & Finn Vol.1 Cap.1–2
Fuentes de ejercicios: Nelson Cap.11–13 · Wells Cap.1–2

---

## Base para el prompt de Parcial 2

### Punto de partida recomendado
Fork de **v3** — es la versión más completa:
- TikZJax con `\begin{tikzpicture}` obligatorio ✓
- M3 para enunciados externos ✓
- Lista de ejercicios de referencia con descripción ✓

### Qué actualizar para Parcial 2
- **Temario**: reemplazar T1–T2 por los temas del Parcial 2 (T3–T8 según corresponda)
- **Fuentes**: actualizar según `_library_ETN607.md` para los nuevos temas
- **Ejercicios de referencia**: cargar los ejercicios resueltos del Parcial 2
- **Alcance**: actualizar la regla de rechazo (`Solo T1 y T2` → temas del P2)
- **Nombre sugerido**: `ETN607-study-NLMv4.md` o `ETN607-study-P2v1.md`

---

%%
# galaxy-links
[[ETN607-study]]
[[ETN607-study-NLMv2]]
[[ETN607-study-NLMv3]]
[[DOC-ETN607-transcription]]
[[_library_ETN607]]
%%
