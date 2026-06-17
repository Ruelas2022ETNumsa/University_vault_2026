# Ejercicio 1 (ingeniero)
Un profesor de ingeniería adquiere una computadora nueva cada dos años. El profesor puede elegir de entre tres modelos: M1, M2 y M3. Si el modelo actual es M1, la siguiente computadora puede ser M2 con probabilidad 0.2, o M3 con probabilidad 0.15. Si el modelo actual es M2, las probabilidades de cambiar a M1 y M3 son 0.6 y 0.25, respectivamente. Pero si el modelo actual es M3, entonces las probabilidades de comprar los modelos M1 y M2 son 0.5 y 0.1, respectivamente. Hallar la matriz de probabilidades de transición

## solución

### Diagrama de la Cadena de Markov

```tikz
%\documentclass[margin=10pt]{standalone}
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}

    % ESTADO_1: M1 (Posición: 90 grados)
    \node[draw,circle,thick,orange] (M1) at (6,10) {M1};

    % ESTADO_2: M2 (Posición: -30 grados)
    \node[draw,circle,thick,pink] (M2) at (9.46,4) {M2};

    % ESTADO_3: M3 (Posición: -150 grados)
    \node[draw,circle,thick,lime] (M3) at (2.54,4) {M3};

    % TRANSICIONES DESDE M1
    \draw[->,ultra thick,orange] (M1) .. controls (5,12) and (7,12) ..node[above] {$0.65$} (M1);
    \draw[->,very thick,orange] (M1) to[bend left=15] node[pos=0.2, right] {$0.2$} (M2);
    \draw[->,very thick,orange] (M1) to[bend left=15] node[pos=0.2, left] {$0.15$} (M3);

    % TRANSICIONES DESDE M2
    \draw[->,ultra thick,pink] (M2) .. controls (11,5) and (11,3) ..node[right] {$0.15$} (M2);
    \draw[->,very thick,pink] (M2) to[bend left=15] node[pos=0.2, left] {$0.6$} (M1);
    \draw[->,very thick,pink] (M2) to[bend left=15] node[pos=0.2, below] {$0.25$} (M3);

    % TRANSICIONES DESDE M3
    \draw[->,ultra thick,lime] (M3) .. controls (1,5) and (1,3) ..node[left] {$0.4$} (M3);
    \draw[->,very thick,lime] (M3) to[bend left=15] node[pos=0.2, right] {$0.5$} (M1);
    \draw[->,very thick,lime] (M3) to[bend left=15] node[pos=0.2, above] {$0.1$} (M2);

\end{tikzpicture}
\end{document}
```

---

### Resolución del Ejercicio

#### 1. Identificación del Tipo de Ejercicio y Tema

Este es un ejercicio de **procesos estocásticos**, específicamente sobre **Cadenas de Markov en tiempo discreto**. Se identifica como tal porque cumple con las siguientes características:

- El sistema puede estar en un número finito de situaciones o categorías denominadas **estados** (modelos de computadora M1, M2 y M3).
- Se presentan probabilidades de cambio fijas entre estados que dependen únicamente del estado actual y no de la historia pasada, lo que se conoce como la **Propiedad de Markov**.
- El proceso ocurre en intervalos de tiempo fijos (cada dos años).

#### 2. Identificación de los Datos del Problema

El sistema tiene tres estados posibles:

- **Estado 1 ($M_1$):** Poseer el modelo de computadora 1.
- **Estado 2 ($M_2$):** Poseer el modelo de computadora 2.
- **Estado 3 ($M_3$):** Poseer el modelo de computadora 3.

Las probabilidades condicionales de transición dadas en el enunciado son:

- Desde $M_1$: Probabilidad de pasar a $M_2 = 0.2$; probabilidad de pasar a $M_3 = 0.15$.
- Desde $M_2$: Probabilidad de cambiar a $M_1 = 0.6$; probabilidad de cambiar a $M_3 = 0.25$.
- Desde $M_3$: Probabilidad de comprar $M_1 = 0.5$; probabilidad de comprar $M_2 = 0.1$.

