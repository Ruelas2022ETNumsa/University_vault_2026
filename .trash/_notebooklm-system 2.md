---
title: Sistema NotebookLM — University Vault
galaxy_body: beacon
scope: vault
audience:
  - usuario
  - claude
related_notes:
  - "[[_galaxy-system]]"
  - "[[_TABnote-system]]"
  - "[[_library-system]]"
  - "[[desmos_guide]]"
  - "[[tikzjax_guide]]"
  - "[[_ToDo-system]]"
tags:
  - beacon
  - notebooklm
  - infraestructura
date_created: 2026-06-03
date_updated: 2026-07-02
status: activo
---

# Sistema NotebookLM — University Vault

> Sistema TABnote (transcripción de apuntes): [[_TABnote-system]]
> Protocolo de libros y fuentes: [[_library-system]]
> Guías de graficación (fuentes del notebook): [[desmos_guide]] · [[tikzjax_guide]]
> Pendientes: [[_ToDo-system]]

NotebookLM es el tutor externo del vault. Tiene dos usos distintos y bien separados:
**transcripción de apuntes manuscritos** y **estudio activo por materia**.
No reemplaza las notas galaxy — las produce (transcripción) o las enriquece (estudio).

---

## Los dos usos de NotebookLM

### Uso 1 — Transcripción de apuntes de tablet

Convierte apuntes manuscritos (`.sdocx` de Samsung Notes) en texto `.md` con LaTeX
listo para integrarse al vault como notas `supernova`.

**Flujo:**

```
1. Apunte escrito en Samsung Notes (.sdocx)
   Editado/limpiado desde PC o tablet vía Samsung Cloud
        ↓
2. Export puntual a PDF para subir a NotebookLM
   (el .sdocx nativo no se sube directamente)
        ↓
3. NotebookLM transcribe → entrega .md con LaTeX
        ↓
4. El .md se guarda en el vault como nota supernova
   Ruta: Semesters/Sem_NN/ETNXXX/Partial_N/
   Ver ciclo de vida completo: [[_TABnote-system]]
        ↓
5. La supernova se disecciona en notas galaxy
   (planet, moon, comet, etc.) según su contenido
```

**Guías de transcripción disponibles:**

| Archivo | Materia | Estado |
|---|---|---|
| `notebooklm-guides/MAT101-transcription_guide.md` | Cálculo 1 | activo |
| `ETNXXX-transcription_guide_tab.md` (general para tablet) | todas | **en pausa** — pendiente definir formato de apuntes manuscritos |

> La guía general de transcripción para apuntes de tablet está en pausa hasta
> resolver cómo estructurar los apuntes manuscritos para que NotebookLM los
> procese correctamente. Es tema de sesión dedicada. Ver [[_ToDo-system]].

---

### Uso 2 — Estudio activo por materia

NotebookLM actúa como tutor: resuelve ejercicios, explica conceptos, genera
bloques de código Desmos/TikZJax, y responde según el programa y las fuentes
de cada materia.

**Flujo:**

```
1. Se configuran las fuentes del notebook:
   - Libros de la materia (PDFs) — ver [[_library-system]]
   - Fuentes de ejercicios y formulario propio (.md del vault)
   - Guías de graficación (desmos_guide.md, tikzjax_guide.md, etc.)
        ↓
2. Se carga el prompt de configuración de la materia/parcial
   Vive en: _app/notebooklm/ETNXXX-PN-notebooklm_prompt.md
        ↓
3. Se estudia: ejercicios, explicaciones, graficación
   NotebookLM entrega bloques de código Desmos/TikZJax
   que se pegan directamente en notas galaxy del vault
        ↓
4. Si la nota en el vault cambia significativamente,
   se resubí el .md a NotebookLM (no sincroniza automático)
```

**Por qué .md como fuente y no PDF:**

| Aspecto | .md | PDF |
|---|---|---|
| LaTeX | Texto legible — NotebookLM lo interpreta sin ambigüedad | Puede renderizarse como imagen — pierde contenido |
| Desmos | Código fuente visible — útil como referencia de sintaxis | Imagen estática — NotebookLM lo ve como figura sin contenido |
| YAML | Ignorado naturalmente | No presente |

> Si en alguna consulta el YAML genera ruido, agregar al prompt:
> `"El bloque entre los primeros --- es YAML de metadatos — ignoralo."`

---

## Carpeta `_app/notebooklm/` — inventario y convención

Todos los archivos del sistema NotebookLM viven en `_app/notebooklm/`.
Hay tres tipos de archivos con roles distintos:

### Prompts (`ETNXXX-PN-notebooklm_prompt.md`)

