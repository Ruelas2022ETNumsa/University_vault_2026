## AXIOMAS DE IGUALDAD

```
cornell
::cue
Propiedades de la igualdad<br>Igualdad · Identidad · Ecuación<br>¿Cuáles son los tres axiomas fundamentales que rigen la relación de igualdad en los números reales?<br>¿En qué se diferencia una ecuación de una identidad matemática?<br>$a = b \land b = c \Rightarrow a = c$<br>ver también: Axiomas de cuerpo

::note
Si $a, b, c \in \mathbb{R}$:

1. **Reflexividad**
	- $a = a$

2. **Simetría**
	- $a = b \Rightarrow b = a$

3. **Transitividad**
	- $(a = b \land b = c) \Rightarrow a = c$

> [!note] Resta y división son solo casos especiales de $+$ y $\cdot$
> - **Resta**: $a - b = a + (-b)$
> - **División**: $\dfrac{a}{b} = a \cdot \dfrac{1}{b} = a \cdot b^{-1}, b \neq 0$

**No confundir:**
- $2^3 = 8 \Rightarrow$ Igualdad $\rightarrow$ Verdad evidente.
- $x^2 - 4 = 0 \Rightarrow$ Ecuación $\rightarrow$ Verdad para algunas "$x$".
- $x^2 - 4 = (x - 2)(x + 2) \Rightarrow$ Identidad $\rightarrow$ Verdad para toda $x \in \mathbb{R}$.
```

> [!summary] La igualdad en $\mathbb{R}$ es una relación de equivalencia (reflexiva, simétrica y transitiva) que permite distinguir entre igualdades numéricas, ecuaciones condicionales e identidades universales.

> [!note] Complemento (Nivel C)
> 
> **Definición formal de Igualdad de Conjuntos** Según Apostol, se dice que dos conjuntos $A$ y $B$ son iguales (o idénticos) si constan exactamente de los mismos elementos, lo cual se denota como $A = B$. Un teorema fundamental derivado de esto es que $A = B$ si y solo si $A \subseteq B$ y $B \subseteq A$.
> 
> **Identidad en Polinomios** En el contexto de funciones reales, dos polinomios son idénticamente iguales si los coeficientes de un polinomio son iguales a los coeficientes correspondientes del otro. Esto implica que la diferencia entre ambos es un polinomio nulo para todo valor de la variable.
> 
> ##### Ej. Identificación de Identidades vs. Ecuaciones
> 
> Determine si las siguientes afirmaciones son verdaderas (identidades) o falsas (ecuaciones condicionales o falsedades):
> 
> a) $\sqrt{a^2 + b^2} = a + b$ $$\begin{array}{rcll} \sqrt{3^2 + 4^2} & = & 3 + 4 & (\text{Valores de prueba: } a=3, b=4) \ \sqrt{9 + 16} & = & 7 & \ 5 & \neq & 7 & (\text{Falso. No es una identidad}) \end{array}$$
> 
> b) $\dfrac{1}{x} + \dfrac{1}{y} = \dfrac{1}{x+y}$ $$\begin{array}{rcll} \dfrac{1}{1} + \dfrac{1}{1} & = & \dfrac{1}{1+1} & (\text{Valores de prueba: } x=1, y=1) \ 2 & \neq & 0.5 & (\text{Falso. Es una falacia algebraica común}) \end{array}$$
> 
> c) $(p - q)^2 = p^2 - q^2$ $$\begin{array}{rcll} (p - q)^2 & = & p^2 - 2pq + q^2 & (\text{Desarrollo correcto}) \ p^2 - 2pq + q^2 & \neq & p^2 - q^2 & (\text{Falso. Solo es cierto si } q=0 \text{ o } p=q) \end{array}$$ _(Fuente: Stewart 7ed, Examen de diagnóstico de álgebra, pág. A2)_.