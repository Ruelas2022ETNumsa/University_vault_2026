---
title: "ToDo Sistema — Plugins y Pendientes del Vault"
galaxy_body: beacon
scope: vault
audience: [usuario, claude]
related_notes:
  - "[[_galaxy-system]]"
  - "[[_note-system]]"
  - "[[_sync-system]]"
  - "[[_TABnote-system]]"
  - "[[_notebooklm-system]]"
tags: [beacon, todo, plugins, infraestructura]
date_created: 2026-05-29
date_updated: 2026-06-25
status: activo
---

# ToDo Sistema — Plugins y Pendientes del Vault

> Sistema Galaxy: [[_galaxy-system]]
> Convención de notas: [[_note-system]]
> Sistema Sync: [[_sync-system]]
> Sistema TABnote (apuntes de tablet): [[_TABnote-system]]

---

## Plugins

### Instalados ✅

| Plugin | Función | Estado |
|--------|---------|--------|
| Obsidian Git | Auto-commit, auto-push y auto-pull cada 5 min | ✅ Instalado y configurado |
| Templater | Creación dinámica de notas con YAML y movimiento automático | ✅ Instalado y configurado |
| Commander | Botón en ribbon para selector de plantillas | ✅ Instalado y configurado |
| Excalidraw | Motor de dibujo y mapas mentales — reemplaza Canvas | ✅ Instalado y configurado |
| PDF++ | Lectura y anotación de PDFs con links a página exacta | ✅ Instalado y configurado — guía en `_app/_appnotes/PDF_PP-guide.md` |
| Annotator | Lectura de EPUBs y PDFs escaneados | ✅ Instalado |
| OmniSearch | Búsqueda en todo el vault incluyendo PDFs | ✅ Instalado |
| Text Extractor | Dependencia de OmniSearch — extrae texto de PDFs e imágenes | ✅ Instalado |
| Remotely Save | ~~Sync del vault con Dropbox~~ — descartado para tablet | ⚠️ Instalado en PC — en desuso |
| File Hider | Ocultar archivos por extensión (.tmp, .bat, .ps1) | ✅ Instalado y configurado |
| Desmos | Renderizado de gráficas matemáticas interactivas en notas | ✅ Instalado y configurado |
| Completr | Autocompletado de LaTeX, tags y propiedades YAML | ✅ Instalado y configurado |
| Quick LaTeX | Shortcuts de escritura LaTeX: fracciones automáticas, cierre de llaves, salto entre bloques, shorthands personalizados | ✅ Instalado y configurado |
| TikZJax | Renderizado de diagramas TikZ y circuitos (circuitikz) | ✅ Instalado y funcionando |

---

### Retrasados — instalar cuando corresponda ⏳

| Plugin | Estado | Razón |
|--------|--------|-------|
| **Dataview** | ⏸️ Retrasado | Alenta el inicio de Obsidian — instalar en Fase 4 |
| **Linter** | ⏸️ Retrasado | Pendientes más prioritarios — instalar cuando se estabilice la infraestructura |
| **DB Folder** | ⏸️ Retrasado | Requiere Dataview primero — instalar en Fase 4 |

---

## Pendientes del sistema

### Sincronización tablet — HISTÓRICO (Google Drive, descartado)
> Este modelo ya no existe. `TAB_nexus` y todo Google Drive fueron eliminados — ver [[_sync-system]] (migración a Mega, 2026-06-13). Se deja la lista tal cual quedó, marcada como histórica, en vez de borrarla, para que quede registro de que se intentó y se abandonó.
- [x] ~~Decidir flujo tablet: Samsung Notes → PDF → Google Drive → vault~~ — descartado
- [x] ~~Carpeta `_pdf/TAB_nexus/` creada en el vault~~ — eliminada
- [x] ~~Crear carpeta `TAB_nexus` en Google Drive~~ — eliminada
- [x] ~~Google Drive File Stream configurado~~ — eliminado
- [x] ~~Symlink `_pdf/TAB_nexus` → `Mi unidad/TAB_nexus`~~ — eliminado
- [x] ~~Autosync instalado y configurado en tablet~~ — reemplazado por FolderSync + Mega
- [x] ~~Flujo tablet → vault verificado (Drive)~~ — superado por el flujo Mega
- [x] ~~Flujo vault → tablet verificado (Drive)~~ — superado por el flujo Mega