#### 3. Explicación de lo que se Pide

Se solicita hallar la **matriz de probabilidades de transición ($P$)**. Esta matriz organiza las probabilidades de moverse de un estado $i$ a un estado $j$ en un solo paso del tiempo.

#### 4. Fórmulas Utilizadas y Razonamiento

La matriz de transición se define como: $$P = \begin{bmatrix} P_{11} & P_{12} & P_{13} \\ P_{21} & P_{22} & P_{23} \\ P_{31} & P_{32} & P_{33} \end{bmatrix}$$

Una propiedad fundamental de las matrices estocásticas es que **la suma de las probabilidades de cada renglón debe ser igual a 1**. Esto se debe a que el profesor debe elegir obligatoriamente uno de los tres modelos disponibles para el siguiente periodo (los estados son colectivamente exhaustivos).

Por lo tanto, si el enunciado no da explícitamente la probabilidad de permanecer en el mismo estado ($P_{ii}$), esta se calcula despejando: $$P_{ii} = 1 - \sum_{j \neq i} P_{ij}$$

#### 5. Sustitución de Valores y Operaciones Intermedias

- **Para el renglón 1 (Estado $M_1$):** Dados $P_{12} = 0.2$ y $P_{13} = 0.15$: $$P_{11} = 1 - (0.2 + 0.15)$$ $$P_{11} = 1 - 0.35 = 0.65$$
    
- **Para el renglón 2 (Estado $M_2$):** Dados $P_{21} = 0.6$ y $P_{23} = 0.25$: $$P_{22} = 1 - (0.6 + 0.25)$$ $$P_{22} = 1 - 0.85 = 0.15$$
    
- **Para el renglón 3 (Estado $M_3$):** Dados $P_{31} = 0.5$ y $P_{32} = 0.1$: $$P_{33} = 1 - (0.5 + 0.1)$$ $$P_{33} = 1 - 0.60 = 0.40$$
    

#### 6. Resultado Final: Matriz de Transición

Insertamos todos los valores calculados y conocidos en la estructura de la matriz:

$$P = \begin{bmatrix} 0.65 & 0.20 & 0.15 \\ 0.60 & 0.15 & 0.25 \\ 0.50 & 0.10 & 0.40 \end{bmatrix}$$

#### 7. Verificación del Resultado

Comprobamos que cada fila sume la unidad:

- Fila 1: $0.65 + 0.20 + 0.15 = 1.00$ (Correcto)
- Fila 2: $0.60 + 0.15 + 0.25 = 1.00$ (Correcto)
- Fila 3: $0.50 + 0.10 + 0.40 = 1.00$ (Correcto)

La matriz obtenida es una **matriz estocástica** válida que describe completamente las transiciones del sistema cada dos años.

---

# Ejercicio 2 (ingeniero)
El departamento de estudios de mercado de una fábrica estima que el 20% de la gente que compra un producto un mes, no lo comprará el mes siguiente. Además, el 30% de quienes no lo compren un mes lo adquirirá al mes siguiente. En una población de 1000 individuos, 100 compraron el producto el primer mes. ¿Cuántos lo comprarán al mes próximo? ¿Y dentro de dos meses?

## solución

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


---

# Ejercicio 3 (ingeniero)
En una población de 10,000 habitantes, 5000 no fuman, 2500 fuman uno o menos de un paquete diario y 2500 fuman más de un paquete diario. En un mes hay un 5% de probabilidad de que un no fumador comience a fumar un paquete diario, o menos, y un 2% de que un no fumador pase a fumar más de un paquete diario. Para los que fuman un paquete, o menos, hay un 10% de probabilidad de que dejen el tabaco, y un 10% de que pasen a fumar más de un paquete diario. Entre los que fuman más de un paquete, hay un 5% de probabilidad de que dejen el tabaco y un 10% de que pasen a fumar un paquete, o menos. ¿Cuántos individuos habrá de cada clase el próximo mes?

