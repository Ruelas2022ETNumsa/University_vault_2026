---
galaxy_body: chronicle
scope: pdfpp_embed_nblm
date_updated: 2026-08-16
---

%%
Registro cronológico de pruebas. Cada entrada corresponde a una prueba o experimento.
Formato por entrada:

### YYYY-MM-DD — descripción breve
**Objetivo:** qué se quería probar
**Resultado:** qué pasó
**Veredicto:** ok | falla | parcial | pendiente
**Notas:** observaciones relevantes
%%

## Pruebas

### 2026-08-16 — sesión inicial
**Objetivo:** definir el flujo y analizar viabilidad del embed desde NotebookLM
**Resultado:** flujo definido, análisis de PDF++ completado, restricción de numeración identificada
**Veredicto:** pendiente — sin pruebas reales realizadas aún
**Notas:** Ver `logbook.md` para decisiones y riesgos.

### 2026-08-16 — pngquant instalado, prueba optimize 2
**Objetivo:** probar si --optimize 2 con pngquant reduce el tamaño del PDF con OCR
**Resultado:** 41.087 KB — idéntico a prueba 3 con --optimize 1
**Veredicto:** sin ahorro — optimize 2 no tiene efecto en este PDF
**Notas:** El PDF de Alonso & Finn es un escaneado en escala de grises. pngquant trabaja cuantizando paletas de color — en grises no hay paleta que reducir, por lo que no tiene efecto. Ninguna de las tres optimizaciones (sin flag, opt1, opt2) produjo reducción. Para este PDF el resultado final es el OCR base (prueba 2, 41.087 KB) sin ninguna optimización adicional.

### 2026-08-17 — Ctrl+F en Obsidian con PDF con OCR
**Objetivo:** verificar que la búsqueda funciona en Obsidian con el archivo procesado por OCRmyPDF
**Resultado:** ✅ Ctrl+F encuentra texto correctamente
**Veredicto:** ok
**Notas:** flujo OCR confirmado para PDFs escaneados en escala de grises. La capa de texto es funcional para búsqueda en Obsidian.

### 2026-08-17 — creacion del script 
**Objetivo:**  la creacion del script (E:\University_vault_2026\_app\shellcommands\shellcmd_pdf_figure_search.md) simplifica la busqueda de la imagen
**Resultado:** muy bueno
**Veredicto:** ok
**Notas:** se esta revisando la posibilidad de mejorar el script a una version 2 (la version 1 es bueno paro los datos ingresados pueden ser mejoradas)
