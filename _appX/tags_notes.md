# Tags Routes — Guía de mantenimiento del plugin

> Archivo de referencia para entender, navegar y modificar el plugin `tags-routes`.
> El `main.js` tiene **~69,820 líneas / 2.5MB**, generado por esbuild desde TypeScript.
> Todo el código vive en un único archivo — no es posible separarlo en múltiples archivos.

---

## Por qué no se puede modularizar en archivos separados

Obsidian carga cada plugin como un único archivo `main.js` usando un loader interno de Electron. En ese contexto:

- `require()` **solo** acepta `"obsidian"` y módulos nativos de Node (`"path"`, `"fs"`, etc.)
- `require('./src/vendors.js')` falla con `Cannot find module` porque el loader no resuelve paths locales
- `__dirname` apunta a `C:\Program Files\Obsidian\resources\electron.asar\renderer` — incorrecto
- `module.filename` es `undefined` — no está expuesto en el contexto del plugin

**Se intentó en tres variantes y las tres fallaron:**

| Intento | Path usado | Error |
|---|---|---|
| v1 | `require('./src/vendors.js')` | `Cannot find module './src/vendors.js'` |
| v2 | `require(path.join(__dirname, 'src', 'vendors.js'))` | Resuelve a `C:\Program Files\Obsidian\...` |
| v3 | `require(path.join(path.dirname(module.filename), ...))` | `TypeError: "path" must be string. Received undefined` |

**Conclusión:** el `main.js` debe ser siempre un único archivo. La organización es lógica, no física.

---

## Estrategia adoptada — organización interna del main.js

Dado que no podemos separar archivos, el objetivo es hacer el código **navegable y mantenible** dentro del único `main.js` mediante:

1. **Marcadores de sección estandarizados** al inicio de cada bloque de código
2. **Tabla de contenidos comentada** al inicio del archivo (después de las librerías)
3. **Comentarios de método** en las funciones del código propio
4. **Etiquetas de riesgo** junto a las secciones delicadas

Esto permite usar `Ctrl+F` o la búsqueda del editor para navegar directamente a cualquier sección sin perderse en 70k líneas.

---

## Mapa del archivo main.js

### Bloque 1 — Librerías externas (NO TOCAR)
Líneas 1 – 66,521 · 2.4 MB · generado automáticamente por esbuild

| Rango | Librería | Qué hace |
|---|---|---|
| 1 – 36 | Boilerplate esbuild | Helpers `__export`, `__commonJS`, `__toESM`, etc. |
| 37 – 2,084 | ngraph | Motor de física de grafos alternativo |
| 2,085 – 24,447 | Three.js r169 | Motor 3D completo (WebGL) |
| 24,448 – 26,555 | DragControls | Arrastrar objetos 3D |
| 26,556 – 29,850 | three-forcegraph | Une Three.js con D3-force |
| 29,851 – 60,938 | three.webgpu.js | Motor 3D alternativo (WebGPU) |
| 60,939 – 62,699 | TrackballControls / OrbitControls / FlyControls | Modos de cámara 3D |
| 62,700 – 65,566 | EffectComposer + pipeline | Postprocesado de imagen |
| 65,567 – 66,091 | UnrealBloomPass | Efecto glow/bloom |
| 66,092 – 66,521 | three-spritetext | Texto flotante sobre nodos |

### Bloque 2 — Código propio del plugin (EDITABLE)
Líneas 66,522 – 69,820 · ~136 KB · esto es lo que mantenemos

| Rango | Sección | Estado |
|---|---|---|
| 65,878 – 66,521 | `settings.ts` | ✅ Comentado (sesión 5) |
| 66,522 – 68,852 | `TagsRoutes.ts` | ⏳ Pendiente (sesión 7+) |
| 68,853 – 69,203 | `CodeBlockProcessor.ts` | ✅ Comentado (sesión 5) |
| 69,204 – 69,820 | `main.ts` | ✅ Comentado (sesión 5) · ✅ Paleta galaxy (sesión 6) |

> **Nota:** Las funciones de utilidad (`DebugMsg`, `getTags`, `getFileType`, `PathFilter`, etc.) están mezcladas dentro del bloque de librerías entre las líneas 24,148 – 65,877 junto a las dependencias D3 y Three extras. Son código propio pero no conviene moverlas.

---

## Zonas por riesgo de modificación

### 🔴 NO TOCAR — Librerías bundleadas (líneas 1 – 66,521)

Cualquier cambio aquí rompe el plugin. Si una actualización del plugin sobreescribe `main.js`, este bloque se regenera automáticamente.

