# CONTEXTO DE TRABAJO — PROCESOS ESTOCÁSTICOS 806

## INSTRUCCIÓN INMEDIATA — LEER AL CARGAR ESTE ARCHIVO

Cuando el usuario comparta este archivo, Claude debe hacer lo siguiente **antes de responder cualquier otra cosa**:

1. Leer el archivo `E:\University_vault_2026\Formulario_806_ii.md` completo.
2. Leer el archivo `E:\University_vault_2026\_app\_appnotes\desmos_intro.md` para las graficas.
3. leer el archivo `E:\University_vault_2026\Resuelto 1.md` completo.
4. Confirmar al usuario con un mensaje breve: *"Contexto cargado. Formulario leído. Listo para revisar ejercicios."*

No esperar a que el usuario pida revisar un ejercicio. La lectura del formulario es el primer paso obligatorio al iniciar la conversación con este contexto.

---

## PROPÓSITO DE ESTE DOCUMENTO

Este documento describe el flujo de trabajo completo para resolver, revisar y graficar ejercicios de **Variables Aleatorias Continuas Múltiples** (Procesos Estocásticos 806). Define qué notas existen, qué rol cumple cada una, y cómo debe actuar Claude en cada etapa.

---

## NOTAS DEL SISTEMA

| Nota | Ubicación | Rol |
|------|-----------|-----|
| `Formulario_806_ii.md` | `E:\University_vault_2026\` | Fuente de verdad matemática. Contiene todas las fórmulas, definiciones y procedimientos válidos para el curso. |
| `desmoslm.md` | `E:\University_vault_2026\_app\_appnotes\` | Instrucciones para generar bloques `desmos-graph` compatibles con Obsidian. |
| `E1.md`, `E2.md`, `E3.md`, ... | `E:\University_vault_2026\` | Ejercicios resueltos por NotebookLM. Cada archivo contiene un enunciado y su resolución por incisos. Claude los revisa y corrige. |

---

## FLUJO DE TRABAJO

```
1. El usuario pide a NotebookLM resolver un ejercicio
         ↓
2. NotebookLM genera la respuesta (enunciado + resolución por incisos)
         ↓
3. El usuario guarda esa respuesta en Obsidian como E1.md, E2.md, etc.
         ↓
4. El usuario le pide a Claude que revise el archivo
         ↓
5. Claude lee el ejercicio y lo verifica contra el Formulario_806_ii.md
         ↓
6. Claude agrega correcciones debajo de cada inciso usando callouts
         ↓
