# Números reales y desigualdades

## Axiomas de cuerpo de los números reales

--- start-multi-column: cornell-001
```column-settings
number of columns: 2
column size: [60%, 40%]
border: off
```

📝 **Desarrollo**

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
	- Neutro aditivo: $\exists\,0\in\mathbb{R}: a+0=a$
	- Neutro multiplicativo: $\exists\,1\in\mathbb{R}: a\cdot1=a$
5. **Existencia de negativos**
	- $\forall\,a\in\mathbb{R},\ \exists\,(-a)\in\mathbb{R}: a+(-a)=0$
6. **Existencia de inversos**
	- $\forall\,a\in\mathbb{R},\ a\neq0,\ \exists\,a^{-1}\in\mathbb{R}: a\cdot a^{-1}=1$
7. **Distributividad**
	- $a(b+c)=ab+ac$

--- end-column ---

🔑 **Claves**

- $\mathbb{R}$ es un **cuerpo** — cerrado bajo suma y producto
- Neutros: $0$ para suma, $1$ para producto
- Todo real tiene opuesto $(-a)$; todo real no nulo tiene inverso $a^{-1}$
- Distributividad conecta suma y producto
- Resta y división **no** son axiomas — se derivan

--- end-multi-column

> **Resumen:** Los 7 axiomas de cuerpo garantizan que $\mathbb{R}$ tiene operaciones de suma y producto bien definidas, con neutros, inversos y distributividad.

---

## Axiomas de igualdad

--- start-multi-column: cornell-002
```column-settings
number of columns: 2
column size: [60%, 40%]
border: off
```

📝 **Desarrollo**

Sea $a,b,c\in\mathbb{R}$.
1. **Reflexividad**
	- $a=a$
2. **Simetría**
	- $a=b \implies b=a$
3. **Transitividad**
	- $a=b \land b=c \implies a=c$

--- end-column ---

🔑 **Claves**

- Reflexividad: todo elemento es igual a sí mismo
- Simetría: la igualdad no tiene dirección
- Transitividad: base de las cadenas de igualdades en demostraciones
- Estos 3 axiomas definen una **relación de equivalencia**

--- end-multi-column

> **Resumen:** La igualdad en $\mathbb{R}$ es reflexiva, simétrica y transitiva — una relación de equivalencia sobre los reales.

---

## Definiciones

--- start-multi-column: cornell-003
```column-settings
number of columns: 2
column size: [60%, 40%]
border: off
```

📝 **Desarrollo**

1. **Resta**
	- $b-a=b+(-a)$
2. **División**
	- $\dfrac{b}{a}=b\cdot a^{-1}$, con $a\neq0$

--- end-column ---

🔑 **Claves**

- Restar $a$ ≡ sumar $(-a)$
- Dividir por $a$ ≡ multiplicar por $a^{-1}$
- $a\neq0$ es **condición obligatoria** para la división
- Son operaciones **derivadas**, no primitivas

--- end-multi-column

> [!note]
> La resta y la división no son operaciones fundamentales.
> - La resta se define a partir de la suma y del opuesto aditivo.
> - La división se define a partir de la multiplicación y del inverso multiplicativo.

> **Resumen:** Resta y división son abreviaciones de suma con opuesto y producto con inverso, respectivamente.

---

## Observaciones

Es importante distinguir entre una igualdad, una ecuación y una identidad.

| Tipo                  | Ejemplo            | Descripción                                   | Alcance                                                                    |
|:--------------------- |:------------------ |:--------------------------------------------- |:-------------------------------------------------------------------------- |
| **Igualdad numérica** | $2^3=8$            | Afirmación entre valores numéricos concretos. | Puede ser verdadera o falsa.                                               |
| **Ecuación**          | $x^2-4=0$          | Contiene incógnitas.                          | Verdadera únicamente para los valores que pertenecen al conjunto solución. |
| **Identidad**         | $x^2-4=(x-2)(x+2)$ | Equivalencia algebraica.                      | Verdadera para todo valor del dominio.                                     |

### Ejemplos

- **Igualdad numérica :**  $2^3=8$

- **Ecuación :** $x^2-4=0$
	Conjunto solución:  $x=\pm2$

- **Identidad :** $x^2-4=(x-2)(x+2)$
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

$a+b+(-a)=a+c+(-a)$ *Sumando $(-a)$ a ambos lados:*