Librerías incluidas: `ngraph`, `Three.js r169`, `three.webgpu.js`, `DragControls`, `three-forcegraph`, `three-render-objects`, `3d-force-graph`, `d3-force-3d`, `d3-binarytree/quadtree/octree`, `EffectComposer`, `UnrealBloomPass`, `TrackballControls`, `OrbitControls`, `FlyControls`, `tinycolor2`, `polished`, `d3-scale`, `@tweenjs/tween.js`, `three-spritetext`, `lodash-es`, `kapsule`, `accessor-fn`.

---

### 🟡 REVISAR CON CUIDADO — Núcleo visual (líneas 66,522 – 68,852)

Clase `TagRoutesView` — interactúa con Three.js y con la API de Obsidian.

| Método | Qué hace | Riesgo |
|---|---|---|
| `buildGdata()` | Lee el vault, extrae enlaces y tags, construye nodos | Medio |
| `createGraph(container)` | Inicializa Three.js + física + eventos de ratón | Alto |
| `getNodeColorByType(node)` | Color según tipo de nodo | Bajo |
| `animate()` | Añade nodos progresivamente (time-lapse) | Medio |
| `captureAndSaveScreenshot()` | Captura canvas WebGL → PNG | Bajo |
| `handleNodeClick(node)` | Click en nodo → abre archivo | Bajo |
| `handleTagClick(node)` | Click en tag → genera reporte | Bajo |
| `switchTheme(visual)` | Cambia dark/light, reconstruye efectos bloom | Medio |
| `onSettingsSave()` | Aplica cambios de configuración en vivo | Medio |
| `focusGraphNodeById()` | Mueve cámara suavemente a un nodo | Bajo |
| `applyThemeColor()` | Lee colores CSS de Obsidian y los aplica | Bajo |

---

### 🟢 MODIFICAR LIBREMENTE — Lógica de negocio (líneas 68,853 – 69,820)

#### `CodeBlockProcessor.ts` (líneas 68,853 – 69,203)
Procesa bloques ` ```tagsroutes``` ` en las notas. Sin dependencias de Three.js.

```
tagProcessor(query)             → busca tags en contenido de archivos
frontmatterTagProcessor(query)  → busca tags en frontmatter YAML
timeDurationProcessor(query)    → filtra por rango de fechas
codeBlockProcessor()            → registrador principal del bloque
performanceCount                → mide duración de operaciones
```

#### `main.ts` (líneas 69,204 – 69,820)
Punto de entrada. Configuración y arranque del plugin.

```
globalProgramControl            → flags de debugging y comportamiento global
defaultolorMapDark/Light        → paletas de color por defecto
DEFAULT_DISPLAY_SETTINGS        → configuración de pantalla por defecto
TagsRoutes3 (clase Plugin)      → onload, initializePlugin, loadSettings, saveSettings
colorPickerGroup                → widget color picker (texto + selector de color)
TagsroutesSettingsTab           → página Settings → Tags Routes
```

#### `settings.ts` (líneas 65,878 – 66,521)
Clase `settingGroup` — construye la UI del panel lateral con sliders, toggles, botones y dropdowns mediante un patrón builder encadenado (`.addSlider().addToggle().addButton()`).

---

## Paleta de colores actual — defaultolorMapDark

Inspirada en fotografía real de galaxia espiral (núcleo dorado-naranja, brazos azul eléctrico, fondo negro profundo).

| Clave | Name | Value | Grupo temático |
|---|---|---|---|
| `markdown` | Spiral Arm | `#4FC3F7` | Brazos espirales (azul frío) |
| `attachment` | Star Cluster | `#81D4FA` | Brazos espirales (azul frío) |
| `excalidraw` | Ice Nebula | `#00B4D8` | Brazos espirales (azul frío) |
| `pdf` | Deep Blue | `#1565C0` | Brazos espirales (azul frío) |
| `tag` | Galactic Core | `#FFB347` | Núcleo galáctico (dorado) |
| `frontmatter_tag` | Solar Burst | `#FF8C42` | Núcleo galáctico (naranja) |
| `screenshot` | Amber Glow | `#FFC857` | Núcleo galáctico (ámbar) |
| `broken` | Red Dwarf | `#FF4444` | Errores |
| `nodeFocusColor` | Nova Flash | `#FFD166` | Estado de nodo |
| `nodeHighlightColor` | Arc Light | `#00E5FF` | Interacción |
| `linkHighlightColor` | Starlight | `#E3F2FD` | Interacción |
| `linkNormalColor` | Cosmic Dust | `#5B8FB9` | Links |
| `linkParticleColor` | Photon | `#B3E5FC` | Partículas |
| `linkParticleHighlightColor` | Flare | `#FFB347` | Partículas highlight |
| `selectionBoxColor` | Gold Ring | `#FFC857` | Selección |
| `backgroundColor` | Galaxy Black | `#080808` | Fondo |

