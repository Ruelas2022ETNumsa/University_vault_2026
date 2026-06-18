Este ejercicio se identifica como una **Cadena de Markov en tiempo discreto**. Presenta un número finito de estados (categorías de fumadores), probabilidades de transición constantes de un mes al siguiente y la propiedad de que la situación futura depende únicamente del estado actual.

### Diagrama de la Cadena de Markov

```tikz
\begin{document}
\begin{tikzpicture}
% Definición de estados (N=3, posicionamiento circular)
\node[draw,circle,thick,color=orange] (NF) at (90:4) {NF};
\node[draw,circle,thick,color=pink] (F1) at (210:4) {F1};
\node[draw,circle,thick,color=lime] (F2) at (330:4) {F2};

% Bucles (Permanencia en el estado)
\draw[->,ultra thick,orange] (NF) .. controls (70:6) and (110:6) .. node[above] {$0.93$} (NF);
\draw[->,ultra thick,pink] (F1) .. controls (190:6) and (230:6) .. node[left] {$0.80$} (F1);
\draw[->,ultra thick,lime] (F2) .. controls (310:6) and (350:6) .. node[right] {$0.85$} (F2);

% Flechas de transición
\draw[->,very thick,orange] (NF) to[bend left=20] node[pos=0.2, right] {$0.05$} (F1);
\draw[->,very thick,orange] (NF) to[bend right=20] node[pos=0.2, left] {$0.02$} (F2);

\draw[->,very thick,pink] (F1) to[bend left=20] node[pos=0.2, left] {$0.10$} (NF);
\draw[->,very thick,pink] (F1) to[bend left=20] node[pos=0.2, above] {$0.10$} (F2);

\draw[->,very thick,lime] (F2) to[bend right=20] node[pos=0.2, right] {$0.05$} (NF);
\draw[->,very thick,lime] (F2) to[bend left=20] node[pos=0.2, below] {$0.10$} (F1);

\end{tikzpicture}
\end{document}
```

---

### Resolución del Ejercicio

#### 1. Identificación de datos y estados

- **Población total ($N$):** $10,000$ habitantes.
- **Estados del sistema:**
    - **Estado 1 ($NF$):** No fumadores.
    - **Estado 2 ($F1$):** Fuman un paquete o menos diariamente.
    - **Estado 3 ($F2$):** Fuman más de un paquete diariamente.
- **Distribución inicial (Mes 0):**
    - $\pi_{NF}(0) = 5,000 / 10,000 = 0.50$.
    - $\pi_{F1}(0) = 2,500 / 10,000 = 0.25$.
    - $\pi_{F2}(0) = 2,500 / 10,000 = 0.25$.
    - Vector inicial: $\pi(0) = [0.50, \quad 0.25, \quad 0.25]$.

#### 2. Construcción de la matriz de transición ($P$)

Las probabilidades se organizan por renglones, asegurando que la suma de cada uno sea igual a 1 (probabilidad total).

- **Renglón 1 (Desde NF):** Hacia F1 es $0.05$; hacia F2 es $0.02$; permanece en NF: $1 - (0.05 + 0.02) = 0.93$.
- **Renglón 2 (Desde F1):** Hacia NF es $0.10$; hacia F2 es $0.10$; permanece en F1: $1 - (0.10 + 0.10) = 0.80$.
- **Renglón 3 (Desde F2):** Hacia NF es $0.05$; hacia F1 es $0.10$; permanece en F2: $1 - (0.05 + 0.10) = 0.85$.

La matriz de transición resultante es: $$P = \begin{bmatrix} 0.93 & 0.05 & 0.02 \ 0.10 & 0.80 & 0.10 \ 0.05 & 0.10 & 0.85 \end{bmatrix}$$

#### 3. Proyección para el próximo mes (Mes 1)

Se utiliza la fórmula $\pi(n+1) = \pi(n) \cdot P$ para calcular la distribución del siguiente periodo.

**Cálculo de $\pi_{NF}(1)$ (Individuos que no fuman):** $\pi_{NF}(1) = (0.50 \times 0.93) + (0.25 \times 0.10) + (0.25 \times 0.05)$. $\pi_{NF}(1) = 0.465 + 0.025 + 0.0125 = \mathbf{0.5025}$.

**Cálculo de $\pi_{F1}(1)$ (Fuman $\le 1$ paquete):** $\pi_{F1}(1) = (0.50 \times 0.05) + (0.25 \times 0.80) + (0.25 \times 0.10)$. $\pi_{F1}(1) = 0.025 + 0.20 + 0.025 = \mathbf{0.25}$.

**Cálculo de $\pi_{F2}(1)$ (Fuman $> 1$ paquete):** $\pi_{F2}(1) = (0.50 \times 0.02) + (0.25 \times 0.10) + (0.25 \times 0.85)$. $\pi_{F2}(1) = 0.01 + 0.025 + 0.2125 = \mathbf{0.2475}$.

#### 4. Conversión a número de individuos

Multiplicamos las probabilidades obtenidas por la población total ($10,000$ habitantes).

- **No fumadores:** $0.5025 \times 10,000 = \mathbf{5,025}$.
- **Fumadores $\le 1$ paquete:** $0.25 \times 10,000 = \mathbf{2,500}$.
- **Fumadores $> 1$ paquete:** $0.2475 \times 10,000 = \mathbf{2,475}$.

---

### Resultado Final

El próximo mes la población se distribuirá de la siguiente manera:

- **5,025** individuos que no fuman.
- **2,500** individuos que fuman un paquete diario o menos.
- **2,475** individuos que fuman más de un paquete diario.

**Verificación:** La suma total es $5025 + 2500 + 2475 = 10,000$ habitantes, lo que confirma que el cálculo es correcto.