Este es un ejercicio de **procesos estocásticos**, específicamente sobre **Cadenas de Markov en tiempo discreto**. Se identifica como tal porque el sistema puede estar en un número finito de situaciones denominadas **estados** (modelos de computadora $M1, M2, M3$), las probabilidades de cambio son fijas y dependen únicamente del estado actual (Propiedad de Markov), y el proceso ocurre en intervalos de tiempo fijos (cada dos años).

### Diagrama de la Cadena de Markov

A continuación se presenta el diagrama de estados siguiendo el patrón de posicionamiento circular y la paleta de colores establecida en la guía técnica.

```tikz
%\documentclass[tikz,border=10pt]{standalone}
%\usepackage[utf8]{inputenc}
\begin{document}
\begin{tikzpicture}

% CONFIGURACIÓN DE NODOS (Posicionamiento circular)
% M1: (6,10) - orange
% M2: (9.46,4) - pink
% M3: (2.54,4) - lime

\node[draw,circle,thick,color=orange,minimum size=1.2cm] (M1) at (6,10) {\textbf{M1}};
\node[draw,circle,thick,color=pink,minimum size=1.2cm] (M2) at (9.46,4) {\textbf{M2}};
\node[draw,circle,thick,color=lime,minimum size=1.2cm] (M3) at (2.54,4) {\textbf{M3}};

% ESTADO M1 (orange)
\draw[->,ultra thick,orange] (M1) .. controls (5,12) and (7,12) ..node[pos=0.5,above,black] {$0.65$} (M1);
\draw[->,very thick,orange] (M1) to[bend left=10] node[pos=0.3,right,black] {$0.20$} (M2);
\draw[->,very thick,orange] (M1) to[bend left=10] node[pos=0.3,left,black] {$0.15$} (M3);

% ESTADO M2 (pink)
\draw[->,ultra thick,pink] (M2) .. controls (11,4) and (11,2) ..node[pos=0.5,right,black] {$0.15$} (M2);
\draw[->,very thick,pink] (M2) to[bend left=20] node[pos=0.3,left,black] {$0.60$} (M1);
\draw[->,very thick,pink] (M2) to[bend left=20] node[pos=0.3,below,black] {$0.25$} (M3);

% ESTADO M3 (lime)
\draw[->,ultra thick,lime] (M3) .. controls (1,2) and (1,4) ..node[pos=0.5,left,black] {$0.40$} (M3);
\draw[->,very thick,lime] (M3) to[bend left=30] node[pos=0.3,right,black] {$0.50$} (M1);
\draw[->,very thick,lime] (M3) to[bend left=30] node[pos=0.3,above,black] {$0.10$} (M2);

\end{tikzpicture}
\end{document}
```

---

### Resolución del Ejercicio

#### 1. Identificación de los Datos del Problema

El sistema tiene tres estados posibles que representan el modelo de computadora poseído:

- **Estado 1 ($M_1$):** Poseer el modelo de computadora 1.
- **Estado 2 ($M_2$):** Poseer el modelo de computadora 2.
- **Estado 3 ($M_3$):** Poseer el modelo de computadora 3.

Las probabilidades condicionales de transición dadas son:

- **Desde $M1$:** $P(M2|M1) = 0.2$; $P(M3|M1) = 0.15$.
- **Desde $M2$:** $P(M1|M2) = 0.6$; $P(M3|M2) = 0.25$.
- **Desde $M3$:** $P(M1|M3) = 0.5$; $P(M2|M3) = 0.1$.

#### 2. Fórmulas Utilizadas y Razonamiento

La matriz de transición $P$ organiza las probabilidades de moverse del estado $i$ al estado $j$ en un solo paso: $$P = \begin{bmatrix} P_{11} & P_{12} & P_{13} \ P_{21} & P_{22} & P_{23} \ P_{31} & P_{32} & P_{33} \end{bmatrix}$$