Le dicen a NotebookLM cómo comportarse: modos de respuesta, reglas de
graficación, programa de la materia, prioridad de fuentes.
**Un prompt por materia/parcial. Se carga en el campo "Instructions" del notebook.**

Convención de nombres:
```
ETNXXX-PN-notebooklm_prompt.md    → prompt por parcial
ETNXXX-notebooklm_prompt.md       → si aplica a todos los parciales
```

**Inventario actual:**

| Archivo                           | Materia               | Parcial           | Estado    |
| --------------------------------- | --------------------- | ----------------- | --------- |
| `ETN806-P1-notebooklm_prompt.md`  | Procesos Estocásticos | P1 — Discretas    | activo    |
| `ETN806-P1-notebooklm(legacy).md` | Procesos Estocásticos | P1                | histórico |
| `ETN806-P2-notebooklm_prompt.md`  | Procesos Estocásticos | P2 — Continuas    | activo    |
| `ETN806-P3-notebooklm_prompt.md`  | Procesos Estocásticos | P3 — Markov/Colas | activo    |
| `MAT101-notebooklm_prompt.md`     | Cálculo 1             | todos             | activo    |

> MAT101 tiene un solo prompt para todos los parciales. En el futuro se separará
> por parciales siguiendo la misma convención `MAT101-PN-notebooklm_prompt.md`.

### Guías fuente (`notebooklm-guides/`)

Archivos `.md` que se suben como **fuentes al notebook** para que NotebookLM
los consulte al responder. No son instrucciones de comportamiento — son
conocimiento técnico de referencia.

**Inventario actual:**

| Archivo | Contenido | Aplica a |
|---|---|---|
| `desmos_guide.md` | Sintaxis Desmos para Obsidian — sección NotebookLM | todas las materias |
| `tikzjax_guide.md` | Sintaxis TikZJax para Obsidian — sección NotebookLM | todas las materias |
| `ETN806-P3-colas_guide_s.md` | Estructuras de teoría de colas con Mermaid | ETN806 P3 |
| `ETN806-P3-Tikz_markov_guide.md` | Diagramas de Markov con TikZ | ETN806 P3 |
| `MAT101-transcription_guide.md` | Guía de transcripción de apuntes | MAT101 |

### Guías de uso personal (`ETNXXX-notebooklm-user_guide.md`)

Documentación para el usuario: qué modos existen, cómo activarlos,
ejemplos de uso. No se suben a NotebookLM — son referencia personal.

| Archivo | Materia | Estado |
|---|---|---|
| `MAT101-notebooklm-user_guide.md` | Cálculo 1 | activo — base para otras materias |

---

## Cómo crear un prompt para una materia nueva

1. Copiar como base el prompt de una materia similar ya existente
2. Renombrar con la convención `ETNXXX-PN-notebooklm_prompt.md`
3. Adaptar: rol/materia, fuentes prioritarias por tema, modos si cambian
4. Subir las guías fuente necesarias al notebook (`desmos_guide.md` siempre,
   más las específicas de la materia si existen)
5. Actualizar el inventario de esta sección

> Plantilla base para prompts nuevos: pendiente — tema de sesión dedicada.
> Ver [[_ToDo-system]].

---

## Registro de decisiones

| Decisión | Razón |
|---|---|
| Dos usos separados (transcripción / estudio) | Son flujos con fuentes, prompts y outputs distintos — mezclarlos en un solo modelo generaba confusión |
| Prompts en `_app/notebooklm/`, no en `_config/` | Los prompts son operativos por materia/parcial, no infraestructura del vault — pertenecen a su propia carpeta |
| `_notebooklm-prompt.md` eliminado de `_config/` | Su contenido (prompt de MAT101) migró a `MAT101-notebooklm_prompt.md`. El beacon de infraestructura es este archivo (`_notebooklm-system.md`) |
| Un prompt por materia/parcial | Cada parcial tiene programa, fórmulas y nivel de rigor distintos — un prompt único por materia produce respuestas menos precisas a medida que avanza el semestre |
| .md como fuente principal, no PDF | El .md preserva LaTeX como texto y código Desmos como referencia — el PDF los convierte a imagen y pierde contenido matemático |
| Guía de transcripción general en pausa | Requiere definir primero cómo estructurar los apuntes manuscritos para optimizar la transcripción — es decisión de diseño previa a la guía técnica |
| Resubida manual al actualizar la nota | NotebookLM no sincroniza con el vault — resubir el .md cuando la nota cambie significativamente |
| `desmos_guide.md` siempre como fuente | Todas las materias pueden necesitar graficación — la guía garantiza sintaxis correcta en cualquier notebook |

%%
galaxy-links
[[_galaxy-system]]
[[_TABnote-system]]
[[_library-system]]
[[desmos_guide]]
[[tikzjax_guide]]
[[_ToDo-system]]
%%
