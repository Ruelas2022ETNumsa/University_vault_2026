---
title: "Side-Notes — Integración Galaxy"
galaxy_body: beacon
scope: vault
audience: [usuario, claude]
related_notes:
  - "[[_galaxy-system]]"
  - "[[_marginalia_system]]"
  - "[[_comments-system]]"
tags: [beacon, obsidian, plugins, infraestructura, sidenotes, galaxy]
date_created: 2026-08-24
date_updated: 2026-08-24
status: activo
plugin_version: "0.5.1"
---

# Side-Notes — Integración Galaxy

> Plugin: **Side-Notes** by cparsell — [GitHub](https://github.com/cparsell/sidenotes)
> Versión estable en uso: `0.5.1` (Latest — 2026-08-23)
> Referencia de Marginalia: [[_marginalia_system]]
> Referencia de Document Comments: [[_comments-system]]

Side-Notes agrega notas narrativas al margen de las notas, estilo Tufte. El contenido de la sidenote **forma parte de la nota** — no es metadata de revisión ni aprendizaje activo, sino contenido que complementa el cuerpo sin interrumpir su flujo.

**Las tres capas del margen en Galaxy:**

| Capa | Plugin | Qué hace |
|---|---|---|
| Contenido al margen | **Side-Notes** | Fórmulas, imágenes, links, referencias ancladas al texto |
| Aprendizaje activo | **Cornell Marginalia** | Semantic highlighting, active recall, flashcards, threads |
| Gestión / revisión | **Document Comments** | Estados open/resolved, canal asíncrono con Claude |

Cada capa hace una cosa distinta. No se reemplazan.

---

## Formato oficial: HTML

El plugin soporta dos formatos: **HTML** y **footnotes Markdown**. El formato oficial de Galaxy es **HTML**.

```
<span class="sidenote">contenido de la nota</span>
```

Los footnotes (`[^1]`) tienen comportamiento inconsistente en Live Preview, especialmente dentro de callouts, y están pendientes de evaluación futura. Ver [Footnotes — estado y pendiente](#footnotes--estado-y-pendiente).

**Inserción:** `Ctrl+P` → `Side-Notes: Insert Sidenote` — inserta el `<span>` con el cursor dentro. No escribir el HTML a mano.

---

## Sintaxis HTML

### Sidenote numerada (tipo principal)

```html
texto del cuerpo<span class="sidenote">contenido al margen</span>, continuación del cuerpo.
```

El número se gestiona automáticamente por el plugin según configuración. En Galaxy: números desactivados (`showSidenoteNumbers: false`).

### Margin note (sin número)

```html
texto del cuerpo<span class="sidenote margin-note">nota sin número</span>, continuación.
```

Se muestra como popup al hacer hover sobre el ícono `ⓘ` en el texto. No ocupa espacio fijo en el margen.

### Sidenote en margen opuesto

```html
<span class="sidenote right">va al margen derecho</span>
<span class="sidenote left">va al margen izquierdo (explícito)</span>
```

> ⚠️ **Margen derecho reservado para Document Comments en Galaxy.** Las sidenotes van siempre al margen izquierdo (default). `right` queda disponible técnicamente pero no se usa en notas de contenido — evita conflicto visual con las tarjetas de Document Comments.

---

## Contenido soportado — probado en v0.5.1

Todos los siguientes tipos de contenido funcionan dentro de `<span class="sidenote">`:

| Tipo | Sintaxis dentro del span | Estado |
|---|---|---|
| Texto plano | `texto normal` | ✅ |
| **Bold** / *italic* / `code` | `**bold** *italic* \`code\`` | ✅ |
| Fórmula LaTeX inline | `$f(x) = x^2$` | ✅ |
| Fórmula LaTeX bloque | `$$\int f\,dx$$` | ✅ |
| Imagen del vault | `![[_assets/nombre.png\|220]]` | ✅ |
| Imagen + caption | `![[img.png\|200]] Texto de caption` | ✅ |
| Wikilink interno | `[[ruta/nota.md\|alias]]` | ✅ |
| Link a PDF del vault | `[[_PDF/archivo.pdf\|alias]]` | ✅ |
| Combinado imagen + link | `![[img.png\|180]] — [[pdf.pdf\|alias]]` | ✅ |
| Combinado bold + code + link | `**IR** \`REG_IR\` — [[pdf.pdf\|§3.2]]` | ✅ |
| Dentro de callout | cualquier contenido | ✅ (fixeado en v0.5.0) |

> La combinación imagen + LaTeX + wikilinks en una sola sidenote permite construir una **referencia académica completa al margen** — fórmula, diagrama y fuente juntos, sin tocar el cuerpo.

---

## Uso por galaxy_body

### `planet` — complemento de teoría

El cuerpo muestra el concepto limpio. La sidenote lleva la demostración parcial, la fuente del teorema, o la imagen del diagrama que lo ilustra.

```
Ejemplo:
→ Cuerpo: "La transformada de Fourier de la autocorrelación es la densidad espectral de potencia."
→ Sidenote: $$S_{XX}(f) = \int_{-\infty}^{\infty} R_{XX}(\tau)\,e^{-j2\pi f\tau}\,d\tau$$
```

| Qué va en sidenote | Qué NO va en sidenote |
|---|---|
| Fórmula extendida del concepto | Desarrollo paso a paso (va en `moon`) |
| Imagen del diagrama asociado | Ejercicio resuelto (va en `comet`) |
| Link al asteroid de fuente | Aclaración larga que rompe el flujo |

---

### `moon` — fórmula clave con contexto visual

La moon es la fórmula. La sidenote puede llevar la imagen del caso geométrico, el link al libro fuente, o una nota de restricción de validez.

```
Ejemplo:
→ Cuerpo: densidad marginal — fórmula de integración
→ Sidenote: ![[_assets/region-soporte.png|200]] — región válida de integración
```

---

### `comet` — referencia cruzada durante resolución

En un ejercicio resuelto, la sidenote ancla el paso a la teoría que lo justifica, sin interrumpir la cadena de desarrollo.

```
Ejemplo:
→ Cuerpo: "Por independencia estadística, f(x,y) = f_X(x)·f_Y(y)"
→ Sidenote: Ver [[ETN806-T01-independencia-estadistica|Independencia — definición]]
```

> Diferencia con Marginalia `R-`: la sidenote es contenido permanente de la nota. La marginalia `R-` es una anotación personal de revisión.

---

### `asteroid` — extracto con fuente al margen

El cuerpo transcribe el extracto. La sidenote lleva la referencia exacta (autor, capítulo, página) o una imagen del diagrama del libro.

```
Ejemplo:
→ Cuerpo: desarrollo del teorema de Papoulis
→ Sidenote: ![[_assets/papoulis-fig6-2.png|180]] Papoulis, Cap. 6, p. 142
```

---

### `dwarf` — referencia rápida en resumen

El cuerpo condensa el tema. La sidenote puede llevar la fórmula completa mientras el cuerpo solo muestra el resultado o el enunciado.

```
Ejemplo:
→ Cuerpo: "Varianza de suma de independientes = suma de varianzas."
→ Sidenote: $$\text{Var}\!\left(\sum X_i\right) = \sum \sigma_i^2$$
```

---

## Configuración activa (data.json)

Valores en uso — no modificar manualmente sin respaldo:

| Campo | Valor | Efecto |
|---|---|---|
| `sidenoteFormat` | `html` | Formato oficial |
| `sidenotePosition` | `left` | Margen izquierdo por defecto |
| `showSidenoteNumbers` | `false` | Sin numeración visible |
| `pageOffsetFactor` | `0.6` | El cuerpo se desplaza poco para dar lugar al margen |
| `minSidenoteWidth` | `4` (rem) | Ancho mínimo de la columna de sidenotes |
| `maxSidenoteWidth` | `8` (rem) | Ancho máximo |
| `fontSize` | `75` (%) | Tamaño de fuente relativo al texto principal |
| `fontSizeCompact` | `65` (%) | Fuente en modo compacto (pane estrecho) |
| `compactBelow` | `1100` (px) | Activa modo compacto bajo este ancho de pane |
| `fullAbove` | `1600` (px) | Modo full solo en pantallas anchas |
| `marginNoteDisplay` | `popup` | Margin notes como popup al hover, no en margen fijo |
| `popupIcon` | `ⓘ` | Ícono de margin note en el texto |

Respaldo del estado original: `data.json.bk` en la carpeta del plugin.

---

## CSS snippet — ocultar en Reading Mode

Archivo: `.obsidian/snippets/sidenotes-hide-reading.css`

Activa/desactiva desde **Settings → Appearance → CSS Snippets**.

- **ON** → sidenotes ocultos en Reading Mode (vista limpia del cuerpo)
- **OFF** → sidenotes visibles en ambos modos

> La clase DOM real es `.sidenote-margin`, no `.sidenote`. El `<span class="sidenote">` del Markdown es transformado por el plugin al renderizar — el span original queda colapsado a `width: 0` y el contenido se mueve a `.sidenote-margin`.

---

## Limitaciones conocidas (v0.5.1)

| Limitación | Detalle |
|---|---|
| Bullet lists en PDF | Al exportar PDF con sidenotes, las listas con bullet no indentan correctamente y las sidenotes se salen del margen. Issue conocido del autor. |
| Margen derecho reduce cuerpo | Usar `right` hace que el texto principal se adelgace para dar lugar. En Galaxy el margen derecho no se usa por esta razón y por reserva para Document Comments. |
| Editing de sidenotes en Reading Mode | Desactivado desde v0.4.8 — solo editable en Live Preview (click en el margen para abrir el editor inline). |
| Mobile | El plugin funciona en móvil en modo lectura, pero la edición inline del margen no está optimizada para touch. |

---

## Footnotes — estado y pendiente

Los footnotes Markdown (`[^1]`) son el formato alternativo del plugin. **No son el formato oficial de Galaxy** por las siguientes razones verificadas:

- En Live Preview, las sidenotes de footnotes dentro de callouts no renderizan (limitación de cómo Obsidian expone los footnotes en ese contexto — funciona en Reading Mode)
- El cursor tarda más en moverse alrededor de los números de referencia (mejorado en v0.5.1 pero no resuelto del todo)

**Cuándo podría tener sentido en Galaxy (pendiente futuro):** notas tipo `asteroid` con texto narrativo largo sin callouts, donde el estilo de cita académica con número al pie es natural y el cuerpo nunca entra en callouts. Evaluar cuando el plugin estabilice el comportamiento en Live Preview.

> Registrar avances en una nueva sesión de `plan` si se decide revisar.

---

%%
# galaxy-links
[[_app/_config/_galaxy-system.md]]
[[_app/_config/_marginalia_system.md]]
[[_app/_config/_comments-system.md]]
%%
