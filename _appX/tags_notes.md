# Tags Routes — Guía de Modularización

> Archivo de referencia para el proceso de refactorización del plugin `tags-routes`.  
> El `main.js` original tiene **~69,820 líneas / 2.5MB**, generado por esbuild desde TypeScript.

---

## Estado actual del archivo

| Rango de líneas | Contenido | Tamaño estimado |
|---|---|---|
| 1 – 2,061 | Dependencias externas (ngraph) | ~2k líneas |
| 2,062 – 24,447 | Three.js r169 completo (bundleado) | ~22k líneas |
| 24,448 – 65,877 | `util.ts` + todas sus dependencias D3/Three extras | ~41k líneas |
| 65,878 – 66,521 | `settings.ts` — UI del panel lateral | ~644 líneas |
| 66,522 – 68,852 | `TagsRoutes.ts` — núcleo visual | ~2,330 líneas |
| 68,853 – 69,203 | `CodeBlockProcessor.ts` — bloques de código | ~350 líneas |
| 69,204 – 69,820 | `main.ts` — punto de entrada del plugin | ~617 líneas |

---

## Zonas clasificadas por riesgo de modificación

### 🔴 NO TOCAR — Librerías de terceros bundleadas
Estas secciones son código de terceros comprimido. Modificarlas rompe el plugin.

- **Three.js r169** (líneas ~2,085 – 24,447)  
  Motor 3D completo. Renderizado WebGL, geometrías, materiales, cámara.

- **ngraph** (líneas 1 – 2,061)  
  Motor de simulación de fuerzas alternativo.

- **d3-force-3d / d3-binarytree / d3-quadtree / d3-octree** (dentro de util.ts)  
  Simulación de física del grafo en 3D.

- **three-forcegraph / three-render-objects / 3d-force-graph** (dentro de util.ts)  
  Capa de alto nivel que une Three.js con D3.

- **EffectComposer / UnrealBloomPass / RenderPass** (dentro de util.ts)  
  Pipeline de postprocesado — el efecto glow/bloom.

- **TrackballControls / OrbitControls / FlyControls** (dentro de util.ts)  
  Los tres modos de cámara 3D.

- **tinycolor2 / polished / d3-scale / d3-scale-chromatic** (dentro de util.ts)  
  Manejo de colores y escalas.

- **@tweenjs/tween.js** (dentro de util.ts)  
  Animaciones suaves con interpolación.

- **three-spritetext** (dentro de util.ts)  
  Texto flotante en 3D sobre los nodos.

- **lodash-es / kapsule / accessor-fn / data-joint** (dentro de util.ts)  
  Utilidades generales del grafo.

- **three.webgpu.js** (dentro de util.ts)  
  Versión WebGPU de Three.js.

- **DragControls** (dentro de util.ts)  
  Permite arrastrar objetos 3D.

---

### 🟡 REVISAR CON CUIDADO — Lógica central del plugin

Código propio que interactúa directamente con Obsidian y con las librerías 3D. Cambios posibles pero requieren pruebas.

#### `TagRoutesView` — Clase principal (líneas ~66,522 – 68,852)

| Método | Qué hace | Riesgo |
|---|---|---|
| `buildGdata()` | Lee vault, extrae enlaces y tags, construye nodos/conexiones | Medio — lógica compleja |
| `createGraph(container)` | Inicializa Three.js + física + eventos de mouse | Alto — toca muchas librerías |
| `getNodeColorByType(node)` | Color según tipo de nodo | Bajo |
| `animate()` | Añade nodos progresivamente (time-lapse) | Medio |
| `captureAndSaveScreenshot()` | Captura canvas WebGL → PNG | Bajo |
| `handleNodeClick(node)` | Click en nodo → abre archivo | Bajo |
| `handleTagClick(node)` | Click en tag → genera reporte | Bajo |
| `switchTheme(visual)` | Cambia dark/light, reconstruye efectos | Medio |
| `onSettingsSave()` | Aplica cambios de configuración en vivo | Medio |
| `focusGraphNodeById()` | Mueve cámara suavemente a un nodo | Bajo |
| `applyThemeColor()` | Lee colores CSS de Obsidian y los aplica | Bajo |

