---
title: "ToDo Sistema — Plugins y Pendientes del Vault"
galaxy_body: beacon
scope: vault
audience: [usuario, claude]
related_notes:
  - "[[_galaxy-system]]"
  - "[[_note-system]]"
  - "[[_sync-system]]"
tags: [beacon, todo, plugins, infraestructura]
date_created: 2026-05-29
date_updated: 2026-06-09
status: activo
---

# ToDo Sistema — Plugins y Pendientes del Vault

> Sistema Galaxy: [[_galaxy-system]]
> Convención de notas: [[_note-system]]
> Sistema Sync: [[_sync-system]]

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

### Sincronización tablet — Google Drive
- [x] Decidir flujo tablet: Samsung Notes → PDF → Google Drive → vault ✅
- [x] Carpeta `_pdf/TAB_nexus/` creada en el vault ✅
- [x] Crear carpeta `TAB_nexus` en Google Drive ✅
- [x] Apuntar Google Drive File Stream a sincronizar `_pdf/TAB_nexus/` en PC ✅
- [x] Verificar que la tablet puede exportar PDFs directamente a `TAB_nexus` en Drive ✅
- [x] Confirmar que los PDFs llegan físicamente al vault en PC sin depender de internet ✅

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
%%
