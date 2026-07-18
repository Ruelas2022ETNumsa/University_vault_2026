---
title: Claude Boot — Arranque de sesión
galaxy_body: beacon
scope: vault
audience:
  - claude
related_notes:
  - "[[_galaxy-system]]"
  - "[[_note-system]]"
  - "[[_template-system]]"
  - "[[_pdf_pp-system]]"
  - "[[_library-system]]"
  - "[[_mindmap-system]]"
  - "[[_excalidraw-system]]"
  - "[[_graph-system]]"
  - "[[_sync-system]]"
  - "[[_basic-memory-system]]"
  - "[[_notebooklm-system]]"
  - "[[_TABnote-system]]"
  - "[[_ToDo-system]]"
  - "[[claude_solve]]"
  - "[[_claude-matter-boot]]"
  - "[[cornell_guide]]"
  - "[[Marginalia_guide]]"
tags:
  - beacon
  - claude
  - arranque
  - infraestructura
date_created: 2026-05-30
date_updated: 2026-07-18
status: activo
fase: infraestructura
---

%% fase: infraestructura — el vault está en construcción del sistema base (beacons, convenciones, plantillas, plugins, conectores). Aún no se crean notas académicas de forma sistemática. Cuando cambie la fase, actualizar este campo. %%
# Claude Boot — Arranque de sesión

> Este archivo es el punto de entrada de Claude al vault. Leerlo es suficiente para operar correctamente en cualquier conversación. Los beacons completos están en `_app/_config/` si se necesita mayor profundidad.

---

## INSTRUCCIÓN DE ARRANQUE

Cuando el usuario comparta este archivo, Claude debe:

1. Leerlo completo.
2. Determinar el **modo de acceso** (ver sección Conectores) — incluyendo si Basic Memory está disponible para búsqueda semántica.
3. Determinar si el usuario quiere trabajar con una **materia específica** o con la **infraestructura del vault**.
4. Si hay materia específica → leer su contexto según las rutas de la sección Materias.
5. Confirmar con un mensaje breve: _"Contexto cargado. ¿En qué trabajamos?"_
6. Para editar archivos existentes con Filesystem MCP: siempre `edit_file`, nunca `write_file` salvo que el usuario pida explícitamente sobrescribir o crear un archivo nuevo. (Ver [[claude_solve]] para errores conocidos.)
7. **Convención de backups establecida:** el usuario crea el respaldo (`nombre 1.md`) antes de pedir una edición significativa a un beacon de `_app/_config/`. Claude **no necesita ofrecer ni confirmar respaldo** — edita el original directamente. Ver convención completa en la sección **NOMENCLATURA DE BACKUPS** de este archivo.

---

## EL VAULT — IDEA CENTRAL

`E:\University_vault_2026` es un cerebro digital para ingeniería universitaria. Cada nota tiene una ubicación precisa, un nombre limpio y un YAML que define su rol y sus conexiones.

El vault está organizado como un **universo de galaxias**. Cada materia es una galaxia. La metáfora vive en el campo `galaxy_body` del YAML de cada nota — no en los nombres de carpetas.

**Estado actual del vault (verificado en disco, 2026-06-24): fase de construcción avanzada, no fase cero.**
- El Sistema Galaxy está definido y estable.
- Materia activa: `Semesters/Sem_09/ETN901/Partial_1/` — carpeta creada, sin notas todavía.
- `ETN506` fue eliminada — materia ya no relevante, carpeta borrada del vault.
- `MOC/` no tiene ninguna MOC real — solo 2 capturas de pantalla sueltas (`comfor numbss.png` y su copia), que no son parte del sistema y deberían moverse a `_assets/` o `borrar/`.
- `ETN302` es una materia legacy de un trabajo anterior — se considera obsoleta, no se le crean notas ni carpetas nuevas.
- El foco sigue siendo infraestructura: terminar Dataview, y luego recién empezar contenido académico real en ETN901. Las decisiones de tablet/TABnote ya quedaron cerradas (2026-06-24).

---

## ESTRUCTURA DEL VAULT

