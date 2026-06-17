# 1111


### Diagrama de la Cadena de Markov en TikZ

```tikz
%\documentclass[margin=10pt]{standalone}
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=stealth, line width=1pt]

% CONFIGURACIÓN DE NODOS (Estados)
% Estado 0 (M1): Ángulo 90, Posición (6, 11)
\node[draw,circle,thick,color=orange,minimum size=1.2cm] (M1) at (6,11) {\textbf{M1}};
% Estado 1 (M2): Ángulo -30, Posición (10, 4)
\node[draw,circle,thick,color=pink,minimum size=1.2cm] (M2) at (10,4) {\textbf{M2}};
% Estado 2 (M3): Ángulo -150, Posición (2, 4)
\node[draw,circle,thick,color=lime,minimum size=1.2cm] (M3) at (2,4) {\textbf{M3}};

% BUCLES (Probabilidades de permanencia Pii)
% M1 (Arriba)
\draw[->,ultra thick,orange] (M1) .. controls (5,13) and (7,13) .. node[above] {$0.65$} (M1);
% M2 (Derecha)
\draw[->,ultra thick,pink] (M2) .. controls (12,5) and (12,3) .. node[right] {$0.15$} (M2);
% M3 (Izquierda)
\draw[->,ultra thick,lime] (M3) .. controls (0,5) and (0,3) .. node[left] {$0.40$} (M3);

% TRANSICIONES (Flechas curvas bend left)
% Desde M1
\draw[->,very thick,orange] (M1) to[bend left=10] node[pos=0.3, right] {$0.2$} (M2);
\draw[->,very thick,orange] (M1) to[bend left=10] node[pos=0.3, left] {$0.15$} (M3);

% Desde M2
\draw[->,very thick,pink] (M2) to[bend left=20] node[pos=0.3, left] {$0.6$} (M1);
\draw[->,very thick,pink] (M2) to[bend left=20] node[pos=0.3, below] {$0.25$} (M3);

% Desde M3
\draw[->,very thick,lime] (M3) to[bend left=30] node[pos=0.3, right] {$0.5$} (M1);
\draw[->,very thick,lime] (M3) to[bend left=30] node[pos=0.3, above] {$0.1$} (M2);

\end{tikzpicture}
\end{document}
```

---

### Resolución del Ejercicio

#### 1. Identificación de los datos y qué se pide

El problema describe el comportamiento de un profesor de ingeniería que cambia de modelo de computadora cada dos años. Se identifi can tres condiciones posibles o **estados** del sistema:

- **Estado 1 ($M_1$):** Poseer el modelo de computadora 1.
- **Estado 2 ($M_2$):** Poseer el modelo de computadora 2.
- **Estado 3 ($M_3$):** Poseer el modelo de computadora 3.

Se proporcionan las siguientes probabilidades de transición (cambio entre modelos):

- Si tiene $M_1$: Cambia a $M_2$ con $0.2$ y a $M_3$ con $0.15$.
- Si tiene $M_2$: Cambia a $M_1$ con $0.6$ y a $M_3$ con $0.25$.
- Si tiene $M_3$: Cambia a $M_1$ con $0.5$ y a $M_2$ con $0.1$.

**Se pide:** Hallar la matriz de probabilidades de transición ($P$).

#### 2. Identificación del tipo de ejercicio y fórmulas

Este es un ejercicio de **procesos estocásticos**, específi camente una **Cadena de Markov de tiempo discreto**. Se reconoce como tal porque:

1. Existe un número fi nito de estados ($M_1, M_2, M_3$).
2. La probabilidad de cambiar de estado depende únicamente del estado actual (Propiedad de Markov).
3. El proceso ocurre en intervalos de tiempo fi jos (cada dos años).

**Fórmula de la matriz de transición:** La matriz $P$ organiza las probabilidades de moverse del estado $i$ al estado $j$ ($P_{ij}$): $$P = \begin{bmatrix} P_{11} & P_{12} & P_{13} \ P_{21} & P_{22} & P_{23} \ P_{31} & P_{32} & P_{33} \end{bmatrix}$$

Una propiedad fundamental es que los estados son **colectivamente exhaustivos**, por lo que la suma de las probabilidades en cada renglón debe ser igual a 1: $$\sum_{j} P_{ij} = 1 \implies P_{ii} = 1 - \sum_{j \neq i} P_{ij}$$

