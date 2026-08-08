# _TABnote-ref · Sistema de apuntes en tablet

> Referencia del sistema TABnote para apuntes en Samsung Notes (Tab S6 Lite, S Pen).
> Versión 1 — 2026-08-05

---

## 1. Template

### Estructura de página

- **Tamaño:** A4 (210 × 297 mm)
- **Márgenes externos:** 15 mm en los 4 lados
- **Margen interno (área utilizable):** 2 mm superior, izquierdo y derecho / 1 mm inferior — representado con líneas segmentadas color `#CED4DA`
- **Grilla:** 44 × 56 recuadros de 4 mm, color `#CED4DA`, cubre solo el área utilizable

### Recuadros notables

| Elemento | Posición | Tamaño |
|---|---|---|
| Running header | Esquina superior derecha, sobre el margen externo | 88 × 9 mm — 2 líneas de escritura de 84 × 4 mm separadas por 1 mm |
| Número de página | Esquina inferior derecha, sobre el margen externo | 7 × 7 mm |

### Divisiones internas de la grilla

Todas las divisiones son líneas segmentadas color `#CED4DA`. Las intersecciones de dos líneas se marcan con una **X segmentada** del mismo color.

**Mitades:**
- Vertical: recuadro 22 desde la izquierda
- Horizontal: recuadro 28 desde arriba
- Intersección: X en (22, 28)

**División áurea (φ ≈ 0.618):**
- Vertical: 17 recuadros desde el borde derecho (= recuadro 27 desde la izquierda)
- Horizontal: 21 recuadros desde el borde inferior (= recuadro 35 desde arriba)
- Intersección: X en (27, 35)

**Cornell:**

| Zona | Medida |
|---|---|
| Título | 6 recuadros de alto desde el borde superior |
| Preguntas / dudas | 13 recuadros de ancho desde el borde izquierdo |
| Resumen | 10 recuadros de alto desde el borde inferior |
| Desarrollo | resto del área (31 recuadros de ancho × altura variable) |

Hay dos líneas horizontales de Cornell: una contando el bloque de título (referencia con título) y otra sin él (referencia sin título), para flexibilizar el uso por página.

Cada bloque Cornell se subdivide internamente en 4 partes con líneas segmentadas + X en la intersección, excepto el bloque de título que solo se divide verticalmente en 2 (sin X).

### Variantes cargadas en Samsung Notes

| Variante | Descripción |
|---|---|
| White theme | Fondo blanco, modo claro |
| Dark theme | Sin fondo — Samsung Notes aplica el negro del modo oscuro automáticamente |
| Sin cuadrícula | Solo márgenes y recuadros notables, para imprimir en tareas |

### Grosor S Pen (punto de partida, ajustar en clase)

| Uso | Grosor |
|---|---|
| Texto normal | 5 |
| Subtítulos | 8 |
| Títulos / énfasis | 12 |

### Grosor y opacidad por elemento

| Elemento | G | O | O anterior |
|---|---|---|---|
| Título principal | 50 | 90 | 70 |
| Subtítulo | 30 | 80 | 60 |
| Línea fina (bajo título) | 1 | 100 | 100 |
| Callout (caja) | 15 | 100 | 100 |

> Valores anteriores registrados para restauración si la prueba no convence.

---

## 2. Jerarquía visual

### Título principal
- Texto centrado
- Resaltador a ambos lados del texto (líneas simétricas)
- Línea delgada debajo que separa el título del contenido
- Color fijo: `#BB3E03` para el título, el resaltado lateral y la línea inferior
- Incluye la indicación `Capítulo #n` en el mismo color

### Subtítulo
- Texto + resaltador en la misma línea, el resaltador llega hasta el borde derecho del área útil
- Texto y resaltador del mismo color — se puede usar cualquier color cálido
- Numerado: `1.`, `2.`, `3.` — ancla de orden para NLM
- Renglón en blanco antes del siguiente subtítulo

### Apunte
- Texto libre, cualquier color
- La paleta de colores ayuda a separar párrafos e ideas — no hay restricción de color único
- El sistema de convenciones (callouts, resaltados, márgenes) diferencia los apuntes de otros elementos sin depender del color

