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
date_updated: 2026-05-29
status: activo
---

# ToDo Sistema — Plugins y Pendientes del Vault

> Sistema Galaxy: [[_galaxy-system]]
> Convención de notas: [[_note-system]]
> Sistema Sync: [[_sync-system]]

---

## Plugins recomendados

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
| Remotely Save | Sync del vault con Dropbox | ✅ Instalado en PC — pendiente configurar en móvil |
| File Hider | Ocultar archivos por extensión (.tmp, .bat, .ps1) | ✅ Instalado y configurado |
| Completr | Autocompletado de LaTeX, tags y propiedades YAML | ✅ Instalado |

---

### Pendientes de instalar ⏳

| Plugin | Prioridad | Función | Razón para instalarlo |
|--------|-----------|---------|----------------------|
| **Dataview** | 🔴 Alta — Fase 4 del sistema | Consultas sobre el YAML de las notas directamente en Obsidian | Hace útil todo el YAML del Sistema Galaxy: filtrar comets pendientes, listar asteroids por parcial, ver todas las stars de ETN806, etc. |
| **Linter** | 🟡 Media | Revisa y corrige automáticamente YAML y formato al guardar | Mantiene consistencia del Sistema Galaxy sin revisión manual — detecta campos faltantes, tags mal escritos, fechas incorrectas |
| **DB Folder** | 🟢 Baja — depende de Dataview | Muestra carpetas como tabla tipo base de datos con campos YAML editables | Útil para ver todos los ejercicios de un parcial como filas y editarlos directamente. Requiere Dataview instalado primero |

---

## Pendientes del sistema

### Sincronización móvil
- [ ] Instalar Remotely Save en Android y conectar al mismo Dropbox — ver [[_sync-system]]
- [ ] (Opcional, cuando haya tiempo) Configurar Git en Android con MGit — ver [[_sync-system]]

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

### Excalidraw
- [ ] Verificar que `tpl-constellation.md` y `tpl-observatory.md` abren correctamente como lienzo con Templater
- [ ] Crear primer `constellation` de prueba para ETN806-P2

### Fase 2 — Materias nuevas
- [ ] Aplicar Sistema Galaxy desde el primer día a cualquier materia nueva
- [ ] Actualizar `contextogen.md` para incluir el campo `galaxy_body`

### Fase 3 — Conexiones entre galaxias
- [ ] Identificar conceptos compartidos entre ETN806 y ETN302
- [ ] Crear notas bridge
- [ ] Crear MOC a nivel universo en `MOC/`

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
%%
