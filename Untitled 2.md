Este ejercicio se identifica como una **Cadena de Markov en tiempo discreto** porque presenta un número finito de estados (comprar o no comprar), probabilidades de transición constantes en el tiempo y la propiedad de que el estado futuro depende únicamente del estado actual.

### Diagrama de la Cadena de Markov

```tikz
\begin{document}
\begin{tikzpicture}
% Definición de estados (N=2, posicionamiento en línea horizontal)
\node[draw,circle,thick,color=orange] (C) at (2,6) {C};
\node[draw,circle,thick,color=pink] (NC) at (10,6) {NC};

% Bucles (hacia afuera)
\draw[->,ultra thick,orange] (C) .. controls (0,8) and (0,4) .. node[left] {$0.8$} (C);
\draw[->,ultra thick,pink] (NC) .. controls (12,8) and (12,4) .. node[right] {$0.7$} (NC);

% Flechas de transición
\draw[->,very thick,orange] (C) to[bend left=30] node[above] {$0.2$} (NC);
\draw[->,very thick,pink] (NC) to[bend left=30] node[below] {$0.3$} (C);

\end{tikzpicture}
\end{document}
```

---

### Resolución del Ejercicio

#### 1. Identificación de datos y estados

- **Población total ($N$):** $1000$ individuos.
- **Estados del sistema:**
    - **Estado 1 ($C$):** Comprar el producto.
    - **Estado 2 ($NC$):** No comprar el producto.
- **Probabilidades dadas:**
    - De compra a no compra: $P_{12} = 0.2$ ($20%$).
    - De no compra a compra: $P_{21} = 0.3$ ($30%$).

#### 2. Construcción de la matriz de transición ($P$)

La suma de las probabilidades de cada fila debe ser igual a $1$ (propiedad estocástica).

- $P_{11} = 1 - P_{12} = 1 - 0.2 = \mathbf{0.8}$ (Probabilidad de seguir comprando).
- $P_{22} = 1 - P_{21} = 1 - 0.3 = \mathbf{0.7}$ (Probabilidad de seguir sin comprar).

La matriz de transición es: $$P = \begin{bmatrix} 0.8 & 0.2 \ 0.3 & 0.7 \end{bmatrix}$$

#### 3. Definición del vector de estado inicial ($\pi(1)$)

En el primer mes, $100$ personas compraron el producto. Expresamos esto en probabilidades dividiendo por la población total ($1000$):

- $\pi_1(1) = 100 / 1000 = 0.1$
- $\pi_2(1) = (1000 - 100) / 1000 = 0.9$ $$\pi(1) = [0.1, \quad 0.9]$$

#### 4. Proyección para el próximo mes (Mes 2)

Aplicamos la relación recurrente $\pi(n+1) = \pi(n) \cdot P$: $$\pi(2) = [0.1, \quad 0.9] \begin{bmatrix} 0.8 & 0.2 \ 0.3 & 0.7 \end{bmatrix}$$

- $\pi_1(2) = (0.1 \times 0.8) + (0.9 \times 0.3) = 0.08 + 0.27 = \mathbf{0.35}$
- $\pi_2(2) = (0.1 \times 0.2) + (0.9 \times 0.7) = 0.02 + 0.63 = \mathbf{0.65}$

**Número de compradores (Mes 2):** $0.35 \times 1000 = \mathbf{350}$ individuos.

#### 5. Proyección para dentro de tres meses (Mes 4)

Para calcular el estado en el periodo 4 (tres meses después del primero), podemos iterar paso a paso:

**Cálculo para el Mes 3:** $$\pi(3) = \pi(2) \cdot P = [0.35, \quad 0.65] \begin{bmatrix} 0.8 & 0.2 \ 0.3 & 0.7 \end{bmatrix}$$

- $\pi_1(3) = (0.35 \times 0.8) + (0.65 \times 0.3) = 0.28 + 0.195 = \mathbf{0.475}$
- $\pi_2(3) = (0.35 \times 0.2) + (0.65 \times 0.7) = 0.07 + 0.455 = \mathbf{0.525}$

**Cálculo para el Mes 4:** $$\pi(4) = \pi(3) \cdot P = [0.475, \quad 0.525] \begin{bmatrix} 0.8 & 0.2 \ 0.3 & 0.7 \end{bmatrix}$$

- $\pi_1(4) = (0.475 \times 0.8) + (0.525 \times 0.3) = 0.38 + 0.1575 = \mathbf{0.5375}$
- $\pi_2(4) = (0.475 \times 0.2) + (0.525 \times 0.7) = 0.095 + 0.3675 = \mathbf{0.4625}$

**Número de compradores (Mes 4):** $0.5375 \times 1000 = \mathbf{537.5}$ (aproximadamente **538 individuos**).

---

### Resultado Final

- Al mes próximo lo comprarán **350 individuos**.
- Dentro de tres meses lo comprarán aproximadamente **538 individuos**.

**Verificación:** En cada paso, las probabilidades suman $1$ ($0.5375 + 0.4625 = 1.0$), lo que valida la consistencia del modelo.