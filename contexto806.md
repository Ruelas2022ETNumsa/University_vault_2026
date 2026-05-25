# CONTEXTO DE TRABAJO — PROCESOS ESTOCÁSTICOS ETN806

## INSTRUCCIÓN INMEDIATA — LEER AL CARGAR ESTE ARCHIVO

Cuando el usuario comparta este archivo, Claude debe hacer lo siguiente **antes de responder cualquier otra cosa**:

1. Leer el archivo `E:\University_vault_2026\ETN806-Formulario-2doP-Variables-Aleatorias-Multiples.md` completo.
2. Leer el archivo `E:\University_vault_2026\_app\_appnotes\desmos_guide.md` (sección Claude) para las gráficas.
3. Confirmar al usuario con un mensaje breve: *"Contexto cargado. Formulario leído. Listo para revisar ejercicios."*

> Si en el futuro existe un `Formulario_iii` u otro formulario indicado por el usuario, leerlo en lugar del anterior o además de él según se indique.

---

## PROPÓSITO DE ESTE DOCUMENTO

Describe el flujo de trabajo para **resolver, revisar y graficar** ejercicios de Variables Aleatorias Continuas Múltiples de ETN806. Es independiente del parcial o del conjunto de ejercicios activo — aplica a cualquier ejercicio nuevo que el usuario traiga.

---

## ARCHIVOS DEL SISTEMA

| Archivo | Ubicación | Rol |
|---------|-----------|-----|
| `ETN806-Formulario-2doP-Variables-Aleatorias-Multiples.md` | `E:\University_vault_2026\` | **Fuente de verdad matemática.** Todas las fórmulas, definiciones y procedimientos válidos del curso. |
| `ETN806-Practica2-Enunciados-Variables-Aleatorias-Multiples.md` | `E:\University_vault_2026\` | Enunciados de la Práctica 2. Referencia de enunciados originales. |
| `ETN806-Resuelto-Referencia-Densidad-Conjunta-Triangular.md` | `E:\University_vault_2026\` | Ejercicio resuelto por el docente. Referencia de nivel y formato. NO se modifica. |
| `desmos_intro.md` | `E:\University_vault_2026\_app\_appnotes\` | Guía completa de sintaxis Desmos para Obsidian. Usar siempre al generar o corregir gráficas. |
| `ETN806-P2-E*.md` | `E:\University_vault_2026\` | Ejercicios resueltos de la Práctica 2 (serie a). |
| `ETN806-2P-E*.md` | `E:\University_vault_2026\` | Ejercicios resueltos del 2do Parcial (serie b). |

---

## FLUJO DE TRABAJO

```
1. El usuario trae un ejercicio (archivo .md o texto directo)
         ↓
2. Claude lee el enunciado e identifica qué piden los incisos
         ↓
3. Claude verifica la resolución contra el formulario, inciso por inciso
         ↓
4. Si el método usado no coincide con el formulario → agrega resolución alternativa
   Si hay errores → agrega callout de corrección
   Si está correcto → agrega callout de verificación
         ↓
5. Claude revisa las gráficas Desmos: corrige sintaxis y elimina las que no aportan
         ↓
