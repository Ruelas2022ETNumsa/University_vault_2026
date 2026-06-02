# Números reales y desigualdades

## Axiomas de cuerpo de los números reales

Sea $a,b,c \in \mathbb{R}$.

1. **Clausura**
- $a+b \in \mathbb{R}$
- $a\cdot b \in \mathbb{R}$

Es decir, la suma y el producto de dos números reales siguen siendo números reales.

2. **Conmutatividad**
- Suma
$a+b=b+a$


#### Producto

$$
a\cdot b=b\cdot a
$$

El orden de los operandos no altera el resultado.

### 3. Asociatividad

#### Suma

$$
(a+b)+c=a+(b+c)
$$

#### Producto

$$
(a\cdot b)\cdot c=a\cdot(b\cdot c)
$$

La forma de agrupar los términos no modifica el resultado.

### 4. Existencia de neutros

#### Neutro aditivo

Existe un número real $0$ tal que:

$$
a+0=a
$$

para todo $a\in\mathbb{R}$.

#### Neutro multiplicativo

Existe un número real $1$ tal que:

$$
a\cdot1=a
$$

para todo $a\in\mathbb{R}$.

### 5. Existencia de negativos

Para todo $a\in\mathbb{R}$ existe un número real $-a$ tal que:

$$
a+(-a)=0
$$

El número $-a$ se denomina opuesto o inverso aditivo de $a$.

### 6. Existencia de inversos

Para todo $a\in\mathbb{R}$, con $a\neq0$, existe un número real $a^{-1}$ tal que:

$$
a\cdot a^{-1}=1
$$

equivalentemente,

$$
a^{-1}=\frac{1}{a}
$$

El número $a^{-1}$ se denomina inverso multiplicativo o recíproco de $a$.

### 7. Distributividad

La multiplicación distribuye respecto de la suma:

$$
a(b+c)=ab+ac
$$

y de forma equivalente,

$$
(a+b)c=ac+bc
$$

---

## Axiomas de igualdad

Sea $a,b,c\in\mathbb{R}$.

### 1. Reflexividad

Todo número es igual a sí mismo:

$$
a=a
$$

### 2. Simetría

Si dos números son iguales, el orden puede invertirse:

$$
a=b \implies b=a
$$

### 3. Transitividad

Si un número es igual a un segundo y este a un tercero, entonces el primero es igual al tercero:

$$
a=b \land b=c \implies a=c
$$

---

## Definiciones

Las operaciones de resta y división no se consideran operaciones primitivas; se definen a partir de la suma y la multiplicación.

### Resta

La resta de $a$ a $b$ se define como:

$$
b-a=b+(-a)
$$

donde $-a$ es el opuesto aditivo de $a$.

### División

La división de $b$ entre $a$, con $a\neq0$, se define como:

$$
\frac{b}{a}=b\cdot a^{-1}
$$

donde

$$
a^{-1}=\frac{1}{a}
$$

es el inverso multiplicativo de $a$.