#### 3. Sustitución de valores y operaciones paso a paso

Para completar la matriz, debemos calcular las probabilidades de permanecer en el mismo estado ($P_{ii}$), ya que no se dan explícitamente.

- **Para el Renglón 1 (Estado $M_1$):** Datos: $P_{12} = 0.2$ y $P_{13} = 0.15$. Cálculo: $P_{11} = 1 - (P_{12} + P_{13})$ $P_{11} = 1 - (0.2 + 0.15) = 1 - 0.35$ **$P_{11} = 0.65$**
    
- **Para el Renglón 2 (Estado $M_2$):** Datos: $P_{21} = 0.6$ y $P_{23} = 0.25$. Cálculo: $P_{22} = 1 - (P_{21} + P_{23})$ $P_{22} = 1 - (0.6 + 0.25) = 1 - 0.85$ **$P_{22} = 0.15$**
    
- **Para el Renglón 3 (Estado $M_3$):** Datos: $P_{31} = 0.5$ y $P_{32} = 0.1$. Cálculo: $P_{33} = 1 - (P_{31} + P_{32})$ $P_{33} = 1 - (0.5 + 0.1) = 1 - 0.60$ **$P_{33} = 0.40$**
    

#### 4. Resultado final y verificación

Organizando los valores conocidos y calculados en la estructura matricial:

$$P = \begin{bmatrix} 0.65 & 0.20 & 0.15 \ 0.60 & 0.15 & 0.25 \ 0.50 & 0.10 & 0.40 \end{bmatrix}$$

**Verificación de la matriz estocástica:**

- Fila 1: $0.65 + 0.20 + 0.15 = 1.00$ (Correcto)
- Fila 2: $0.60 + 0.15 + 0.25 = 1.00$ (Correcto)
- Fila 3: $0.50 + 0.10 + 0.40 = 1.00$ (Correcto)

La matriz obtenida describe completamente las probabilidades de transición del sistema cada dos años.
# 2222

Este ejercicio se identifica como un proceso estocástico, específicamente una **Cadena de Markov en tiempo discreto**. Cumple con las condiciones de estados finitos (comprar o no comprar), probabilidades de transición constantes y la propiedad de que el estado futuro depende únicamente del presente.

### 1. Diagrama de la Cadena de Markov

```tikz
%\documentclass[tikz,border=10pt]{standalone}
\begin{document}
\begin{tikzpicture}

% Configuración de los estados (N=2)
% Ángulos: 90 - i*(360/2) -> 90, -90
\node (C) at (6, 9) [draw,circle,thick,color=orange] {C};
\node (NC) at (6, 3) [draw,circle,thick,color=pink] {NC};

% Bucles (Self-loops)
\draw[->,ultra thick,orange] (C) .. controls (5,11) and (7,11) ..node[above] {$0.8$} (C);
\draw[->,ultra thick,pink] (NC) .. controls (7,1) and (5,1) ..node[below] {$0.7$} (NC);

% Transiciones entre estados
\draw[->,very thick,orange] (C) to[bend left=30] node[pos=0.2,right] {$0.2$} (NC);
\draw[->,very thick,pink] (NC) to[bend left=30] node[pos=0.2,left] {$0.3$} (C);

\end{tikzpicture}
\end{document}
```

---

### 2. Resolución Técnica del Ejercicio

#### **Paso 1: Identificación de datos y estados**

El sistema se define por una población total ($N$) de 1000 individuos y dos estados mutuamente excluyentes:

- **Estado 1 ($C$):** Comprar el producto.
- **Estado 2 ($NC$):** No comprar el producto.

Probabilidades de transición dadas en el enunciado:

- Probabilidad de pasar de $C$ a $NC$: $P_{12} = 0.2$.
- Probabilidad de pasar de $NC$ a $C$: $P_{21} = 0.3$.

#### **Paso 2: Construcción de la matriz de transición ($P$)**

Para completar la matriz, calculamos las probabilidades de permanencia (la suma de cada fila debe ser 1):

- $P_{11} = 1 - P_{12} = 1 - 0.2 = 0.8$ (Probabilidad de seguir comprando).
- $P_{22} = 1 - P_{21} = 1 - 0.3 = 0.7$ (Probabilidad de seguir sin comprar).

La matriz de transición resultante es: $$P = \begin{bmatrix} 0.8 & 0.2 \ 0.3 & 0.7 \end{bmatrix}$$

