---
galaxy_body: carrier
project: "TABnote"
date: 2026-08-03
status: delayed
fleet: sistema-movil
blocked_by: prueba real en clase — ajustes post-prueba antes de cerrar
---

> [!info] alx_gml — 2026-08-05
> Template v1 especificado en detalle y documentado en borrador. Catálogo de símbolos tablet cerrado. Borrador en `_TABnote-template-draft.md` en raíz del vault. Pendiente: prueba real en clase → ajustes → `_TABnote-ref.md`.

## Handoff

**Última sesión:** 2026-08-05 → cierre
**Completado esta sesión:** Resolución de 4 preguntas abiertas, convenciones de identificador de página, running header, marginalia en tablet, notas adhesivas, herramientas descartadas, diseño completo del template en Excalidraw (cuadrícula 44×56 de 4mm, Cornell, áurea, subdivisiones internas, cruces segmentadas), exportado a Samsung Notes en 3 variantes, catálogo de símbolos tablet cerrado, borrador de especificaciones completo creado
**Próximo paso:** Prueba del template en clase real → si hay problemas se retoma describiendo el problema puntual → documentar `_TABnote-ref.md`

---

## Resumen y objetivo

Diseñar una plantilla estándar para tomar apuntes en Samsung Notes (tablet S6 Lite, S Pen) que permita a NotebookLM extraer y transcribir el contenido sin fricción, enriquecido con fuentes. La plantilla debe ser adoptable en clase sin interrumpir el ritmo de escritura.

---

## Decisiones

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
| 2026-08-03 | Un solo color para apuntes: #005F73 | Consistencia y legibilidad OCR |
| 2026-08-03 | Título centrado con resaltado simétrico a ambos lados | Así ya lo usa el usuario — confirmado con PDF real |
| 2026-08-03 | Subtítulo: texto + resaltado mismo color hasta borde derecho | Señal visual clara para NLM independiente del color usado |
| 2026-08-03 | Callout = caja cerrada 4 lados, no ancho completo | NLM reconoce por `> Título` como primera línea dentro de la caja |
| 2026-08-03 | Imagen = subtítulo en gris + área vacía | Señal para NLM de omitir; screenshot va directo al vault |
| 2026-08-03 | Numeración de subtítulos (1. 2. 3.) | Ancla de orden para NLM |
| 2026-08-03 | Renglón en blanco entre subtítulos | NLM corta bloques sin mezclar temas |
| 2026-08-04 | Unidades en corchetes: `470[Ω]`, `2[A]` | NLM identifica valor+unidad como unidad semántica |
| 2026-08-04 | Síntesis con `∴` | Cierre de desarrollos y fórmulas; NLM lo transcribe como símbolo |
| 2026-08-04 | Referencia cruzada `→ ver T02` | Registrada, implementación gradual; no va al prompt NLM aún |
| 2026-08-04 | Identificador página 1: `MAT101 — T01 — DD/MM/YYYY` | Running header esquina superior derecha, a mano sobre el margen |
| 2026-08-04 | Identificador páginas siguientes: `MAT101 — subtítulo activo` | Misma posición; indica continuación sin romper contexto |
| 2026-08-04 | Separador: `—` (guion largo) con `/` para fecha | Robusto a mano; si NLM da problemas se corrige |
| 2026-08-04 | Numeración de páginas: esquina superior derecha en recuadro sobre el margen | Orientación en PDF; no usada por NLM pero útil para revisar |
| 2026-08-04 | Notas adhesivas (Sticky Memo): uso interno, no llegan al PDF | Recordatorios, fechas de examen, cosas que no deben ir a NLM |
| 2026-08-04 | Herramienta "Cinta" (Tape): descartada | Causa problemas de sincronización tablet → PC |
| 2026-08-04 | Marginalia en tablet: línea de resaltador desde elemento al margen | Conector visual; NLM ignora la línea, lee solo el texto marginal |
| 2026-08-04 | Notación marginalia: `[!, nota]` `[?, nota]` etc. | Prefijo dentro de corchete; NLM reconoce y transcribe; se convierte en marginalia Obsidian al transcribir |
| 2026-08-04 | Flecha de ubicación en marginalia | Flecha + subrayado indica el elemento exacto al que pertenece la nota marginal |
| 2026-08-04 | Template TABnote v1 diseñado en Excalidraw | Página A4, cuadrícula 44×56 recuadros de 4mm, márgenes 15mm externos + 2mm internos (1mm inferior), divisiones Cornell y áureas segmentadas, recuadros de running header (88×9mm) y nº de página (7×7mm) |
| 2026-08-05 | Catálogo de símbolos tablet cerrado | 9 símbolos de 1 carácter, cualquier color, sin guiones: `!` `?` `X` `V` `C` `F` `R` `T` `*` |
| 2026-08-05 | Símbolos al margen: resaltador que sobrepasa el borde | Línea de resaltador desde el contenido hasta fuera del margen; símbolo escrito en el margen externo; ambos lados válidos |
| 2026-08-05 | Borrador de especificaciones del template creado | `_TABnote-template-draft.md` en raíz del vault — detalla todas las medidas, divisiones internas y sistema de símbolos |
| 2026-08-04 | 3 variantes del template cargadas en Samsung Notes | White theme (modo claro) · Dark theme (modo oscuro, sin fondo para aprovechar el modo de Notes) · Sin cuadrícula (para imprimir en tareas) |
| 2026-08-04 | Grosor S Pen con nueva cuadrícula (18 cuad. ancho) | Texto: 5 · Subtítulos: 8 · Títulos/énfasis: 12 (punto de partida, ajustar en clase) |
| 2026-08-04 | Template listo pero editable | Si algo no funciona en clase se edita en Excalidraw explicando el problema puntual; no se rediseña desde cero |
| 2026-08-08 | Prompts ETN607 son la base del sistema TABnote en producción | `ETN607-transcription.md` y `ETN607-transcription-divisions.md` son la primera instancia completa del sistema TABnote con NLM — el prototipo genérico `tpl_prompt_transcription.md` se deriva de ellos |