### Callout
- Caja cerrada de 4 lados, grosor notable — significativamente más grueso que el trazo de apunte normal
- No ocupa el ancho completo de la página
- Primera línea dentro de la caja: `> Título`
- Desarrollo debajo del título, dentro de la misma caja
- Catálogo de títulos (en construcción): `> Tarea` — se amplía según uso en clase

> Nota: las fórmulas y otros elementos también se encierran en cajas, pero con grosor similar al trazo normal — esto los diferencia visualmente de los callouts.

### Imagen
- Delimitada por 2 líneas resaltadas en gris, una arriba y una abajo
- El subtítulo de la imagen va en gris e incluye la sigla `IMA` para señalizar a NLM que debe omitir el bloque
- NLM no transcribe imágenes — el usuario realiza un screenshot y lo pega manualmente en la supernova de Obsidian
- Si es posible dentro del prompt, NLM puede incluir una breve descripción de la imagen como pie, para que el usuario la ubique al pegar el screenshot

### Énfasis inline
- Subrayado o trazo más grueso puntual dentro del apunte
- Sin convención de color fija

---

## 3. Convenciones de escritura

| Convención | Uso |
|---|---|
| `valor[unidad]` | Magnitudes: `940[V]`, `470[Ω]`, `2[A]` — valor y unidad siempre juntos |
| `∴` | Síntesis al cerrar un desarrollo o fórmula: `∴ V = 940[V]` |
| `→ ver T02` | Referencia cruzada al margen o al final del bloque — implementación gradual |

---

## 4. Identificador de página (running header)

Escrito a mano en el recuadro superior derecho sobre el margen:

- **Página 1 del tema:** `MAT101 — T01 — DD/MM/YYYY`
- **Páginas siguientes:** `subtítulo activo`

El recuadro tiene 2 líneas de escritura — identificador en la primera, subtítulo en la segunda si es necesario.

---

## 5. Sistema de marginalia

### Señal visual
Una línea de resaltador parte del elemento relevante (título, apunte, fórmula, imagen) y sobrepasa el borde del área utilizable hacia el margen externo. El símbolo se escribe en el margen externo, fuera de la grilla. Se puede usar cualquier lado (izquierdo o derecho).

Una flecha + subrayado sobre el elemento exacto indica la ubicación precisa de la nota, para referencia al transcribir en Obsidian.

### Catálogo de símbolos

| Símbolo | Significado |
|---|---|
| `!` | Importante / examen |
| `?` | Pregunta / duda |
| `X` | Error / corrección |
| `V` | Verificado |
| `C` | Comentario neutro |
| `F` | Fórmula clave |
| `R` | Relación entre materias |
| `T` | Tarea docente |
| `*` | Revisar después |

- **Color:** libre, cualquier color del S Pen
- **Flujo:** NLM transcribe el símbolo tal cual desde el PDF → al crear la nota en Obsidian se convierte en marginalia del plugin Marginalia con el prefijo correspondiente

---

## 6. Flujo de exportación a NotebookLM

1. Apuntes en Samsung Notes con plantilla TABnote
2. Sincronización automática vía Samsung Account → Samsung Notes PC
3. Export como PDF desde Samsung Notes PC → `MAT101_T01.pdf`
4. PDF reemplaza la fuente anterior en NotebookLM (misma fuente, mismo nombre)
5. Prompt de transcripción solicita el subtítulo específico → NLM entrega la supernota enriquecida con fuentes

**Nota:** una sola nota continua por capítulo. Se reexporta y reemplaza cada vez que se agregan subtítulos — no se crean notas nuevas por clase.

---

## 7. Herramientas de Samsung Notes

### Notas adhesivas (Sticky Memo)
Capa flotante sobre la nota. No se exportan al PDF — invisibles para NLM. Uso libre: recordatorios, fechas de examen, estado del capítulo, cualquier información que no deba llegar a NLM.

### Herramienta Cinta (Tape)
**Descartada** — causa pérdida de sincronización tablet → PC.

---

## 8. Pendientes

- [ ] Prueba real en clase — primer uso del template en condiciones reales
- [ ] Ajustes post-prueba si los hay — retomar describiendo el problema puntual
- [ ] Prompt NLM para tablet — adaptar `MAT101-transcription.md` al flujo de apuntes en tablet; incluir instrucción para imágenes (`IMA`) y marginalia

---

*Este archivo es la referencia definitiva del sistema TABnote v1. Reemplaza al borrador `_TABnote-template-draft.md` una vez aprobado post-prueba.*
