---
galaxy_body: dropship
carrier: "[[_hangar/pdfpp_embed_nblm/pdfpp_embed_nblm.md]]"
scope: prueba
status: activo
date: 2026-08-16
---

## Proposito

Prompts de prueba para el carrier `pdfpp_embed_nblm`. El objetivo es probar si NotebookLM puede, dado un subtítulo de ETN607, entregar un complemento nivel B simple con referencias a figuras de los libros fuente en formato embed de PDF++ (`![[archivo.pdf#page=N]]`), listo para pegar en Obsidian.

Estas pruebas son independientes del notebook de transcripción — van en un notebook duplicado o separado con las fuentes ya cargadas.

**Fuentes en el vault** (`E:\University_vault_2026\_PDF\ETN-607`):
- `Alonso & Finn-Mecánica_Vol 1-1970-.pdf`
- `Dare A. Wells-SCHAUM'S Lagrangian Dynamics-McGraw-Hill.pdf`
- `Goldstein & Poole & Safko-Classical Mechanics-3th ed-Pearson.pdf`
- `H. Goldstein-Mecánica clásica-1994-ED REVERTE.pdf`
- `John R. Taylor-Classical mechanics-eng.pdf`
- `John R. Taylor-Instructor's Manual to accompany Classical Mechanics-2005.pdf`
- `John R. Taylor-Mecánica clásica-2005-ED REVERTÉ-esp.pdf`
- `LimYung-kuo-Problems and Solutions on Mechanics-1994.pdf`
- `Nelson & Best & McLean-schaums Statics and dynamics.pdf`

> ⚠️ **Restricción conocida:** NotebookLM entrega el número de página impreso en el libro, no el número que el visor PDF cuenta. El embed puede tener desfase según el PDF (portada, índice, etc.). Registrar en `chronicle.md` si el desfase es consistente o variable.

---

## Prompts

%%
Convención:
### v[N] — descripción breve
**Objetivo:** qué se quiere probar
**Uso:** cómo se usa en NotebookLM
**Resultado:** completar tras la prueba
**Notas:** observaciones
[bloque de código con el prompt]
%%

---

### v1 — complemento B con embed PDF++

**Objetivo:** probar si NotebookLM puede entregar un complemento nivel B de un subtítulo dado directamente en el chat, con referencias a figuras de los libros fuente en formato embed PDF++.

**Uso:** pegar el prompt en el notebook con las fuentes ETN607 cargadas. Luego en el chat escribir el subtítulo a desarrollar (ej: `"Coordenadas generalizadas"`).

**Resultado:** pendiente

**Notas:** si NotebookLM genera el número de página impreso, el embed puede no coincidir con la página del visor — registrar en `chronicle.md`.

```
TAREA:
Dado un subtítulo de ETN607 (Mecánica Aplicada), desarrollar un complemento breve nivel B.

FUENTES: usar solo los libros cargados en este notebook — no usar conocimiento general.

FORMATO DE RESPUESTA:

1. Definición formal
Extraer del libro fuente la definición más clara y directa del concepto.
Una sola definición — sin parafrasear, sin expandir.

2. Idea clave (opcional)
Solo si hay una propiedad o relación central que la definición no captura.
Máximo 2 líneas.

3. Figura (si existe)
Si en las fuentes hay una figura que ilustre directamente el concepto, incluir exactamente este formato:
[[nombre_exacto_del_archivo.pdf#page=N]]
Etiqueta: [etiqueta de figura tal como aparece en el libro, ej: "Figure 4.3", "Fig. 7.1"]
Figura vista: [descripción breve de qué muestra la figura — 1 línea]
Donde N es el número de página impreso en el libro.
Si no hay figura relevante, omitir esta sección.

REGLAS:
- Solo citar si podés confirmar fuente + página + etiqueta de figura. Si no, omitir — no inventar.
- El enlace debe usar exactamente el formato [[archivo.pdf#page=N]] con doble corchete — no usar ! delante, no usar corchete simple.
- El nombre del archivo debe coincidir exactamente con el nombre del PDF cargado.
- La etiqueta de figura es obligatoria — si el libro no tiene etiqueta, usar el pie de figura textual.
- Sin introducción, sin cierre, sin comentarios — solo el contenido estructurado.
- Respuesta compacta: no más de lo necesario para entender el concepto.
```

---

### v2 — complemento B con embed + IMA-SRC (comparación)

**Objetivo:** probar la misma consulta que v1 pero pidiendo ambos formatos — embed PDF++ e IMA-SRC — para comparar cuál es más útil en la práctica y detectar diferencias en el número de página reportado.

**Uso:** igual que v1. Correr con el mismo subtítulo que v1 para comparar output.

**Resultado:** pendiente

**Notas:** comparar el número de página en IMA-SRC vs el del embed — si difieren, el problema de numeración es real y consistente.

```
TAREA:
Dado un subtítulo de ETN607 (Mecánica Aplicada), desarrollar un complemento breve nivel B.

FUENTES: usar solo los libros cargados en este notebook — no usar conocimiento general.

FORMATO DE RESPUESTA:

1. Definición formal
Extraer del libro fuente la definición más clara y directa del concepto.
Una sola definición — sin parafrasear, sin expandir.

2. Idea clave (opcional)
Solo si hay una propiedad o relación central que la definición no captura.
Máximo 2 líneas.

3. Figura (si existe)
Si en las fuentes hay una figura que ilustre directamente el concepto, incluir ambos formatos:

Embed PDF++:
![[nombre_exacto_del_archivo.pdf#page=N]]
*[pie de figura o etiqueta tal como aparece en el libro]*

Localizador IMA-SRC:
IMA-SRC | fuente: [nombre del archivo PDF] | página: [número impreso] | id: [etiqueta o pie de figura] | posición: [dónde está en la página]

Donde N es el número de página impreso en el libro.
Si no hay figura relevante, omitir esta sección.

REGLAS:
- Solo citar si podés confirmar fuente + página. Si no, omitir — no inventar.
- El nombre del archivo en el embed debe coincidir exactamente con el nombre del PDF cargado.
- Sin introducción, sin cierre, sin comentarios — solo el contenido estructurado.
- Respuesta compacta: no más de lo necesario para entender el concepto.
```
