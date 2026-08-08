---
galaxy_body: dropship
carrier: "[[_hangar/TPL_TAB/tsk_tabnote.md]]"
scope: prueba
status: docked
date: 2026-08-05
blocked_by: prueba real en clase — necesario saber cómo responde NLM al PDF de Samsung Notes antes de escribir el prompt
---

## Objetivo

Crear el prompt de transcripción para NotebookLM adaptado al flujo de apuntes en tablet (TABnote). Se basa en el prompt existente `MAT101-transcription.md` y se adapta a las convenciones del sistema TABnote.

---

## Contexto necesario para esta sesión

Leer antes de arrancar:

- `E:\University_vault_2026\_TABnote-ref.md` — sistema TABnote completo (jerarquía visual, convenciones, marginalia, flujo NLM)
- `E:\University_vault_2026\_app\notebooklm\prompts\MAT101\MAT101-transcription.md` — prompt base a adaptar
- `E:\University_vault_2026\_app\_appnotes\Marginalia_guide.md` — sistema de marginalia Obsidian (para el flujo de conversión)

---

## Lo que debe cubrir el prompt

1. **Jerarquía visual → estructura Obsidian**
   - Título centrado + resaltado → `# Título`
   - Subtítulo numerado + resaltado hasta margen → `## 1. Subtítulo`
   - Apunte normal → texto plano
   - Callout `> Título` → callout Obsidian correspondiente

2. **Imágenes (IMA)**
   - Bloque delimitado por 2 líneas grises con subtítulo IMA → omitir transcripción
   - Opcional: incluir breve descripción como pie si el espacio del prompt lo permite

3. **Marginalia**
   - Símbolo al margen + texto → transcribir tal cual como pie o nota inline
   - Formato sugerido: `[símbolo: texto]` al final del bloque al que pertenece
   - Solo si no ocupa demasiado espacio en el prompt — si no, transcripción simple como pie de página

4. **Unidades y símbolos**
   - `valor[unidad]` → respetar el corchete
   - `∴` → respetar el símbolo
   - `→ ver T02` → respetar como referencia cruzada

5. **Lo que NLM debe ignorar**
   - Running header (MAT101 — T01 — ...)
   - Número de página
   - Líneas de cuadrícula y divisiones segmentadas

---

## Prerequisito

Realizar al menos una prueba real en clase con el template TABnote y exportar el PDF a NLM antes de escribir el prompt. Observar qué transcribe bien y qué no para ajustar las instrucciones.

---

## Flujo de pasos

1. [ ] Prueba real en clase — exportar PDF a NLM
2. [ ] Relevar qué transcribe NLM bien y qué no del PDF de Samsung Notes
3. [ ] Leer archivos de contexto listados arriba
4. [ ] Adaptar MAT101-transcription.md al flujo TABnote
5. [ ] Probar el prompt con un subtítulo real
6. [ ] Ajustes si los hay
7. [ ] Guardar prompt final en `E:\University_vault_2026\_app\notebooklm\prompts\TABnote\TABnote-transcription.md`

---

## Tareas

- [ ] Prueba real en clase
- [ ] Relevamiento de comportamiento NLM con PDF tablet
- [ ] Redacción del prompt
- [ ] Prueba del prompt
- [ ] Ajustes finales
- [ ] Guardar prompt final en vault
