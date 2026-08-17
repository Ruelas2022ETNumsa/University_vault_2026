---
galaxy_body: dropship
carrier: "[[_hangar/pdfpp_embed_nblm/pdfpp_embed_nblm.md]]"
scope: prueba
status: activo
date: 2026-08-16
---

## Proposito

Archivo de prompts de prueba para el carrier `pdfpp_embed_nblm`. Contiene los prompts usados en NotebookLM para probar si puede entregar el formato de embed de PDF++ (`![[libro.pdf#page=N]]`) de forma separada al flujo de transcripción principal.

---

## Contenido

%%
Convención de secciones:
### v[N] — descripción breve
**Objetivo:** qué se quiere probar con este prompt
**Prompt:**
```
[texto del prompt]
```
**Resultado:** completar tras la prueba — ver también chronicle.md
%%

### v1 — prompt base separado (sin modificar v3)

**Objetivo:** probar si NotebookLM puede generar el embed `![[libro.pdf#page=N]]` cuando se le da un subtítulo específico de la transcripción, en un notebook duplicado con un prompt simple dedicado a esta tarea.

**Consideraciones:**
- NotebookLM entrega el número de página impreso en el libro, no el número del visor PDF — el embed puede tener desfase según el PDF.
- El formato objetivo es: `![[nombre_archivo.pdf#page=N]]`
- No usar el prompt v3 — este prompt va en el notebook duplicado, separado.

**Prompt:**
```
[pendiente — diseñar en sesión de trabajo]
```

**Resultado:** pendiente
