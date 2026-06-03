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

1. **Simetría**: $|-x|=|x|$
2. **No negatividad**: $|x|\ge 0$
3. **Producto**: $|x\cdot y|=|x||y|$
4. **Cociente**: $\left|\dfrac{x}{y}\right|=\dfrac{|x|}{|y|}$, $\quad$ $y\neq0$
5. **Ecuación de valor absoluto**: $(|x|=a \land a\ge0)\Rightarrow$ $(x=a \lor x=-a)$ $\quad$ $(x=\pm a)$
6. **Valor absoluto de una potencia par**: $|x^2|=|x|^2=x^2$
7. **Raíz cuadrada principal**: $\sqrt{x^2}=|x|$
8. **Desigualdad de valor absoluto.**
	- **(caso menor que)**: $(|x|<a \land a>0)$ $\Rightarrow -a<x<a$
	- **(caso mayor que)**: $(|x|>a \land a>0)$ $\Rightarrow (x>a \lor x<-a)$    
9.  **Desigualdad triangular**: $|x+y|\le |x|+|y|$
10. **Desigualdad triangular inversa**: $\bigl||x|-|y|\bigr| \le |x-y|$
11. **Desigualdad de Schwarz**: $|x\cdot y|\le |x||y|$
 
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