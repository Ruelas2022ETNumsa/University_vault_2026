---
title: "Claude Boot — Arranque de sesión"
galaxy_body: beacon
scope: vault
audience: [claude]
related_notes:
  - "[[_galaxy-system]]"
  - "[[_note-system]]"
  - "[[_template-system]]"
  - "[[_pdf-system]]"
  - "[[_mindmap-system]]"
  - "[[_sync-system]]"
  - "[[_ToDo-system]]"
tags: [beacon, claude, arranque, infraestructura]
date_created: 2026-05-30
date_updated: 2026-05-30
status: activo
---

# Claude Boot — Arranque de sesión

> Este archivo es el punto de entrada de Claude al vault. Leerlo es suficiente para operar correctamente en cualquier conversación. Los beacons completos están en `_app/_config/` si se necesita mayor profundidad.

---

## INSTRUCCIÓN DE ARRANQUE

Cuando el usuario comparta este archivo, Claude debe:

1. Leerlo completo.
2. Determinar el **modo de acceso** (ver sección Conectores).
3. Determinar si el usuario quiere trabajar con una **materia específica** o con la **infraestructura del vault**.
4. Si hay materia específica → leer su contexto según las rutas de la sección Materias.
5. Confirmar con un mensaje breve: _"Contexto cargado. ¿En qué trabajamos?"_

---

## EL VAULT — IDEA CENTRAL

`E:\University_vault_2026` es un cerebro digital para ingeniería universitaria. Cada nota tiene una ubicación precisa, un nombre limpio y un YAML que define su rol y sus conexiones.

El vault está organizado como un **universo de galaxias**. Cada materia es una galaxia. La metáfora vive en el campo `galaxy_body` del YAML de cada nota — no en los nombres de carpetas.

**Estado actual del vault: fase de construcción.**
El Sistema Galaxy está definido pero las carpetas de materias y notas académicas aún no existen. ETN302 es una materia legacy de un trabajo anterior — se considera obsoleta. Las materias nuevas se crearán cuando termine la fase de construcción.

---

## ESTRUCTURA DEL VAULT

```
University_Vault_2026/
│
├── Semesters/                  ← contenido académico (vacío en fase de construcción)
│   └── Sem_NN/
│       └── ETNXXX/
│           ├── Partial_1/
│           │   └── Topic_NN_nombre/
│           │       └── [notas]
│           ├── Partial_2/
│           └── Partial_3/
│
├── MOC/                        ← índices por materia (vacío en fase de construcción)
│
├── _app/
│   ├── _config/                ← beacons del sistema (aquí vive este archivo)
│   │   ├── _claude-boot.md     ← ESTE ARCHIVO
│   │   ├── _galaxy-system.md   ← sistema completo: tipos, YAML, convenciones
│   │   ├── _note-system.md     ← convención de nombres
│   │   ├── _template-system.md ← plantillas Templater
│   │   ├── _pdf-system.md      ← integración de PDFs
│   │   ├── _mindmap-system.md  ← Excalidraw + Mindmap Builder
│   │   ├── _excalidraw-system.md ← configuración del plugin
│   │   ├── _sync-system.md     ← sincronización GitHub + Dropbox
│   │   └── _ToDo-system.md     ← pendientes del sistema
│   ├── _appnotes/              ← guías de herramientas (Desmos, LaTeX, tags)
│   ├── Excalidraw/
│   │   ├── Constellations/     ← mapas mentales galaxy
│   │   └── Observatory/        ← dibujos técnicos libres
│   └── scripts/
│
├── _assets/                    ← imágenes exportadas (.png, .svg, .jpeg)
├── _pdf/                       ← archivos PDF físicos (una carpeta por materia)
├── _templates/                 ← plantillas de notas (tpl-star, tpl-planet, etc.)
└── borrar/                     ← zona de espera antes de eliminar archivos
```

---

## SISTEMA GALAXY — RESUMEN OPERATIVO

### Convención de nombres de notas

```
ETNXXX-TNN-nombre-descriptivo.md
```

- `ETNXXX` → código de materia (ej. `ETN806`)
- `TNN` → número de tema con cero (`T01`, `T03`). Usar `T00` para notas de parcial completo.
- `nombre-descriptivo` → slug corto en inglés con guiones

### Tipos de cuerpo galaxy (`galaxy_body`)

| Tipo | Símbolo | Rol |
|------|---------|-----|
| `star` | ☀️ | MOC del tema — enlaza todas las notas en órbita |
| `planet` | 🪐 | Teoría central — un concepto por nota |
| `moon` | 🌙 | Propiedad o fórmula — orbita un planet |
| `comet` | ☄️ | Ejercicio resuelto |
| `nebula` | 🌫️ | Agrupador de sesión |
| `dwarf` | ⬛ | Resumen de tema o parcial |
| `asteroid` | 🪨 | Referencia externa (libro, PDF, paper) |
| `photon` | 💡 | Imagen estática pura (.png, .jpg arrastrado, recorte PDF++) |
| `neutrino` | ⚛️ | Código que genera imagen (Desmos, TikZJax) — embebido en planet/comet, sin nota propia |
| `constellation` | 🌌 | Mapa mental — Excalidraw + Mindmap Builder |
| `observatory` | 🔭 | Dibujo técnico libre en Excalidraw |
| `bridge` | 🌉 | Conexión entre dos materias |
| `beacon` | 📡 | Guía de infraestructura del vault |

### Dos capas de conexión obligatorias

