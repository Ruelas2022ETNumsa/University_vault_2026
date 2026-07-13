## 4. Cornell Marginalia — Notas al margen en el editor

**Plugin:** [latazadehomero/cornell-marginalia](https://github.com/latazadehomero/cornell-marginalia) — v4.9.0 (Community Plugins)

**Propósito:** Agrega notas al margen (marginalia) directamente en el editor, fuera del área de texto principal. Complementa a Cornell Notes: mientras Cornell Notes maneja el layout de dos columnas, Marginalia permite anotar al margen sin interrumpir el flujo del texto.

> Ver sintaxis completa y uso por tipo de nota en [[cornell_guide]].

### Coexistencia con Cornell Notes — parche aplicado

Ambos plugins registraban el mismo bloque ` ```cornell `, lo que impedía activarlos simultáneamente (Obsidian desactivaba uno automáticamente al activar el otro).

**Parche aplicado** en `.obsidian/plugins/cornell-marginalia/main.js`, línea 14017:

```
// Antes:
this.registerMarkdownCodeBlockProcessor("cornell", ...)

// Después:
this.registerMarkdownCodeBlockProcessor("marginalia", ...)
```

Cambio de una sola línea: el bloque de Marginalia pasó de `cornell` a `marginalia`. Cornell Notes sigue usando `````cornell` (5 backticks) sin modificación. Los dos plugins ahora coexisten sin conflicto.

> **Nota de mantenimiento:** si Cornell Marginalia se actualiza vía BRAT, el `main.js` se sobreescribe y el parche se pierde. Volver a aplicar el cambio en la línea `registerMarkdownCodeBlockProcessor` después de cada actualización.

### Sintaxis

**Modo inline** (funciona en cualquier parte del documento):

```
%%> Nota al margen izquierda %%
%%< Nota al margen derecha %%
```

**Modo bloque dentro de cornell** (obligatorio anidar para que renderice):

``````markdown
`````cornell
::cue
````marginalia
%%> %%
Contenido claves...
````
::note
````marginalia
%%< %%
Contenido desarrollo...
````
``````

> El script `notebooklm_fix` inserta los bloques `marginalia` automáticamente. Ver sección 8.

### Ejemplo de uso

En una nota planet o comet, dentro o fuera de un bloque Cornell Notes:

```
La transformada de Laplace se define como:

$\mathcal{L}\{f(t)\} = \int_0^\infty e^{-st} f(t)\, dt$

%%> Ver demostración en ETN806-T03. %%

La condición de convergencia requiere que $\text{Re}(s) > \sigma_0$.
```

La nota `%%> Ver demostración... %%` aparece al margen derecho sin ocupar espacio en el flujo del texto.

### Notas de configuración

- La posición del margen (izquierda/derecha por defecto) se configura en **Settings → Cornell Marginalia → Alignment**.
- El ancho del margen y el estilo visual son ajustables desde el mismo panel.
- Las marginalia son visibles en **Live Preview** y en **Reading View** — no en Source Mode.

---

