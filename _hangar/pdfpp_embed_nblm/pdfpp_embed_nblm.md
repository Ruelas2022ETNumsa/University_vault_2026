---
galaxy_body: carrier
project: "PDF++ embed desde IMA-SRC de NotebookLM"
date: 2026-08-16
status: docking
fleet: ETN607
blocked_by:
---

## Handoff

**Última sesión:** 2026-08-16
**Retomar desde:** `ocrmypdf-install.md` — instalar pngquant y probar --optimize 2
**Completado esta sesión:** carrier creado, prompts v1 y v2 diseñados, OCRmyPDF instalado y probado (pruebas 1-3 con Alonso & Finn), flujo de búsqueda por etiqueta definido y documentado
**Próximo paso:** instalar pngquant — `winget install -e --id ImageOptim.pngquant` — luego probar --optimize 2, luego probar prompts v1/v2 en NotebookLM
**Preguntas de cierre:** —

---

## Tareas

- [ ] Verificar nombres de PDFs de libros ETN607 en vault vs nombres reportados por IMA-SRC
- [ ] Probar embed básico `![[libro.pdf#page=N]]` manualmente en una nota de Obsidian
- [ ] Probar si NotebookLM entrega el embed de forma separada (notebook duplicado, prompt simple)
- [ ] Evaluar el problema de numeración: página impresa vs página del visor PDF
- [ ] Documentar resultado de cada prueba en `chronicle.md`
- [ ] Decidir si el embed convive con IMA-SRC o lo reemplaza
- [ ] Script delta: descartado — reemplazado por flujo de búsqueda por etiqueta
- [ ] Script búsqueda por etiqueta: diseñar e implementar — lista todas las coincidencias, usuario elige — fase pruebas CLI antes de integrar a Obsidian
- [x] OCRmyPDF: instalado y probado (pruebas 1-3) — optimize 1 sin ahorro — pendiente optimize 2 con pngquant

---

## Archivos del carrier

| Archivo | Tipo | Estado | Descripción |
| ------- | :--: | :----: | ----------- |
| `pdfpp_embed_nblm.md` | tsk | — | este archivo — trabajo activo del carrier |
| `logbook.md` | logbook | — | README histórico del proyecto |
| `chronicle.md` | chronicle | — | registro cronológico de pruebas |
| `ocrmypdf-install.md` | dropship | activo | instalación y config de OCRmyPDF — fase pruebas CLI |
| `prompts.md` | dropship | activo | prompts de prueba para NotebookLM |
