# TABnote — Template v1 · Borrador de especificaciones

---

## Estructura general de la página

La página exportada es de tamaño **A4 (210 × 297 mm)**. Toda medida se toma desde el borde de la hoja salvo que se indique lo contrario.

### Márgenes externos
- **15 mm en los 4 lados** — separan el área de trabajo del borde de la hoja.

### Margen interno (borde del área utilizable)
Dentro del margen externo existe un segundo borde que delimita el **área utilizable**, donde se ubica la grilla y todos los elementos de escritura. Este borde interno se representa con líneas segmentadas del mismo color que la grilla (`#CED4DA`):
- **Superior, izquierdo y derecho:** 2 mm de separación desde el margen externo hacia adentro.
- **Inferior:** 1 mm de separación desde el margen externo hacia adentro.

Todo lo que se describe a continuación se posiciona y mide **dentro del área utilizable**, salvo los recuadros de running header y número de página que se ubican sobre el margen externo.

---

## Grilla principal

- **Tamaño de cada recuadro:** 4 mm × 4 mm.
- **Cantidad de recuadros en el área utilizable:** 44 recuadros de ancho × 56 recuadros de alto.
- **Color de las líneas:** `#CED4DA`.
- La grilla cubre únicamente el área utilizable — no se extiende sobre los márgenes ni el margen interno.

---

## Recuadros notables

### Running header (identificador de página)
- **Posición:** esquina superior derecha, sobre el margen externo (fuera del área utilizable).
- **Tamaño externo:** 88 mm de ancho × 9 mm de alto.
- **Contenido interno:** 2 líneas de escritura de 84 mm de ancho × 4 mm de alto cada una, separadas por 1 mm entre sí.
- **Uso:** línea superior para el identificador del capítulo (`MAT101 — T01 — DD/MM/YYYY`), línea inferior para el subtítulo activo en páginas de continuación.

### Número de página
- **Posición:** esquina inferior derecha, sobre el margen externo.
- **Tamaño:** 7 mm de ancho × 7 mm de alto.

---

## Divisiones internas de la grilla

Las divisiones internas se representan con **líneas segmentadas** del mismo color que la grilla (`#CED4DA`), diferenciándose de las líneas sólidas del borde del área utilizable. Son guías visuales — no delimitan zonas rígidas sino referencias opcionales para estructurar los apuntes.

En la **intersección de dos líneas segmentadas** se dibuja una **X segmentada** del mismo color, como marcador visual del punto de cruce.

---

### 1. División en la mitad de la grilla completa
- **Vertical:** línea segmentada en el recuadro 22 desde la izquierda (mitad de 44).
- **Horizontal:** línea segmentada en el recuadro 28 desde arriba (mitad de 56).
- **Intersección:** X segmentada en el centro del área utilizable (recuadro 22, 28).

---

### 2. División áurea
Basada en la proporción φ ≈ 0.618, aplicada desde los bordes hacia el centro del área utilizable:
- **Vertical (desde el borde derecho):** línea segmentada a 17 recuadros desde el borde derecho del área utilizable (equivale al recuadro 27 desde la izquierda).
- **Horizontal (desde la base):** línea segmentada a 21 recuadros desde el borde inferior del área utilizable (equivale al recuadro 35 desde arriba).
- **Intersección:** X segmentada en el punto áureo (recuadro 27 desde izquierda, 35 desde arriba).

---

### 3. Notas Cornell
Sistema de división en zonas para estructurar apuntes. Se representa con líneas segmentadas sobre la grilla.

#### Zonas Cornell

| Zona | Descripción | Medida |
|---|---|---|
| Título | Franja superior horizontal | 6 recuadros de alto desde el borde superior |
| Preguntas / dudas | Columna izquierda vertical | 13 recuadros de ancho desde el borde izquierdo |
| Desarrollo | Zona central principal | resto del área (31 ancho × altura variable) |
| Resumen | Franja inferior horizontal | 10 recuadros de alto desde el borde inferior |

#### Líneas horizontales de Cornell
Existen **dos líneas horizontales** que delimitan el bloque de título:
- **Línea 1:** a 6 recuadros desde arriba — separa el bloque de título del resto (incluye el bloque de título en la zona superior).
- **Línea 2:** a 6 recuadros desde arriba contando solo el área de dudas y desarrollo (sin el bloque de título) — referencia alternativa para cuando no se usa el bloque de título en una página.

#### Subdivisión interna de cada bloque Cornell
Cada bloque Cornell se divide internamente en 4 partes iguales mediante líneas segmentadas, generando una subgrilla de referencia dentro de cada zona:
- **Bloque de preguntas/dudas:** subdividido en 4 con líneas vertical y horizontal segmentadas + X en la intersección.
- **Bloque de desarrollo:** subdividido en 4 con líneas vertical y horizontal segmentadas + X en la intersección.
- **Bloque de resumen:** subdividido en 4 con líneas vertical y horizontal segmentadas + X en la intersección.
- **Bloque de título:** subdividido solo verticalmente en 2 (sin subdivisión horizontal, sin X) — por su altura reducida no se divide en 4.

---

## Sistema de símbolos al margen (Marginalia tablet)

Los símbolos se escriben con S Pen en el margen externo, conectados al contenido mediante una línea de resaltador que parte del elemento relevante (título, apunte, fórmula) y sobrepasa el borde del área utilizable hasta el margen. El símbolo se escribe en el extremo del margen, fuera del área de escritura.

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

- **Color:** libre, cualquier color del S Pen.
- **Lado:** izquierdo o derecho, indistinto.
- **Flujo de transcripción:** NLM transcribe el símbolo tal cual desde el PDF exportado; al crear la nota en Obsidian se convierte en marginalia del plugin Marginalia con el prefijo correspondiente.

---

## Variantes del template cargadas en Samsung Notes

| Variante | Descripción |
|---|---|
| White theme | Fondo blanco, para modo claro |
| Dark theme | Sin fondo (transparente), Samsung Notes aplica el negro del modo oscuro automáticamente |
| Sin cuadrícula | Solo márgenes y recuadros notables, para imprimir en tareas |

---

## Notas adhesivas (Sticky Memo)

Disponibles en Samsung Notes como capa flotante sobre la nota. **No se exportan al PDF** — son invisibles para NotebookLM. Uso libre para recordatorios, fechas de examen, estado del capítulo y cualquier información que no deba llegar a NLM.

---

## Herramientas descartadas

| Herramienta | Motivo |
|---|---|
| Cinta (Tape) | Causa pérdida de sincronización tablet → PC |

---

*Borrador — pendiente revisión post-prueba en clase. Las especificaciones aquí descritas pueden ajustarse una vez probado el template en condiciones reales.*