> [!note]- Descartadas
> Cornell de 2 columnas — el usuario casi nunca la usa, se descartó como plantilla base. El resaltado horizontal es suficiente separador visual sin columnas.

---

## Convenciones del sistema

### Jerarquía visual

| Elemento | Convención visual | Señal para NLM |
| -------- | ----------------- | -------------- |
| Título | Centrado + resaltado simétrico ambos lados | Posición centrada + resaltado |
| Subtítulo | Texto + resaltado hasta borde derecho, numerado `1.` | Número + resaltado |
| Apunte | Texto libre color #005F73 | Flujo principal |
| Énfasis | Subrayado o negrita puntual | Inline |
| Callout | Caja cerrada 4 lados, no ancho completo | `> Título` como primera línea |
| Imagen | Subtítulo en gris + área vacía | Señal de omisión para NLM |
| Fórmula | A mano; unidades en `[unidad]` | NLM extrae bien manuscrito + corchetes |

### Callouts

Estructura interna:
```
> Título
desarrollo dentro de la caja...
```

Catálogo de títulos (parcial, en construcción):
- `> Tarea`
- más títulos a definir según uso en clase

El título es fijo del catálogo o libre según el momento — ambos válidos.

### Identificador de página

- **Página 1 del tema:** `MAT101 — T01 — DD/MM/YYYY` — esquina superior derecha, sobre el margen, a mano
- **Páginas siguientes:** `MAT101 — subtítulo activo` — misma posición
- **Número de página:** recuadro en esquina superior derecha sobre el margen

Flujo de exportación: una nota continua por capítulo. Se reexporta como `MAT101_T01.pdf` reemplazando la fuente en NLM cada vez que se agregan subtítulos.

### Sugerencias de escritura adoptadas

| Convención | Uso |
| ---------- | --- |
| `[unidad]` | Siempre junto al valor: `940[V]`, `470[Ω]` |
| `∴` | Síntesis al cerrar un desarrollo o fórmula |
| `→ ver T02` | Referencia cruzada al margen o al final del bloque (implementación gradual) |

### Marginalia en tablet

Sistema de notas al margen integrado al flujo S Pen:

**Señal visual:**
- Línea de resaltador (cualquier color) desde el elemento origen (título, apunte, fórmula, imagen) hasta el margen
- En el extremo del margen: la nota escrita con prefijo de categoría

**Notación:**
```
[!, nota]    → importante / examen
[?, nota]    → duda / pregunta a aclarar
[F-, nota]   → fórmula clave
[X-, nota]   → error / corrección
[∴, nota]    → síntesis marginal
```

**Flecha de ubicación:** flecha + subrayado sobre el elemento exacto al que pertenece la nota, para que al transcribir quede claro dónde insertarla en Obsidian.

**Flujo de transcripción:**
1. NLM transcribe la marginalia tal cual, con su prefijo
2. Al crear la supernova en Obsidian, se convierte en marginalia Marginalia plugin con el mismo prefijo semántico
3. La flecha indica la línea exacta donde va la `%%> [!...] %%`

**Si la nota marginal necesita más desarrollo:** callout debajo en el área principal, mismo color de referencia que la línea.

### Notas adhesivas (Sticky Memo)