Toda nota debe tener sus conexiones en **dos lugares**:

```yaml
# En el YAML (para DataView y búsquedas):
orbiting:
  - "[[ETN806-T01-joint-pdf-definition]]"
```

```markdown
%% Al final del cuerpo (para el grafo de Obsidian):
galaxy-links
[[ETN806-T01-joint-pdf-definition]]
%%
```

### Ruta de carpeta por tipo

| `galaxy_body` | Carpeta destino |
|---|---|
| `star` | `MOC/` |
| `planet`, `moon`, `comet`, `nebula`, `asteroid`, `photon` | `Semesters/Sem_NN/ETNXXX/Partial_N/Topic_NN_nombre/` |
| `dwarf` | `Semesters/Sem_NN/ETNXXX/Partial_N/` |
| `bridge` | `Semesters/ETNXXX1-ETNXXX2/` |
| `constellation` | `_app/Excalidraw/Constellations/` |
| `observatory` | `_app/Excalidraw/Observatory/` |
| `beacon` | `_app/_config/` |

---

## CONECTORES — CÓMO ACCEDE CLAUDE AL VAULT

Claude tiene dos vías de acceso. Usar la que esté disponible:

| Situación | Conector | Acceso |
|-----------|----------|--------|
| PC encendida | **Filesystem MCP** | Lee y escribe directo en `E:\University_vault_2026` |
| PC apagada / móvil | **GitHub MCP** | Lee y escribe en `https://github.com/Ruelas2022ETNumsa/University_vault_2026` |

Obsidian Git sincroniza PC ↔ GitHub automáticamente cada 5 minutos. Los cambios hechos por Claude desde GitHub llegan al vault local en el próximo auto-pull.

**Claude no puede ejecutar comandos de terminal.** Solo leer y escribir archivos.

---

## MATERIAS ACTIVAS

> En fase de construcción. Ninguna materia tiene carpetas ni notas creadas aún.
> Completar esta sección cuando comience la fase de contenido.

### Plantilla para registrar una materia nueva

```
| Código | Nombre completo | Semestre | Parcial actual | Ruta |
|--------|----------------|----------|----------------|------|
| ETNXXX | Nombre         | N        | N              | Semesters/Sem_NN/ETNXXX/ |
```

### Materia legacy (no usar)

| Código | Estado |
|--------|--------|
| ETN302 | legacy — no forma parte del Sistema Galaxy |

---

## CÓMO OPERAR SEGÚN EL PEDIDO DEL USUARIO

### Si el usuario pide ayuda con una materia

1. Verificar que la materia existe en la sección Materias Activas.
2. Si existe → leer la star del tema correspondiente en `MOC/` o en `Semesters/`.
3. Leer las notas relevantes según el tipo de pedido (planet para teoría, comet para ejercicios, etc.).
4. Responder con el contexto real del vault — no de memoria genérica.

### Si el usuario pide crear una nota nueva

1. Respetar siempre el patrón de nombre: `ETNXXX-TNN-nombre-descriptivo.md`
2. Usar el YAML mínimo del tipo correspondiente (ver `_galaxy-system.md` para plantillas completas).
3. Incluir el bloque `%%` al final con los wikilinks galaxy.
4. Guardar en la ruta correcta según el tipo.
5. Si la carpeta destino no existe aún → avisarle al usuario antes de crear el archivo.

### Si el usuario pide ayuda con la infraestructura del vault

Leer el beacon específico según el tema:

| Tema | Beacon a leer |
|------|--------------|
| Sistema completo, tipos galaxy, YAML | `_app/_config/_galaxy-system.md` |
| Nombres de archivos, convención | `_app/_config/_note-system.md` |
| Plantillas Templater | `_app/_config/_template-system.md` |
| PDFs, plugin PDF++, asteroids | `_app/_config/_pdf-system.md` |
| Excalidraw, Mindmap Builder | `_app/_config/_mindmap-system.md` |
| Configuración plugin Excalidraw | `_app/_config/_excalidraw-system.md` |
| Sincronización GitHub, Dropbox | `_app/_config/_sync-system.md` |
| Pendientes del sistema | `_app/_config/_ToDo-system.md` |

### Si el usuario está en móvil sin PC encendida

- Usar GitHub MCP para leer y escribir notas.
- Avisar al usuario que los cambios llegarán al vault local en el próximo auto-pull de Obsidian Git (hasta 5 min después de encender la PC).

---

## REGLAS DE COMPORTAMIENTO DE CLAUDE EN ESTE VAULT

1. **Nunca borrar contenido original** — solo agregar o editar lo que se indica explícitamente.
2. **Respetar siempre la convención de nombres** — sin excepciones.
3. **Mantener las dos capas de conexión sincronizadas** — si se agrega un enlace al YAML, también va en el bloque `%%`.
4. **Respuestas concisas en el chat** — el detalle va en el archivo `.md`, no en la conversación.
5. **Si una ruta no existe aún** → decírselo al usuario antes de crear archivos, no asumir rutas.
6. **ETN302 es legacy** — no crear notas ni carpetas para esta materia.
7. **En fase de construcción** → el foco es la infraestructura, no el contenido académico.
8. **Actualizar `date_updated`** en el YAML de cualquier beacon que se modifique.

%%
galaxy-links
[[_galaxy-system]]
[[_note-system]]
[[_template-system]]
[[_pdf-system]]
[[_mindmap-system]]
[[_graph-system]]
[[_sync-system]]
[[_ToDo-system]]
%%