#### **Paso 3: Definición del vector de estado inicial ($\pi(1)$)**

En el primer mes, 100 personas compraron el producto de un total de 1000. Expresamos esto como probabilidades:

- $\pi_1(1) = 100 / 1000 = 0.1$
- $\pi_2(1) = (1000 - 100) / 1000 = 0.9$

Vector inicial: $$\pi(1) = [0.1, \quad 0.9]$$

#### **Paso 4: Cálculo para el mes próximo (Mes 2)**

Utilizamos la relación recurrente $\pi(n+1) = \pi(n) \cdot P$: $$\pi(2) = [0.1, \quad 0.9] \begin{bmatrix} 0.8 & 0.2 \ 0.3 & 0.7 \end{bmatrix}$$

Realizamos las operaciones vector-matriz:

- $\pi_1(2) = (0.1 \times 0.8) + (0.9 \times 0.3) = 0.08 + 0.27 = 0.35$
- $\pi_2(2) = (0.1 \times 0.2) + (0.9 \times 0.7) = 0.02 + 0.63 = 0.65$

**Resultado en individuos:**

- Compradores = $0.35 \times 1000 = \mathbf{350}$ **individuos**.

#### **Paso 5: Cálculo para dentro de dos meses (Mes 3)**

Aplicamos la fórmula partiendo del estado del Mes 2: $$\pi(3) = [0.35, \quad 0.65] \begin{bmatrix} 0.8 & 0.2 \ 0.3 & 0.7 \end{bmatrix}$$

Realizamos las operaciones:

- $\pi_1(3) = (0.35 \times 0.8) + (0.65 \times 0.3) = 0.28 + 0.195 = 0.475$
- $\pi_2(3) = (0.35 \times 0.2) + (0.65 \times 0.7) = 0.07 + 0.455 = 0.525$

**Resultado en individuos:**

- Compradores = $0.475 \times 1000 = \mathbf{475}$ **individuos**.

#### **Verificación**

La suma de las probabilidades en cada paso debe ser igual a la unidad (100% de la población):

- Mes 2: $0.35 + 0.65 = 1.0$
- Mes 3: $0.475 + 0.525 = 1.0$ El cálculo es consistente con las propiedades de las Cadenas de Markov.









# 333333

Este ejercicio se identifica como un proceso estocástico, específicamente una **Cadena de Markov de tiempo discreto**. El sistema presenta un número finito de estados (categorías de fumadores), probabilidades de transición constantes mes a mes y la propiedad de que el estado futuro depende únicamente del estado actual.

### 1. Diagrama de la Cadena de Markov

```tikz
%\documentclass[margin=10pt]{standalone}
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}

% ESTADOS (Nodos)
\node (NF) at (6,10) [draw,circle,thick,color=orange] {NF};
\node (F1) at (9.46,4) [draw,circle,thick,color=pink] {F1};
\node (F2) at (2.53,4) [draw,circle,thick,color=lime] {F2};

% BUCLES (Self-loops)
\draw[->,ultra thick,orange] (NF) .. controls (5,12) and (7,12) ..node[above] {$0.93$} (NF);
\draw[->,ultra thick,pink] (F1) .. controls (11,3) and (11,5) ..node[right] {$0.80$} (F1);
\draw[->,ultra thick,lime] (F2) .. controls (1,5) and (1,3) ..node[left] {$0.85$} (F2);

% TRANSICIONES (Flechas)
% Desde NF
\draw[->,very thick,orange] (NF) to[bend left=15] node[pos=0.2, right] {$0.05$} (F1);
\draw[->,very thick,orange] (NF) to[bend right=15] node[pos=0.2, left] {$0.02$} (F2);

% Desde F1
\draw[->,very thick,pink] (F1) to[bend left=15] node[pos=0.3, left] {$0.10$} (NF);
\draw[->,very thick,pink] (F1) to[bend left=20] node[pos=0.5, above] {$0.10$} (F2);

% Desde F2
\draw[->,very thick,lime] (F2) to[bend right=15] node[pos=0.3, right] {$0.05$} (NF);
\draw[->,very thick,lime] (F2) to[bend left=20] node[pos=0.5, below] {$0.10$} (F1);

\end{tikzpicture}
\end{document}
```

---

### 2. Resolución del Ejercicio

#### A. Identificación de los datos y estados

