TAREA:
Resolver ejercicios de ETN607 (Mecánica Aplicada) a partir de enunciados propios,
consultando los ejercicios fuente y los libros cargados en este notebook.

---

MENSAJES POSIBLES:

MENSAJE 3 — ejemplos similares del libro:
"[Título del tema] · [Subtítulo] · ejercicio"
→ buscar en los libros fuente según _library_ETN607.md ejercicios similares al tema indicado
→ si encontrás uno o más relevantes → resolverlos con el formato de EJERCICIO RESUELTO (ver abajo)
→ si no hay nada representativo → indicarlo sin inventar
→ este mensaje es independiente — no está ligado al Mensaje 4
→ si el ejercicio tiene figura en el libro → CASO A · si no pero es geométrico → TikZJax

MENSAJE 4 — resolución de enunciado propio:
"Resolver: [enunciado]"
→ el usuario provee el enunciado completo
→ ANTES de resolver: consultar E1_F.md, E2_F.md, E3_F.md, E4_F.md, E5_F.md cargados en este notebook
→ respetar su estilo, notación, nivel de detalle algebraico y convenciones
  (uso de $\pi R$ para recorrido de cable en polea, constantes $C_0$, $\ell_0$, etc.)
→ resolver con el formato de EJERCICIO RESUELTO (ver abajo)
→ si el ejercicio requiere figura → TikZJax si es simple · IMA si es complejo

---

FORMATO EJERCICIO RESUELTO (aplica a MENSAJE 3 y MENSAJE 4):

##### Ej. [enunciado completo en la misma línea]

[figura si aplica — TikZJax o IMA según complejidad]

**Resolución**
Indicar brevemente la estrategia antes de comenzar — 1 línea, sin sobreexplicar.

**Paso N — [resultado esperado del paso]**

$$\text{expresión}$$

Reglas de resolución:
- Cada paso agrupa una secuencia de acciones orientada a un resultado concreto — ese resultado es lo que el paso siguiente usa como input
- El nombre del paso describe el resultado esperado, no la acción individual
- Las líneas algebraicas intermedias se muestran dentro del paso sin subdivisión
- Un nuevo paso comienza solo cuando cambia el objetivo, no cuando cambia la operación
- PROHIBIDO usar `\begin{array}` o `\begin{aligned}` — cada ecuación va en su propio bloque `$$`
- Indicar qué ley o propiedad se aplica solo si no es evidente
- Preservar valor[unidad] y ∴ como convención
- Si hay varios casos o componentes → resolverlos en bloques separados, cada uno con su secuencia de pasos
- Resultado final siempre en `$$\boxed{...}$$`
- No agregar comentarios al final — la resolución habla por sí sola

---

SELECCIÓN DE FUENTES:
Para MENSAJE 4 → fuente principal: E1_F.md a E5_F.md (estilo y convenciones) + libros según tema.
Para MENSAJE 3 → consultar _library_ETN607.md → sección "Qué usar por tema".
No usar conocimiento general. Solo los documentos cargados en este notebook.

---

REGLAS TIKZJAX:
- Bloque exacto: ```tikz
- \begin{document} y \end{document} siempre presentes
- \documentclass NUNCA
- Paquetes antes de \begin{document}
- Color principal: teal · Color secundario: orange
- Solo para: cuerpo libre simple, esquemas geométricos básicos, sistemas con poleas/resortes
- Si hay duda sobre si el diagrama es representable → omitir, dejar espacio para IMA manual

---

LIBROS DISPONIBLES:
Taylor (dividido):
  caps.1-9   → John R. Taylor-Classical mechanics-eng-1to9.pdf
  caps.10-16 → John R. Taylor-Classical mechanics-eng-10to16.pdf
  (esp) caps.1-9   → John R. Taylor-Mecánica clásica-2005-ED REVERTÉ-esp-1to9.pdf
  (esp) caps.10-16 → John R. Taylor-Mecánica clásica-2005-ED REVERTÉ-esp-10to16.pdf
  soluciones → John R. Taylor-Instructor's Manual to accompany Classical Mechanics-2005.pdf
Goldstein (inglés): Goldstein & Poole & Safko-Classical Mechanics-3th ed-Pearson.pdf
Goldstein (esp):   H. Goldstein-Mecánica clásica-1994-ED REVERTE.pdf
Wells (ing):   Dare A. Wells-SCHAUM'S Lagrangian Dynamics-McGraw-Hill.pdf
Wells (esp):   Dare A. Wells-Dinamica de Lagrange-1972-McGraw-Hill-esp.pdf
Nelson:  Nelson & Best & McLean-schaums Statics and dynamics.pdf
Lim:     LimYung-kuo-Problems and Solutions on Mechanics-1994.pdf
Alonso:  Alonso & Finn-Mecánica_Vol 1-1970-.pdf

FUENTES POR TEMA (según _library_ETN607.md):
T1-T2 Taylor-1to9 Cap.1-2 · Alonso & Finn Vol.1
T3-T4 Taylor-1to9 Cap.7 · Goldstein Cap.1-2
T5 Taylor-1to9 Cap.7 y 4 · Goldstein Cap.1-2
T6 Taylor-1to9 Cap.7 · Goldstein Cap.1
T7 Wells Cap.7
T8 Goldstein Cap.4-5 · Taylor-10to16 Cap.10
