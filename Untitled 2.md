Puntuación final — **caso de uso: circuito electrónico para analizar con Claude**

|Formato|Costo (tokens)|Precisión|Facilidad de uso|Editabilidad|**Total /10**|
|---|---|---|---|---|---|
|**PNG**|9/10|7/10|10/10|1/10|**7.2**|
|**SVG** (Excalidraw export)|2/10|9/10|6/10|8/10|**6.2**|
|**Excalidraw .md** (Obsidian)|4/10|8/10|3/10|9/10|**6.0**|

**Veredicto por situación:**

- **Solo quieres que Claude entienda el circuito → PNG**, sin dudarlo. Barato, inmediato, suficientemente preciso.
- **Quieres editar o que Claude modifique el archivo después → .excalidraw JSON crudo** (no el .md comprimido), que no probamos hoy pero sería el mejor — texto legible + estructura clara + sin el overhead del blob base64.
- **SVG solo vale** si desactivás el modo "hand-drawn" de Excalidraw al exportar (estilo Architect/líneas rectas), lo que reduciría los paths de ~78k tokens a quizás 8-10k. Con eso subiría a primer lugar en precisión/costo combinados.


### Comparación final de los 3 formatos

|Formato|Tokens aprox.|Qué tan bien lo interpreté|Por qué|
|---|---|---|---|
|**.md (Excalidraw/Obsidian, comprimido)**|~27.000-29.000|Correcto en estructura, tuve que decodificar con código|El JSON real es eficiente, pero viene comprimido en base64 (LZ-String), así que pagué el costo de leer ruido binario antes de poder extraer el JSON útil|
|**.png**|~1.500-3.000|Correcto, salvo que no distinguí que eran 3 instancias del mismo circuito (lo interpreté como esquemas algo distintos)|Visión interpreta forma, no estructura; barato pero con margen de error en relaciones complejas|
|**.svg (exportado por Excalidraw, estilo "hand-drawn")**|~78.000|Correcto y exacto (mismo resultado que el PNG, sin ambigüedad)|Texto 100% legible y preciso, pero el estilo rough.js infla los paths con geometría decorativa innecesaria para interpretación|

**Conclusión real (corrigiendo lo que dije antes):** para este circuito específico, el **PNG fue el más eficiente en tokens por lejos**, y su precisión fue prácticamente igual de buena que el SVG. El SVG solo justificaría su costo si necesitaras coordenadas exactas para edición programática (mover un elemento, cambiar un valor en el código), no para "entender qué dice el diagrama". Y el .md comprimido quedó en el medio: ni tan preciso de leer directo (tuve que descomprimir con Python) ni tan barato como la imagen.

Si tuviera que elegir un ganador general para "mostrale un diagrama a Claude": **PNG con buen contraste y resolución moderada** gana en costo/beneficio, salvo que desactives el modo "hand-drawn" de Excalidraw al exportar el SVG (Excalidraw tiene una opción de estilo "Architect" con líneas rectas, que generaría paths mucho más simples y baratos).