Una propiedad fundamental de las matrices estocásticas es que **la suma de las probabilidades de cada renglón debe ser igual a 1**. Esto se debe a que los estados son colectivamente exhaustivos y el profesor debe elegir uno de los tres modelos para el siguiente periodo. Si la probabilidad de permanecer en el mismo estado ($P_{ii}$) no se indica, se calcula mediante el despeje: $$P_{ii} = 1 - \sum_{j \neq i} P_{ij}$$

#### 3. Sustitución de Valores y Operaciones Parciales

Se procede a calcular las probabilidades de "no cambio" o permanencia en cada estado:

- **Para el renglón 1 (Desde $M_1$):** Dados $P_{12} = 0.2$ y $P_{13} = 0.15$: $$P_{11} = 1 - (0.2 + 0.15)$$ $$P_{11} = 1 - 0.35 = 0.65$$
    
- **Para el renglón 2 (Desde $M_2$):** Dados $P_{21} = 0.6$ y $P_{23} = 0.25$: $$P_{22} = 1 - (0.6 + 0.25)$$ $$P_{22} = 1 - 0.85 = 0.15$$
    
- **Para el renglón 3 (Desde $M_3$):** Dados $P_{31} = 0.5$ y $P_{32} = 0.1$: $$P_{33} = 1 - (0.5 + 0.1)$$ $$P_{33} = 1 - 0.60 = 0.40$$
    

#### 4. Resultado Final: Matriz de Transición

Insertando los valores conocidos y los calculados en la estructura matricial, obtenemos: $$P = \begin{bmatrix} 0.65 & 0.20 & 0.15 \ 0.60 & 0.15 & 0.25 \ 0.50 & 0.10 & 0.40 \end{bmatrix}$$

#### 5. Verificación del Resultado

Se comprueba que cada fila sume exactamente la unidad:

- Fila 1 ($M1$): $0.65 + 0.20 + 0.15 = 1.00$ (Correcto)
- Fila 2 ($M2$): $0.60 + 0.15 + 0.25 = 1.00$ (Correcto)
- Fila 3 ($M3$): $0.50 + 0.10 + 0.40 = 1.00$ (Correcto)

La matriz resultante describe completamente el comportamiento de compra del profesor cada dos años.


# 22222


Este es un ejercicio de **procesos estocásticos**, específicamente sobre **Cadenas de Markov de tiempo discreto**. Se identifica como tal porque cumple con las tres condiciones fundamentales: tiene estados finitos (comprar o no comprar), probabilidades de transición constantes en el tiempo y la propiedad de Markov, donde el estado futuro depende solo del estado actual.

### Diagrama de la Cadena de Markov

Siguiendo las reglas de diseño para $N=2$ estados, los nodos se ubican en una línea horizontal.

```tikz
%\documentclass[tikz,border=10pt]{standalone}
%\usepackage[utf8]{inputenc}
\begin{document}
\begin{tikzpicture}

% CONFIGURACIÓN DE NODOS (Posicionamiento horizontal para N=2)
% Estado 1 (C): (2,6) - orange
% Estado 2 (NC): (10,6) - pink

\node[draw,circle,thick,color=orange,minimum size=1.5cm] (C) at (2,6) {\textbf{C}};
\node[draw,circle,thick,color=pink,minimum size=1.5cm] (NC) at (10,6) {\textbf{NC}};

% ESTADO 1: Comprar (C) - orange
\draw[->,ultra thick,orange] (C) .. controls (1,8) and (3,8) ..node[pos=0.5,above,black] {$0.8$} (C);
\draw[->,very thick,orange] (C) to[bend left=20] node[pos=0.5,above,black] {$0.2$} (NC);

% ESTADO 2: No Comprar (NC) - pink
\draw[->,ultra thick,pink] (NC) .. controls (9,8) and (11,8) ..node[pos=0.5,above,black] {$0.7$} (NC);
\draw[->,very thick,pink] (NC) to[bend left=20] node[pos=0.5,below,black] {$0.3$} (C);

\end{tikzpicture}
\end{document}
```