**Nota:** `defaultolorMapLight` no se modificó, conserva los valores originales.

---

## Plan de trabajo — organización interna

### ✅ Completado

- [x] `settings.ts` — sesión 5
- [x] `CodeBlockProcessor.ts` — sesión 5
- [x] `main.ts` comentado — sesión 5
- [x] `main.ts` paleta galaxy — sesión 6

### ⏳ Pendiente

- [ ] `TagRoutesView` (líneas 66,522 – 68,852) — ~2,330 líneas, se divide en sub-bloques por método
- [ ] Paso E — marcar funciones de util mezcladas con vendors (`DebugMsg`, `PathFilter`, etc.)

### Paso A — Añadir tabla de contenidos al inicio del bloque propio
Insertar justo en la línea 66,522 un bloque de comentario con el índice de secciones y números de línea.

### Paso B — Etiquetar métodos de TagRoutesView ⏳
Añadir comentarios estandarizados encima de cada método indicando: qué hace, qué parámetros recibe, nivel de riesgo.

### Paso C — Marcar secciones de CodeBlockProcessor ✅
Completado en sesión 5.

### Paso D — Documentar globalProgramControl ✅
Completado en sesión 5.

### Paso E — Marcar funciones de util mezcladas con vendors ⏳
Las funciones `DebugMsg`, `getTags`, `getFileType`, `PathFilter`, `namedColor`, etc. están enterradas en el bloque de librerías. Añadir marcadores `// ▶ INICIO FUNCIONES PROPIAS` y `// ◀ FIN FUNCIONES PROPIAS` para localizarlas fácilmente.

---

## Notas importantes

- El `main.js` es generado por **esbuild** desde TypeScript. Si el plugin recibe una actualización, `main.js` se sobreescribirá y se perderán todos los cambios.
- **Recomendación:** antes de cualquier modificación, hacer copia manual en `_appX/backups/` con fecha.
- Para modificaciones permanentes, la vía correcta es hacer un fork del repositorio original y recompilar: https://github.com/kctekn/obsidian-TagsRoutes
- El backup automático del plugin está en: `main.js.1.2.3.bak` (raíz del plugin)

---

## Historial de cambios

### Sesión 1 — Análisis inicial
Mapeo completo de la estructura del `main.js`. Identificación de bloques, rangos de líneas y clasificación por riesgo.

### Sesión 2 — Intento: separación de vendors (FALLIDO)
**Objetivo:** Extraer las 66,521 líneas de librerías a `src/vendors.js` y cargarlas desde `main.js` con `require()`.

**Resultado:** Fallo. Obsidian no resuelve `require()` de paths locales. El loader interno de Electron solo acepta módulos de Node y `"obsidian"`. Tres variantes probadas, las tres con errores diferentes (ver tabla al inicio del documento).

**Restauración:** Se recuperó el `main.js` original desde el backup `main.js.1.2.3.bak`.

### Sesión 3 — Intento: extracción de CodeBlockProcessor (FALLIDO por la misma causa)
**Objetivo:** Extraer las ~350 líneas de `CodeBlockProcessor` a `src/CodeBlockProcessor.js`.

**Resultado:** Fallo por la misma razón que la sesión 2. El `require()` local no funciona en el entorno de Obsidian independientemente del path usado.

### Sesión 4 — Replanteo de estrategia
Conclusión: la modularización en archivos separados no es viable. La organización debe hacerse dentro del propio `main.js` mediante marcadores de sección, comentarios de métodos y una tabla de contenidos interna.

**Método de trabajo acordado:**
1. Se pega un bloque en el chat
2. Claude devuelve el mismo bloque con marcadores, comentarios de métodos y etiquetas de riesgo añadidos
3. Se revisa y se pega de vuelta en `main.js` en el rango correspondiente
4. Se pasa al siguiente bloque

**Orden de trabajo acordado** (de menor a mayor riesgo):
1. `settings.ts` — ~644 líneas
2. `CodeBlockProcessor.ts` — ~350 líneas
3. `main.ts` — ~617 líneas
4. `TagRoutesView` — ~2,330 líneas, dividida en sub-bloques

