---
title: "NotebookLM — Errores conocidos y observaciones"
galaxy_body: beacon
scope: vault
audience: [claude, usuario]
related_notes:
  - "[[]]"
tags: [beacon, solve]
date_created: 2026-08-29
status: activo
---

## Botón de copiar stripea notación `[N]`

**Observación:** El botón de copiar de NotebookLM elimina todo contenido con formato `[N]` (corchetes con número) del texto copiado.

**Causa:** NotebookLM usa `[1]`, `[2]`, `[3]`... como marcadores de cita a fuentes. Esos marcadores son elementos de interfaz — no forman parte del texto subyacente. El botón de copiar descarta todos los elementos de interfaz al exportar el texto plano, lo que incluye cualquier fragmento que comparta ese formato.

**Impacto en AHPL:** Los tamaños de registros usan la misma notación — `DR[18]`, `AC[8]`, `DBUS[6]`. Cuando el modelo coloca un tamaño en la columna Tamaño de la tabla de declaraciones, ese valor queda como elemento de cita y el botón lo borra. La celda aparece vacía al pegar.

**Workaround confirmado:** Seleccionar el texto manualmente con el cursor y copiar. El texto copiado así sí incluye los `[N]` visibles en pantalla.

**Fecha de confirmación:** 2026-08-29

---

## Tamaños incorrectos en tabla de declaraciones (problema abierto)

**Observación:** El modelo infiere tamaños incorrectos para los registros en la tabla de declaraciones — por ejemplo `[6]` o `[7]` en lugar de `[8]`. En el bloque de código el tamaño puede diferir al de la tabla (inconsistencia interna).

**Causa probable:** El modelo no tiene ejemplos concretos de cómo se ve una declaración correcta en contexto. Sin referencia explícita, infiere el tamaño desde el enunciado o lo alucina.

**Estado:** pendiente de resolución. Líneas de ataque en curso:
- [x] Tabla de notación de registros agregada al prompt
- [x] Tabla de tamaños estándar del SIC agregada al prompt
- [x] OCR aplicado a PDFs de Hill & Peterson y recargados como fuentes
- [ ] Guía de ejemplos separada con pares pregunta→respuesta y tamaños explícitos

**Archivo relacionado:** `E:\University_vault_2026\_hangar\dock\ship_ETN825_AHPL_N16.md`

**Fecha de apertura:** 2026-08-29

---

%%
# galaxy-links

%%