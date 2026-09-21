---
title: "DOC — ETN607 Study Prompt"
galaxy_body: beacon
scope: vault
audience: [usuario, claude]
tags: [beacon, notebooklm, ETN607, infraestructura, prompts, study, ejercicios]
date_created: 2026-09-20
date_updated: 2026-09-21
reviewed: 2026-09-21
status: activo
---

# DOC — ETN607 Study Prompt

Documentación del prompt de estudio y resolución de ejercicios para ETN607 (Mecánica Clásica / Lagrange) en NotebookLM.

---

## Archivos activos

| Archivo | Rol | Estado |
|---|---|---|
| `ETN607-study-P2v1.md` | Resolución de ejercicios T3–T4 + generación de figuras TikZJax | activo ✅ |

> Los prompts de Parcial 1 (`ETN607-study.md`, `ETN607-study-NLMv2.md`, `ETN607-study-NLMv3.md`) son **legacy** — conservados como referencia en `legacy/`. No usar.

---

## Para qué sirve `ETN607-study-P2v1`

Exclusivamente resolución de ejercicios T3–T4. No incluye consulta de concepto teórico.

**Mensajes disponibles:**
- **M1 / Resolver** — resolución de enunciado propio ingresado directamente
- **M2 / Enunciado** — recibe enunciado pulido desde Claude (detector P2) y lo resuelve
- **M3 / Variante** — recibe variante de un ejercicio base (P2-E1 a P2-E5) y lo resuelve completo

**Ejercicios de referencia cargados (P2):**

| Archivo | Sistema | N | Coord. |
|---|---|---|---|
| `P2-E1-607.md` | Bloque horizontal + 2 masas colgantes + 2 resortes | 2 | x₁, y₃ |
| `P2-E2-607.md` | Bloque en plano 60° + masa colgante | 1 | x₁ |
| `P2-E3-607.md` | 3 masas + polea + 2 resortes | 2 | y₃, a |
| `P2-E4-607.md` | Carro M + péndulo simple m | 2 | x, θ |
| `P2-E5-607.md` | Péndulo doble (igual longitud ℓ) | 2 | θ, φ |

**Procedimiento obligatorio:** Paso 0 (identificación) → Paso 1 (coord + GDL) → Paso 2 (T) → Paso 3 (V) → Paso 4 (Lagrange por cada qᵢ) → Paso 5 (EDOs encuadradas con `\boxed{}`)

**Genera figura TikZJax** de cada sistema antes de la resolución.

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

## Alcance temático — Parcial 2

| Tema | Contenido |
|---|---|
| T3 — Lagrange para una partícula | Deducción · integración · marcos móviles · restricciones móviles |
| T4 — Lagrange para sistema de partículas | Deducción · fuerzas generalizadas · marcos móviles · restricciones móviles |

Fuentes de teoría: Taylor Cap.7 · Goldstein Cap.1–2
Fuentes de ejercicios: Wells Cap.4–5 · Lim (sección Mechanics of a System)

## Detector de ejercicio — P2

Prompt para Claude (pre-NLM) que genera enunciados formales a partir de fotos o descripciones:

| Archivo | Alcance | Estado |
|---|---|---|
| `ETN607-ejercicio-detector_P1.md` | T1–T2 | legacy |
| `ETN607-ejercicio-detector_P2.md` | T3–T4 | activo ✅ |

Flujo: foto/descripción → Claude (detector P2) → snippet `Enunciado: ...` → NLM (study-P2v1 M2)

---

%%
# galaxy-links
[[ETN607-study-P2v1]]
[[ETN607-ejercicio-detector_P2]]
[[ETN607-ejercicio-detector_P1]]
[[ETN607-study]]
[[ETN607-study-NLMv2]]
[[ETN607-study-NLMv3]]
[[DOC-ETN607-transcription]]
[[_library_ETN607]]
[[P2-E1-607]]
[[P2-E2-607]]
[[P2-E3-607]]
[[P2-E4-607]]
[[P2-E5-607]]
%%