```
University_Vault_2026/
│
├── Semesters/                  ← contenido académico
│   └── Sem_09/
│       └── ETN901/
│           └── Partial_1/      ← creada, vacía
│
├── MOC/                        ← índices por materia (vacío de MOCs reales; tiene 2 imágenes sueltas a limpiar)
│
├── _app/
│   ├── notebooklm/    ← prompts y guías fuente — ver [[_notebooklm-system]]
│   │   ├── prompts/
│   │   ├── guides/
│   │   ├── general/
│   │   └── other/
│   │
│   ├── _config/                ← beacons del sistema (aquí vive este archivo)
│   │   ├── _claude-boot.md       ← ESTE ARCHIVO
│   │   ├── _galaxy-system.md     ← sistema completo: tipos, YAML, convenciones
│   │   ├── _note-system.md       ← convención de nombres
│   │   ├── _template-system.md   ← plantillas Templater
│   │   ├── _pdf-system.md        ← integración de PDFs (convención documentada — ver nota de discrepancia abajo)
│   │   ├── _library-system.md    ← protocolo de búsqueda y selección de libros
│   │   ├── _mindmap-system.md    ← Excalidraw + Mindmap Builder
│   │   ├── _excalidraw-system.md ← configuración del plugin Excalidraw
│   │   ├── _graph-system.md      ← Desmos / TikZJax (`neutrino`)
│   │   ├── _sync-system.md       ← sincronización GitHub + Mega
│   │   ├── _basic-memory-system.md ← MCP Basic Memory (memoria semántica)
│   │   ├── _notebooklm-system.md ← beacon del sistema NotebookLM (transcripción + estudio)
│   │   ├── _TABnote-system.md    ← apuntes de tablet — status: activo (cerrado 2026-06-24)
│   │   └── _ToDo-system.md       ← pendientes del sistema
│   ├── _appnotes/               ← guías de herramientas (LaTeX, tags, etc)
│   ├── Excalidraw/
│   │   ├── Constellations/      ← mapas mentales galaxy
│   │   └── Observatory/         ← dibujos técnicos libres
│   └── scripts/
│
├── _assets/                     ← imágenes exportadas (.png, .svg, .jpeg)
├── _PDF/                        ← ★ archivos PDF físicos — ver nota de discrepancia abajo
├── _skills/                     ← skills de Claude — work, plan, close, setup, boot
├── _projects/                  ← proyectos activos y backlog de ideas — ver [[_galaxy-system]]
├── _tabnotes_archivo/           ← propuesto en [[_TABnote-system]], aún no aprobado/creado — snapshots de cierre de parcial, fuera de Git
├── _templates/                  ← plantillas de notas (tpl-star, tpl-planet, etc.)
└── borrar/                      ← zona de espera antes de eliminar archivos
```

> ⚠️ **Discrepancia conocida en `_PDF/` (sin resolver, ver [[_ToDo-system]]):** `_pdf-system.md` documenta subcarpetas por sigla de materia (`_PDF/ETN806/`). En disco, las subcarpetas reales son por nombre de materia/tema en texto: `PDF-601`, `PDF-903`, `PDF-921`, `PDF-Electrónica analógica`, `PDF-Microprocesadores`, `PDF-telefonia`. También hay PDFs sueltos directo en la raíz de `_PDF/` sin subcarpeta. Claude debe usar la convención **real** que encuentre en disco al leer o guardar PDFs, no asumir `ETNXXX/` hasta que esta discrepancia se resuelva y `_pdf-system.md` se actualice.

---

## SISTEMA GALAXY — RESUMEN OPERATIVO

### Convención de nombres de notas

```
ETNXXX-TNN-nombre_descriptivo.md
```

- `ETNXXX` → código de materia (ej. `ETN806`, `ETN506`, `ETN901`)
- `TNN` → número de tema con cero (`T01`, `T03`). Usar `T00` para notas de parcial completo.
- `nombre_descriptivo` → slug corto en español o inglés con barra baja, sin tildes ni ñ.

### Tipos de cuerpo galaxy (`galaxy_body`)

| Tipo            | Símbolo | Rol                                                                                                                                     |
| --------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `star`          | ☀️      | MOC del tema — enlaza todas las notas en órbita                                                                                         |
| `planet`        | 🪐      | Teoría central — un concepto por nota                                                                                                   |
| `moon`          | 🌙      | Propiedad o fórmula — orbita un planet                                                                                                  |
| `comet`         | ☄️      | Ejercicio resuelto                                                                                                                      |
| `nebula`        | 🌫️     | Agrupador de sesión                                                                                                                     |
| `dwarf`         | ⬛       | Resumen de tema o parcial                                                                                                               |
| `asteroid`      | 🪨      | Referencia externa (libro, PDF, paper)                                                                                                  |
| `photon`        | 💡      | Imagen estática pura (.png, .jpg arrastrado, recorte PDF++)                                                                             |
| `neutrino`      | ⚛️      | Código que genera imagen (Desmos, TikZJax) — embebido en planet/comet, sin nota propia                                                  |
| `constellation` | 🌌      | Mapa mental — Excalidraw + Mindmap Builder                                                                                              |
| `observatory`   | 🔭      | Dibujo técnico libre en Excalidraw                                                                                                      |
| `bridge`        | 🌉      | Conexión entre dos materias                                                                                                             |
| `beacon`        | 📡      | Guía de infraestructura del vault                                                                                                       |
| `supernova`     | ✨       | Transcripción bruta de NotebookLM de apuntes de clase — material en bruto pendiente de disección en notas galaxy                        |
| `workshop`      | 🔧      | Tarea académica por materia — seguimiento de transcripción, estudio o proyecto puntual. Vive en `Semesters/`. Ver [[_template-system]]. |

