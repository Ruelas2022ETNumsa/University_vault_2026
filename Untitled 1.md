# Números Reales y Desigualdades

## Axiomas de cuerpo de los números reales

Sean $a,b,c \in \mathbb{R}$.

### A1) Clausura

- $a+b \in \mathbb{R}$
- $a \cdot b \in \mathbb{R}$

### A2) Conmutatividad

- $a+b=b+a$
- $a\cdot b=b\cdot a$

### A3) Asociatividad

- $(a+b)+c=a+(b+c)$
- $(a\cdot b)\cdot c=a\cdot(b\cdot c)$

### A4) Existencia de elementos neutros

- Existe $0\in\mathbb{R}$ tal que

  $$
  a+0=a
  $$

  donde $0$ es el elemento neutro de la suma.

- Existe $1\in\mathbb{R}$ tal que

  $$
  a\cdot 1=a
  $$

  donde $1$ es el elemento neutro del producto.

### A5) Existencia de inversos aditivos

Para todo $a\in\mathbb{R}$ existe $-a\in\mathbb{R}$ tal que

$$
a+(-a)=0
$$

El número $-a$ se denomina **inverso aditivo** de $a$.

### A6) Existencia de inversos multiplicativos

Para todo $a\in\mathbb{R}\setminus\{0\}$ existe $a^{-1}\in\mathbb{R}$ tal que

$$
a\cdot a^{-1}=1
$$

donde

$$
a^{-1}=\frac{1}{a}
$$

es el **inverso multiplicativo** de $a$.

### A7) Distributividad

$$
a(b+c)=ab+ac
$$

---

## Axiomas de igualdad

Sean $a,b,c\in\mathbb{R}$.

### A1) Reflexividad

$$
a=a
$$

### A2) Simetría

$$
a=b \Rightarrow b=a
$$

### A3) Transitividad

$$
(a=b \wedge b=c)\Rightarrow a=c
$$

---

## Definiciones

### Resta

La resta se define como

$$
a-b=a+(-b)
$$

### División

La división se define como

$$
\frac{a}{b}=a\cdot\frac{1}{b}=a\cdot b^{-1},
\qquad b\neq 0
$$

---

## Observaciones

### Igualdad numérica

$$
2^3=8
$$

Es una igualdad verdadera.

### Ecuación

$$
x^2-4=0
$$

Es verdadera únicamente para algunos valores de $x$.

### Identidad

$$
x^2-4=(x-2)(x+2)
$$

Es verdadera para todo $x\in\mathbb{R}$.

---

## Teoremas básicos

Sean $a,b,c,x\in\mathbb{R}$.

### 1. Ley de cancelación para la suma

$$
a+b=a+c \Rightarrow b=c
$$

### 2. Ley de cancelación para el producto

$$
(a\cdot b=a\cdot c)\wedge a\neq 0
\Rightarrow
b=c
$$

### 3. Resolución de ecuaciones lineales aditivas

$$
a+x=b
\Rightarrow
x=b-a
$$

### 4. Resolución de ecuaciones lineales multiplicativas

$$
(a\cdot x=b)\wedge a\neq 0
\Rightarrow
x=\frac{b}{a}
$$

### 5. Producto por cero

$$
a\cdot 0=0
$$

### 6. Propiedad del producto nulo

$$
a\cdot b=0
\Rightarrow
(a=0 \vee b=0)
$$

### 7. Opuesto de una igualdad

$$
a=b
\Rightarrow
-a=-b
$$

### 8. Producto por un número negativo

$$
a(-b)=-(ab)
$$

### 9. Producto de dos números negativos

$$
(-a)(-b)=ab
$$

### 10. Suma de fracciones con igual denominador

$$
\frac{a}{b}+\frac{c}{b}
=
\frac{a+c}{b},
\qquad b\neq 0
$$