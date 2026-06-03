# Números reales y desigualdades

## Axiomas de cuerpo de los números reales

Sea $a,b,c \in \mathbb{R}$.

1. **Clausura**
	- $a+b \in \mathbb{R}$
	- $a\cdot b \in \mathbb{R}$

2. **Conmutatividad**
	- Suma: $a+b=b+a$
	- Producto: $a\cdot b=b\cdot a$

3. **Asociatividad**
	- Suma: $(a+b)+c=a+(b+c)$
	- Producto: $(a\cdot b)\cdot c=a\cdot(b\cdot c)$

4. **Existencia de neutros**
	- Neutro aditivo:
	  $\exists\,0\in\mathbb{R}: a+0=a$
	- Neutro multiplicativo:
	  $\exists\,1\in\mathbb{R}: a\cdot1=a$

5. **Existencia de negativos**
	- $\forall\,a\in\mathbb{R},\ \exists\,(-a)\in\mathbb{R}:$
	  $a+(-a)=0$

6. **Existencia de inversos**
	- $\forall\,a\in\mathbb{R},\ a\neq0,\ \exists\,a^{-1}\in\mathbb{R}:$
	  $a\cdot a^{-1}=1$

7. **Distributividad**
	- $a(b+c)=ab+ac$

---

## Axiomas de igualdad

Sea $a,b,c\in\mathbb{R}$.

1. **Reflexividad**
	- $a=a$

2. **Simetría**
	- $a=b \implies b=a$

3. **Transitividad**
	- $a=b \land b=c \implies a=c$

---

## Definiciones

1. **Resta**
	- $b-a=b+(-a)$

2. **División**
	- $\dfrac{b}{a}=b\cdot a^{-1}$, con $a\neq0$

> [!note]
> La resta y la división no son operaciones fundamentales.
> - La resta se define a partir de la suma y del opuesto aditivo.
> - La división se define a partir de la multiplicación y del inverso multiplicativo.

---

## Observaciones

Es importante distinguir entre una igualdad, una ecuación y una identidad.

| Tipo | Ejemplo | Descripción | Alcance |
|:---|:---|:---|:---|
| **Igualdad numérica** | $2^3=8$ | Afirmación entre valores numéricos concretos. | Puede ser verdadera o falsa. |
| **Ecuación** | $x^2-4=0$ | Contiene incógnitas. | Verdadera únicamente para los valores que pertenecen al conjunto solución. |
| **Identidad** | $x^2-4=(x-2)(x+2)$ | Equivalencia algebraica. | Verdadera para todo valor del dominio. |

### Ejemplos

- **Igualdad numérica**

	$2^3=8$

- **Ecuación**

	$x^2-4=0$

	Conjunto solución:

	$x=\pm2$

- **Identidad**

	$x^2-4=(x-2)(x+2)$

	Se verifica para todo $x\in\mathbb{R}$.

---
## Teoremas sobre números reales

Sea $a,b,c,d,x \in \mathbb{R}$.

1. **Ley de cancelación aditiva**
	- $a+b=a+c \Rightarrow b=c$
2. **Ley de cancelación multiplicativa**
	- $(a\cdot b=a\cdot c)\land a\neq0 \Rightarrow b=c$
3. **Solución de ecuaciones aditivas**
	- $a+x=b \Rightarrow x=b-a$
4. **Solución de ecuaciones multiplicativas**
	- $(a\cdot x=b)\land a\neq0 \Rightarrow x=\dfrac{b}{a}$
5. **Producto por cero**
	- $a\cdot0=0$
6. **Regla del producto nulo**
	- $a\cdot b=0 \Rightarrow (a=0 \lor b=0)$
7. **Igualdad de opuestos**
	- $a=b \Rightarrow -a=-b$
8. **Producto por un negativo**
	- $a(-b)=-(ab)$
9. **Producto de negativos**
	- $(-a)(-b)=ab$
10. **Suma de fracciones con igual denominador**
	- $\dfrac{a}{b}+\dfrac{c}{b}=\dfrac{a+c}{b}$
11. **Suma de fracciones con distinto denominador**
	- $\dfrac{a}{b}+\dfrac{c}{d}=\dfrac{ad+cb}{bd}$
