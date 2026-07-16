---
title: "Better Export PDF — Guía de flujo de trabajo"
galaxy_body: beacon
scope: vault
tool: better-export-pdf
audience: [usuario, claude]
tags: [beacon, better-export-pdf, notebooklm, infraestructura]
date_created: 2026-05-27
status: activo
---

# 📄 BETTER EXPORT PDF — FLUJO DE TRABAJO

> Plugin: `better-export-pdf` — exporta notas `.md` a PDF con soporte de LaTeX, índice de marcadores, headers/footers y exportación de carpetas completas.
> Caso de uso principal en este vault: exportar temas de ETN806 como PDF para subir a NotebookLM.

---

## Configuración global — Settings > Better Export PDF

Valores configurados una sola vez. Se aplican como defaults a todas las exportaciones.

| Setting | Valor | Razón |
|---|---|---|
| **Show title** | ON | Usa el campo `title:` del YAML frontmatter como título del PDF |
| **Add timestamp** | OFF | No necesario — genera nombres de archivo confusos para NotebookLM |
| **Enable select CSS snippets** | ON | Habilita aplicar CSS de print sin afectar la apariencia en pantalla |
| **Limit concurrency** | 5 (default) | Archivos renderizados en paralelo al exportar carpetas. Bajar a 2–3 si Obsidian se congela con carpetas grandes |
| **Debug mode** | OFF | Solo activar si un PDF sale mal y hay que diagnosticar en la consola (`Ctrl+Shift+I`) |
| **Header template** | vacío | No necesario para NotebookLM |
| **Footer template** | vacío | No necesario para NotebookLM |
| **Open after export** | a gusto | ON para verificar antes de subir, OFF para exportación rápida en batch |

---

## Configuración del modal de exportación

Aparece cada vez que se exporta. El plugin recuerda la última configuración usada automáticamente.

| Opción | Valor recomendado |
|---|---|
| **Page size** | A4 |
| **Orientation** | Portrait |
| **Margin** | Small |
| **Scale** | 100 |
| **Show title** | ON |

---

## Flujo — exportar nota individual

1. Abrir la nota en Obsidian.
2. Clic en los tres puntos `···` (esquina superior derecha) → **Better Export PDF**.
   - Alternativa: `Ctrl+P` → buscar `Better Export PDF: Export Current File to PDF`.
3. Verificar configuración en el modal → **Export**.
4. Seleccionar carpeta de destino → Enter.

---

## Flujo — exportar carpeta completa (para NotebookLM)

Produce un único PDF con todas las notas de la carpeta en orden. Ideal para mandar un tema completo.

1. En el explorador de archivos de Obsidian, clic derecho sobre la carpeta deseada.
   - Ejemplo: `Partial_2/Topic_01_joint-pdf/`
2. Seleccionar **Export folder to PDF**.
3. Verificar configuración → **Export**.
4. Subir el PDF resultante a NotebookLM como nueva fuente.

---

## Comportamiento con el vault

**Lo que sí renderiza correctamente:**
- Fórmulas LaTeX inline (`$...$`) y display (`$$...$$`) fuera de tablas → salen como imágenes matemáticas tipografiadas.
- Headings, listas, tablas de texto, bloques de código.
- El campo `title:` del YAML aparece como título del PDF (con Show title ON).

**Lo que NO renderiza o tiene limitaciones:**
- Fórmulas LaTeX dentro de celdas de tabla → comportamiento inconsistente, verificar caso a caso.
- Bloques `desmos-graph` → **se renderizan correctamente si la nota está abierta** en el editor al momento de exportar. Better Export PDF captura lo que Obsidian ya tiene renderizado en pantalla — no renderiza por su cuenta. Si la gráfica es visible antes de exportar, aparece en el PDF como imagen. Posible excepción: exportación en batch de carpeta completa, donde las notas no se abren visualmente y Desmos puede no tener tiempo de ejecutar.
- Bloques `%%...%%` (galaxy-links) → invisibles en el PDF, igual que en modo lectura. ✅

---

## CSS snippet — `.obsidian/snippets/print.css`

### Cómo lo detecta el plugin

El plugin no busca el archivo por nombre. Al exportar, su función `getAllStyles()` recorre todos los `<style>` que Obsidian tiene cargados en el DOM en ese momento — tema, snippets habilitados, todo. Lo que encuentre dentro de `@media print {}` lo extrae con `getPrintStyle()` y lo inyecta directamente en el webview antes de llamar a `printToPDF()`.