---

### Resolución del Ejercicio

#### 1. Identificación de los Datos del Problema

- **Población total ($N$):** $1000$ individuos.
- **Estados del sistema:**
    - **Estado 1 ($C$):** Comprar el producto.
    - **Estado 2 ($NC$):** No comprar el producto.
- **Probabilidades de transición dadas:**
    - Probabilidad de pasar de $C$ a $NC$: $P_{12} = 0.2$.
    - Probabilidad de pasar de $NC$ a $C$: $P_{21} = 0.3$.
- **Estado inicial (Mes 1):**
    - Individuos que compran: $100$.
    - Individuos que no compran: $1000 - 100 = 900$.

#### 2. Fórmulas Utilizadas y Razonamiento

Para proyectar la población, utilizaremos la **matriz de probabilidades de transición ($P$)** y el **vector de probabilidades de estado ($\pi$)**.

- **Matriz de Transición ($P$):** Organiza las probabilidades $P_{ij}$ de transición entre estados. Cada fila debe sumar 1.
- **Relación Recurrente:** El estado en el periodo $n+1$ se halla multiplicando el vector del periodo actual por la matriz: $$\pi(n+1) = \pi(n) \cdot P$$

#### 3. Desarrollo Paso a Paso

**Paso 1: Construcción de la matriz de transición $P$** Calculamos las probabilidades de permanencia (probabilidades de que no haya cambio):

- $P_{11} = 1 - P_{12} = 1 - 0.2 = 0.8$ (Seguir comprando).
- $P_{22} = 1 - P_{21} = 1 - 0.3 = 0.7$ (Seguir sin comprar). La matriz resulta en: $$P = \begin{bmatrix} 0.8 & 0.2 \ 0.3 & 0.7 \end{bmatrix}$$

**Paso 2: Definición del vector de estado inicial $\pi(1)$** Expresamos la población inicial como probabilidades dividiendo cada grupo entre el total ($1000$):

- $\pi_1(1) = 100 / 1000 = 0.1$
- $\pi_2(1) = 900 / 1000 = 0.9$ $$\pi(1) = [0.1, \quad 0.9]$$

**Paso 3: Cálculo para el mes próximo (Mes 2)** Aplicamos la multiplicación vector-matriz: $$\pi(2) = [0.1, \quad 0.9] \begin{bmatrix} 0.8 & 0.2 \ 0.3 & 0.7 \end{bmatrix}$$

- $\pi_1(2) = (0.1 \times 0.8) + (0.9 \times 0.3) = 0.08 + 0.27 = 0.35$
- $\pi_2(2) = (0.1 \times 0.2) + (0.9 \times 0.7) = 0.02 + 0.63 = 0.65$ Convertimos a número de individuos:
- Compradores = $0.35 \times 1000 = \mathbf{350}$.

**Paso 4: Cálculo para dentro de dos meses (Mes 3)** Tomamos el vector $\pi(2)$ y volvemos a multiplicar por $P$: $$\pi(3) = [0.35, \quad 0.65] \begin{bmatrix} 0.8 & 0.2 \ 0.3 & 0.7 \end{bmatrix}$$

- $\pi_1(3) = (0.35 \times 0.8) + (0.65 \times 0.3) = 0.28 + 0.195 = 0.475$
- $\pi_2(3) = (0.35 \times 0.2) + (0.65 \times 0.7) = 0.07 + 0.455 = 0.525$ Convertimos a número de individuos:
- Compradores = $0.475 \times 1000 = \mathbf{475}$.

#### 4. Resultado Final

- **Al mes próximo:** Comprarán el producto **350 individuos**.
- **Dentro de dos meses:** Comprarán el producto **475 individuos**.

#### 5. Verificación

En cada paso, la suma de las probabilidades es igual a 1 (100% de la población):

- Mes 2: $0.35 + 0.65 = 1.0$ (Correcto).
- Mes 3: $0.475 + 0.525 = 1.0$ (Correcto).