## solución

### Diagrama de la Cadena de Markov

```tikz
%\documentclass[margin=10pt]{standalone}
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}

    % ESTADO_1: No fuman (NF) - Posición: 90 grados
    \node[draw,circle,thick,orange] (NF) at (6,10) {NF};

    % ESTADO_2: Fuman <= 1 paquete (F1) - Posición: -30 grados
    \node[draw,circle,thick,pink] (F1) at (9.46,4) {F1};

    % ESTADO_3: Fuman > 1 paquete (F2) - Posición: -150 grados
    \node[draw,circle,thick,lime] (F2) at (2.54,4) {F2};

    % TRANSICIONES ESTADO NF (No fuman)
    % Bucle: 1 - (0.05 + 0.02) = 0.93
    \draw[->,ultra thick,orange] (NF) .. controls (5,12) and (7,12) ..node[above] {$0.93$} (NF);
    % Hacia F1: 0.05
    \draw[->,very thick,orange] (NF) to[bend left=15] node[pos=0.2, right] {$0.05$} (F1);
    % Hacia F2: 0.02
    \draw[->,very thick,orange] (NF) to[bend left=15] node[pos=0.2, left] {$0.02$} (F2);

    % TRANSICIONES ESTADO F1 (Fuman <= 1 paquete)
    % Bucle: 1 - (0.10 + 0.10) = 0.80
    \draw[->,ultra thick,pink] (F1) .. controls (11,5) and (11,3) ..node[right] {$0.80$} (F1);
    % Hacia NF: 0.10
    \draw[->,very thick,pink] (F1) to[bend left=15] node[pos=0.2, left] {$0.10$} (NF);
    % Hacia F2: 0.10
    \draw[->,very thick,pink] (F1) to[bend left=15] node[pos=0.2, below] {$0.10$} (F2);

    % TRANSICIONES ESTADO F2 (Fuman > 1 paquete)
    % Bucle: 1 - (0.05 + 0.10) = 0.85
    \draw[->,ultra thick,lime] (F2) .. controls (1,5) and (1,3) ..node[left] {$0.85$} (F2);
    % Hacia NF: 0.05
    \draw[->,very thick,lime] (F2) to[bend left=15] node[pos=0.2, right] {$0.05$} (NF);
    % Hacia F1: 0.10
    \draw[->,very thick,lime] (F2) to[bend left=15] node[pos=0.2, above] {$0.10$} (F1);

\end{tikzpicture}
\end{document}
```

---

### Análisis Técnico y Resolución del Ejercicio

#### 1. Identificación del Tipo de Ejercicio y Tema

Este es un ejercicio de **procesos estocásticos**, específicamente sobre **Cadenas de Markov de tiempo discreto**,,. Se identifica como tal porque cumple con las tres condiciones fundamentales de Markov,:

1. **Estados finitos:** La población se divide en tres categorías o estados mutuamente excluyentes ($NF, F1, F2$),.
2. **Probabilidades de transición estacionarias:** Los porcentajes de cambio de un mes al siguiente permanecen constantes durante el análisis,,.
3. **Propiedad de Markov:** La situación futura (el próximo mes) depende únicamente del estado actual de los fumadores y no de su historial previo,,.

#### 2. Identificación de los Datos del Problema

- **Población Total ($N$):** $10,000$ habitantes.
- **Estados:**
    - **Estado 1 ($NF$):** No fumadores.
    - **Estado 2 ($F1$):** Fuman un paquete o menos diariamente.
    - **Estado 3 ($F2$):** Fuman más de un paquete diariamente.
- **Vector de Estado Inicial ($\pi(0)$):** Basado en el número de habitantes iniciales,:
    - $\pi_{NF}(0) = 5000 / 10000 = 0.50$ (50% de la población)
    - $\pi_{F1}(0) = 2500 / 10000 = 0.25$ (25% de la población)
    - $\pi_{F2}(0) = 2500 / 10000 = 0.25$ (25% de la población) $$\pi(0) = [0.50, \quad 0.25, \quad 0.25]$$