#### `darkStyle` / `lightStyle`
Aplican el tema al grafo y activan `UnrealBloomPass`. Modificables con cuidado.

---

### 🟢 MODIFICAR LIBREMENTE — Código seguro

Código propio sin dependencias críticas. Se puede editar, extraer y reorganizar.

#### `util.ts` — Funciones propias (líneas ~24,148 – 24,447 aprox.)
```
DebugMsg(level, ...args)       → logging con niveles (ERROR/WARN/INFO/DEBUG)
setViewType()                  → cambia modo de vista Obsidian
createFolderIfNotExists()      → crea carpetas en el vault
getTags(cache)                 → extrae tags del metadata cache
getFileType(filePath)          → detecta tipo de archivo
shouldRemove(path, filterList) → aplica filtros de rutas
showFile(filePath)             → abre archivo en Obsidian
getLineTime(line)              → extrae timestamp de línea de texto
PathFilter (clase)             → maneja filtros glob (base64, validación)
namedColor (mapa)              → nombres CSS → hex
```

#### `settings.ts` (líneas ~65,878 – 66,521)
Clase `settingGroup` — construye dinámicamente sliders, botones, dropdowns, toggles.  
Patrón builder encadenado. **Completamente extraíble.**

#### `CodeBlockProcessor.ts` (líneas ~68,853 – 69,203)
```
tagProcessor(query)             → busca tags en contenido de archivos
frontmatterTagProcessor(query)  → busca tags en frontmatter YAML
codeBlockProcessor()            → registrador principal para bloques ```tagsroutes```
performanceCount                → mide duración de operaciones
```
**Completamente extraíble.**

#### `main.ts` — Punto de entrada (líneas ~69,204 – 69,820)
```
globalProgramControl            → flags de debugging global
currentSaveSpecVer: 10203       → versión del formato data.json
defaultColorMapDark/Light       → paletas de color por defecto
TagsRoutes3 (clase Plugin)      → onload, initializePlugin, loadSettings, saveSettings, mergeDeep
colorPickerGroup                → widget color picker (texto + selector)
TagsroutesSettingsTab           → página de configuración global del plugin
```
**Completamente extraíble y reorganizable.**

---

## Plan de modularización propuesto

### Paso 1 — Separar librerías (sin tocar nada)
Identificar exactamente los rangos de líneas de cada librería y documentarlos.  
**Objetivo:** saber qué NO mover.

### Paso 2 — Extraer `CodeBlockProcessor.ts`
Es el módulo más pequeño (~350 líneas) y sin dependencias hacia los otros módulos propios.  
Ideal para empezar y probar el flujo de trabajo.

### Paso 3 — Extraer `settings.ts`
~644 líneas, clase autocontenida. Solo depende de la API de Obsidian.

### Paso 4 — Extraer funciones de `util.ts`
Las funciones propias (ver lista 🟢 arriba) separadas de las librerías bundleadas.

### Paso 5 — Limpiar `main.ts`
Dejar solo el punto de entrada mínimo: `onload()` y registro de componentes.

### Paso 6 — Revisar `TagRoutesView`
Última fase. Separar `buildGdata()` de `createGraph()` si es posible.

---

## Notas importantes

- El `main.js` fue generado por **esbuild** desde TypeScript. El código fuente original (`src/`) es mucho más limpio y corto.
- Si tienes acceso al repo fuente (`src/`), es preferible trabajar desde ahí y recompilar, en lugar de editar `main.js` directamente.
- Cualquier cambio en `main.js` se **sobreescribirá** si el plugin se actualiza. Considerar hacer un fork del repositorio.
- Repositorio original: https://github.com/kctekn/obsidian-TagsRoutes

---

## Próximos pasos acordados

