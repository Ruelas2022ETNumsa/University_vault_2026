---
galaxy_body: logbook
scope: pdfpp_embed_nblm
status: on-track
date_updated: 2026-08-17
---

## Visión general

Explorar si NotebookLM puede generar automáticamente un link embed de PDF++ que apunte a la página exacta donde se encuentra una figura, en lugar de solo entregar los metadatos de IMA-SRC para localización manual. El carrier es grande porque involucra pruebas en NotebookLM, configuración de PDF++, y una restricción no resuelta de numeración de páginas. El criterio de éxito es lograr que el usuario pegue el embed en una nota `.md` y PDF++ renderice la página del libro inline sin intervención adicional.

---

## Estado actual

**Salud:** on-track
**Resumen:** Script `pdf_figure_search` v1 creado, probado e integrado en Shell Commands. Problema de numeración de páginas resuelto via ranking por error mínimo. OCRmyPDF integrado como fallback automático en el script. Pendiente: pruebas de prompts v4 y BCv4 en NotebookLM.
**Último avance:** Script v1 funcional — búsqueda por etiqueta con 6 variantes, ranking top 3 por proximidad al hint de NLM, comando OCR automático para PDFs sin texto.
**Próximo hito:** Probar `ETN607-transcription_Av4` en notebook de transcripción (detección de figuras del apunte) y `BCv4` con Mensaje 2 (concepto individual).

---

## Archivos del carrier

| Archivo | Tipo | Estado | Descripción |
| ------- | :--: | :----: | ----------- |
| `pdfpp_embed_nblm.md` | tsk | — | archivo de trabajo activo |
| `logbook.md` | logbook | — | este archivo — README histórico del proyecto |
| `chronicle.md` | chronicle | — | registro cronológico de pruebas |
| `ocrmypdf-install.md` | dropship | activo | instalación y config de OCRmyPDF |
| `prompts.md` | dropship | activo | prompts de prueba para NotebookLM |
| `[[shellcmd_pdf_figure_search]]` | doc | activo | script v1 — búsqueda por etiqueta con ranking por error mínimo |

---

## Hitos

- 2026-08-16 — definición del flujo completo y análisis de PDF++ features. Carrier creado.
- 2026-08-17 — OCRmyPDF instalado y probado (5 pruebas). Ctrl+F confirmado en Obsidian.
- 2026-08-17 — prompts BCv4 y Av4 creados. BCv4 probado y comprobado.
- 2026-08-17 — script `pdf_figure_search` v1 creado, probado e integrado en Shell Commands. Problema de numeración resuelto.

---

## Riesgos y dependencias

- **Numeración de páginas:** ~~Sin resolver~~ **Resuelto** — el script calcula `error = |página_visor - hint_page|` y devuelve los 3 candidatos con menor error. El de error 0 es coincidencia exacta; los siguientes cubren desfase por portada/índice.
- **[[]] vs ![[]]:** confirmado — usar `[[]]` sin `!` en los prompts. Más liviano, abre en otra ventana.

## Pendientes futuros

- **Script v2 — campo NLM obligatorio:** el campo `etiqueta` desaparece como campo separado. El bloque completo de NLM (link markdown + etiqueta en línea siguiente) será el único input. La etiqueta se extrae siempre del bloque.
- **Script búsqueda por etiqueta — múltiples coincidencias:** resuelto por ranking de error mínimo — cerrado.
- **Script búsqueda por etiqueta — integración Obsidian:** completado en v1 via Shell Commands.
- **OCRmyPDF — integración Obsidian:** integrado como fallback automático en el script — entrega el comando listo en el portapapeles cuando no encuentra texto.

## Herramientas disponibles

### OCRmyPDF
Herramienta de línea de comandos para agregar capa de texto a PDFs escaneados. El PDF resultante es visualmente idéntico al original pero con texto seleccionable y buscable.
- **Uso básico:** `ocrmypdf input.pdf output.pdf`
- **Motor OCR:** Tesseract (soporta español, inglés, otros)
- **Ventaja:** local, sin límites de tamaño ni páginas, gratuito, open source
- **Instalación:** OCRmyPDF + Tesseract — ambos instalados en Windows via pip/instalador
- **Estado:** fase de pruebas por línea de comandos — no integrado a Obsidian aún
- **Caso de uso ETN-607:** PDFs escaneados como Alonso & Finn 1970. La mayoría de los libros de ETN-607 son PDFs digitales y no lo necesitan.

## Flujo resuelto — búsqueda por etiqueta

Para PDFs con texto seleccionable en Obsidian, el flujo óptimo es:

1. Copiar etiqueta entregada por NotebookLM (ej: `Figure 4.3`)
2. Abrir el enlace `[[libro.pdf#page=N]]` en Obsidian
3. `Ctrl+F` en el visor PDF
4. Pegar la etiqueta — PDF++ navega directo a la figura
5. Seleccionar el área con PDF++ (rectangular selection → genera `&rect=`)
6. Pegar en la nota reemplazando el link y la etiqueta

Resultado final en la nota: `![[libro.pdf#page=N&rect=x1,y1,x2,y2]]`
Ventaja: el número de página del visor se resuelve solo — PDF++ lo genera al hacer la selección.
- **PDFs en vault:** Los libros de ETN607 deben estar en `_PDF\ETN-607\` con nombres consistentes con lo que IMA-SRC reporta como `fuente`. Por el momento la carpeta está vacía.
- **Límite del prompt v3:** 9985/10000 chars — sin margen para agregar instrucciones al prompt existente. Decisión tomada: no se modifica el prompt v3, se prueba de forma separada.

---

## Decisiones clave

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
| 2026-08-16 | No modificar el prompt v3 — probar el embed de forma separada con notebook duplicado | El prompt ya estaba al límite de caracteres |
| 2026-08-16 | IMA-SRC sigue siendo el flujo principal — este carrier es una mejora opcional | Si el embed no funciona bien, IMA-SRC no se toca |
| 2026-08-16 | Pendiente a futuro: duplicar el notebook — uno para transcripción, otro para el embed y complementos | Buena idea registrada, no es prioridad actual |
| 2026-08-17 | Script delta de numeración descartado — reemplazado por ranking de error mínimo en el script | Más simple y efectivo |
| 2026-08-17 | OCRmyPDF integrado como fallback automático en el script — no como paso manual separado | Reduce fricción: el comando aparece directamente en el portapapeles |

> [!note]- Descartadas
> - Redibujo automático con Gemini — descartado por complejidad; pruebas en `_hangar/IMA_NBLM/`