### Sincronización tablet — modelo actual (dos canales, cerrado 2026-06-24)
> Ver [[_TABnote-system]]. Dos canales independientes:
> - **Mega** → sincroniza el vault de Obsidian completo (PC ↔ laptop ↔ tablet ↔ celular).
> - **Samsung Account / Samsung Notes** → sincroniza los archivos `.sdocx` (apuntes manuscritos). Estos `.sdocx` **no forman parte del vault** — son material bruto que NotebookLM transcribe a notas `supernova`.
> El PDF activo en el baúl quedó descartado; solo se genera un snapshot PDF al cerrar cada parcial, archivado en `_tabnotes_archivo/` (separado de `_PDF/`, fuera de Git). `galaxy_body: supernova` aprobado como tipo #14.
- [x] Validar empíricamente edición multi-dispositivo tablet ↔ PC vía Samsung Cloud (2026-06-20) ✅
- [ ] Repetir la prueba de edición multi-dispositivo en la laptop ASUS (Windows 11) — confirmar que el comportamiento se repite en un segundo equipo
- [x] Decidir: `supernova` como `galaxy_body` nuevo (tipo #14) — aprobado 2026-06-24. Resuelve la pregunta de `tabnote vs asteroid`. Registrado en [[_galaxy-system]], [[_note-system]], [[_template-system]], [[_TABnote-system]].
- [x] Definir disparador/recordatorio para generar el snapshot PDF al cerrar cada parcial — resuelto: campo `archive_snapshot` en plantilla + ítem en `_TABnote-system` registro de decisiones cerradas.
- [ ] Medir tamaño real del PDF+(Samsung) de cierre de parcial — para estimar peso acumulado en `_tabnotes_archivo/` a lo largo del semestre
- [x] Confirmar convención real de subcarpetas dentro de `_PDF/` — **RESUELTO**: la convención real usa `PDF-nombre` (ej. `PDF-telefonia`, `PDF-921`), no siglas `ETNXXX`. Documentado en [[_pdf-system]]. Diagrama de carpetas en [[_galaxy-system]] actualizado a `PDF-nombre` (2026-06-25).

### PDF++ — estado
- [x] Guía `PDF_PP-guide.md` creada en `_app/_appnotes/` ✅ — flujo completo con `_PDF/` + Mega documentado

### Plugins — estado actualizado (2026-06-24)
- [x] **TikZJax** — instalado y funcionando, `circuitikz` verificado ✅
- [x] **Completr** — instalado y configurado ✅
- [x] **Quick LaTeX** — instalado y configurado ✅
- [ ] **Dataview** — ⏸️ retrasado (alenta inicio de Obsidian) — instalar en Fase 4
- [ ] **Linter** — ⏸️ retrasado (pendientes más prioritarios)
- [ ] **DB Folder** — ⏸️ retrasado (requiere Dataview primero) — instalar en Fase 4

### Excalidraw
> ⏸️ Retrasado — revisar en sesión futura
- [ ] Verificar que `tpl-constellation.md` y `tpl-observatory.md` abren correctamente como lienzo con Templater
- [ ] Crear primer `constellation` de prueba para ETN806-P2
- [ ] Instalar Mindmap Builder desde el Script Store de Excalidraw (si no está instalado)
- [ ] Ajustar configuración pendiente del plugin Excalidraw — ver [[_excalidraw-system]]

### Fase 1 — ETN806
> ⏸️ Retrasado — se hará con tiempo
- [ ] Crear estructura de carpetas: `Semesters/Sem_08/ETN806/Partial_2/Topic_NN.../`
- [ ] Mover archivos ETN806 existentes a las carpetas de tema correctas
- [ ] Agregar YAML galaxy a los archivos `ETN806-2P-E*.md` existentes → `galaxy_body: comet`
- [ ] Agregar YAML galaxy al Formulario → `galaxy_body: moon`
- [ ] Agregar YAML galaxy a Práctica enunciados → `galaxy_body: asteroid`
- [ ] Agregar YAML galaxy a Resuelto Referencia → `galaxy_body: comet`
- [ ] Crear notas star para cada tema del Parcial 2
- [ ] Crear notas planet para los conceptos centrales
- [ ] Crear MOC de ETN806 en `MOC/`
- [ ] Agregar bloques `%%` a todas las notas de ETN806

### Fase 2 — Materias nuevas
> ⏸️ Retrasado — se hará con tiempo
- [ ] Aplicar Sistema Galaxy desde el primer día a cualquier materia nueva
- [x] ~~Actualizar `contextogen.md`~~ → renombrado a `_claude-matter-boot.md`, movido a `_app/_config/`, convertido a beacon galaxy con YAML completo (2026-06-25). Pendiente aún: actualizar la entrevista y el contexto generado para incluir campos `galaxy_body` y `neutrino_type` — sesión futura.

### Fase 3 — Conexiones entre galaxias
> ⏸️ Retrasado — se hará con tiempo
- [ ] Identificar conceptos compartidos entre ETN806 y ETN302
- [ ] Crear notas bridge
- [ ] Crear MOC a nivel universo en `MOC/`

### LaTeX
- [x] Crear `latex_guide.md` en `_app/_appnotes/` — referencia de comandos frecuentes para ETN806, snippets de Completr y atajos de Quick LaTeX documentados

### NotebookLM — prompts por materia
- [x] **ETN806** (Procesos Estocásticos) — prompts para los 3 parciales ✅. Enfoque: resolución de ejercicios con Desmos, TikZJax y Mermaid. Contexto: guías de Desmos y TikZJax + archivos `.md` con ejercicios y fórmulas. Prompts muy funcionales — se usaron en los 3 parciales y ayudaron a generar gráficas con Desmos y diagramas TikZJax (incl. cadenas de Markov). **Pendiente de sesión futura aparte:** revisión minuciosa de los prompts reales — ver [[_notebooklm-system]] y `_app/notebooklm/`.
- [x] **MAT101** (Cálculo 1) — prompt para transcripción ✅. Enfoque: solo transcripción, no resolución de ejercicios.
- [ ] **ETN901** — sin prompt todavía.
- [ ] Prompts para materias futuras — sesión futura: Claude ayuda a crear un **generador de prompts** para sistematizar esto.
- [ ] Guía de formato de apuntes manuscritos para transcripción TABnote → supernova `.md` — sesión futura aparte, junto con la revisión de prompts.

### Sincronización de beacons — sesión 2026-06-25
- [x] **`_galaxy-system.md`** — ediciones rápidas: diagrama de `_PDF/` actualizado a `PDF-nombre`, conteo "Trece tipos" → "Catorce tipos" (la tabla ya incluía `supernova`). **Pendiente: revisión minuciosa completa en sesión futura aparte** (el usuario lo marcó explícitamente como insuficiente para una revisión rápida).
- [x] **`_pdf-system.md`** — verificado contra su backup (`_pdf-system 1.md`, may-2026) — ya estaba correctamente sincronizado con la convención `PDF-nombre`. Backup confirmado eliminable por el usuario. Sin cambios de contenido.
- [x] **`_library-system.md`** — estandarizado: agregado YAML frontmatter completo (no tenía) con `galaxy_body: beacon`, `related_notes`, tags, fechas; reemplazado el footer suelto por bloque `%% galaxy-links %%` sincronizado con el YAML.
- [x] **`_graph-system.md`** — verificado: ya describía TikZJax como instalado y funcionando (consistente con el cierre de Fase de plugins del 2026-06-24). Sin cambios de contenido, solo `date_updated`.
- [x] **`_mindmap-system.md`** — corregido: faltaba `[[_pdf-system]]` en el bloque `%%` final aunque estaba en el YAML `related_notes` y mencionado en el cuerpo — rompía la regla de dos capas sincronizadas del Sistema Galaxy. Agregado.
- [x] **`_basic-memory-system.md`** — versión instalada verificada con el usuario (`pip show basic-memory` / `basic-memory --version`): **0.21.6**, coincide con lo documentado. Sin cambios de contenido.
- [x] **`_notebooklm-system.md`** — reestructurado en sesión 2026-06-25: dos usos separados (transcripción / estudio), inventario completo de `_app/notebooklm/`, flujo TABnote actualizado, eliminada referencia a `_notebooklm-prompt.md`. **`_notebooklm-prompt.md` eliminado** — contenido migrado a `MAT101-study.md` y `MAT101-transcription.md` en `prompts/MAT101/`. Pendiente de sesión futura: revisión minuciosa de prompts reales de ETN806 — ver `_app/notebooklm/`.
- [ ] **`_excalidraw-system.md`** — sigue retrasado, sin tocar esta sesión (ver sección Excalidraw arriba).

### Fase 4 — DataView
> ⏸️ Retrasado — instalar cuando se estabilice la infraestructura
- [ ] Instalar Dataview
- [ ] Instalar DB Folder (después de Dataview)
- [ ] Consulta: todos los comets por materia y parcial
- [ ] Consulta: todas las notas pendientes de revisión
- [ ] Consulta: todos los bridges
- [ ] Dashboard por materia usando Dataview

%%
galaxy-links
[[_galaxy-system]]
[[_note-system]]
[[_sync-system]]
[[_excalidraw-system]]
[[_graph-system]]
[[_TABnote-system]]
[[_notebooklm-system]]
%%