#### 3. Explicación de lo que se Pide y Fórmulas

Se pide determinar la **distribución de la población el próximo mes**. Para ello, utilizaremos la matriz de probabilidades de transición ($P$),. La fórmula para proyectar el estado en el periodo $n+1$ es,,: $$\pi(n+1) = \pi(n) \cdot P$$ Donde $\pi(1)$ será el vector de probabilidades del próximo mes.

#### 4. Construcción de la Matriz de Transición ($P$)

La matriz se organiza por renglones, donde cada renglón debe sumar 1 (probabilidad total),,.

- **Renglón 1 (Desde $NF$):**
    - Hacia $F1$ ($P_{12}$): $0.05$
    - Hacia $F2$ ($P_{13}$): $0.02$
    - Permanece $NF$ ($P_{11}$): $1 - (0.05 + 0.02) = 0.93$
- **Renglón 2 (Desde $F1$):**
    - Hacia $NF$ ($P_{21}$): $0.10$
    - Hacia $F2$ ($P_{23}$): $0.10$
    - Permanece $F1$ ($P_{22}$): $1 - (0.10 + 0.10) = 0.80$
- **Renglón 3 (Desde $F2$):**
    - Hacia $NF$ ($P_{31}$): $0.05$
    - Hacia $F1$ ($P_{32}$): $0.10$
    - Permanece $F2$ ($P_{33}$): $1 - (0.05 + 0.10) = 0.85$

$$P = \begin{bmatrix} 0.93 & 0.05 & 0.02  \\ 0.10 & 0.80 & 0.10  \\ 0.05 & 0.10 & 0.85 \end{bmatrix}$$

#### 5. Desarrollo de los Cálculos Paso a Paso

Multiplicamos el vector inicial por la matriz: $$\pi(1) = [0.50, \quad 0.25, \quad 0.25] \begin{bmatrix} 0.93 & 0.05 & 0.02 \\ 0.10 & 0.80 & 0.10 \\ 0.05 & 0.10 & 0.85 \end{bmatrix}$$

**Cálculo de $\pi_{NF}(1)$ (Individuos que no fuman):**
 $\pi_{NF}(1) = (0.50 \times 0.93) + (0.25 \times 0.10) + (0.25 \times 0.05)$
 $\pi_{NF}(1) = 0.465 + 0.025 + 0.0125$ 
 $\pi_{NF}(1) = 0.5025$

**Cálculo de $\pi_{F1}(1)$ (Individuos que fuman $\leq 1$ paquete):**
 $\pi_{F1}(1) = (0.50 \times 0.05) + (0.25 \times 0.80) + (0.25 \times 0.10)$
  $\pi_{F1}(1) = 0.025 + 0.20 + 0.025$
   $\pi_{F1}(1) = 0.25$

**Cálculo de $\pi_{F2}(1)$ (Individuos que fuman $> 1$ paquete):** $\pi_{F2}(1) = (0.50 \times 0.02) + (0.25 \times 0.10) + (0.25 \times 0.85)$ 
$\pi_{F2}(1) = 0.01 + 0.025 + 0.2125$ 
$\pi_{F2}(1) = 0.2475$

#### 6. Conversión a Número de Individuos

Multiplicamos las probabilidades finales por la población total ($10,000$):

- **No fumadores:** $0.5025 \times 10,000 = \mathbf{5,025}$
- **Fumadores $\leq 1$ paquete:** $0.25 \times 10,000 = \mathbf{2,500}$
- **Fumadores $> 1$ paquete:** $0.2475 \times 10,000 = \mathbf{2,475}$

#### 7. Resultado Final y Verificación

El próximo mes habrá:

- **5,025 individuos que no fuman.**
- **2,500 individuos que fuman un paquete diario o menos.**
- **2,475 individuos que fuman más de un paquete diario.**

**Verificación:** La suma total debe ser igual a la población original: $5025 + 2500 + 2475 = 10,000$ habitantes., El cálculo es correcto.