7. Si hay gráficas mal ubicadas, Claude las separa por inciso y las reubica
```

---

## ROL DE CLAUDE EN LA REVISIÓN

Cuando el usuario pida revisar un ejercicio `E1.md`, `E2.md`, etc., Claude debe:

### 1. Verificar contra el formulario

El formulario ya fue leído al iniciar la sesión. Usarlo como única fuente de verdad matemática para verificar procedimientos, fórmulas y resultados.

### 2. Revisar inciso por inciso

Recorrer el ejercicio inciso por inciso (a, b, c, ...) y en cada uno verificar:

- Que el planteamiento de la integral sea correcto (límites, orden de integración, región).
- Que la fórmula aplicada corresponda al formulario.
- Que el desarrollo algebraico sea correcto paso a paso.
- Que el resultado final sea correcto.
- Que los límites de integración sean consistentes con la región del problema.

### 3. Agregar correcciones con callout

Si un inciso tiene errores, agregar **debajo del inciso** (sin borrar ni modificar el contenido original) un bloque callout en este formato:

```
> [!correction] Corrección
> **Error identificado:** [descripción del error]
>
> **Corrección:**
> [desarrollo correcto paso a paso]
>
> **Resultado correcto:** [resultado final]
```

Si el inciso está correcto, agregar:

```
> [!check] Correcto
> Procedimiento y resultado verificados con el formulario.
```

### 4. No sobreescribir el contenido original

Claude NUNCA borra ni modifica el texto original del ejercicio. Solo agrega callouts debajo de cada inciso. El usuario debe poder ver el original y la corrección en paralelo.

---

## MANEJO DE GRÁFICAS DESMOS EN LOS EJERCICIOS

### Problema frecuente

NotebookLM tiende a generar todas las gráficas del ejercicio en un solo bloque `desmos-graph` al final del archivo, mezclando ecuaciones de distintos incisos.

>**NOTA — Bloques de código Desmos en este documento:** En este archivo `contexto806.md` los bloques de código Desmos se escriben como ` ```desmos-graphx ` (con x al final) únicamente para evitar que Obsidian los renderice y poder leer el texto plano del ejemplo.
>
>**Al corregir o generar bloques en los ejercicios** (`E1.md`, `E2.md`, etc.) Claude debe usar siempre ` ```desmos-graph ` **sin la x**, para que el plugin renderice la gráfica correctamente.
>
>Regla: `desmos-graphx` = solo en este documento de contexto. `desmos-graph` = en todos los ejercicios.

### Lo que Claude debe hacer

Cuando encuentre gráficas mal ubicadas (todas juntas al final), debe:

1. **Identificar** a qué inciso pertenece cada ecuación o región graficada.
2. **Separar** el bloque original en bloques individuales, uno por inciso.
3. **Reubicar** cada bloque dentro del inciso correspondiente, inmediatamente después del desarrollo matemático de ese inciso.
4. **Eliminar** el bloque original acumulado al final.

### Formato correcto para cada gráfica

Cada gráfica debe ir dentro de su inciso con una etiqueta clara:

#### Gráfica — inciso [letra]

```desmos-graphx
left=; right=; bottom=; top=;
width=500; height=500;
---
[ecuaciones del inciso]
```

### Reglas para generar/corregir bloques Desmos

- El separador `---` es SIEMPRE obligatorio.
- Cada inciso tiene su propio bloque independiente.
- Ajustar `left`, `right`, `bottom`, `top` para que la región del inciso quede bien visible.
- Usar colores hexadecimales claros para rellenos: `#a5d8ff`, `#b2f2bb`, `#ffd8a8`, `#d0bfff`.
- Etiquetar los puntos clave (vértices, intersecciones, medias) con `|label:`.
- Solo generar gráfica si aporta claridad visual al resultado. No todos los incisos la necesitan.

---

## TEMAS CUBIERTOS POR EL FORMULARIO

El formulario `Formulario_806_ii.md` cubre los siguientes temas. Claude debe verificar que los ejercicios usen correctamente:

1. **Función de densidad de probabilidad** — propiedades, normalización, $P(a \leq X \leq b)$
2. **Esperanza matemática** — $E[X]$, $E[g(X,Y)]$, linealidad
3. **Varianza** — $VAR[X] = E[X^2] - \mu_X^2$, desviación estándar
4. **Densidad conjunta** — propiedades, normalización doble, probabilidad en región $R$
5. **Función de distribución acumulativa conjunta** — $F_{X,Y}(x,y)$ y sus propiedades marginales
6. **Densidades marginales** — $f_X(x)$, $f_Y(y)$ por integración
7. **Independencia estadística** — verificación por $f_{X,Y} = f_X \cdot f_Y$
8. **Valor esperado de dos variables** — $E[W]$ con $W = g(X,Y)$
9. **Varianza de la suma y covarianza** — $VAR[X+Y]$, $COV[X,Y] = E[XY] - \mu_X\mu_Y$
10. **Coeficiente de correlación** — $\rho_{X,Y}$, rango $[-1, 1]$
11. **Densidad condicional** — dado evento $B$ y dado otra variable

---

## ERRORES COMUNES A VIGILAR

- **Límites de integración incorrectos** — región mal interpretada del enunciado (el error más común).
- **Orden de integración invertido** — integrar primero en $x$ cuando corresponde en $y$ o viceversa.
- **Constante $k$ mal calculada** — error al despejar $k$ de la condición de normalización.
- **Marginal con límites fijos en vez de variables** — usar números donde deberían ir expresiones en $x$ o $y$.
- **Independencia mal verificada** — concluir independencia sin hacer el producto $f_X \cdot f_Y$ explícitamente.
- **Covarianza mal calculada** — confundir $E[XY]$ con $E[X] \cdot E[Y]$.
- **Densidad condicional sin normalizar** — olvidar dividir por $P[B]$.
- **Gráficas de todos los incisos mezcladas en un solo bloque** — separar siempre por inciso.

---

## EJEMPLO DE ESTRUCTURA ESPERADA EN UN EJERCICIO EN.md