El problema define una población total ($N$) de **10,000 habitantes**. Los estados posibles son:

- **Estado 1 (NF):** No fumadores.
- **Estado 2 (F1):** Fuman un paquete o menos diariamente.
- **Estado 3 (F2):** Fuman más de un paquete diariamente.

**Distribución inicial (Mes 0):** Para obtener el vector de probabilidades de estado inicial $\pi(0)$, dividimos la cantidad de habitantes de cada clase entre el total:

- $\pi_{NF}(0) = 5,000 / 10,000 = 0.50$ (50%)
- $\pi_{F1}(0) = 2,500 / 10,000 = 0.25$ (25%)
- $\pi_{F2}(0) = 2,500 / 10,000 = 0.25$ (25%) $$\pi(0) = [0.50, \quad 0.25, \quad 0.25]$$

#### B. Construcción de la Matriz de Transición (P)

La matriz se organiza de modo que la suma de cada renglón sea igual a 1 (colectivamente exhaustivos):

1. **Renglón 1 (Desde NF):**
    
    - Hacia F1 ($P_{12}$): $0.05$ (5%).
    - Hacia F2 ($P_{13}$): $0.02$ (2%).
    - Permanece NF ($P_{11}$): $1 - (0.05 + 0.02) = \mathbf{0.93}$.
2. **Renglón 2 (Desde F1):**
    
    - Hacia NF ($P_{21}$): $0.10$ (10%).
    - Hacia F2 ($P_{23}$): $0.10$ (10%).
    - Permanece F1 ($P_{22}$): $1 - (0.10 + 0.10) = \mathbf{0.80}$.
3. **Renglón 3 (Desde F2):**
    
    - Hacia NF ($P_{31}$): $0.05$ (5%).
    - Hacia F1 ($P_{32}$): $0.10$ (10%).
    - Permanece F2 ($P_{33}$): $1 - (0.05 + 0.10) = \mathbf{0.85}$.

**Matriz resultante:** $$P = \begin{bmatrix} 0.93 & 0.05 & 0.02 \ 0.10 & 0.80 & 0.10 \ 0.05 & 0.10 & 0.85 \end{bmatrix}$$

#### C. Cálculos para el próximo mes

Utilizamos la fórmula de predicción de estado $\pi(1) = \pi(0) \cdot P$:

$$\pi(1) = [0.50, \quad 0.25, \quad 0.25] \begin{bmatrix} 0.93 & 0.05 & 0.02 \ 0.10 & 0.80 & 0.10 \ 0.05 & 0.10 & 0.85 \end{bmatrix}$$

Realizamos las operaciones de producto matriz-vector paso a paso:

1. **Probabilidad de No fumadores ($\pi_{NF}(1)$):** $$(0.50 \times 0.93) + (0.25 \times 0.10) + (0.25 \times 0.05)$$ $$0.465 + 0.025 + 0.0125 = \mathbf{0.5025}$$
    
2. **Probabilidad de Fumadores $\leq 1$ paquete ($\pi_{F1}(1)$):** $$(0.50 \times 0.05) + (0.25 \times 0.80) + (0.25 \times 0.10)$$ $$0.025 + 0.20 + 0.025 = \mathbf{0.25}$$
    
3. **Probabilidad de Fumadores $> 1$ paquete ($\pi_{F2}(1)$):** $$(0.50 \times 0.02) + (0.25 \times 0.10) + (0.25 \times 0.85)$$ $$0.01 + 0.025 + 0.2125 = \mathbf{0.2475}$$
    

#### D. Conversión a número de individuos

Multiplicamos las probabilidades obtenidas por la población total ($N = 10,000$):

- **No fumadores:** $0.5025 \times 10,000 = \mathbf{5,025}$.
- **Fumadores $\leq 1$ paquete:** $0.25 \times 10,000 = \mathbf{2,500}$.
- **Fumadores $> 1$ paquete:** $0.2475 \times 10,000 = \mathbf{2,475}$.

### 3. Resultado Final y Verificación

El próximo mes habrá:

- **5,025** individuos que **no fuman**.
- **2,500** individuos que fuman **un paquete diario o menos**.
- **2,475** individuos que fuman **más de un paquete diario**.

**Verificación:** La suma total debe ser igual a la población original: $$5,025 + 2,500 + 2,475 = 10,000 \text{ habitantes. El cálculo es correcto.}$$