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
---
---


# Capítulo 0

## Números reales y desigualdades

### Axiomas de cuerpo de los números reales
#### Clausura
#### Conmutatividad
#### Asociatividad
#### Existencia de neutros
#### Existencia de negativos
#### Existencia de inversos
#### Distributividad

### Axiomas de igualdad
#### Reflexividad
#### Simetría
#### Transitividad

### Definiciones
#### Resta
#### División

### Observaciones sobre tipos de igualdad
#### Igualdad
#### Ecuación
#### Identidad

### Teoremas sobre números reales
#### Leyes de cancelación
#### Solución de ecuaciones lineales
#### Producto por cero
#### Regla del producto nulo
#### Propiedades de signos
#### Operaciones con fracciones







### Axiomas de orden de los números reales
#### Clausura de los positivos
#### Tricotomía
#### Exclusión del cero
#### Relación de orden
##### Mayor que
##### Menor que
##### Mayor o igual que
##### Menor o igual que
##### Positivos y negativos

### Teoremas de desigualdades e inecuaciones
#### Tricotomía
#### Transitividad
#### Monotonía
#### Multiplicación por positivos
#### Multiplicación por negativos
#### Cuadrados no negativos
#### Inversos multiplicativos y orden

### Recta real e intervalos
#### Correspondencia entre ℝ y la recta real
#### Intervalos cerrados
#### Intervalos semiabiertos
#### Intervalos abiertos
#### Semirrectas

### Valor absoluto
#### Definición
#### Interpretación geométrica
#### Propiedades del valor absoluto
##### No negatividad
##### Producto
##### Cociente
##### Ecuación |x| = a
##### Potencias
##### Raíz cuadrada
##### Intervalo interior
##### Intervalo exterior
##### Desigualdad triangular
##### Desigualdad de Schwarz

### Resolución de inecuaciones en una variable
#### Inecuaciones de primer grado
##### Forma general
##### Conjunto solución
##### Ejemplo

### Método de signos para resolver inecuaciones
#### Forma general
#### Paso 1: Comparar con cero
#### Paso 2: Factorizar
#### Paso 3: Representar en la recta real
#### Paso 4: Prueba de signos
#### Paso 5: Repetición por intervalos
#### Paso 6: Unión de intervalos solución

### Ejemplos de resolución de inecuaciones
#### Ejemplo A
#### Ejemplo B
#### Ejemplo C
#### Ejemplo D
#### Ejemplo E
#### Ejemplo F

# Capítulo I

## Funciones reales

### Definición de función
#### Dominio
#### Codominio
#### Regla de correspondencia

### Lenguaje matemático de funciones

### Notación funcional
#### y = f(x)
#### f : D → R

### Notación conjuntista

### Ejemplos de funciones