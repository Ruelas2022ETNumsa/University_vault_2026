---
galaxy_body: carrier
project: "PDF++ embed desde IMA-SRC de NotebookLM"
date: 2026-08-16
status: docking
fleet: ETN607
blocked_by:
---

## Handoff

**Última sesión:** 2026-08-17
**Retomar desde:** probar ETN607-transcription-v4 en NotebookLM (detección de figuras del apunte) y probar prompt v3 de complemento
**Completado esta sesión:** pngquant instalado, optimize 1 y 2 sin efecto (PDF en escala de grises), Ctrl+F confirmado, ETN607-transcription-v4.md creado (solo transcripción, sin complemento), prompts.md v3 creado y refinado (complemento B/C + embed PDF++ + admonition ad-note + TikZJax fallback + IMA-SRC en %% %%)
**Próximo paso:** 1) probar v4 en notebook de transcripción — foco en detección de figuras del apunte y bloque IMA · 2) probar prompts.md v3 en notebook de complemento con un concepto individual (Mensaje 2)
**Preguntas de cierre:** —

---

## Tareas

- [x] Verificar nombres de PDFs de libros ETN607 en vault vs nombres reportados por IMA-SRC — confirmados en prompts.md
- [x] Probar embed básico `[[libro.pdf#page=N]]` manualmente — confirmado, usar `[[]]` sin `!`
- [x] Probar si NotebookLM entrega el embed — sí, formato v3 funciona (prueba coordenadas generalizadas)
- [x] Evaluar problema de numeración: página impresa vs visor — riesgo conocido, IMA-SRC queda como respaldo en `%% %%`
- [ ] Documentar resultados de pruebas v4 y v3 en `chronicle.md` — pendiente tras pruebas
- [x] Decidir si embed convive con IMA-SRC — conviven: embed visible, IMA-SRC oculto en `%% %%`
- [x] Script delta: descartado — reemplazado por flujo de búsqueda por etiqueta
- [ ] Script búsqueda por etiqueta: pendiente — fase pruebas CLI antes de integrar a Obsidian
- [x] OCRmyPDF: instalado y probado (pruebas 1-5) — optimize 1 y 2 sin efecto en grises — Ctrl+F confirmado
- [ ] Probar ETN607-transcription-v4 en notebook de transcripción — foco en detección de figuras del apunte
- [ ] Probar prompts.md v3 en notebook de complemento — Mensaje 2 con concepto individual

---

## Archivos del carrier

| Archivo | Tipo | Estado | Descripción |
| ------- | :--: | :----: | ----------- |
| `pdfpp_embed_nblm.md` | tsk | — | este archivo — trabajo activo del carrier |
| `logbook.md` | logbook | — | README histórico del proyecto |
| `chronicle.md` | chronicle | — | registro cronológico de pruebas |
| `ocrmypdf-install.md` | dropship | activo | instalación y config de OCRmyPDF — fase pruebas CLI |
| `prompts.md` | dropship | activo | prompts de prueba para NotebookLM |