$(a+(-a))+b=(a+(-a))+c$  *Por asociatividad:*

$0+b=0+c$  *existe el negativo $a+(-a)=0$:*

$b=c$  *Por existencia del neutro aditivo*

---

## Axiomas de orden de los números reales

--- start-multi-column: cornell-004
```column-settings
number of columns: 2
column size: [60%, 40%]
border: off
```

📝 **Desarrollo**

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

--- end-column ---

🔑 **Claves**

- $\mathbb{R}^{+}$ es el conjunto **primitivo** del orden
- Tricotomía: para $a\neq0$, exactamente uno de $a$ o $-a$ es positivo
- El cero **no** es positivo ni negativo
- Clausura: suma y producto de positivos es positivo
- El orden $<$ y $>$ se **definen** a partir de $\mathbb{R}^{+}$, no se asumen

--- end-multi-column

> **Resumen:** El orden en $\mathbb{R}$ se construye desde $\mathbb{R}^{+}$: un real es positivo, negativo, o cero — nunca dos a la vez.

---

### Definiciones

--- start-multi-column: cornell-005
```column-settings
number of columns: 2
column size: [60%, 40%]
border: off
```

📝 **Desarrollo**

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

--- end-column ---

🔑 **Claves**

- $a>b$ ≡ $a-b$ es positivo
- $a<b$ ≡ $b-a$ es positivo
- $\ge$ y $\le$ incluyen la igualdad
- Positivo $\iff$ mayor que cero; negativo $\iff$ menor que cero
- Las 4 relaciones se derivan de $\mathbb{R}^{+}$

--- end-multi-column

> **Resumen:** Las relaciones de orden $<$, $>$, $\le$, $\ge$ se definen formalmente mediante restas y pertenencia a $\mathbb{R}^{+}$.


---

## Teoremas de desigualdades e inecuaciones

--- start-multi-column: cornell-006
```column-settings
number of columns: 2
column size: [60%, 40%]
border: off
```

📝 **Desarrollo**

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

--- end-column ---

🔑 **Claves**

- Tricotomía: exactamente **una** de las 3 relaciones es verdadera
- Monotonía: negar **invierte** la desigualdad
- Multiplicar por negativo **invierte** la desigualdad — error frecuente
- $a^2\ge0$ siempre — clave para demostrar desigualdades
- $a>0 \iff a^{-1}>0$: el inverso conserva el signo

--- end-multi-column

> **Resumen:** Sumar a ambos lados conserva la desigualdad; multiplicar por negativo la invierte.




---

## La recta real e intervalos

Existe correspondencia biunívoca (uno a uno) entre el conjunto $\mathbb{R}$ y una recta a escala llamada **la recta real**.

> [!note]  
> Un intervalo es un subconjunto de la recta real.

1. **Intervalo cerrado**: $[a,b]=\{x\mid a\le x\le b\}$

```desmos-graph
left=2; right=5; bottom=-1; top=1;
width=350; height=120;
---
y=0 \{3<=x<=4\}|#ff7b7b

(3,0)|label:a|#ff7b7b
(4,0)|label:b|#ff7b7b
```

2. **Intervalo semiabierto por la izquierda**: $]a,b]=\{x\mid a<x\le b\}$

```desmos-graph
left=2; right=5; bottom=-1; top=1;
width=350; height=120;
---
y=0 \{3<x<=4\}|#ff7b7b

(3,0)|OPEN|label:a|#ff7b7b
(4,0)|label:b|#ff7b7b
```

3. **Intervalo abierto**: $]a,b[=\{x\mid a<x<b\}$

```desmos-graph
left=2; right=5; bottom=-1; top=1;
width=350; height=120;
---
y=0 \{3<x<4\}|#ff7b7b

(3,0)|OPEN|label:a|#ff7b7b
(4,0)|OPEN|label:b|#ff7b7b
```

4. **Semirrecta hacia $+\infty$**: $]a,+\infty[=\{x\mid x>a\}$

```desmos-graph
left=0; right=8; bottom=-1; top=1;
width=350; height=120;
---
y=0 \{3<x<7\}|#ff7b7b
y=0 \{x>7\}|DOTTED|#ff7b7b

(3,0)|OPEN|label:a|#ff7b7b
```

5. **Semirrecta desde $-\infty$**: $]-\infty,b[=\{x\mid x<b\}$

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