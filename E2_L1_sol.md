### **Soporte y Longitud de la Secuencia**

La longitud de la convolución lineal $y(n)$ de dos secuencias de duración finita de longitudes $L_x$ y $L_h$ se calcula mediante:

$$
L_y = L_x + L_h - 1
$$


Para $L_x = 4$ y $L_h = 3$:

$$
L_y = 4 + 3 - 1 = 6
$$


El soporte temporal de $y(n)$ se determina por los límites de las señales individuales:
*   **Índice de inicio:** $n_{\text{min}} = n_{x,\text{min}} + n_{h,\text{min}} = 0 + 0 = 0$
*   **Índice de finalización:** $n_{\text{max}} = n_{x,\text{max}} + n_{h,\text{max}} = 3 + 2 = 5$

Por lo tanto, el soporte de la salida corresponde a **$n = 0, 1, 2, 3, 4, 5$**.

---

### **Fórmula de la Suma de Convolución**

La convolución lineal discreta se define como:

$$
y(n) = \sum_{k=-\infty}^{\infty} x(k)h(n-k)
$$


Dado que la secuencia de entrada $x(k)$ es nula fuera del intervalo $0 \le k \le 3$, la sumatoria se reduce a:

$$
y(n) = \sum_{k=0}^{3} x(k)h(n-k)
$$


Sustituyendo los valores de $x(k) = 1$ para $k \in$:

$$
y(n) = h(n) + h(n-1) + h(n-2) + h(n-3)
$$


---

### **Desarrollo Término a Término**

*   **Para $n = 0$:**
    
$$
y(0) = x(0)h(0) = 1 \cdot 1 = 1
$$


*   **Para $n = 1$:**
    
$$
y(1) = x(0)h(1) + x(1)h(0) = 1 \cdot 2 + 1 \cdot 1 = 3
$$


*   **Para $n = 2$:**
    
$$
y(2) = x(0)h(2) + x(1)h(1) + x(2)h(0) = 1 \cdot 3 + 1 \cdot 2 + 1 \cdot 1 = 6
$$


*   **Para $n = 3$:**
    
$$
y(3) = x(0)h(3) + x(1)h(2) + x(2)h(1) + x(3)h(0) = 1 \cdot 0 + 1 \cdot 3 + 1 \cdot 2 + 1 \cdot 1 = 6
$$


*   **Para $n = 4$:**
    
$$
y(4) = x(1)h(3) + x(2)h(2) + x(3)h(1) = 1 \cdot 0 + 1 \cdot 3 + 1 \cdot 2 = 5
$$


*   **Para $n = 5$:**
    
$$
y(5) = x(2)h(3) + x(3)h(2) = 1 \cdot 0 + 1 \cdot 3 = 3
$$


---

### **Tabla de Productos Desplazados**

El cálculo se puede verificar y visualizar estructuradamente mediante la siguiente tabla deslizante:

| $k$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | Suma de productos $y(n)$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **$x(k)$** | **1** | **1** | **1** | **1** | **0** | **0** | |
| $h(0-k)$ | 1 | 0 | 0 | 0 | 0 | 0 | **$y(0) = 1$** |
| $h(1-k)$ | 2 | 1 | 0 | 0 | 0 | 0 | **$y(1) = 3$** |
| $h(2-k)$ | 3 | 2 | 1 | 0 | 0 | 0 | **$y(2) = 6$** |
| $h(3-k)$ | 0 | 3 | 2 | 1 | 0 | 0 | **$y(3) = 6$** |
| $h(4-k)$ | 0 | 0 | 3 | 2 | 1 | 0 | **$y(4) = 5$** |
| $h(5-k)$ | 0 | 0 | 0 | 3 | 2 | 1 | **$y(5) = 3$** |

---

### **Resultado Final**

La secuencia de salida obtenida analíticamente es:

$$
y(n) = [1, \quad 3, \quad 6, \quad 6, \quad 5, \quad 3]
$$


donde el soporte está definido para los índices $n = 0, 1, 2, 3, 4, 5$.

---

### **Diagrama de Tallo y Hojas de la Señal Resultante**

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=1.2]
\draw[->] (-1,0) -- (6.5,0) node[right] {n};
\draw[->] (0,-0.5) -- (0,7) node[above] {y(n)};
\foreach \x/\y in {0/1, 1/3, 2/6, 3/6, 4/5, 5/3} {
    \draw[teal, thick] (\x,0) -- (\x,\y);
    \fill[teal] (\x,\y) circle (2.5pt);
    \node[above, yshift=2pt] at (\x,\y) {\footnotesize \y};
    \node[below, yshift=-2pt] at (\x,0) {\footnotesize \x};
}
\end{tikzpicture}
\end{document}
```

```tikz
\begin{tikzpicture}[scale=1.2]

% Ejes
\draw[->] (-1,0) -- (6.5,0) node[right] {$n$};
\draw[->] (0,-0.5) -- (0,7) node[above] {$y(n)$};

% Señal discreta
\foreach \x/\y in {
    0/1,
    1/3,
    2/6,
    3/6,
    4/5,
    5/3
}{
    \draw[teal, thick] (\x,0) -- (\x,\y);
    \fill[teal] (\x,\y) circle (2.5pt);

    % Valor de la señal
    \node[above, yshift=2pt] at (\x,\y) {\footnotesize \y};

    % Índice n
    \node[below, yshift=-2pt] at (\x,0) {\footnotesize \x};
}

\end{tikzpicture}
```