12. **Producto de fracciones**
	- $\left(\dfrac{a}{b}\right)\left(\dfrac{c}{d}\right)=\dfrac{ac}{bd}$
13. **División de fracciones**
	- $\dfrac{\frac{a}{b}}{\frac{c}{d}}=\dfrac{ad}{cb}$

### Demostración de la ley de cancelación aditiva

Hipótesis: $a+b=a+c$

$a+b+(-a)=a+c+(-a)$ //Sumando $(-a)$ a ambos lados:

$(a+(-a))+b=(a+(-a))+c$ //Por asociatividad:

$0+b=0+c$ //existe el negativo $a+(-a)=0$:

$b=c$ //Por existencia del neutro aditivo

---

## Axiomas de orden de los números reales

Sea $a,b \in \mathbb{R}$.

1. **Clausura de los positivos**
	Si $a,b \in \mathbb{R}^{+}$, entonces:
	- $a+b \in \mathbb{R}^{+}$
	- $ab \in \mathbb{R}^{+}$
2. **Tricotomía**
	Para todo $a\neq0$:
	- $a\in\mathbb{R}^{+}$ ó $-a\in\mathbb{R}^{+}$
3. **Exclusión del cero**
	- $0\notin\mathbb{R}^{+}$

> [!note]
> Estos axiomas garantizan que el conjunto de los números reales pueda ordenarse sobre una recta numérica.
>
> Ejemplos:
>
> $4>2>1>0>-3$
>
> $-4<-1<1<10$
### Notación
- Reales positivos:
	- $\mathbb{R}^{+}=\{x\in\mathbb{R}:x>0\}$
- Reales negativos:
	- $\mathbb{R}^{-}=\{x\in\mathbb{R}:x<0\}$

---

### Definiciones
1. **Relación de orden**
	- Permite comparar dos números reales y determinar cuál es mayor o menor.
2. **Mayor que**
	- $a>b \iff a-b\in\mathbb{R}^{+}$
3. **Menor que**
	- $a<b \iff b-a\in\mathbb{R}^{+}$
4. **Mayor o igual que**
	- $a\ge b \iff (a>b)\lor(a=b)$
5. **Menor o igual que**
	- $a\le b \iff (a<b)\lor(a=b)$
6. **Positivos y negativos**
	- $a>0 \Rightarrow a$ es positivo.
	- $a<0 \Rightarrow a$ es negativo.

---

## Teoremas de desigualdades e inecuaciones

Sea $a,b,c,x \in \mathbb{R}$.

1. **Tricotomía**
	- $a<b \;\lor\; a=b \;\lor\; a>b$
2. **Transitividad**
	- $a<b \land b<c \Rightarrow a<c$
3. **Monotonía**
	- $a<b \Rightarrow -a>-b$
4. **Despeje aditivo**
	- $a+x<b \Rightarrow x<b-a$
5. **Multiplicación por positivos**
	- $(ab<ac)\land a>0 \Rightarrow b<c$
6. **Multiplicación por negativos**
	- $(ab<ac)\land a<0 \Rightarrow b>c$
7. **Cuadrados no negativos**
	- $a^2\ge0$
8. **Inversos multiplicativos y orden**
	- $a>0 \iff \dfrac{1}{a}>0$

---

## La recta real e intervalos

Existe correspondencia biunívoca (uno a uno) entre el conjunto $\mathbb{R}$ y una recta a escala llamada **la recta real**.

> [!note]  
> Un intervalo es un subconjunto de la recta real.

1. **Intervalo cerrado**: $[a,b]={x\mid a\le x\le b}$

```desmos-graph
left=2; right=5; bottom=-1; top=1;
width=350; height=120;
---
y=0 \{3<=x<=4\}|#ff7b7b

(3,0)|label:a|#ff7b7b
(4,0)|label:b|#ff7b7b
```

2. **Intervalo semiabierto por la izquierda**: $]a,b]={x\mid a<x\le b}$

```desmos-graph
left=2; right=5; bottom=-1; top=1;
width=350; height=120;
---
y=0 \{3<x<=4\}|#ff7b7b

(3,0)|OPEN|label:a|#ff7b7b
(4,0)|label:b|#ff7b7b
```

