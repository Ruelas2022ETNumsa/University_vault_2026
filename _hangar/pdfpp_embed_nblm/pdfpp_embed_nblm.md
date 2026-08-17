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
**Retomar desde:** pruebas de PDF++ y flujo de embed desde NotebookLM — leer Tareas
**Completado esta sesión:** definición del flujo, análisis de PDF++ y su feature de rectangular selection embed. Convertido de ship a carrier.
**Próximo paso:** probar embed básico `![[libro.pdf#page=N]]` en Obsidian y probar si NotebookLM entrega el formato de embed de forma separada (sin modificar el prompt v3)
**Preguntas de cierre:** ver ## Tareas — pendientes de prueba

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
- [ ] OCRmyPDF: instalar y probar en PDF escaneado (ej: Alonso & Finn) — fase pruebas CLI antes de integrar a Obsidian

---

## Archivos del carrier

| Archivo | Tipo | Estado | Descripción |
| ------- | :--: | :----: | ----------- |
| `pdfpp_embed_nblm.md` | tsk | — | este archivo — trabajo activo del carrier |
| `logbook.md` | logbook | — | README histórico del proyecto |
| `chronicle.md` | chronicle | — | registro cronológico de pruebas |
| `ocrmypdf-install.md` | dropship | activo | instalación y config de OCRmyPDF — fase pruebas CLI |
| `prompts.md` | dropship | activo | prompts de prueba para NotebookLM |