```markdown
# Ejercicio N — [título o descripción breve]

## Enunciado
[texto del enunciado]

## Inciso a)
[desarrollo de NotebookLM]

> [!correction] Corrección
> **Error identificado:** ...
> **Corrección:** ...
> **Resultado correcto:** ...

#### Gráfica — inciso a)

```
```desmos-graphx
left=; right=; bottom=; top=;
width=500; height=500;
---
[ecuaciones del inciso a]
```
```

## Inciso b)
[desarrollo de NotebookLM]

> [!check] Correcto
> Procedimiento y resultado verificados con el formulario.

---
```

## NOTAS FINALES

- Si una fórmula del ejercicio no aparece en el formulario, señalarlo explícitamente.
- Si el enunciado es ambiguo (región no especificada, función incompleta), indicarlo antes de corregir.
- Los ejercicios `E1.md`, `E2.md`, etc. pueden tener cualquier combinación de temas. No asumir estructura fija.

---

## ANÁLISIS TEMÁTICO — PRÁCTICA Nº2 Y Resuelto 1

> Este análisis fue generado a partir de los PDFs de diapositivas del curso (P1_SP, P2_SP, ejercicio_variable_multiple_continua) y los enunciados de la Práctica Nº2. Sirve como mapa de contenido para que Claude identifique qué fórmulas y procedimientos aplicar en cada ejercicio.

---

### EJERCICIO Resuelto 1 — Densidad conjunta con región triangular

**Función:** $f_{X,Y}(x,y) = kx$ para $0 \le x \le 1,\; x \le y \le 2-x$

| Inciso | Tema específico | Procedimiento aplicado | Fórmula clave |
|--------|----------------|----------------------|---------------|
| a) | Normalización de densidad conjunta — hallar constante $k$ | Integral doble igualada a 1; integrar primero en $y$ (límites variables $x$ a $2-x$), luego en $x$ | $\int_0^1\int_x^{2-x} kx\,dy\,dx = 1$ |
| b) | Densidades marginales — región triangular con partición | Marginal de $X$: integrar en $y$ con límites variables. Marginal de $Y$: partir en dos tramos $[0,1]$ y $[1,2]$ por cambio de frontera | $f_X(x)=\int_x^{2-x}3x\,dy$; $f_Y(y)$ por tramos |
| c) | Independencia estadística — verificación por producto de marginales | Evaluar en un punto $(0.5, 0.5)$ y comparar $f_{X,Y}$ con $f_X \cdot f_Y$ | $f_{X,Y}(x,y) \stackrel{?}{=} f_X(x)\cdot f_Y(y)$ |
| d) | Probabilidad en región acotada por curva — intersección con dominio | Integral doble con límite superior curvo $y=\sqrt{x}$; límite inferior $y=x$ dentro del dominio | $P = \int_0^1\int_x^{\sqrt{x}} 3x\,dy\,dx$ |
| e) | Probabilidad por complemento — región lineal dentro del dominio | Hallar $P(Y>2x)$ integrando hasta el cruce $x=2/3$ de $y=2x$ con $y=2-x$; restar de 1 | $P(Y\le 2x) = 1 - \int_0^{2/3}\int_{2x}^{2-x}3x\,dy\,dx$ |
| f) | Probabilidad condicional de evento sobre rectas — partición del dominio | Aplicar $P(A\|B) = P(A\cap B)/P(B)$; región $2x\le y\le 3x$ se parte en $[0,1/2]$ y $[1/2,2/3]$ | $P(A\|B) = \frac{P(2x\le Y\le 3x)}{P(Y\ge 2x)} = \frac{7/36}{4/9}$ |
| g) | Esperanza matemática y varianza desde densidad marginal | Usar $f_X(x)=6x(1-x)$; calcular $E[X]$, $E[X^2]$, luego $VAR[X]=E[X^2]-(E[X])^2$ | $E[X]=\int_0^1 x\cdot f_X(x)\,dx$; $VAR[X]=E[X^2]-\mu_X^2$ |

---

### PRÁCTICA Nº2 — Análisis por ejercicio

#### E1 — Normalización + Densidad marginal de $X$ (dominio infinito)

**Función:** $f_{X,Y}(x,y) = \frac{k}{(1+x+y)^4}$ para $x\ge 0,\; y\ge 0$

