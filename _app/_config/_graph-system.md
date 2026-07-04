---
title: "Sistema Graph — Herramientas de visualización por código"
galaxy_body: beacon
scope: vault
audience: [usuario, claude]
related_notes:
  - "[[_galaxy-system]]"
  - "[[_note-system]]"
  - "[[_mindmap-system]]"
  - "[[_ToDo-system]]"
tags: [beacon, graph, desmos, tikzjax, neutrino, infraestructura]
date_created: 2026-05-30
date_updated: 2026-07-03
status: activo
---

# Sistema Graph — Herramientas de visualización por código

> Sistema Galaxy: [[_galaxy-system]]
> Convención de notas: [[_note-system]]
> Sistema Mindmap (Excalidraw): [[_mindmap-system]]
> Pendientes: [[_ToDo-system]]
> Guía Desmos: [[guides/MAT101/MAT101_desmos]]
> Guía TikZJax: [[guides/MAT101/MAT101_TikzJax]]

---

## Idea central

Este vault usa herramientas que generan imágenes desde código. Son fundamentalmente distintas a una imagen estática (.png, .jpg) y a un dibujo en Excalidraw. El código **es** el artefacto — la imagen es solo su output visible.

En el Sistema Galaxy estas herramientas se tipifican como `neutrino` ⚛️ — no existen como notas separadas sino como bloques embebidos dentro de un `planet` o `comet`.

---

## Las tres formas de visual en el vault

| Tipo | `galaxy_body` | Símbolo | Qué es | Ejemplos |
|------|--------------|---------|--------|---------|
| Imagen estática | `photon` | 💡 | Archivo visual puro — sin lógica ni código | .png arrastrado, recorte PDF++ |
| Código generador | `neutrino` | ⚛️ | Bloque de código que produce una imagen al renderizar | Desmos, TikZJax |
| Dibujo vectorial | `observatory` | 🔭 | Lienzo libre en Excalidraw | Diagramas técnicos, esquemas |

> Para mapas mentales estructurados → `constellation`. Ver [[_mindmap-system]].

---

## Herramientas `neutrino` disponibles

### Comparación rápida

| Característica | Desmos | TikZJax |
|----------------|--------|---------|
| Bloque de código | ` ```desmos-graph ` | ` ```tikz ` |
| Lenguaje | Sintaxis propia de Desmos | LaTeX / TikZ |
| Para qué | Gráficas matemáticas 2D interactivas | Diagramas de precisión: circuitos, geometría, plots 3D |
| Caché | `.cache/desmos/` — SVGs en disco, accesibles | IndexedDB de Electron — interno, no accesible como archivo |
| Versionado Git | El código sí ✅ / El caché no ❌ | El código sí ✅ / No hay caché en disco |
| Claude puede generarlo | ✅ | ✅ |
| Requiere internet | No (funciona offline) | No (WebAssembly local) |
| Nota separada | Casi nunca | Casi nunca |

### Cuándo usar cada una

**Usar Desmos cuando:**
- La visualización es una función matemática, curva, región sombreada o gráfica 2D
- Se necesita interactividad o exploración rápida
- El contexto es cálculo, probabilidad, álgebra, análisis

**Usar TikZJax cuando:**
- El diagrama requiere precisión técnica: circuitos electrónicos, diagramas de bloques, geometría exacta
- Se usan paquetes LaTeX especializados: `circuitikz`, `pgfplots`, `tikz-cd`
- El resultado debe verse como una figura de publicación académica

**Usar Excalidraw (observatory) cuando:**
- El dibujo es libre, conceptual o esquemático — no requiere precisión matemática
- Se necesita anotar sobre una imagen existente
- El diagrama tiene una narrativa visual que se construye a mano

---

## Desmos — referencia rápida