- Uso: contenido que **no debe llegar a NLM** — recordatorios, fechas de examen, preguntas pendientes, estado del capítulo
- Comportamiento: no se exportan al PDF aunque estén abiertas
- No tienen rol fijo en el sistema — uso libre según necesidad del momento

### Herramientas descartadas

| Herramienta | Motivo |
| ----------- | ------ |
| Cinta (Tape) | Causa pérdida de sincronización tablet → PC |
| Cornell de 2 columnas | No adoptada por el usuario |

---

## Planificación

Flujo final del sistema:
1. Apuntes en Samsung Notes (S Pen, plantilla TABnote)
2. Export a PDF vía Samsung Account sync → Samsung Notes PC
3. PDF sube a NotebookLM como fuente (`MAT101_T01.pdf`)
4. Prompt de transcripción solicita subtítulo específico → NLM entrega supernova enriquecida con fuentes

Restricciones:
- Debe funcionar en clase sin interrumpir escritura
- Fórmulas siempre a mano (ya probado que NLM las extrae bien)
- Imágenes se omiten en transcripción — screenshot va al vault manualmente
- Sin Cornell: plantilla lineal simple con jerarquía por color + resaltado

---

## Flujo de pasos

1. [x] Relevar sistema actual del usuario (colores, export, flujo NLM)
2. [x] Definir jerarquía visual: título / subtítulo / apunte / énfasis
3. [x] Definir convención de callouts (caja + > título)
4. [x] Definir convención de imágenes (subtítulo gris + área vacía)
5. [x] Crear catálogo de tipos de callout para ingeniería electrónica
6. [x] Diseñar plantilla visual v4 con todas las convenciones
7. [x] Responder preguntas abiertas
8. [x] Diseñar sistema de marginalia para tablet
9. [x] Diseñar cuadrícula del template (18×26 cuadrados de 5mm, A4, márgenes, Cornell + áurea)
10. [ ] El usuario prueba la plantilla en clase real
11. [ ] Ajustes post-prueba (si los hay — retomar explicando el problema)
12. [x] Documentar plantilla final como archivo de referencia `_TABnote-ref.md`
13. [x] Separar prompt NLM a tsk independiente → `tsk_tabnote-prompt-nlm.md`

---

## Tareas

- [x] Leer archivos de configuración del sistema
- [x] Diseño plantilla v1, v2, v3, v4
- [x] Catálogo de callouts universitarios — ingeniería electrónica
- [x] Sugerencias de mejora de apuntes
- [x] Resolver preguntas abiertas de diseño
- [x] Sistema de marginalia tablet (notación + flujo transcripción)
- [x] Diseño de cuadrícula del template (Excalidraw → PNG → Samsung Notes)
- [x] Catálogo de símbolos tablet (9 símbolos, 1 carácter, cualquier color)
- [x] Borrador de especificaciones completo (`_TABnote-template-draft.md`)
- [ ] Prueba real en clase
- [ ] Ajustes post-prueba si los hay
- [x] Archivo de referencia final `_TABnote-ref.md` en vault
- [x] Prompt NLM separado a tsk independiente → `tsk_tabnote-prompt-nlm.md`

---

## Archivos del carrier

| Archivo | Tipo | Estado | Descripción |
| ------- | ---- | ------ | ----------- |
| `tsk_tabnote.md` | carrier | delayed | Este archivo — plantilla TABnote y sistema de apuntes |
| `logbook.md` | logbook | — | README histórico del proyecto |
| `chronicle.md` | chronicle | — | Registro cronológico de pruebas |
| `tsk_tabnote-prompt-nlm.md` | dropship | docked | Prompt de transcripción NLM para tablet |
| `tpl_prompt_transcription.md` | dropship | activo | Prototipo genérico de prompt TABnote para cualquier materia — base: ETN607-transcription.md / ETN607-transcription-divisions.md |
| `_TABnote-ref.md` | ref | — | Referencia definitiva del sistema TABnote v1 |

---

## Recursos

- `E:\University_vault_2026\_app\_config\_notebooklm-system.md`
- `E:\University_vault_2026\_app\_config\_TAB_note-system.md`
- `E:\University_vault_2026\_app\_config\_note-system.md`
- `E:\University_vault_2026\_app\_appnotes\cornell_guide.md`
- `E:\University_vault_2026\_app\_appnotes\Marginalia_guide.md`
- `E:\University_vault_2026\_app\notebooklm\prompts\ETN607\ETN607-transcription.md` ← instancia completa del sistema TABnote simple en producción
- `E:\University_vault_2026\_app\notebooklm\prompts\ETN607\ETN607-transcription-divisions.md` ← instancia completa del sistema TABnote con divisiones en producción
