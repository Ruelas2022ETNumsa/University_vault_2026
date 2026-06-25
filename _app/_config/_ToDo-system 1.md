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
tags: [beacon, todo, plugins, infraestructura]
date_created: 2026-05-29
date_updated: 2026-06-24
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
| PDF++ | Lectura y anotación de PDFs con links a página exacta | ✅ Instalado |
| Annotator | Lectura de EPUBs y PDFs escaneados | ✅ Instalado |
| OmniSearch | Búsqueda en todo el vault incluyendo PDFs | ✅ Instalado |
| Text Extractor | Dependencia de OmniSearch — extrae texto de PDFs e imágenes | ✅ Instalado |
| Remotely Save | ~~Sync del vault con Dropbox~~ — descartado para tablet | ⚠️ Instalado en PC — en desuso |
| File Hider | Ocultar archivos por extensión (.tmp, .bat, .ps1) | ✅ Instalado y configurado |
| Desmos | Renderizado de gráficas matemáticas interactivas en notas | ✅ Instalado y configurado |
| Completr | Autocompletado de LaTeX, tags y propiedades YAML | ✅ Instalado — pendiente configurar |
| Quick LaTeX | Shortcuts de escritura LaTeX: fracciones automáticas, cierre de llaves, salto entre bloques, shorthands personalizados | ✅ Instalado — pendiente configurar |

---

### Pendientes de instalar y configurar ⏳

| Plugin | Prioridad | Función |
|--------|-----------|---------|
| **TikZJax** | 🟡 Media | Renderizado de diagramas TikZ y circuitos electrónicos (circuitikz) dentro de notas |
| **Dataview** | 🔴 Alta — Fase 4 del sistema | Consultas sobre el YAML de las notas — filtra comets, asteroids, stars, notas pendientes por materia y parcial |
| **Linter** | 🟡 Media | Revisa y corrige automáticamente YAML y formato al guardar — detecta campos faltantes, tags mal escritos |
| **DB Folder** | 🟢 Baja — requiere Dataview | Vista de carpeta como tabla editable con campos YAML — instalar después de Dataview |

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

### Sincronización tablet — modelo actual (Samsung Cloud nativo, en discusión)
> Ver [[_TABnote-system]] — `status: activo` (cerrado 2026-06-24). El apunte manuscrito vive nativo en Samsung Cloud (`.sdocx`), sincronizado tablet ↔ PC. El PDF activo en el baúl quedó descartado; solo se genera un snapshot PDF al cerrar cada parcial, archivado en `_tabnotes_archivo/` (separado de `_PDF/`, fuera de Git). `galaxy_body: supernova` aprobado como tipo #14.
- [x] Validar empíricamente edición multi-dispositivo tablet ↔ PC vía Samsung Cloud (2026-06-20) ✅
- [ ] Repetir la prueba de edición multi-dispositivo en la laptop ASUS (Windows 11) — confirmar que el comportamiento se repite en un segundo equipo
- [x] Decidir: `supernova` como `galaxy_body` nuevo (tipo #14) — aprobado 2026-06-24. Resuelve la pregunta de `tabnote vs asteroid`. Registrado en [[_galaxy-system]], [[_note-system]], [[_template-system]], [[_TABnote-system]].
- [x] Definir disparador/recordatorio para generar el snapshot PDF al cerrar cada parcial — resuelto: campo `archive_snapshot` en plantilla + ítem en `_TABnote-system` registro de decisiones cerradas.
- [ ] Medir tamaño real del PDF+(Samsung) de cierre de parcial — para estimar peso acumulado en `_tabnotes_archivo/` a lo largo del semestre
- [ ] Confirmar convención real de subcarpetas dentro de `_PDF/` — el usuario reportó carpetas tipo `PDF-telefonia`, `PDF-921` (nombre de materia/tema en texto), que no coincide con el patrón documentado en [[_pdf-system]] (`_PDF/ETN806/`, una carpeta por sigla `ETNXXX`). Hay que decidir cuál es la convención real y actualizar [[_pdf-system]] en consecuencia.

### PDF++ — pendientes
- [ ] Crear guía `_pdf-plus-guide.md` en `_app/_appnotes/` — cómo anotar, subrayar, quemar anotaciones (flatten), y flujo completo actual con `_PDF/` + Mega (ya no con TAB_nexus)

### NotebookLM — guía de transcripción (TABnote)
- [ ] Guía de formato de apuntes manuscritos para que NotebookLM transcriba bien (¿Cornell? ¿headers claros? ¿prompt de configuración dedicado?) — documentar en [[_notebooklm-system]], referenciado desde [[_TABnote-system]]

### Plugins — configuración pendiente
- [ ] **TikZJax** — instalar y verificar que `circuitikz` renderiza correctamente (puede requerir reabrir Obsidian al primer render)
- [ ] **Completr** — revisar y ajustar configuración: activar sugerencias LaTeX, modo de trigger (backslash vs cualquier carácter), delay de sugerencias, y si se quiere word list del vault
- [ ] **Quick LaTeX** — revisar configuración: activar/desactivar funciones individuales (auto-fraction, auto-close brackets, align block, matrix block, shorthands personalizados); todas están en Settings → Quick LaTeX
- [ ] **Dataview** — instalar y configurar (ver Fase 4)
- [ ] **Linter** — instalar y configurar reglas para el Sistema Galaxy
- [ ] **DB Folder** — instalar después de Dataview

### Excalidraw
- [ ] Verificar que `tpl-constellation.md` y `tpl-observatory.md` abren correctamente como lienzo con Templater
- [ ] Crear primer `constellation` de prueba para ETN806-P2
- [ ] Instalar Mindmap Builder desde el Script Store de Excalidraw (si no está instalado)
- [ ] Ajustar configuración pendiente del plugin Excalidraw — ver [[_excalidraw-system]]

### Fase 1 — ETN806
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
- [ ] Aplicar Sistema Galaxy desde el primer día a cualquier materia nueva
- [ ] Actualizar `contextogen.md` para incluir el campo `galaxy_body` y `neutrino_type`

### Fase 3 — Conexiones entre galaxias
- [ ] Identificar conceptos compartidos entre ETN806 y ETN302
- [ ] Crear notas bridge
- [ ] Crear MOC a nivel universo en `MOC/`

### LaTeX
- [x] Crear `latex_guide.md` en `_app/_appnotes/` — referencia de comandos frecuentes para ETN806, snippets de Completr y atajos de Quick LaTeX documentados

### NotebookLM — prompts por materia
- [ ] Crear prompt de configuración para cada materia nueva siguiendo el modelo de Cálculo 1 (`_notebooklm-prompt.md`) — definir modos, stack de libros, programa y mapeo tema → libro prioritario. Ver [[notebooklm_modes]] para referencia de estructura.

### Fase 4 — DataView
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
%%