> ✅ **Tipo #14 aprobado (2026-06-24):** `supernova` quedó cerrado como `galaxy_body` oficial para transcripciones de NotebookLM de apuntes de clase (ver [[_TABnote-system]] y [[_ToDo-system]]). La propuesta original era `tabnote`, pero se descartó ese nombre a favor de `supernova` antes de aprobarse.

> ✅ **Tipo #15 aprobado (2026-07-18):** `workshop` quedó cerrado como `galaxy_body` oficial para tareas académicas por materia (ver [[_galaxy-system]]). Cuatro variantes según etapa: `tpl-w-initial`, `tpl-w-transcription`, `tpl-w-study`, `tpl-w-project`. Vive en `Semesters/`.

### Dos capas de conexión obligatorias

Toda nota debe tener sus conexiones en **dos lugares**:

```yaml
# En el YAML (para DataView y búsquedas):
orbiting:
  - "[[ETN806-T01-ejemplo_pdf_definicio]]"
```

```markdown
%% Al final del cuerpo (para el grafo de Obsidian):
galaxy-links
[[ETN806-T01-ejemplo_pdf_definicio]]
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
| `supernova` | `Semesters/Sem_NN/ETNXXX/Partial_N/` (raíz del parcial, no dentro de `Topic_NN/`) |

---

## SISTEMA DE LINKS — DOS CAPAS

El vault mantiene dos capas de conexión en cada nota. Son redundantes intencionalmente durante la fase de transición:

| Capa | Ubicación | Para quién | Estado |
|---|---|---|---|
| `related_notes` en YAML | Frontmatter | Obsidian + Claude | Activo — se elimina cuando se confirme que `galaxy-links` sostiene el grafo solo |
| `%% galaxy-links %%` | Pie del archivo | Obsidian + Claude | Activo — fuente principal a largo plazo |

### Cómo Claude usa los galaxy-links

El Filesystem MCP tiene como raíz `E:\University_vault_2026`. Los `galaxy-links` usan ruta relativa desde esa raíz:

```
%%
# galaxy-links
[[_app/_config/_galaxy-system]]
[[Semesters/Sem_01/MAT101/Partial_1/T00-numeros_reales/MAT101-T00-axiomas_cuerpo.md]]
## Links a notas pendientes de crear
[[Semesters/Sem_01/MAT101/Partial_1/T00-numeros_reales/no_existe.md]]



%%
```

Si Claude necesita más contexto sobre un archivo enlazado, puede leerlo directamente usando la ruta del wikilink como ruta relativa desde la raíz del vault. No es necesario escribir la ruta absoluta en el link.

---

## CONECTORES — CÓMO ACCEDE CLAUDE AL VAULT

Claude tiene **tres** vías de acceso. Usar la que esté disponible y la que corresponda a la tarea:

| Situación / tarea | Conector | Acceso |
|---|---|---|
| PC encendida — leer/crear/editar archivos puntuales | **Filesystem MCP** | Lee y escribe directo en `E:\University_vault_2026` |
| PC apagada / móvil — leer o editar sin PC | **GitHub MCP** | Lee y escribe en `https://github.com/Ruelas2022ETNumsa/University_vault_2026` |
| Cualquier situación — buscar por significado, no por nombre exacto; recordar contexto entre sesiones | **Basic Memory MCP** | Indexado semántico local de todo el vault (`BASIC_MEMORY_PROJECT_PATH`) — ver [[_basic-memory-system]] |

**Cómo elegir:**
- Si el usuario pide "busca las notas sobre X" sin saber el nombre exacto del archivo → preferir **Basic Memory** (`search_notes`) sobre Filesystem.
- Si el usuario pide editar, mover o crear un archivo específico → **Filesystem MCP** (PC encendida) o **GitHub MCP** (sin PC).
- Basic Memory y Filesystem conviven — no son excluyentes. Basic Memory no reemplaza la necesidad de Filesystem/GitHub para escribir, solo aporta búsqueda semántica y memoria.

