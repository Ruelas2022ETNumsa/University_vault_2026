---
title: Sistema NotebookLM — University Vault
galaxy_body: beacon
scope: vault
audience:
  - usuario
  - claude
related_notes:
  - "[[_galaxy-system]]"
  - "[[_TAB_note-system]]"
  - "[[_library-system]]"
  - "[[guides/MAT101/MAT101_desmos]]"
  - "[[guides/MAT101/MAT101_TikzJax]]"
  - "[[_ToDo-system]]"
  - "[[Rclone_guide]]"
tags:
  - beacon
  - notebooklm
  - infraestructura
date_created: 2026-06-03
date_updated: 2026-07-10
status: activo
---

# Sistema NotebookLM — University Vault

> Sistema TABnote (transcripción de apuntes): [[_TAB_note-system]]
> Sistema de prompts: [[_app/_config/_prompt-system.md]]
> Protocolo de libros y fuentes: [[_library-system]]
> Guías de graficación (fuentes del notebook): [[guides/MAT101/MAT101_desmos]] · [[guides/MAT101/MAT101_TikzJax]]
> Pendientes: [[_ToDo-system]]

NotebookLM es el tutor externo del vault. Tiene dos usos distintos y bien separados:
**transcripción de apuntes manuscritos** y **estudio activo por materia**.
No reemplaza las notas galaxy — las produce (transcripción) o las enriquece (estudio).

---

## Los dos usos de NotebookLM

### Uso 1 — Transcripción de apuntes manuscritos

Convierte apuntes manuscritos en texto `.md` con LaTeX
listo para integrarse al vault como notas `supernova`.

**Flujo:**