Plugin: `obsidian-desmos` — renderiza gráficas de [desmos.com](https://www.desmos.com/calculator) directamente en notas.

**Caché:** `.cache/desmos/` dentro del vault — SVGs generados automáticamente por el plugin. Carpeta configurada manualmente. No es contenido académico.

**Bloque básico:**
`````
```desmos-graph
left=-5; right=5; bottom=-3; top=3;
width=500; height=400;
---
y=x^2|BLUE
```
`````

**Regla crítica:** el separador `---` es **siempre obligatorio**, incluso sin configuración.

> Documentación completa: [[MAT101_desmos]]

---

## TikZJax — referencia rápida

Plugin: `obsidian-tikzjax` — renderiza LaTeX/TikZ como SVG dentro de las notas usando WebAssembly.

**Paquetes disponibles:** `circuitikz` · `pgfplots` · `tikz-cd` · `chemfig` · `amsmath` · `amssymb` · `tikz-3dplot`

**Caché:** IndexedDB de Electron — interno al proceso de Obsidian, no existe como archivo en el vault. Si se limpia el caché (Settings del plugin) o se cambia de PC, TikZJax re-renderiza desde el código fuente en la nota. El código es siempre la fuente de verdad.

**Estructura obligatoria:**
`````
```tikz
\usepackage{paquete}      ← cargar paquetes necesarios
\begin{document}
  \begin{tikzpicture}
    ...
  \end{tikzpicture}
\end{document}
```
`````

> No incluir `\documentclass{standalone}` — el plugin lo usa automáticamente.

**Nota sobre renders:** circuitikz puede no cargar al primer render. Si el diagrama no aparece, cerrar y reabrir Obsidian lo resuelve.

> Documentación completa: [[tikzjax_guide-legacy]]

---

## El `neutrino` en el Sistema Galaxy

### Reglas

1. **No es nota separada.** Un `neutrino` vive dentro de un `planet` o `comet` — es un bloque de código en el cuerpo de la nota, no un archivo `.md` propio.
2. **No tiene YAML propio ni bloque `%%`.** La nota host lleva el YAML y los wikilinks.
3. **El código es la fuente de verdad.** Nunca guardar solo el output visual — el bloque de código debe estar siempre en la nota.
4. **Una imagen por concepto.** No acumular múltiples bloques en una sola nota si cada uno ilustra algo distinto — en ese caso separar en notas planet/comet distintas.

### Cuándo sí justifica una nota `neutrino` separada

Casi nunca. Los únicos casos válidos:
- El mismo diagrama se reutiliza en múltiples notas y necesita un punto único de mantenimiento
- El diagrama es tan complejo que domina la nota host y oscurece el contenido académico

En esos casos crear una nota con `galaxy_body: neutrino` y embeber desde la nota host con `![[nombre]]`.

### YAML para neutrino independiente (caso excepcional)

```yaml
---
title: "Circuito equivalente Thevenin — ETN806"
galaxy_body: neutrino
neutrino_type: tikz
attached_to: "[[ETN806-T03-thevenin-theorem]]"
subject: ETN806
semester: 8
partial: 2
topic: 3
tags: [ETN806, galaxy-neutrino, P2, T03]
date_created: YYYY-MM-DD
---
```

```markdown
%%
galaxy-links
[[ETN806-T03-thevenin-theorem]]
%%
```

---

## Exportar un neutrino como archivo estático

Si necesitas el output visual como archivo (para incluir en un PDF, compartir, etc.):

**Desde Desmos:** clic derecho sobre el gráfico renderizado → "Save image" → guardar en `_assets/` con el mismo nombre que la nota host.

**Desde TikZJax:** no hay exportación directa desde el plugin. Opciones:
- Captura de pantalla de la región del diagrama → guardar en `_assets/`
- Abrir el código en Overleaf o un compilador LaTeX online → exportar como SVG/PDF

El archivo exportado pasa a ser un `photon` (imagen estática) adjunto a la misma nota.

---

## Registro de decisiones de diseño

| Decisión | Razón |
|----------|-------|
| `neutrino` como tipo galaxy separado de `photon` | Código que genera imagen y archivo de imagen estática son conceptualmente distintos. Uno tiene lógica, el otro no. Mezclarlos era un error de diseño. |
| `neutrino` embebido en la nota host | Casi nunca justifica nota separada — su contexto es inseparable de la teoría o el ejercicio que ilustra. |
| El código es la fuente de verdad | El output visual puede regenerarse siempre desde el código. El código no puede recuperarse desde el output. |
| Desmos para matemáticas, TikZJax para técnico | Cada herramienta tiene su dominio natural. Desmos es más rápido para funciones 2D. TikZJax es más preciso para diagramas técnicos con paquetes LaTeX especializados. |
| Caché Desmos en `.cache/desmos/` | Separado de `_assets/` para distinguir archivos generados automáticamente de exports manuales. No es contenido académico. |
| Caché TikZJax en IndexedDB | No es configurable — es interno al plugin. El código en la nota es suficiente para reconstruir el output en cualquier PC con el plugin instalado. |
| `_graph-system.md` como beacon unificador | Sin este archivo cada guía individual documenta su herramienta pero nadie documenta cuándo usar cuál ni cómo conviven. Este beacon resuelve esa capa de decisión. |

%%
galaxy-links
[[_galaxy-system]]
[[_note-system]]
[[_mindmap-system]]
[[MAT101_desmos]]
[[guides/MAT101/MAT101_TikzJax]]
[[_ToDo-system]]
%%
