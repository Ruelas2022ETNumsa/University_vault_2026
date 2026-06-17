### Diagrama de la Cadena de Markov

```tikz
\begin{document}
\begin{tikzpicture}

    % ESTADO_1: Comprar (Posición horizontal para N=2)
    \node[draw,circle,thick,orange] (C) at (2,6) {C};

    % ESTADO_2: No Comprar
    \node[draw,circle,thick,pink] (NC) at (10,6) {NC};

    % TRANSICIONES ESTADO C (Comprar)
    % Bucle: 1 - 0.20 = 0.80
    \draw[->,ultra thick,orange] (C) .. controls (0.5,8) and (3.5,8) .. node[above] {$0.8$} (C);
    % Salida hacia NC: 0.20
    \draw[->,very thick,orange] (C) to[bend left=25] node[pos=0.5, above] {$0.2$} (NC);

    % TRANSICIONES ESTADO NC (No Comprar)
    % Bucle: 1 - 0.30 = 0.70
    \draw[->,ultra thick,pink] (NC) .. controls (8.5,8) and (11.5,8) .. node[above] {$0.7$} (NC);
    % Salida hacia C: 0.30
    \draw[->,very thick,pink] (NC) to[bend left=25] node[pos=0.5, below] {$0.3$} (C);

\end{tikzpicture}
\end{document}
```

---

### Análisis Técnico y Resolución del Ejercicio

#### 1. Identificación del Tipo de Ejercicio y Tema

Este es un ejercicio de **procesos estocásticos**, específicamente sobre **Cadenas de Markov de tiempo discreto**. Se identifica como tal porque cumple con las tres condiciones fundamentales:

1. **Estados finitos:** La población se divide en dos categorías mutuamente excluyentes: quienes compran el producto ($C$) y quienes no lo compran ($NC$).
2. **Probabilidades de transición constantes:** El problema define porcentajes fijos de cambio de un mes al siguiente (probabilidades estacionarias).
3. **Propiedad de Markov:** La decisión de compra en el mes próximo depende únicamente de la situación en el mes actual.

#### 2. Identificación de los Datos del Problema

- **Población total ($N$):** $1000$ individuos.
- **Estados:**
    - Estado 1 ($C$): Comprar el producto.
    - Estado 2 ($NC$): No comprar el producto.
- **Probabilidades de transición dadas:**
    - Probabilidad de pasar de $C$ a $NC$: $P_{12} = 0.2$.
    - Probabilidad de pasar de $NC$ a $C$: $P_{21} = 0.3$.
- **Estado Inicial (Mes 1):**
    - Compradores: $100$.
    - No compradores: $1000 - 100 = 900$.

#### 3. Explicación de las Fórmulas Utilizadas

Para resolver este problema, utilizaremos la **matriz de probabilidades de transición ($P$)** y el **vector de probabilidades de estado ($\pi$)**:

1. **Matriz de Transición ($P$):** Representa las probabilidades de moverse entre estados en un paso. Cada fila debe sumar 1. $$P = \begin{bmatrix} P_{11} & P_{12} \\ P_{21} & P_{22} \end{bmatrix}$$
2. **Vector de Estado ($\pi(n)$):** Contiene la probabilidad de que el sistema esté en cada estado en el tiempo $n$.
3. **Relación Recurrente:** Para predecir el estado en el periodo $n+1$, multiplicamos el vector de estado actual por la matriz de transición: $$\pi(n+1) = \pi(n) \cdot P$$

#### 4. Desarrollo Paso a Paso

**Paso 1: Construcción de la matriz de transición $P$** Calculamos las probabilidades de permanencia (bucles):

- $P_{11} = 1 - P_{12} = 1 - 0.2 = 0.8$ (Probabilidad de seguir comprando).
- $P_{22} = 1 - P_{21} = 1 - 0.3 = 0.7$ (Probabilidad de seguir sin comprar).

La matriz resulta: $$P = \begin{bmatrix} 0.8 & 0.2 \\ 0.3 & 0.7 \end{bmatrix}$$

**Paso 2: Definición del vector de estado inicial $\pi(1)$** Expresamos el número de individuos como probabilidades dividiendo entre el total ($1000$):

- $\pi_1(1) = 100 / 1000 = 0.1$.
- $\pi_2(1) = 900 / 1000 = 0.9$. $$\pi(1) = [0.1, \quad 0.9]$$

**Paso 3: Cálculo para el próximo mes (Mes 2)** Aplicamos la fórmula $\pi(2) = \pi(1) \cdot P$: $$\pi(2) = [0.1, \quad 0.9] \begin{bmatrix} 0.8 & 0.2 \\ 0.3 & 0.7 \end{bmatrix}$$

- $\pi_1(2) = (0.1 \times 0.8) + (0.9 \times 0.3) = 0.08 + 0.27 = 0.35$
- $\pi_2(2) = (0.1 \times 0.2) + (0.9 \times 0.7) = 0.02 + 0.63 = 0.65$

Convertimos a número de individuos:

- Compradores = $0.35 \times 1000 = 350$.

**Paso 4: Cálculo para dentro de dos meses (Mes 3)** Aplicamos la fórmula $\pi(3) = \pi(2) \cdot P$: $$\pi(3) = [0.35, \quad 0.65] \begin{bmatrix} 0.8 & 0.2 \\ 0.3 & 0.7 \end{bmatrix}$$

- $\pi_1(3) = (0.35 \times 0.8) + (0.65 \times 0.3) = 0.28 + 0.195 = 0.475$
- $\pi_2(3) = (0.35 \times 0.2) + (0.65 \times 0.7) = 0.07 + 0.455 = 0.525$

Convertimos a número de individuos:

- Compradores = $0.475 \times 1000 = 475$.

#### 5. Resultado Final

- **Al mes próximo:** Comprarán el producto **350 individuos**.
- **Dentro de dos meses:** Comprarán el producto **475 individuos**.

#### 6. Verificación

Comprobamos que las probabilidades en cada paso sumen 1 (100% de la población):

- Mes 2: $0.35 + 0.65 = 1.0$ (Correcto).
- Mes 3: $0.475 + 0.525 = 1.0$ (Correcto). Los cálculos son consistentes con las propiedades de una cadena de Markov finita.