```
1. Apunte manuscrito (cuaderno físico → PDF escaneado
   o tablet → export PDF desde Samsung Notes)
        ↓
2. PDF se sube a NotebookLM como fuente apuntesTX
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

**Variantes de transcripción disponibles:**

| Archivo | Materia | Tipo de apunte | Estado |
|---|---|---|---|
| `prompts/MAT101/MAT101-transcription.md` | Cálculo 1 | Cuaderno físico | activo |
| `prompts/MAT101/MAT101-transcription_tab.md` | Cálculo 1 | Tablet (Samsung Notes) | aún no creado |
| `prompts/ETNXXX/ETNXXX-transcription.md` | otras materias | general | aún no creado |

> Los apuntes de cuaderno físico y de tablet tienen estructuras distintas
> y requieren prompts separados. El prompt de tablet para MAT101
> es tema de sesión dedicada. Ver [[_ToDo-system]].

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
   - Guías de graficación (MAT101_desmos.md, MAT101_TikzJax.md, etc.)
        ↓
2. Se carga el prompt de configuración de la materia/parcial
   Vive en: _app/notebooklm/prompts/ETNXXX/
        ↓
3. Se estudia: ejercicios, explicaciones, graficación
   NotebookLM entrega bloques de código Desmos/TikZJax
   que se pegan directamente en notas galaxy del vault
        ↓
4. Si la nota en el vault cambia significativamente,
   rclone sync sube el .md a Drive automáticamente cada 5 horas
   → hacer refresh manual de la fuente en NotebookLM
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

### Prompts (`prompts/`)

Le dicen a NotebookLM cómo comportarse: modos de respuesta, reglas de
graficación, programa de la materia, prioridad de fuentes.
**Un prompt por materia/parcial. Se carga en el campo "Instructions" del notebook.**
Organizados en subcarpetas por materia: `prompts/MAT101/`, `prompts/ETN806/`, etc.
Ver inventario completo y convención de nombres: [[_app/_config/_prompt-system.md]]

Convención de nombres:
```
ETNXXX-PN-description.md    → prompt por parcial        (ej: ETN806-P1-study.md)
ETNXXX-description.md       → todos los parciales       (ej: MAT101-study.md)
```

**Inventario actual:**

| Archivo                                  | Materia               | Parcial                              | Estado    |
| ---------------------------------------- | --------------------- | ------------------------------------ | --------- |
| `prompts/ETN806/ETN806-P1.md`            | Procesos Estocásticos | P1 — Discretas                       | histórico |
| `prompts/ETN806/ETN806-P1-legacy.md`     | Procesos Estocásticos | P1                                   | histórico |
| `prompts/ETN806/ETN806-P2.md`            | Procesos Estocásticos | P2 — Continuas                       | histórico |
| `prompts/ETN806/ETN806-P3.md`            | Procesos Estocásticos | P3 — Markov/Colas                    | histórico |
| `prompts/MAT101/MAT101-study.md`         | Cálculo 1             | estudio activo (todos los parciales) | activo    |
| `prompts/MAT101/MAT101-transcription.md` | Cálculo 1             | transcripción cuaderno físico        | activo    |

### Guías fuente (`guides/`)

Archivos `.md` que se suben como **fuentes al notebook** para que NotebookLM
los consulte al responder. No son instrucciones de comportamiento — son
conocimiento técnico de referencia.
Organizadas en subcarpetas por materia: `guides/MAT101/`, `guides/ETN806/`, etc.

**Inventario actual:**

| Archivo | Contenido | Aplica a |
|---|---|---|
| `guides/MAT101/MAT101_desmos.md` | Sintaxis Desmos para Obsidian — sección NotebookLM | MAT101 |
| `guides/MAT101/MAT101_TikzJax.md` | Sintaxis TikZJax para Obsidian — sección NotebookLM | MAT101 |
| `guides/MAT101/MAT101_latex.md` | Notación LaTeX: cancelaciones, colores, cajas, fracciones | MAT101 |
| `guides/MAT101/MAT101_library.md` | Criterio de fuentes, caps y páginas por tema | MAT101 |
| `guides/ETN806/ETN806-P3-colas_guide_s.md` | Estructuras de teoría de colas con Mermaid | ETN806 P3 |
| `guides/ETN806/ETN806-P3-Tikz_markov_guide.md` | Diagramas de Markov con TikZ | ETN806 P3 |

**Carpeta `general/`:**

Guías reutilizables independientemente de la materia. Se suben como fuente en cualquier notebook.

| Archivo | Contenido | Aplica a |
|---|---|---|
| `general/obsidian_notation.md` | YAML, wikilinks, Cornell, callouts, bloques de visualización | todas las materias |

**Carpeta `other/`:**

Archivos en desuso pendientes de revisión. Cada uno debe resolverse como:
- **legacy** → renombrar con sufijo `-legacy`, mover a su carpeta de materia o a `general/` según scope
- **activar** → mejorar y mover a `prompts/`, `guides/` o `general/` según corresponda

| Archivo | Contenido | Estado |
|---|---|---|
| `other/MAT101-notebooklm-user_guide.md` | Guía personal de uso — modos y ejemplos MAT101 | activo |
| `general/tikzjax_guide-legacy.md` | Guía TikZJax genérica | legacy — renombrado y movido a `general/` |

### Guías de uso personal (`ETNXXX-notebooklm-user_guide.md`)

Documentación para el usuario: qué modos existen, cómo activarlos,
ejemplos de uso. No se suben a NotebookLM — son referencia personal.
Viven en `other/`.

| Archivo | Materia | Estado |
|---|---|---|
| `other/MAT101-notebooklm-user_guide.md` | Cálculo 1 | activo — base para otras materias |

---

## Flujo de incorporación de materia nueva

Cuando llega una materia nueva, el proceso completo para tenerla operativa
en NotebookLM sigue estos pasos en orden.

**Insumos de entrada:**
- Temario oficial (obligatorio)
- Bibliografía sugerida por el docente (opcional)

---

```
Paso 1 — Selección de libros (Claude)
   Entregar a Claude: temario + bibliografía sugerida (si existe)
   Claude evalúa la bibliografía existente y recomienda stack completo
   con roles definidos (teoría principal, rigurosa, ejercicios, complemento)
   Resultado: stack aprobado → ver protocolo completo en [[_library-system]]
        ↓
Paso 2 — Crear _library_ETNXXX.md (Claude)
   Claude genera el archivo en _app/_config/
   Contiene: temario completo + stack + tabla de qué usar por tema
   + tabla de ejercicios por tema + flujo de uso + libros descartados
   Audiencia: usuario — guía personal de referencia
        ↓
Paso 3 — Subir PDFs a NotebookLM y extraer índices
   Subir todos los PDFs del stack a un notebook temporal
   Pedirle a NotebookLM los índices detallados de cada libro
   (capítulos, secciones, páginas exactas)
   Revisar visualmente que los índices coincidan con los índices
   reales de los libros — NotebookLM puede cometer errores puntuales
   Pasar los índices verificados a Claude
        ↓