Obsidian Git sincroniza PC ↔ GitHub automáticamente cada 5 minutos. Mega sincroniza el vault entre PC, laptop, tablet y celular (ver [[_sync-system]]) — esa sincronización es independiente de GitHub y de los conectores de Claude. Los cambios hechos por Claude desde GitHub llegan al vault local en el próximo auto-pull.

**Claude no puede ejecutar comandos de terminal.** Solo leer y escribir archivos (Filesystem/GitHub) o indexar/buscar (Basic Memory).

---

## MATERIAS ACTIVAS

> solo es un ejemplo no tomar como verdad, aun no hay materias activas.

| Código | Nombre completo      | Semestre | Parcial actual | Ruta                                 | Estado                    |
| ------ | -------------------- | -------- | -------------- | ------------------------------------ | ------------------------- |
| ETN901 | *(completar nombre)* | 9        | 1              | `Semesters/Sem_09/ETN901/Partial_1/` | Carpeta creada, sin notas |

> El nombre completo de ETN901 no está registrado todavía — completar con el usuario cuando se inicie trabajo en esa materia.

### Materias eliminadas

| Código | Motivo |
|--------|--------|
| ETN506 | Eliminada 2026-06-24 — materia ya no relevante, carpeta borrada del vault |

### Materia legacy (no usar)

| Código | Estado |
|--------|--------|
| ETN302 | legacy — no forma parte del Sistema Galaxy |

---

## CÓMO OPERAR SEGÚN EL PEDIDO DEL USUARIO

### Si el usuario pide ayuda con una materia

1. Verificar que la materia existe en la sección Materias Activas.
2. Si existe → leer la star del tema correspondiente en `MOC/` o en `Semesters/`. Si la carpeta está vacía (como ETN901 hoy), decírselo en vez de asumir contenido.
3. Leer las notas relevantes según el tipo de pedido (planet para teoría, comet para ejercicios, etc.).
4. Responder con el contexto real del vault — no de memoria genérica.

### Si el usuario pide crear una nota nueva

1. Respetar siempre el patrón de nombre: `ETNXXX-TNN-nombre_descriptivo.md`
2. Usar el YAML mínimo del tipo correspondiente (ver `_galaxy-system.md` para plantillas completas). El tipo #14 aprobado es `supernova` (la propuesta original `tabnote` se descartó antes de aprobarse — nunca usar `galaxy_body: tabnote`).
3. Incluir el bloque `%%` al final con los wikilinks galaxy.
4. Guardar en la ruta correcta según el tipo.
5. Si la carpeta destino no existe aún → avisarle al usuario antes de crear el archivo.

### Si el usuario pide ayuda con la infraestructura del vault

Leer el beacon específico según el tema:

| Tema                                                     | Beacon a leer                                                      |
| -------------------------------------------------------- | ------------------------------------------------------------------ |
| Sistema completo, tipos galaxy, YAML                     | `_app/_config/_galaxy-system.md`                                   |
| Nombres de archivos, convención                          | `_app/_config/_note-system.md`                                     |
| Plantillas Templater                                     | `_app/_config/_template-system.md`                                 |
| PDFs, plugin PDF++, asteroids                            | `_app/_config/_pdf-system.md` (ver discrepancia de `_PDF/` arriba) |
| Excalidraw, Mindmap Builder                              | `_app/_config/_mindmap-system.md`                                  |
| Configuración plugin Excalidraw                          | `_app/_config/_excalidraw-system.md`                               |
| Desmos / TikZJax (`neutrino`)                            | `_app/_config/_graph-system.md`                                    |
| Sincronización GitHub + Mega                             | `_app/_config/_sync-system.md`                                     |
| Memoria semántica (Basic Memory MCP)                     | `_app/_config/_basic-memory-system.md`                             |
| NotebookLM (tutor externo)                               | `_app/_config/_notebooklm-system.md`                               |
| Apuntes de tablet — activo, cerrado 2026-06-24           | `_app/_config/_TABnote-system.md`                                  |
| Pendientes del sistema                                   | `_app/_config/_ToDo-system.md`                                     |
| Protocolo de búsqueda y selección de libros              | `_app/_config/_library-system.md`                                  |
| Contexto de trabajo por materia (ejercicios, formulario) | `_app/_config/_claude-matter-boot.md`                              |
| Prompts y guías NotebookLM por materia                   | `_app/notebooklm/`                                                 |
| Cornell Notes + Marginalia                               | `_app/_appnotes/cornell_guide.md`                                  |
| Skills de Claude (work, plan, close, setup, boot)        | `_skills/`                                                         |
| Sistema de proyectos y backlog (`_projects/`, `tsk_`, `_ideas`) | `_app/_config/_galaxy-system.md` |