Conclusión práctica: si `print.css` está habilitado en Apariencia → CSS Snippets (o seleccionado en el dropdown del modal de exportación), el plugin lo recoge automáticamente. No hay que hacer nada más.

### Cómo activarlo sin que afecte la vista normal

Con **Enable select CSS snippets** ON, en el modal de exportación aparece un dropdown donde se puede elegir `print.css` aunque no esté habilitado globalmente. Así el snippet solo aplica al PDF.

Si todas las reglas van dentro de `@media print {}`, también se puede habilitar globalmente sin problema — esas reglas no se activan en pantalla, solo al exportar.

### Orden de precedencia dentro del plugin

El plugin apila los estilos en este orden (cada capa sobreescribe a la anterior):

1. Estilos core de Obsidian
2. Tema activo
3. Snippets habilitados globalmente ← `print.css` entra aquí si está ON
4. Snippets seleccionados en el modal de exportación ← `print.css` entra aquí si está OFF global
5. `CSS_PATCH` interno del plugin (parches propios)
6. Reglas `@media print` desenvueltas — se aplican al final, máxima prioridad

---

## Reglas del snippet `print.css` — qué hace cada bloque

### Fórmulas display

```css
.math-block,
.katex-display,
mjx-container[display="true"],
.MathJax_Display {
  break-inside: avoid;
  page-break-inside: avoid;
}
```

Con esto: una fórmula display (`$$...$$`) no queda partida entre dos páginas. Sin esto: el contenedor de la fórmula podía cortarse a mitad, dejando la parte superior en una página y el resto en la siguiente.

---

### Tablas

```css
table {
  break-inside: avoid;
  page-break-inside: avoid;
}

thead {
  display: table-header-group;
}

tr {
  break-inside: avoid;
  page-break-inside: avoid;
}
```

Con `table {...}`: la tabla entera intenta mantenerse en una sola página. Si la tabla es más alta que la página, el navegador la cortará igual — en ese caso se puede quitar esta regla y dejar solo `tr`.

Con `thead {...}`: si la tabla sí se parte porque es muy larga, la fila de encabezados se repite al inicio de cada página nueva.

Con `tr {...}`: cada fila individual no se corta a mitad — si no cabe completa al final de una página, se mueve a la siguiente.

Nota: el plugin ya incluye internamente `table { break-inside: auto }` y `tr { break-inside: avoid }`. Las reglas del snippet sobreescriben ese parche porque se aplican después.

---

### Bloques de código

```css
pre,
pre code {
  break-inside: avoid;
  page-break-inside: avoid;
}
```

Con esto: un bloque de código no queda partido a mitad. Sin esto: el texto monoespaciado con indentación pierde contexto visual si se corta entre páginas.

---

### Headings — evitar huérfanos

```css
h1, h2, h3, h4 {
  break-after: avoid;
  page-break-after: avoid;
  break-inside: avoid;
  page-break-inside: avoid;
}
```

Con `break-after: avoid`: el heading no queda solo al pie de la página con el contenido en la siguiente. Sin esto: es común ver un `## Sección` al final de una página y su primer párrafo al inicio de la siguiente.

---

### Callouts

```css
.callout {
  break-inside: avoid;
  page-break-inside: avoid;
}
```

Con esto: un callout (bloque con borde izquierdo y fondo) no se parte a mitad. Sin esto: el borde y el fondo se cortan, el resultado es visualmente roto.

---

### Salto de página manual

```css
.break-page {
  break-before: page;
  page-break-before: always;
}
```

Uso en el markdown: insertar `<div class="break-page"></div>` donde se quiera forzar un salto de página. El div es invisible en pantalla y en el PDF solo produce el salto.

---

## Limitaciones conocidas

- No hay integración directa con NotebookLM — el flujo siempre es Obsidian → PDF → subir manualmente.
- No existe API pública de NotebookLM que un plugin de Obsidian pueda usar.
- Los bloques Desmos no se renderizan como gráficas en el PDF — quedan como código.
- `break-inside: avoid` es una sugerencia para el navegador, no una orden. Si un elemento es más alto que la página completa, se cortará igual.

---

%%
# galaxy-links
[[_app/_config/_galaxy-system.md]]
[[_app/_appnotes/desmos_guide.md]]
%%