---

### Sesión 5 — Comentado de settings.ts, CodeBlockProcessor.ts y main.ts ✅

Se procesaron los tres bloques de menor riesgo en orden. A continuación el detalle de qué se documentó en cada uno.

---

#### settings.ts (líneas 65,878 – 66,521) — clase `settingGroup`

**Cabecera de sección:** se añadió un bloque de descripción general indicando el propósito de la clase, el patrón builder que usa, y la etiqueta de riesgo 🟢.

**Constructor:** se documentaron los cuatro tipos de contenedor (`"group"`, `"root"`, `"flex-box"`, `"normal-box"`) y qué estructura HTML crea cada uno. Se aclaró el comportamiento de los tres estados del tipo `"root"` (panel abierto / panel cerrado / botón oculto) que estaban implícitos en la lógica de `_goAction` y `opacity`, ya que sin comentario era difícil seguir el flujo.

**Métodos builder:** se comentó cada uno con su firma, efecto y nivel de riesgo. Los puntos clave que se aclararon:
- `add()` acepta tanto `HTMLElement` como otra instancia de `settingGroup`
- `hideAll()` afecta también al `_baseContainer` (añade `is-close` y quita padding), no solo a los hijos
- `addDropdown()` tiene el parámetro `defaultValue` que actualmente no se usa; el valor inicial siempre es `"broken"`
- `addToggle()` tiene el parámetro `needSave` que está reservado pero sin lógica activa
- `attachEl()` debe llamarse al final del chain porque es quien establece `_baseContainer`

---

#### CodeBlockProcessor.ts (líneas 68,853 – 69,203) — clase `codeBlockProcessor`

**Cabecera de sección:** descripción del flujo completo del procesador y lista de dependencias externas (`DebugMsg`, `globalProgramControl`, `getLineTime`, `PathFilter`).

**Constantes y regex:** se documentaron las cuatro variables globales del bloque, que antes no tenían explicación:
- `pattern_tags_char` y `pattern_timeStamp` son los bloques base que se combinan en otras regex
- `tagRegEx` detecta block-IDs generados por el plugin (`^tr-xxxxxxxxx`) al final de línea
- `regex_TagsWithTimeStamp` es la regex principal del sistema: captura grupos de tags (grupo 1) y timestamp opcional (grupo 2), y se reutiliza en todos los procesadores

**Clase `performanceCount`:** se explicó que `getTimeCost()` no solo devuelve el tiempo sino que reinicia el contador, lo que permite encadenar mediciones.

**Procesadores de query:** los tres métodos tienen lógica similar pero diferente criterio de filtrado. Se documentó qué los diferencia:
- `frontmatterTagProcessor` busca en YAML y no toca el contenido de los archivos
- `tagProcessor` busca en el body y puede modificar archivos para añadir block-IDs (`vault.modify`) — marcado 🟡
- `timeDurationProcessor` hace lo mismo que `tagProcessor` pero descarta párrafos fuera del rango de días; el filtro usa `getTimeDiffHour()` comparando contra `24 * queryDuration`

**Lógica de block-IDs:** documentada en detalle dentro de los dos procesadores que la usan. Se aclaró que primero busca si ya existe un `^tr-` al final del párrafo (`tagRegEx`) y solo genera uno nuevo si no lo encuentra, evitando duplicados.

**`getMarkdownContent()`:** se explicaron los dos modos controlados por `globalProgramControl`:
- `useGroup=true` agrupa resultados por tag usando un `Map`; el `throw "pushed"` dentro del `forEach` es intencional para salir al primer tag cuando `allowDuplicated=false`
- `useGroup=false` produce una lista plana ordenada por tiempo

**`codeBlockProcessor()` (entry point):** se documentó el flujo de los 6 pasos y se aclaró que muestra "PROCESSING..." antes de ejecutar la query y luego sobreescribe ese mensaje con el resultado final.

---

#### main.ts (líneas 69,204 – 69,820) — constantes globales y clases `TagsRoutes3`, `colorPickerGroup`, `TagsroutesSettingsTab`

**`globalProgramControl`:** se documentó cada flag individualmente, que antes no tenían ningún comentario:
- `useDiv` controla si el reporte se renderiza inline o sobreescribe el archivo fuente
- `debugLevel` es el umbral para `DebugMsg` (3=INFO, 4=DEBUG)
- `useGroup` y `allowDuplicated` controlan el modo de agrupación en `getMarkdownContent()`
- `aimBeforeLink` y `useTrackHighlight` afectan comportamiento del grafo
- `snapshotDirectory` y `generateLinker` son configuración de características específicas