Paso 4 — Crear ETNXXX_library.md (Claude)
   Claude genera el archivo en _app/notebooklm/guides/ETNXXX/
   Contiene: tabla de teoría por tema (1ra fuente, 2da fuente, consulta,
   español) con capítulos y páginas exactas + tabla de ejercicios
   + notas de criterio + índice completo de cada PDF del stack
   Audiencia: NotebookLM — fuente técnica de navegación entre libros
        ↓
Paso 5 — Crear ETNXXX-study.md (Claude)
   Claude adapta el prompt base de MAT101-study.md
   Solo cambia: materia, nivel, fuentes prioritarias por tema
   La estructura de modos de respuesta no cambia
   Ruta: _app/notebooklm/prompts/ETNXXX/ETNXXX-study.md
        ↓
Paso 6 — Configurar NotebookLM
   Subir como fuentes: PDFs del stack + ETNXXX_library.md
   + obsidian_notation.md + guías de graficación si aplica
   Cargar ETNXXX-study.md en el campo Instructions del notebook
   El notebook queda operativo para estudio activo
```

> **Nota sobre el paso 3:** la verificación visual es necesaria porque
> NotebookLM puede reportar páginas o secciones incorrectas. Basta con
> revisar los índices de los libros (primeras páginas) para confirmar
> que los capítulos y rangos de página sean correctos.

> **Archivos que quedan como resultado de este flujo:**
> - `_app/_config/_library_ETNXXX.md` — guía personal
> - `_app/notebooklm/guides/ETNXXX/ETNXXX_library.md` — fuente NotebookLM
> - `_app/notebooklm/prompts/ETNXXX/ETNXXX-study.md` — prompt de estudio
> - Actualizar inventario de esta sección con los nuevos archivos

---

## Registro de decisiones

| Decisión | Razón                                                                                                                                                                           |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Dos usos separados (transcripción / estudio) | Son flujos con fuentes, prompts y outputs distintos — mezclarlos en un solo modelo generaba confusión                                                                           |
| Prompts en `_app/notebooklm/`, no en `_config/` | Los prompts son operativos por materia/parcial, no infraestructura del vault — pertenecen a su propia carpeta                                                                   |
| `_notebooklm-prompt.md` eliminado de `_config/` | Su contenido migró a `prompts/MAT101/MAT101-study.md` y `prompts/MAT101/MAT101-transcription.md`. El beacon de infraestructura es este archivo (`_notebooklm-system.md`)        |
| Un prompt por materia/parcial | Cada parcial tiene programa, fórmulas y nivel de rigor distintos — un prompt único por materia produce respuestas menos precisas a medida que avanza el semestre                |
| .md como fuente principal, no PDF | El .md preserva LaTeX como texto y código Desmos como referencia — el PDF los convierte a imagen y pierde contenido matemático                                                  |
| Guía de transcripción general en pausa | Requiere definir primero cómo estructurar los apuntes manuscritos para optimizar la transcripción — es decisión de diseño previa a la guía técnica                              |
| Sync de guías vía rclone + refresh manual en NotebookLM | NotebookLM no detecta cambios automáticamente — rclone sube las guías a Drive cada 5 horas (Task Scheduler); el refresh en NotebookLM sigue siendo manual. Ver [[Rclone_guide]] |
| `MAT101_desmos.md` siempre como fuente | Todas las materias pueden necesitar graficación — la guía garantiza sintaxis correcta en cualquier notebook                                                                     |
| Flujo de materia nueva documentado aquí y no en `_library-system` | El flujo es operativo de NotebookLM — `_library-system` cubre solo la selección de libros; este beacon cubre todo lo que sigue hasta tener el notebook activo                   |
| `_library_ETNXXX.md` separado de `ETNXXX_library.md` | Audiencias distintas: el primero es guía personal legible para el usuario; el segundo es fuente técnica densa para NotebookLM. Unirlos degradaría la utilidad de ambos          |

---

%%
# galaxy-links
[[_app/_config/_galaxy-system.md]]
[[_TAB_note-system]]
[[_app/_config/_library-system.md]]
[[_app/notebooklm/guides/MAT101/MAT101_desmos.md]]
[[_app/notebooklm/guides/MAT101/MAT101_TikzJax.md]]
[[_app/_config/_ToDo-system.md]]
[[_app/_appnotes/Rclone_guide.md]]
[[_app/_config/_prompt-system.md]]
%%