| Tema específico | Procedimiento | Fórmula clave |
|-----------------|--------------|---------------|
| Normalización de densidad conjunta en dominio no acotado | Integral impropia doble en $[0,\infty)\times[0,\infty)$; resolver con sustitución o integración sucesiva | $\int_0^\infty\int_0^\infty \frac{k}{(1+x+y)^4}\,dy\,dx = 1$ |
| Densidad marginal de $X$ — dominio semi-infinito | Integrar en $y$ de $0$ a $\infty$; resultado es función solo de $x$ | $f_X(x)=\int_0^\infty \frac{k}{(1+x+y)^4}\,dy$ |

**Temas:** normalización con dominio infinito, integral impropia, densidad marginal con límite $\infty$.

---

#### E2 — Independencia estadística en región triangular $u+v\le 1$

**Función:** $f_{U,V}(u,v) = 24uv$ para $u\ge 0,\; v\ge 0,\; u+v\le 1$

| Tema específico | Procedimiento | Fórmula clave |
|-----------------|--------------|---------------|
| Densidad marginal de $U$ con límite superior variable | Integrar en $v$ de $0$ a $1-u$ | $f_U(u)=\int_0^{1-u}24uv\,dv$ |
| Densidad marginal de $V$ con límite superior variable | Integrar en $u$ de $0$ a $1-v$ | $f_V(v)=\int_0^{1-v}24uv\,du$ |
| Independencia estadística — verificación por producto | Comparar $f_{U,V}$ con $f_U(u)\cdot f_V(v)$ en región válida | $f_{U,V}\stackrel{?}{=}f_U\cdot f_V$ solo si factoriza Y los dominios coinciden |

**Alerta clave:** en región triangular ($u+v\le 1$) la condición de independencia es más estricta — el dominio conjunto NO es producto cartesiano de los dominios individuales, por lo tanto $U$ y $V$ **no son independientes** incluso si la función factoriza algebraicamente.

**Temas:** densidades marginales con límite variable, independencia estadística, dominio triangular.

---

#### E3 — Independencia + Varianza de suma $X+Y$ en región cuadrada

**Función:** $f_{X,Y}(x,y) = 4xy$ para $0\le x\le 1,\; 0\le y\le 1$

| Tema específico | Procedimiento | Fórmula clave |
|-----------------|--------------|---------------|
| Independencia estadística — región rectangular (caso favorable) | Factorizar $f_{X,Y}=4xy=(2x)(2y)$; verificar que $f_X(x)=2x$ y $f_Y(y)=2y$ | $f_{X,Y}=f_X(x)\cdot f_Y(y)$ ✓ |
| Esperanza $E[X]$ y $E[Y]$ desde marginales | Calcular con $f_X(x)=2x$ y $f_Y(y)=2y$ | $E[X]=\int_0^1 x\cdot 2x\,dx$ |
| Segundo momento $E[X^2]$, $E[Y^2]$ | Necesario para varianzas individuales | $E[X^2]=\int_0^1 x^2\cdot 2x\,dx$ |
| Covarianza $COV[X,Y]$ — variables independientes | Si son independientes, $COV=0$ | $COV[X,Y]=E[XY]-\mu_X\mu_Y=0$ si independientes |
| Varianza de la suma $VAR[X+Y]$ | Aplicar fórmula con covarianza nula | $VAR[X+Y]=VAR[X]+VAR[Y]+2COV[X,Y]$ |

**Temas:** independencia en región rectangular, densidades marginales simples, varianza de suma, covarianza entre variables independientes.

---

#### E4 — Varianza de $W=X+Y$ con densidad uniforme en triángulo

**Función:** $f_{X,Y}(x,y) = 2$ para $x\ge 0,\; y\ge 0,\; x+y\le 1$