6. Claude edita el archivo directamente en el vault usando Filesystem
```

---

## ROL DE CLAUDE AL REVISAR UN EJERCICIO

### 1. Leer el enunciado completo antes de revisar

Identificar:
- La función conjunta $f_{X,Y}(x,y)$ y su región de soporte.
- Qué pide cada inciso (normalización, marginal, independencia, probabilidad, esperanza, varianza, covarianza, densidad condicional).
- El tipo de dominio (rectangular, triangular, circular, infinito, con valor absoluto).

### 2. Verificar inciso por inciso contra el formulario

Para cada inciso revisar:
- Que la **fórmula aplicada** corresponda al formulario.
- Que los **límites de integración** sean correctos según la región del enunciado.
- Que el **desarrollo algebraico** sea correcto paso a paso.
- Que el **resultado final** sea correcto.

### 3. Actuar según el resultado de la verificación

**Si el método usado no corresponde al formulario** → agregar resolución alternativa debajo usando el método del formulario, sin borrar la original:

```
> [!check] Alternativo — [nombre del método] (Formulario)
> [desarrollo completo con el método del formulario]
```

**Si hay errores** → agregar callout de corrección debajo del inciso:

```
> [!correction] Corrección
> **Error identificado:** [descripción]
>
> **Corrección:**
> [desarrollo correcto paso a paso]
>
> **Resultado correcto:** [resultado]
```

**Si está correcto y usa el método del formulario** → agregar:

```
> [!check] Correcto
> Procedimiento y resultado verificados con el formulario.
```

### 4. Regla absoluta — no borrar contenido original

Claude **nunca** borra ni modifica el texto original del ejercicio. Solo agrega bloques debajo de cada inciso.

---

## CÓMO APLICAR EL FORMULARIO — GUÍA GENERAL

Esta sección describe cómo usar las fórmulas del formulario ante cualquier ejercicio nuevo. No depende de ejercicios específicos previos.

### Paso 0 — Identificar el dominio

El dominio determina todo lo demás. Antes de plantear cualquier integral:

| Tipo de dominio | Ejemplo | Implicación |
|----------------|---------|-------------|
| **Rectangular** | $0\le x\le a,\; 0\le y\le b$ | Límites de marginales constantes. Independencia posible si $f$ factoriza. |
| **Triangular** | $x+y\le 1,\; x,y\ge 0$ | Límites de marginales **variables**. Independencia generalmente imposible. |
| **Con curva** | $x\le y\le\sqrt{x}$ | Identificar intersecciones para acotar $x$. |
| **Circular/semicircular** | $x^2+y^2\le 1$ | Despejar una variable en función de la otra para los límites. |
| **Con valor absoluto** | $\|x\|\ge y$ | Descomponer en $x\ge 0$ y $x<0$ por separado. |
| **Infinito** | $x,y\ge 0$ sin cota superior | Usar integrales impropias con límite $\infty$. |

---

### Paso 1 — Hallar la constante $k$ (si se pide)

**Fórmula del formulario:** $\displaystyle\iint f_{X,Y}(x,y)\,dx\,dy = 1$

**Procedimiento:**
1. Plantear la integral doble con los límites correctos del dominio.
2. Integrar primero respecto a la variable con límites más simples.
3. Despejar $k$.

**Alerta:** el orden de integración importa — elegir el que simplifique más los límites.

---

### Paso 2 — Densidades marginales

**Fórmulas del formulario:**
$$f_X(x) = \int_{y_{min}(x)}^{y_{max}(x)} f_{X,Y}(x,y)\,dy \qquad f_Y(y) = \int_{x_{min}(y)}^{x_{max}(y)} f_{X,Y}(x,y)\,dx$$

**Procedimiento:**
1. Para $f_X(x)$: fijar $x$ e integrar en $y$ con los límites que dependen de $x$.
2. Para $f_Y(y)$: fijar $y$ e integrar en $x$ con los límites que dependen de $y$.
3. Si el dominio cambia de forma al variar la variable de integración → **partir en tramos**.

**Cuándo partir en tramos:** cuando la frontera del dominio tiene un quiebre o vértice intermedio. Ejemplo: dominio triangular con vértice en $y=2$ divide $f_Y(y)$ en $[0,2]$ y $[2,4]$.

---

### Paso 3 — Independencia estadística

**Fórmula del formulario:** $f_{X,Y}(x,y) = f_X(x)\cdot f_Y(y)$ para **todo** $(x,y)$ en el soporte.

**Procedimiento:**
1. Calcular $f_X(x)$ y $f_Y(y)$ (Paso 2).
2. Calcular el producto $f_X(x)\cdot f_Y(y)$ algebraicamente.
3. Comparar con $f_{X,Y}(x,y)$.
4. **Solo si son algebraicamente iguales Y el dominio es rectangular** → independientes.

**Alerta crítica:** un dominio triangular o cualquier dominio no rectangular implica dependencia aunque la función factorize algebraicamente, porque el dominio conjunto NO es producto cartesiano de los dominios individuales.

---

### Paso 4 — Probabilidad en una región

**Fórmula del formulario:** $P\big((X,Y)\in R\big) = \displaystyle\iint_R f_{X,Y}(x,y)\,dx\,dy$

**Procedimiento:**
1. Identificar la región $R$ como intersección del soporte y la condición del evento.
2. Encontrar las intersecciones de las fronteras para acotar los límites.
3. Plantear la integral doble con los límites correctos.
4. Integrar de adentro hacia afuera.

**Complemento:** si $R$ es difícil de integrar directamente, usar $P(R) = 1 - P(R^c)$ si $R^c$ es más simple.

---

### Paso 5 — Esperanza y varianza

**Fórmulas del formulario:**
$$E[X] = \int x\,f_X(x)\,dx \qquad E[X^2] = \int x^2\,f_X(x)\,dx \qquad VAR[X] = E[X^2] - (E[X])^2$$

**Procedimiento desde la marginal:**
1. Obtener $f_X(x)$ del Paso 2.
2. Calcular $E[X]$, luego $E[X^2]$, luego $VAR[X] = E[X^2] - \mu_X^2$.
3. Repetir para $Y$.

---

### Paso 6 — Varianza de la suma $VAR[X+Y]$

**Fórmula del formulario:**
$$VAR[X+Y] = VAR[X] + VAR[Y] + 2\,COV[X,Y]$$
$$COV[X,Y] = E[XY] - \mu_X\mu_Y \qquad E[XY] = \iint xy\,f_{X,Y}(x,y)\,dy\,dx$$

**Procedimiento:**
1. Calcular $VAR[X]$ y $VAR[Y]$ (Paso 5).
2. Calcular $E[XY]$ por integral doble sobre el dominio completo.
3. Calcular $COV[X,Y] = E[XY] - \mu_X\mu_Y$.
4. Si $X,Y$ son independientes → $COV=0$ y la fórmula se reduce a $VAR[X]+VAR[Y]$.

---

### Paso 7 — Densidad condicional dado evento $B$

**Fórmula del formulario:**
$$f_{X,Y|B}(x,y) = \frac{f_{X,Y}(x,y)}{P[B]} \quad \text{para } (x,y)\in B, \qquad 0 \text{ en otro caso}$$

**Procedimiento:**
1. Calcular $P[B] = \displaystyle\iint_B f_{X,Y}(x,y)\,dx\,dy$.
2. Dividir $f_{X,Y}$ entre $P[B]$ dentro de la región $B$.
3. Verificar que $\displaystyle\iint_B f_{X,Y|B}\,dx\,dy = 1$ (opcional pero recomendable).

---

## ERRORES COMUNES A VIGILAR

- **Límites de integración incorrectos** — mal interpretada la región del enunciado. El error más frecuente.
- **Marginal con límites fijos** — usar constantes donde deberían ir expresiones en $x$ o $y$.
- **Independencia en dominio triangular** — declarar independencia solo porque la función factoriza, sin revisar el dominio.
- **$E[XY]$ confundido con $E[X]\cdot E[Y]$** — solo son iguales si hay independencia.
- **Densidad condicional sin dividir por $P[B]$** — olvidar la normalización.
- **Gráficas con sintaxis inválida** — llaves `{}`, espacios alrededor de `|`, `sqrt(x)` sin `\`, comentarios `//`. Ver reglas Desmos abajo.