**Paletas de color:** se alinearon visualmente las entradas del objeto para que sean comparables de un vistazo, y se señaló la única diferencia entre dark y light: `selectionBoxColor` y `backgroundColor`.

**`DEFAULT_DISPLAY_SETTINGS`:** se documentó que `link_distance` difiere entre temas (17 dark, 5 light) y se explicó el sistema de slots: `slot[0]` es siempre el slot de trabajo activo (clon de `slot[currentSlotNum]`), los slots 1–5 son los que persiste el usuario.

**`DEFAULT_SETTINGS`:** se aclaró el comportamiento de `customSlot` — es una referencia al array `dark[]` o `light[]` del tema activo, y se pone a `null` antes de guardar para evitar serializar una referencia circular.

**Clase `TagsRoutes3`:** se documentó el rol de `skipSave` (bloquea guardados durante la inicialización) y el flujo completo de `initializePlugin()` en 7 pasos. Se marcó el listener global de DOM con 🟡 porque captura todos los clicks del documento. Se explicó que `mergeDeep()` es un merge conservador: solo actualiza claves que ya existen en `target`, nunca añade claves nuevas.

**`loadSettings()`:** se documentó la lógica de compatibilidad de versiones con tres casos: merge normal, override por versión incompatible, e instalación nueva.

**Clase `colorPickerGroup`:** se explicó el flag `isProgrammaticChange` que evita bucles de `onChange` al sincronizar el campo de texto y el color picker entre sí.

**Clase `TagsroutesSettingsTab`:** se documentó que `skipSave=true` al inicio de `display()` y `skipSave=false` al final es un patrón deliberado para evitar guardados parciales mientras se construye la UI. Se marcó `colorMapSourceElement` con su clase CSS `tags-routes-need-save` que indica visualmente cambios pendientes.

---

### Sesión 6 — Rediseño de paleta `defaultolorMapDark` ✅

**Objetivo:** reemplazar los colores por defecto del tema oscuro por una paleta inspirada en fotografía real de galaxia espiral (núcleo dorado-naranja, brazos en azul eléctrico, fondo azul marino profundo). Referencia visual: imagen de galaxia espiral tipo Andrómeda.

**Iteraciones realizadas:**

Primera propuesta: colores de nebulosa con verdes saturados (`#00FFC6`), magentas (`#FF0099`) y violetas (`#6A00FF`). Descartada porque no correspondía a la imagen de referencia.

Segunda propuesta (aceptada con ajuste): paleta extraída directamente de la imagen — azules fríos para nodos de archivo, dorados y naranjas para tags, azul marino para fondo. El `backgroundColor` se ajustó posteriormente de `#060D1F` a `#080808` ("Galaxy Black") por preferencia de un negro más puro pero sin el efecto plano del `#000000` absoluto.

**Qué cambió en `defaultolorMapDark`:**

- Nodos de archivo (`markdown`, `attachment`, `excalidraw`, `pdf`): de verdes/cianes saturados a azules fotorrealistas que representan los brazos espirales fríos.
- Tags (`tag`, `frontmatter_tag`, `screenshot`): de magentas/violetas a dorados y naranjas del núcleo galáctico caliente.
- Links normales (`linkNormalColor`): de verde saturado a `#5B8FB9`, azul polvo cósmico de densidad media.
- Partículas highlight (`linkParticleHighlightColor`): a `#FFB347` naranja, simulando destellos del núcleo al activar nodos.
- Fondo (`backgroundColor`): `#080808` "Galaxy Black".
- Se añadieron comentarios de grupo inline en el código para agrupar visualmente las entradas por rol.

**`defaultolorMapLight`:** no se modificó.

**Nota sobre activación:** en instalaciones existentes los colores se cargan desde `data.json`. Para aplicar la nueva paleta: Settings → Tags Routes → Color → botón reset ↺, o borrar `data.json`.

**Posibilidad futura — fondo dinámico:** se evaluó si `backgroundColor` podría animarse con el tiempo. No es posible de forma nativa (valor estático). Para lograrlo habría que modificar `applyThemeColor()` o `onSettingsSave()` en `TagRoutesView` usando `tween.js` (ya bundleado) o HSL con tiempo del sistema. Queda anotado como mejora futura para cuando se trabaje `TagRoutesView` (🟡).

---

*Última actualización: sesión 6 — paleta galaxy aplicada a defaultolorMapDark.*