### Si el usuario está en móvil sin PC encendida

- Usar GitHub MCP para leer y escribir notas.
- Avisar al usuario que los cambios llegarán al vault local en el próximo auto-pull de Obsidian Git (hasta 5 min después de encender la PC), y que la sincronización con Mega hacia tablet/celular es un canal aparte.

---

## NOMENCLATURA DE BACKUPS

Convención interna del vault para respaldar archivos antes de editarlos:

| Archivo | Su backup |
|---|---|
| `nombre.md` | `nombre 1.md` |
| `nombre 1.md` | `nombre 2.md` |

**Reglas:**
- El archivo **sin número** es siempre el **original activo** — el que Claude lee y edita.
- El archivo **con número** (`nombre 1.md`, `nombre 2.md`…) es siempre el **backup** — no se toca, solo se conserva como respaldo.
- Si ya existe un `nombre 1.md`, el siguiente backup es `nombre 2.md`, y así sucesivamente.
- Obsidian puede generar automáticamente copias con este mismo patrón (`nombre 1.md`) al mover o duplicar archivos — eso es compatible con esta convención.
- Claude **nunca edita un archivo con número en el nombre** salvo instrucción explícita del usuario.
- Ejemplo real en este vault: `_pdf-system 1.md` es el backup de `_pdf-system.md`; `_claude-boot 1.md` es el backup de este archivo.

> Esta convención aplica a todos los archivos del vault, no solo a los beacons.

---

## REGLAS DE COMPORTAMIENTO DE CLAUDE EN ESTE VAULT

1. **Nunca borrar contenido original** — solo agregar o editar lo que se indica explícitamente.
2. **Respetar siempre la convención de nombres** — sin excepciones.
3. **Mantener las dos capas de conexión sincronizadas** — mientras `related_notes` esté activo, todo enlace nuevo va también en el bloque `%%` con ruta relativa desde la raíz del vault. Cuando `related_notes` se elimine, el bloque `%%` será la única fuente de verdad.
4. **Respuestas concisas en el chat** — el detalle va en el archivo `.md`, no en la conversación.
5. **Si una ruta no existe aún** → decírselo al usuario antes de crear archivos, no asumir rutas.
6. **ETN302 es legacy** — no crear notas ni carpetas para esta materia.
7. **`galaxy_body: supernova` es el tipo #14 aprobado** — `tabnote` fue la propuesta original, descartada antes de aprobarse. Nunca usar `galaxy_body: tabnote` en notas reales.
8. **Ante discrepancias entre lo documentado y lo que hay en disco** (como `_PDF/`) → confiar en lo que hay en disco y avisar de la discrepancia, no forzar la convención documentada.
9. **El usuario crea los backups, Claude edita el original directamente** — no ofrecer ni confirmar respaldo antes de editar un beacon, salvo que el usuario indique lo contrario.
10. **Actualizar `date_updated`** en el YAML de cualquier beacon que se modifique.
11. **Archivos en `_projects/` no tienen `galaxy_body`** — son operativos y temporales. No agregar `galaxy_body` a ningún `tsk_alias.md`, `tsk_tpl.md` ni `_ideas.md`.
12. **`workshop` es el tipo #15** — usar solo en plantillas `tpl-w-*` dentro de `Semesters/`. Nunca asignar `galaxy_body: workshop` a archivos de `_projects/`.

---

%%
# galaxy-links
[[_app/_config/_galaxy-system.md]]
[[_app/_config/_note-system.md]]
[[_app/_config/_template-system.md]]
[[_pdf_pp-system]]
[[_app/_config/_library-system.md]]
[[_app/_config/_mindmap-system.md]]
[[_app/_config/_excalidraw-system.md]]
[[_app/_config/_graph-system.md]]
[[_app/_config/_sync-system.md]]
[[_app/_config/_basic-memory-system.md]]
[[_app/_config/_notebooklm-system.md]]
[[_app/_config/_TABnote-system.md]]
[[_app/_config/_ToDo-system.md]]
[[_app/solve/claude_solve.md]]
[[_app/_config/_claude-matter-boot.md]]
[[_app/_appnotes/cornell_guide.md]]
[[_app/_appnotes/Marginalia_guide.md]]
%%