---

## MANEJO DE GRÁFICAS DESMOS

### Cuándo incluir gráfica

Solo incluir gráfica si aporta claridad que el texto no puede dar:
- Regiones de soporte con geometría no obvia (triángulos, semicírculos, valor absoluto).
- Regiones de integración para probabilidades con fronteras curvas o partidas.
- Densidades marginales con forma visual relevante.

**No incluir** gráfica para: resultados numéricos simples, varianzas, covarianzas, incisos de independencia donde la conclusión es algebraica.

### Reglas de sintaxis Desmos (plugin Obsidian)

```desmos-graphx
left=; right=; bottom=; top=;
width=500; height=500;
---
y>=x|x>=0|y<=4-x|#a5d8ff
y=\sqrt{x}|0<=x<=1|GREEN
(0,0)|label:(0,0)|BLACK
```

Reglas obligatorias:
- El separador `---` es siempre obligatorio.
- Sin espacios alrededor de `|`. Sin llaves `{}`. Sin comentarios `//`.
- Raíces con `\sqrt{x}`, fracciones con `\frac{a}{b}`, pi con `\pi`.
- Restricciones de dominio dentro de la misma línea: `y=x|0<=x<=2|BLUE`.
- Colores de relleno hexadecimales: `#a5d8ff` (azul), `#b2f2bb` (verde), `#ffd8a8` (naranja), `#ff7b7b` (rojo), `#d0bfff` (morado).
- Áreas sombreadas: una inecuación con todas las condiciones en una línea separadas por `|`.
- Líneas con restricción de dominio para no desbordarse: `y=1-x|0<=x<=1|BLUE`.

> **Nota sobre este archivo:** los bloques de código Desmos aquí usan ` ```desmos-graphx ` (con x) para que Obsidian no los renderice. En los archivos de ejercicios usar siempre ` ```desmos-graph ` sin la x.

---

## INSTRUCCIONES DE FLUJO CON EL USUARIO

1. **Editar siempre directamente** en el `.md` del vault usando Filesystem. Si no es posible, avisar al usuario.

2. **Correcciones Desmos:** no mostrar el bloque corregido en el chat. Solo editar el `.md`.

3. **Resumen por chat:** una línea por inciso:
   - `Inciso a) — correcto`
   - `Inciso b) — corregido`
   - `Inciso c) — alternativo agregado`

   Sin detalles matemáticos en el chat — todo va en el archivo.

4. **Gráficas:** si hay que borrar una gráfica innecesaria, hacerlo sin preguntar. Si hay que corregir sintaxis, hacerlo directamente.

5. **Mantener el chat mínimo.** Todo el contenido matemático va en el archivo.
