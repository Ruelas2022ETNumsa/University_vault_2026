### Diagrama de la Cadena de Markov
```tikz
\begin{document} \begin{tikzpicture}[node distance=4cm, every node/.style={circle, draw, minimum size=1.2cm, very thick}, font=\sffamily]


% ESTADO_1: M1 (Posición: 90 grados)
\node[blue] (M1) at (6,10) {M1};

% ESTADO_2: M2 (Posición: -30 grados)
\node[teal] (M2) at (9.46,4) {M2};

% ESTADO_3: M3 (Posición: -150 grados)
\node[violet] (M3) at (2.54,4) {M3};

% TRANSICIONES ESTADO M1
\path[->, blue, ultra thick] (M1) edge [loop above] node[above] {0.65} (M1);
\path[->, blue, very thick] (M1) edge [bend left=10] node[right, pos=0.3] {0.2} (M2);
\path[->, blue, very thick] (M1) edge [bend left=10] node[left, pos=0.3] {0.15} (M3);

% TRANSICIONES ESTADO M2
\path[->, teal, ultra thick] (M2) edge [loop right] node[right] {0.15} (M2);
\path[->, teal, very thick] (M2) edge [bend left=20] node[left, pos=0.3] {0.6} (M1);
\path[->, teal, very thick] (M2) edge [bend left=20] node[below, pos=0.3] {0.25} (M3);

% TRANSICIONES ESTADO M3
\path[->, violet, ultra thick] (M3) edge [loop left] node[left] {0.4} (M3);
\path[->, violet, very thick] (M3) edge [bend left=30] node[right, pos=0.3] {0.5} (M1);
\path[->, violet, very thick] (M3) edge [bend left=30] node[above, pos=0.3] {0.1} (M2);


\end{tikzpicture} \end{document}
```



---

### Análisis Técnico del Ejercicio

#### 1. Identificación del Tipo de Ejercicio y Tema

Este es un ejercicio de **Procesos Estocásticos**, específicamente sobre **Cadenas de Markov de tiempo discreto**. Se identifica como tal porque el sistema presenta un número finito de estados (modelos de computadora) y la probabilidad de pasar a un estado futuro depende únicamente del estado actual (el modelo que el profesor tiene en el presente), cumpliendo así con la **Propiedad de Markov**. El proceso ocurre en pasos discretos (cada dos años, coincidiendo con la adquisición de una nueva máquina).

#### 2. Identificación de los Datos del Problema

El problema define tres estados posibles para el sistema en cualquier punto del tiempo $n$:

- **Estado 1 ($M_1$):** El profesor posee el modelo de computadora 1.
- **Estado 2 ($M_2$):** El profesor posee el modelo de computadora 2.
- **Estado 3 ($M_3$):** El profesor posee el modelo de computadora 3.

Las probabilidades condicionales de transición dadas son:

- **Desde $M_1$:**
    - Probabilidad de pasar a $M_2$: $P_{12} = 0.2$
    - Probabilidad de pasar a $M_3$: $P_{13} = 0.15$
- **Desde $M_2$:**
    - Probabilidad de pasar a $M_1$: $P_{21} = 0.6$
    - Probabilidad de pasar a $M_3$: $P_{23} = 0.25$
- **Desde $M_3$:**
    - Probabilidad de pasar a $M_1$: $P_{31} = 0.5$
    - Probabilidad de pasar a $M_2$: $P_{32} = 0.1$

#### 3. Explicación de lo que se Pide

Se solicita hallar la **matriz de probabilidades de transición ($P$)**. Esta matriz organiza todas las probabilidades de cambio entre los estados de forma que el elemento en la fila $i$ y columna $j$ represente la probabilidad de que el sistema pase al estado $j$ en el siguiente paso, dado que actualmente se encuentra en el estado $i$.

#### 4. Fórmulas Utilizadas y Razonamiento

Para construir la matriz, aplicamos la definición de una **Matriz Estocástica**: $$P = \begin{bmatrix} P_{11} & P_{12} & P_{13} \ P_{21} & P_{22} & P_{23} \ P_{31} & P_{32} & P_{33} \end{bmatrix}$$

Un requisito fundamental es que **los valores de probabilidad para cualquier renglón deben sumar 1**. Esto se debe a que el sistema debe estar obligatoriamente en uno de los estados definidos en el siguiente periodo (ley de probabilidad total). La fórmula para las probabilidades de "permanencia" (auto-transición) es: $$P_{ii} = 1 - \sum_{j \neq i} P_{ij}$$

#### 5. Sustitución de Valores y Operaciones Intermedias

**Paso 1: Calcular las probabilidades de permanecer en el mismo estado ($P_{ii}$)**

- **Para el Estado 1 ($M_1$):** Sabemos que $P_{12} = 0.2$ y $P_{13} = 0.15$. $$P_{11} = 1 - (P_{12} + P_{13})$$ $$P_{11} = 1 - (0.2 + 0.15)$$ $$P_{11} = 1 - 0.35 = 0.65$$
    
- **Para el Estado 2 ($M_2$):** Sabemos que $P_{21} = 0.6$ y $P_{23} = 0.25$. $$P_{22} = 1 - (P_{21} + P_{23})$$ $$P_{22} = 1 - (0.6 + 0.25)$$ $$P_{22} = 1 - 0.85 = 0.15$$
    
- **Para el Estado 3 ($M_3$):** Sabemos que $P_{31} = 0.5$ y $P_{32} = 0.1$. $$P_{33} = 1 - (P_{31} + P_{32})$$ $$P_{33} = 1 - (0.5 + 0.1)$$ $$P_{33} = 1 - 0.6 = 0.4$$
    

#### 6. Resultado Final: Matriz de Transición

Insertamos los valores obtenidos y los proporcionados en la estructura matricial:

$$P = \begin{bmatrix} 0.65 & 0.20 & 0.15 \\ 0.60 & 0.15 & 0.25 \\ 0.50 & 0.10 & 0.40 \end{bmatrix}$$

#### 7. Verificación del Resultado

Para asegurar que la matriz es válida (estocástica por renglones), sumamos los elementos de cada fila:

- **Fila 1:** $0.65 + 0.20 + 0.15 = 1.00$ (Correcto)
- **Fila 2:** $0.60 + 0.15 + 0.25 = 1.00$ (Correcto)
- **Fila 3:** $0.50 + 0.10 + 0.40 = 1.00$ (Correcto)

La matriz cumple con todas las propiedades de una cadena de Markov homogénea y finita.