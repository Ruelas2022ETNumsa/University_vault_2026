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
- Bloques `desmos-graph` → quedan como bloque de código plano en el PDF. NotebookLM los lee como texto LaTeX, lo cual es suficiente.
- Bloques `%%...%%` (galaxy-links) → invisibles en el PDF, igual que en modo lectura. ✅

---

## CSS snippet de print (pendiente de crear)

Para personalizar el PDF sin afectar la apariencia en pantalla, crear el archivo `.obsidian/snippets/print.css` con:

```css
@media print {
  body {
    --font-text-size: 16px !important;
  }
}
```

Con **Enable select CSS snippets** activado, aparece un dropdown en el modal de exportación donde se puede elegir `print.css` por exportación sin aplicarlo globalmente.

> ⚠️ Este snippet aún no existe en el vault. Crear cuando se necesite ajustar tipografía del PDF.

---

## Limitaciones conocidas

- No hay integración directa con NotebookLM — el flujo siempre es Obsidian → PDF → subir manualmente.
- No existe API pública de NotebookLM que un plugin de Obsidian pueda usar.
- Los bloques Desmos no se renderizan como gráficas en el PDF — quedan como código.

%%
galaxy-links
[[_galaxy-system]]
[[desmos_guide]]
%%