| Tema específico | Procedimiento | Fórmula clave |
|-----------------|--------------|---------------|
| Densidad marginal de $X$ con dominio triangular | Integrar en $y$ de $0$ a $1-x$ | $f_X(x)=\int_0^{1-x}2\,dy=2(1-x)$ |
| Densidad marginal de $Y$ con dominio triangular | Integrar en $x$ de $0$ a $1-y$ | $f_Y(y)=\int_0^{1-y}2\,dx=2(1-y)$ |
| $E[X]$, $E[Y]$, $E[X^2]$, $E[Y^2]$ desde marginales | Integrar con las densidades marginales obtenidas | $E[X]=\int_0^1 x\cdot 2(1-x)\,dx$ |
| $E[XY]$ desde densidad conjunta | Integral doble sobre región triangular | $E[XY]=\int_0^1\int_0^{1-x}xy\cdot 2\,dy\,dx$ |
| Covarianza $COV[X,Y]$ — variables NO independientes | Calcular explícitamente porque dominio triangular implica dependencia | $COV[X,Y]=E[XY]-\mu_X\mu_Y$ |
| Varianza de $W=X+Y$ con covarianza no nula | Aplicar fórmula completa | $VAR[X+Y]=VAR[X]+VAR[Y]+2COV[X,Y]$ |

**Temas:** densidad uniforme en triángulo, densidades marginales con límite variable, $E[XY]$ integral doble, covarianza no nula, varianza de suma.

---

#### E5 — PDF conjunta de 4 variables + probabilidad + marginal

**Función:** $f_{W,X,Y,Z}(w,x,y,z) = 16wxyz$ para $0\le w,x,y,z\le 1$

| Inciso | Tema específico | Procedimiento | Fórmula clave |
|--------|----------------|--------------|---------------|
| a) | Probabilidad en región producto con 4 variables | Factorizar la integral cuádruple porque el dominio es rectangular y la función factoriza | $P=\int_0^{1/2}4w\,dw\cdot\int_0^{3/4}4y\,dy$ (factorización) |
| b) | Densidad marginal de $W$ con 3 variables integradas | Integrar en $x$, $y$, $z$ sobre sus dominios $[0,1]$ | $f_W(w)=\int_0^1\int_0^1\int_0^1 16wxyz\,dx\,dy\,dz$ |

**Temas:** PDF conjunta de 4 variables, factorización de integral múltiple, densidad marginal por integración múltiple, independencia implícita en región rectangular.

---

#### E6 — Región con valor absoluto + marginal + probabilidad + esperanza

**Función:** $f_{X,Y}(x,y) = 1$ para $-1\le x\le 1,\; 0\le y\le 1,\; |x|\ge y$

| Inciso | Tema específico | Procedimiento | Fórmula clave |
|--------|----------------|--------------|---------------|
| a) | Identificación y dibujo de región con valor absoluto | Descomponer $|x|\ge y$ en $x\ge y$ (para $x>0$) y $-x\ge y$ (para $x<0$); dos triángulos simétricos | Región: $\{(x,y): -1\le x\le 1,\; 0\le y\le|x|\}$ |
| b) | Densidad marginal de $X$ con límite superior $|x|$ | Integrar en $y$ de $0$ a $|x|$ para cada signo de $x$ | $f_X(x)=\int_0^{|x|}1\,dy=|x|$ para $-1\le x\le 1$ |
| c) | Probabilidad $P(X>0)$ desde densidad marginal | Integrar $f_X(x)$ en $[0,1]$ | $P(X>0)=\int_0^1|x|\,dx=\frac{1}{2}$ |
| d) | Esperanza $E[X]$ con densidad marginal simétrica | Verificar si $x\cdot f_X(x)=x\cdot|x|$ es función impar → $E[X]=0$ por simetría | $E[X]=\int_{-1}^1 x\cdot|x|\,dx=0$ |

**Temas:** región definida por valor absoluto, descomposición de dominio por signo, densidad marginal con límite $|x|$, probabilidad unilateral, esperanza con función impar.

---

#### E7 — Densidad condicional dado evento $A: x+y\le 1$

**Función:** $f_{X,Y}(x,y) = 6e^{-(2x+3y)}$ para $x\ge 0,\; y\ge 0$

| Tema específico | Procedimiento | Fórmula clave |
|-----------------|--------------|---------------|
| Probabilidad del evento $A: x+y\le 1$ | Integral doble sobre región triangular cortada por $x+y\le 1$ | $P[A]=\int_0^1\int_0^{1-x}6e^{-(2x+3y)}\,dy\,dx$ |
| Densidad condicional dado evento $B$ con $P[B]>0$ | Dividir $f_{X,Y}$ entre $P[A]$ dentro de la región; 0 fuera | $f_{X,Y|A}(x,y)=\frac{f_{X,Y}(x,y)}{P[A]}$ para $(x,y)\in A$ |
| Verificación de normalización de densidad condicional | La integral de $f_{X,Y|A}$ sobre $A$ debe ser 1 | $\iint_A f_{X,Y|A}\,dx\,dy=1$ ✓ |