3. **Intervalo semiabierto por la derecha**: $]a,b[={x\mid a< x<b}$

```desmos-graph
left=2; right=5; bottom=-1; top=1;
width=350; height=120;
---
y=0 \{3<x<4\}|#ff7b7b

(3,0)|OPEN|label:a|#ff7b7b
(4,0)|OPEN|label:b|#ff7b7b
```

4. **Semirrecta hacia $+\infty$**: $]a,+\infty[={x\mid x>a}$

```desmos-graph
left=0; right=8; bottom=-1; top=1;
width=350; height=120;
---
y=0 \{3<x<7\}|#ff7b7b
y=0 \{x>7\}|DOTTED|#ff7b7b

(3,0)|OPEN|label:a|#ff7b7b
```

5. **Semirrecta desde $-\infty$**: $]-\infty,b[={x\mid x<b}$

```desmos-graph
left=-8; right=0; bottom=-1; top=1;
width=350; height=120;
---
y=0 \{x<-7\}|DOTTED|#ff7b7b
y=0 \{-7<x<-3\}|#ff7b7b

(-3,0)|OPEN|label:b|#ff7b7b
```

---

## Valor absoluto (definición)

Sea $a\in\mathbb{R}$.
El **valor absoluto** de un número real $a$, denotado por $|a|$, se define como:

$$  
|a|=  
\begin{cases}  
a, & \text{si } a\ge0\  \\
-a, & \text{si } a<0  
\end{cases}  
$$

> [!note]  
> El valor absoluto representa la distancia de un número al origen en la recta real.  
> Por esta razón, el valor absoluto nunca es negativo.

Ejemplos:
- $|3|=3$
- $|-3|=3$
- $|1.5|=1.5$

---

### Propiedades

Si $x$ y $y$ pertenecen a $\mathbb{R}$:

1. **Simetría**
	- $|-x|=|x|$
2. **No negatividad**
	- $|x|\ge 0$
3. **Producto**
	- $|x\cdot y|=|x||y|$
4. **Cociente**
	- $\left|\dfrac{x}{y}\right|=\dfrac{|x|}{|y|}$, $\quad$ $y\neq0$
5. **Ecuación de valor absoluto**
	- $(|x|=a \land a\ge0)\Rightarrow$ $(x=a \lor x=-a)$ $\quad$ $(x=\pm a)$
6. **Valor absoluto de una potencia par**
	- $|x^2|=|x|^2=x^2$
7. **Raíz cuadrada principal**
	- $\sqrt{x^2}=|x|$
8. **Desigualdad de valor absoluto.**
	- **(caso menor que)**: $(|x|<a \land a>0)$ $\Rightarrow -a<x<a$
	- **(caso mayor que)**: $(|x|>a \land a>0)$ $\Rightarrow (x>a \lor x<-a)$    
9.  **Desigualdad triangular**
	- $|x+y|\le |x|+|y|$
10. **Desigualdad triangular inversa**
	- $\bigl||x|-|y|\bigr| \le |x-y|$
11. **Desigualdad de Schwarz**
	- $|x\cdot y|\le |x||y|$
 
#### Ejemplo
Analizar la V o F de:

$$
\begin{array}{rcl}
-6 & = & -6 \\
4 - 10 & = & 9 - 15
\end{array}
$$

$$
\begin{array}{rcl}
2^2-2\cdot5\left(\dfrac{3}{2}\right)+\left(\dfrac{5}{2}\right)^2
& = &
3^2-3\cdot5\left(\dfrac{2}{2}\right)+\left(\dfrac{5}{2}\right)^2 \\[6pt]
\left(2-\dfrac{5}{2}\right)^2
& = &
\left(3-\dfrac{5}{2}\right)^2
\end{array}
$$

$$
\begin{array}{rcl}
\sqrt{\left(2-\dfrac{5}{2}\right)^2}
& = &
\sqrt{\left(3-\dfrac{5}{2}\right)^2} \\[6pt]
\left|2-\dfrac{5}{2}\right|
& = &
\left|3-\dfrac{5}{2}\right|
\end{array}
$$

$$
\begin{array}{rcl}
\left|-\dfrac{1}{2}\right|
& = &
\left|\dfrac{1}{2}\right| \\[6pt]
\dfrac{1}{2}
& = &
\dfrac{1}{2}
\qquad \checkmark
\end{array}
$$

---

## Solución de inecuaciones en variable real

### Inecuaciones de primer grado

Forma:

$$
ax+b
\begin{cases}
>\\
<\\
\ge\\
\le
\end{cases}
cx+d
$$

donde:

$$
a,b,c,d \in \mathbb{R}
$$

Se recomienda despejar \(x\) con propiedades:

$$
\begin{array}{rcl}
ax-cx & > & d-b \\[4pt]
(a-c)x & > & d-b
\end{array}
$$

Si:

$$
a-c>0
$$

entonces:

$$
x>\dfrac{d-b}{a-c}
$$

**\($C_s$\): conjunto solución de la inecuación**

```desmos-graph
left=2; right=7; bottom=-1; top=1;
width=500; height=120;
---
y=0 \{x>3\}|#ff7b7b
(3,0)|OPEN|label:(d-b)/(a-c)|#ff7b7b
```

$$
C_s:
\left] \frac{d-b}{a-c}, +\infty \right[
=
\left\{ x\in\mathbb{R} \;\middle|\; x>\frac{d-b}{a-c} \right\}
$$

**Ejemplo:** Hallar el $C_s$

$$
\begin{array}{rcl}
(4x-3)^2 & \le & (4x+1)^2 \\[4pt]
16x^2-24x+9 & \le & 16x^2+8x+1 \\[4pt]
-24x+9 & \le & 8x+1 \\[4pt]
-32x+9 & \le & 1 \\[4pt]
-32x & \le & -8 \\[4pt]
x & \ge & \dfrac{1}{4}
\end{array}
$$


```desmos-graph
left=-1; right=6; bottom=-1; top=1;
width=500; height=120;
---
y=0 \{x>=0.25\}|#ff7b7b
(0.25,0)|label:1/4|#ff7b7b
```

$$
C_s:
\left[ \frac{1}{4}, +\infty \right[
=
\left\{ x\in\mathbb{R} \;\middle|\; x\ge\frac{1}{4} \right\}
$$


---

### Método de signos para resolver inecuaciones

Generalizando:

**Método de signos para solución de inecuaciones**

Forma general:

$$
M(x)
\begin{cases}
>\\
<\\
\ge\\
\le
\end{cases}
N(x)
$$

Para resolver se recomiendan los siguientes pasos:

1. Formar una comparación con cero:
$$
\frac{P(x)}{Q(x)} > 0
$$
(o la desigualdad correspondiente).

2. Factorizar totalmente \(P\) y \(Q\):
$$
\frac{
(x-a_1)(x-a_2)\cdots(x-a_k)
}{
(x-b_1)(x-b_2)\cdots(x-b_j)
}
>0
$$

3. Representar en la recta real los valores

$$
a_1,\;a_2,\;\ldots,\;a_k,\;b_1,\;b_2,\;\ldots,\;b_j
$$

quedando definidos \(n\) intervalos:

```desmos-graph
left=-1; right=11; bottom=-1; top=1;
width=350; height=120;
---
y=0 \{0<x<2\}|#ff7b7b
y=0 \{2<x<5\}|#ff7b7b
y=0 \{5<x<8\}|#ff7b7b
y=0 \{8<x<10\}|#ff7b7b

(2,0)|OPEN|label:a_1|#ff7b7b
(5,0)|OPEN|label:a_2|#ff7b7b
(8,0)|OPEN|label:b_1|#ff7b7b
(10,0)|OPEN|label:b_2|#ff7b7b

(1,-0.5)|label:I_1|#2d70b3|hidden
(3,-0.5)|label:I_2|#2d70b3|hidden
(6,-0.5)|label:I_3|#2d70b3|hidden
(9,-0.5)|label:I_4|#2d70b3|hidden


````

Intervalos:

$$  
I_1,;I_2,;I_3,;\ldots,;I_k  
$$

4. **Prueba de signos**
	De $I_1$ se toma un valor cualquiera (no extremo) y se prueban los signos sustituyendo en cada factor.
	
	Ejemplo:
	
	 $\dfrac{(+)(-)(+)}{(-)(+)(+)}=(+) \quad$   o   $\quad \dfrac{(+)(-)(+)}{(-)(+)(-)}=(-)$
	 
	Resultan dos posibilidades:
	- Si la desigualdad es verdadera en el intervalo analizado, entonces: $I_i \subset C_s$
	- Si la desigualdad es falsa en el intervalo analizado, entonces: $I_i \not\subset C_s$

5. Repetir el procedimiento para los demás intervalos: $I_2,;I_3,;\ldots$ 
6. El conjunto solución buscado se obtiene mediante la unión de todos los intervalos que verifican la inecuación:
    $$  C_s=\bigcup I_i  $$
	donde la unión se realiza únicamente sobre los intervalos válidos.

---

### Ejemplos resueltos

#### a) $x^4 \ge 9x^2$

$$
\begin{array}{rcl}
x^4 & \ge & 9x^2 \\[4pt]
x^4-9x^2 & \ge & 0 \\[4pt]
x^2(x^2-9) & \ge & 0 \\[4pt]
x^2(x-3)(x+3) & \ge & 0
\end{array}
$$

- Puntos críticos:
	$$x_1=-3,\quad x_{2,3}=0,\quad x_4=3$$
	
- Prueba
	$I_{1}:$ $x=-10$
	
	$(+)(-)(-)\ge 0\implies (+)\ge 0 \quad \text{verdadero}$
	<BR>

- Tabla de signos:

| Intervalo      | Signo |
| -------------- | ----- |
| $]-\infty,-3[$ | (+)   |
| $]-3,0[$       | (-)   |
| $]0,3[$        | (-)   |
| $]3,+\infty[$  | (+)   |

- Gráfica

```desmos-graph
left=-6; right=6; bottom=-1; top=1;
width=350; height=120;
---
(-4,0.5)|label:V|#2d70b3|hidden
(-2,0.5)|label:F|#2d70b3|hidden
(0,0.5)|label:V|#2d70b3|hidden
(2,0.5)|label:F|#2d70b3|hidden
(4,0.5)|label:V|#2d70b3|hidden

y=0 \{-6<x<=-3\}|#ff7b7b
y=0 \{3<=x<6\}|#ff7b7b

(-3,0)|label:-3|OPEN|#ff7b7b
(0,0)|label:0|OPEN|#ff7b7b
(3,0)|label:3|OPEN|#ff7b7b

(-4,-0.5)|label:I_1|#2d70b3|hidden
(-0.5,-0.5)|label:I_2|#2d70b3|hidden
(0.5,-0.5)|label:I_3|#2d70b3|hidden
(4,-0.5)|label:I_4|#2d70b3|hidden
````




- Prueba de extremos
	$x=-3, 0, 3$  se cumple $0 = 0 \quad \text{verdadero}$ entonces $-3,0,3 \in C_{s}$

```desmos-graph
left=-6; right=6; bottom=-1; top=1;
width=350; height=120;
---
y=0 \{-6<x<=-3\}|#ff7b7b
y=0 \{3<=x<6\}|#ff7b7b

(-3,0)|label:-3|#ff7b7b
(0,0)|label:0|#ff7b7b
(3,0)|label:3|#ff7b7b
````


$$
C_s=
]-\infty,-3]
\cup
\{0\}
\cup
[3,+\infty[
$$















---
---


### Método de signos para resolver inecuaciones

### Ejemplos resueltos

- Inecuaciones polinómicas
- Inecuaciones racionales
- Inecuaciones con valor absoluto
- Inecuaciones con radicales




---
---
---



### Propiedades

---

## Solución de inecuaciones en variable x

### Inecuaciones de primer grado

### Método de signos para solución de inecuaciones

#### Forma general

#### Pasos para resolver por método de signos

### Ejemplos de resolución de inecuaciones

- a)
- b)
- c)
- d)
- e)
- f)

(Estas letras aparecen como ejercicios/ejemplos, no como subtítulos formales.)