- [x] Revisar si existe la carpeta `src/` en el directorio del plugin — **existe pero estaba vacía**
- [x] Decidir: ¿editar `main.js` directamente o trabajar desde el código fuente TypeScript? — **se trabaja sobre `main.js` directamente**
- [x] Comenzar con extracción de `CodeBlockProcessor` (Paso 2) — **completado**
- [ ] Probar el plugin después de cada cambio antes de continuar

---

## Cambios realizados

### Sesión 2 — Separación de vendors (2026-05-14)

**Objetivo:** Extraer todas las librerías externas a un archivo separado para que `main.js` sea editable y legible.

**Archivos generados:**

| Archivo | Ruta | Líneas | Tamaño |
|---|---|---|---|
| `vendors.js` | `src/vendors.js` | 66,553 | 2.4 MB |
| `main.js` (nuevo) | `main.js` | 3,368 | 133 KB |

**Qué se hizo:**
- Se identificaron con precisión los rangos de líneas de cada librería usando los comentarios de sección de esbuild (`// node_modules/...`)
- Se extrajo todo el bloque de librerías (líneas 1–66,521 del original) a `src/vendors.js`
- Al final de `vendors.js` se añadió un bloque `module.exports` con las variables que el código propio necesita:
  - Three.js: `AdditiveBlending`, `BoxGeometry`, `Camera`, `Color`, `DirectionalLight`, `EdgesGeometry`, `Group`, `LineBasicMaterial`, `LineSegments`, `Mesh`, `MeshBasicMaterial`, `MeshLambertMaterial`, `MeshStandardMaterial`, `SphereGeometry`, `Vector3`
  - Postprocesado: `UnrealBloomPass`
  - Grafo 3D: `_3dForceGraph`
  - D3 Force: `link_default`
  - Spritetext: `_default14`
- El nuevo `main.js` arranca con el boilerplate de esbuild (líneas 1–36) + un `require('./src/vendors.js')` con destructuring de todas las vars, seguido del código propio (líneas 66,522–69,820 del original)

**Backup existente:** `main.js.1.2.3.bak` en la raíz del plugin (creado automáticamente por Obsidian).

**Pendiente de verificación:**
- [ ] Recargar Obsidian y confirmar que el plugin funciona correctamente con la nueva estructura
- [ ] Si falla: restaurar `main.js.1.2.3.bak` → `main.js` y revisar los exports de `vendors.js`

### Sesión 3 — Extracción de CodeBlockProcessor (2026-05-14)

**Objetivo:** Separar el procesador de bloques ` ```tagsroutes``` ` a su propio archivo.

**Archivos generados:**

| Archivo | Ruta | Líneas | Tamaño |
|---|---|---|---|
| `CodeBlockProcessor.js` | `src/CodeBlockProcessor.js` | 370 | 16 KB |
| `main.js` (v2) | `main.js` | 3,024 | 120 KB |

**Qué se hizo:**
- Se extrajo el bloque `// src/util/CodeBlockProcessor.ts` (líneas 2401–2751 del main anterior) a `src/CodeBlockProcessor.js`
- El archivo exporta: `module.exports = { codeBlockProcessor }`
- En `main.js` el bloque fue reemplazado por: `const { codeBlockProcessor } = require('./src/CodeBlockProcessor.js')`
- `main.js` pasó de 3,368 → 3,024 líneas

**Dependencias del módulo** (aún resueltas desde el scope global de `main.js`):
- `DebugMsg` — viene de `util.ts` (pendiente extracción en Paso 4)
- `getLineTime` — viene de `util.ts` (pendiente extracción en Paso 4)
- `globalProgramControl` — viene de `src/main.ts` (al final del mismo `main.js`)

**Pendiente de verificación:**
- [ ] Colocar `CodeBlockProcessor.js` en `src/` y `main_v2.js` como `main.js`
- [ ] Recargar Obsidian y probar que los bloques ` ```tagsroutes``` ` siguen funcionando
- [ ] Si falla: revisar que `globalProgramControl` esté definido ANTES del `require` en `main.js`

---

*Última actualización: sesión 3 — CodeBlockProcessor extraído, pendiente instalación y prueba.*