**Temas:** densidad exponencial bivariada, probabilidad de evento en región triangular, densidad condicional dado evento $B$, normalización de densidad condicional.

---

### TABLA RESUMEN GENERAL — PRÁCTICA Nº2

| Ejercicio | Tema principal | Temas secundarios | Fórmulas clave |
|-----------|---------------|-------------------|----------------|
| **P2-E1** | Normalización con dominio infinito | Integral impropia, densidad marginal semi-infinita | $\int_0^\infty\int_0^\infty f\,dy\,dx=1$; $f_X(x)=\int_0^\infty f_{X,Y}\,dy$ |
| **P2-E2** | Independencia estadística en triángulo | Densidades marginales con límite $1-u$, dominio no rectangular | $f_U\cdot f_V \ne f_{U,V}$ por dominio triangular |
| **P2-E3** | Independencia en región rectangular + varianza de suma | Factorización de PDF, covarianza nula, $VAR[X+Y]$ | $VAR[X+Y]=VAR[X]+VAR[Y]$ (independientes) |
| **P2-E4** | Varianza de $W=X+Y$ con covarianza no nula | Densidad uniforme triangular, $E[XY]$, $COV[X,Y]$ | $VAR[X+Y]=VAR[X]+VAR[Y]+2COV[X,Y]$ |
| **P2-E5** | PDF de 4 variables + probabilidad conjunta + marginal | Factorización integral cuádruple, densidad marginal múltiple | $P=\prod_i P_i$ si independientes; $f_W=\int\int\int f\,dx\,dy\,dz$ |
| **P2-E6** | Región con valor absoluto + marginal + $E[X]$ | Descomposición por signo, $f_X(x)=|x|$, función impar | $f_X(x)=\int_0^{|x|}f_{X,Y}\,dy$; $E[X]=\int x f_X\,dx=0$ |
| **P2-E7** | Densidad condicional dado evento $A$ | PDF exponencial bivariada, $P[A]$ en triángulo, normalización | $f_{X,Y|A}=f_{X,Y}/P[A]$ para $(x,y)\in A$ |
| **E1 resuelto** | Densidad conjunta triangular — ejercicio completo | Normalización, marginales partidas, independencia, $P$ con curva, complemento, condicional de evento, $E[X]$, $VAR[X]$ | Todas las fórmulas del formulario aplicadas |

---

### PATRONES Y ALERTAS PARA RESOLVER EJERCICIOS

> Claude debe tener estos puntos en mente al revisar o resolver cualquier ejercicio de la práctica:

**Sobre la región de integración:**
- Dominio **rectangular** ($a\le x\le b$, $c\le y\le d$): límites de marginales constantes, independencia posible.
- Dominio **triangular** ($x+y\le 1$ o similar): límites de marginales **variables**, independencia generalmente **no se cumple**.
- Dominio con **valor absoluto** ($|x|\ge y$): descomponer en dos subregiones según signo de $x$.
- Dominio **infinito** ($x\ge 0$, $y\ge 0$ sin cota): usar integrales impropias.

**Sobre independencia:**
- Verificar SIEMPRE con el dominio conjunto, no solo con la forma algebraica.
- Dominio triangular: NO hay independencia aunque $f_{X,Y}$ factorize algebraicamente.
- Dominio rectangular: puede haber independencia si $f_{X,Y}=g(x)\cdot h(y)$.

**Sobre varianza de suma:**
- $X,Y$ independientes → $COV=0$ → $VAR[X+Y]=VAR[X]+VAR[Y]$.
- $X,Y$ dependientes → calcular $E[XY]$ por integral doble → $COV=E[XY]-\mu_X\mu_Y$.

**Sobre densidad condicional:**
- Dado evento $B$: dividir $f_{X,Y}$ entre $P[B]$ dentro de la región, 0 fuera.
- Calcular $P[B]$ como integral doble de $f_{X,Y}$ sobre la región $B$.
