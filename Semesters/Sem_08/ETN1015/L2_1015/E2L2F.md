---
title: "E2L2F — Convolución Circular con Secuencia Modificada (N = 5)"
subject: ETN1015
method: Gráfico — Círculos Concéntricos (Palani Fig. 2.11)
source: S. Palani — Cap. 2, Ej. 2.22
status: final
---

# Convolución Circular con Secuencia Modificada ($N = 5$)

## Datos del problema

$$
x_1(n) = \{2, 1, 2, 1\} \xrightarrow{\text{zero-pad}} \{2, 1, 2, 1, 0\}, \quad n = 0, 1, 2, 3, 4
$$

$$
x_2(n) = \{1, 2, 3, 4, 5\}, \quad n = 0, 1, 2, 3, 4
$$

$$
N = 5 \quad \text{(longitud de la secuencia más larga)}
$$

> **Zero-padding:** $x_1(n)$ tiene 4 muestras. Se agrega un cero al final para igualar $N = 5$, requerido por la operación de convolución circular de $N$ puntos.

---

## 1. Definición formal

Dadas dos secuencias discretas de longitud $N$, la convolución circular se define como:

$$
x_3(m) = x_1(n) \circledcirc_N x_2(n) = \sum_{n=0}^{N-1} x_1(n)\, x_2\!\left((m-n)_N\right), \quad m = 0, 1, \dots, N-1
$$

donde $(m-n)_N$ es la operación de índice módulo $N$, que mantiene los índices dentro del rango $[0,\, N-1]$.

---

## 2. Método gráfico — Círculos concéntricos (Palani Fig. 2.11)

### Reglas del método

- **Círculo exterior** (fijo): $x_1(n)$ se distribuye en sentido **antihorario (CCW)** a intervalos de $\Delta\theta = 360^\circ / N = 72^\circ$, comenzando en $0^\circ$.
- **Círculo interior** (móvil): $x_2(n)$ se coloca en sentido **horario (CW)** — esto emula la inversión temporal $x_2(-n)$ implícita en la definición de convolución.
- **Cálculo de cada muestra:** se multiplican par a par los valores alineados radialmente y se suman los productos.
- **Avance temporal:** para pasar de $m$ a $m+1$, el círculo interior rota $72^\circ$ en sentido **CCW**.

---

### Paso $m = 0$ — Sin rotación

Disposición inicial: $x_2(0)$ alineado con $x_1(0)$ en $0^\circ$.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=2.0, >=stealth, every node/.style={font=\small}]
  \draw[thick, teal] (0,0) circle (2.2cm);
  \draw[thick, orange] (0,0) circle (1.2cm);
  \foreach \angle in {0, 72, 144, 216, 288} {
    \draw[dashed, gray!40] (\angle:1.2cm) -- (\angle:2.2cm);
  }
  \foreach \angle in {0, 72, 144, 216, 288} { \fill[orange] (\angle:2.2cm) circle (0.06cm); }
  \node[teal, anchor=west]       at (0:2.4cm)   {\(x_1(0)=2\)};
  \node[teal, anchor=south west] at (72:2.4cm)  {\(x_1(1)=1\)};
  \node[teal, anchor=south east] at (144:2.4cm) {\(x_1(2)=2\)};
  \node[teal, anchor=north east] at (216:2.4cm) {\(x_1(3)=1\)};
  \node[teal, anchor=north west] at (288:2.4cm) {\(x_1(4)=0\)};
  \foreach \angle in {0, 288, 216, 144, 72} { \fill[teal] (\angle:1.2cm) circle (0.06cm); }
  \node[orange, anchor=west]       at (0:1.35cm)   {\(x_2(0)=1\)};
  \node[orange, anchor=north west] at (288:1.35cm) {\(x_2(1)=2\)};
  \node[orange, anchor=north east] at (216:1.35cm) {\(x_2(2)=3\)};
  \node[orange, anchor=south east] at (144:1.35cm) {\(x_2(3)=4\)};
  \node[orange, anchor=south west] at (72:1.35cm)  {\(x_2(4)=5\)};
  \draw[->, teal] (2.4,2.4) arc (45:65:2.9) node[midway, above right] {CCW};
  \draw[<-, orange] (0.9,-0.9) arc (-45:-65:1.3) node[midway, below left] {CW};
\end{tikzpicture}
\end{document}
```

$$
x_3(0) = x_1(0)x_2(0) + x_1(1)x_2(4) + x_1(2)x_2(3) + x_1(3)x_2(2) + x_1(4)x_2(1)
$$

$$
= (2 \cdot 1) + (1 \cdot 5) + (2 \cdot 4) + (1 \cdot 3) + (0 \cdot 2) = 2 + 5 + 8 + 3 + 0 = \mathbf{18}
$$

---

### Paso $m = 1$ — Rotación de $72°$ CCW

El círculo interior avanza un paso: $x_2(1)$ queda alineado con $x_1(0)$.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=2.0, >=stealth, every node/.style={font=\small}]
  \draw[thick, teal] (0,0) circle (2.2cm);
  \draw[thick, orange] (0,0) circle (1.2cm);
  \foreach \angle in {0, 72, 144, 216, 288} {
    \draw[dashed, gray!40] (\angle:1.2cm) -- (\angle:2.2cm);
  }
  \foreach \angle in {0, 72, 144, 216, 288} { \fill[orange] (\angle:2.2cm) circle (0.06cm); }
  \node[teal, anchor=west]       at (0:2.4cm)   {\(x_1(0)=2\)};
  \node[teal, anchor=south west] at (72:2.4cm)  {\(x_1(1)=1\)};
  \node[teal, anchor=south east] at (144:2.4cm) {\(x_1(2)=2\)};
  \node[teal, anchor=north east] at (216:2.4cm) {\(x_1(3)=1\)};
  \node[teal, anchor=north west] at (288:2.4cm) {\(x_1(4)=0\)};
  \foreach \angle in {0, 288, 216, 144, 72} { \fill[teal] (\angle:1.2cm) circle (0.06cm); }
  \node[orange, anchor=west]       at (0:1.35cm)   {\(x_2(1)=2\)};
  \node[orange, anchor=north west] at (288:1.35cm) {\(x_2(2)=3\)};
  \node[orange, anchor=north east] at (216:1.35cm) {\(x_2(3)=4\)};
  \node[orange, anchor=south east] at (144:1.35cm) {\(x_2(4)=5\)};
  \node[orange, anchor=south west] at (72:1.35cm)  {\(x_2(0)=1\)};
  \draw[->, teal] (2.4,2.4) arc (45:65:2.9) node[midway, above right] {CCW};
  \draw[<-, orange] (0.9,-0.9) arc (-45:-65:1.3) node[midway, below left] {CW};
\end{tikzpicture}
\end{document}
```

$$
x_3(1) = x_1(0)x_2(1) + x_1(1)x_2(0) + x_1(2)x_2(4) + x_1(3)x_2(3) + x_1(4)x_2(2)
$$

$$
= (2 \cdot 2) + (1 \cdot 1) + (2 \cdot 5) + (1 \cdot 4) + (0 \cdot 3) = 4 + 1 + 10 + 4 + 0 = \mathbf{19}
$$

---

### Paso $m = 2$ — Rotación acumulada de $144°$ CCW

$x_2(2)$ queda alineado con $x_1(0)$.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=2.0, >=stealth, every node/.style={font=\small}]
  \draw[thick, teal] (0,0) circle (2.2cm);
  \draw[thick, orange] (0,0) circle (1.2cm);
  \foreach \angle in {0, 72, 144, 216, 288} {
    \draw[dashed, gray!40] (\angle:1.2cm) -- (\angle:2.2cm);
  }
  \foreach \angle in {0, 72, 144, 216, 288} { \fill[orange] (\angle:2.2cm) circle (0.06cm); }
  \node[teal, anchor=west]       at (0:2.4cm)   {\(x_1(0)=2\)};
  \node[teal, anchor=south west] at (72:2.4cm)  {\(x_1(1)=1\)};
  \node[teal, anchor=south east] at (144:2.4cm) {\(x_1(2)=2\)};
  \node[teal, anchor=north east] at (216:2.4cm) {\(x_1(3)=1\)};
  \node[teal, anchor=north west] at (288:2.4cm) {\(x_1(4)=0\)};
  \foreach \angle in {0, 288, 216, 144, 72} { \fill[teal] (\angle:1.2cm) circle (0.06cm); }
  \node[orange, anchor=west]       at (0:1.35cm)   {\(x_2(2)=3\)};
  \node[orange, anchor=north west] at (288:1.35cm) {\(x_2(3)=4\)};
  \node[orange, anchor=north east] at (216:1.35cm) {\(x_2(4)=5\)};
  \node[orange, anchor=south east] at (144:1.35cm) {\(x_2(0)=1\)};
  \node[orange, anchor=south west] at (72:1.35cm)  {\(x_2(1)=2\)};
  \draw[->, teal] (2.4,2.4) arc (45:65:2.9) node[midway, above right] {CCW};
  \draw[<-, orange] (0.9,-0.9) arc (-45:-65:1.3) node[midway, below left] {CW};
\end{tikzpicture}
\end{document}
```

$$
x_3(2) = x_1(0)x_2(2) + x_1(1)x_2(1) + x_1(2)x_2(0) + x_1(3)x_2(4) + x_1(4)x_2(3)
$$

$$
= (2 \cdot 3) + (1 \cdot 2) + (2 \cdot 1) + (1 \cdot 5) + (0 \cdot 4) = 6 + 2 + 2 + 5 + 0 = \mathbf{15}
$$

---

### Paso $m = 3$ — Rotación acumulada de $216°$ CCW

$x_2(3)$ queda alineado con $x_1(0)$.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=2.0, >=stealth, every node/.style={font=\small}]
  \draw[thick, teal] (0,0) circle (2.2cm);
  \draw[thick, orange] (0,0) circle (1.2cm);
  \foreach \angle in {0, 72, 144, 216, 288} {
    \draw[dashed, gray!40] (\angle:1.2cm) -- (\angle:2.2cm);
  }
  \foreach \angle in {0, 72, 144, 216, 288} { \fill[orange] (\angle:2.2cm) circle (0.06cm); }
  \node[teal, anchor=west]       at (0:2.4cm)   {\(x_1(0)=2\)};
  \node[teal, anchor=south west] at (72:2.4cm)  {\(x_1(1)=1\)};
  \node[teal, anchor=south east] at (144:2.4cm) {\(x_1(2)=2\)};
  \node[teal, anchor=north east] at (216:2.4cm) {\(x_1(3)=1\)};
  \node[teal, anchor=north west] at (288:2.4cm) {\(x_1(4)=0\)};
  \foreach \angle in {0, 288, 216, 144, 72} { \fill[teal] (\angle:1.2cm) circle (0.06cm); }
  \node[orange, anchor=west]       at (0:1.35cm)   {\(x_2(3)=4\)};
  \node[orange, anchor=north west] at (288:1.35cm) {\(x_2(4)=5\)};
  \node[orange, anchor=north east] at (216:1.35cm) {\(x_2(0)=1\)};
  \node[orange, anchor=south east] at (144:1.35cm) {\(x_2(1)=2\)};
  \node[orange, anchor=south west] at (72:1.35cm)  {\(x_2(2)=3\)};
  \draw[->, teal] (2.4,2.4) arc (45:65:2.9) node[midway, above right] {CCW};
  \draw[<-, orange] (0.9,-0.9) arc (-45:-65:1.3) node[midway, below left] {CW};
\end{tikzpicture}
\end{document}
```

$$
x_3(3) = x_1(0)x_2(3) + x_1(1)x_2(2) + x_1(2)x_2(1) + x_1(3)x_2(0) + x_1(4)x_2(4)
$$

$$
= (2 \cdot 4) + (1 \cdot 3) + (2 \cdot 2) + (1 \cdot 1) + (0 \cdot 5) = 8 + 3 + 4 + 1 + 0 = \mathbf{16}
$$

---

### Paso $m = 4$ — Rotación acumulada de $288°$ CCW

Último paso: $x_2(4)$ queda alineado con $x_1(0)$.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=2.0, >=stealth, every node/.style={font=\small}]
  \draw[thick, teal] (0,0) circle (2.2cm);
  \draw[thick, orange] (0,0) circle (1.2cm);
  \foreach \angle in {0, 72, 144, 216, 288} {
    \draw[dashed, gray!40] (\angle:1.2cm) -- (\angle:2.2cm);
  }
  \foreach \angle in {0, 72, 144, 216, 288} { \fill[orange] (\angle:2.2cm) circle (0.06cm); }
  \node[teal, anchor=west]       at (0:2.4cm)   {\(x_1(0)=2\)};
  \node[teal, anchor=south west] at (72:2.4cm)  {\(x_1(1)=1\)};
  \node[teal, anchor=south east] at (144:2.4cm) {\(x_1(2)=2\)};
  \node[teal, anchor=north east] at (216:2.4cm) {\(x_1(3)=1\)};
  \node[teal, anchor=north west] at (288:2.4cm) {\(x_1(4)=0\)};
  \foreach \angle in {0, 288, 216, 144, 72} { \fill[teal] (\angle:1.2cm) circle (0.06cm); }
  \node[orange, anchor=west]       at (0:1.35cm)   {\(x_2(4)=5\)};
  \node[orange, anchor=north west] at (288:1.35cm) {\(x_2(0)=1\)};
  \node[orange, anchor=north east] at (216:1.35cm) {\(x_2(1)=2\)};
  \node[orange, anchor=south east] at (144:1.35cm) {\(x_2(2)=3\)};
  \node[orange, anchor=south west] at (72:1.35cm)  {\(x_2(3)=4\)};
  \draw[->, teal] (2.4,2.4) arc (45:65:2.9) node[midway, above right] {CCW};
  \draw[<-, orange] (0.9,-0.9) arc (-45:-65:1.3) node[midway, below left] {CW};
\end{tikzpicture}
\end{document}
```

$$
x_3(4) = x_1(0)x_2(4) + x_1(1)x_2(3) + x_1(2)x_2(2) + x_1(3)x_2(1) + x_1(4)x_2(0)
$$

$$
= (2 \cdot 5) + (1 \cdot 4) + (2 \cdot 3) + (1 \cdot 2) + (0 \cdot 1) = 10 + 4 + 6 + 2 + 0 = \mathbf{22}
$$

---

## 3. Resultado final

| $m$ | Operación | $x_3(m)$ |
|:---:|---|:---:|
| 0 | $2{\cdot}1 + 1{\cdot}5 + 2{\cdot}4 + 1{\cdot}3 + 0{\cdot}2$ | **18** |
| 1 | $2{\cdot}2 + 1{\cdot}1 + 2{\cdot}5 + 1{\cdot}4 + 0{\cdot}3$ | **19** |
| 2 | $2{\cdot}3 + 1{\cdot}2 + 2{\cdot}1 + 1{\cdot}5 + 0{\cdot}4$ | **15** |
| 3 | $2{\cdot}4 + 1{\cdot}3 + 2{\cdot}2 + 1{\cdot}1 + 0{\cdot}5$ | **16** |
| 4 | $2{\cdot}5 + 1{\cdot}4 + 2{\cdot}3 + 1{\cdot}2 + 0{\cdot}1$ | **22** |

$$
\boxed{x_3(m) = \{18,\ 19,\ 15,\ 16,\ 22\}, \quad m = 0, 1, 2, 3, 4}
$$

---

## 4. Código MATLAB / Octave

Verificación mediante el método de la matriz circulante y visualización con `stem`.

```matlab
% ETN1015 — Convolución circular (N = 5) — Matriz circulante
% Fuente: S. Palani — Cap. 2, Ej. 2.22
clear; clc; close all;

% Secuencias de entrada
x1 = [2, 1, 2, 1, 0];   % x1(n) con zero-padding para N = 5
x2 = [1, 2, 3, 4, 5];   % x2(n) de longitud N = 5
N  = 5;

% Construcción de la matriz circulante asociada a x2
H = zeros(N, N);
for n = 0:N-1
    H(:, n+1) = x2(mod((0:N-1) - n, N) + 1);
end

% Convolución circular: producto matricial
x3 = (H * x1')';

% Visualización
m = 0:N-1;
figure(1);
stem(m, x3, 'filled', 'LineWidth', 1.5, 'Color', [0.8500 0.3250 0.0980]);
xlabel('Indice de tiempo m');
ylabel('Amplitud x3(m)');
title('Convolucion circular x3(m) = x1(n) \otimes_5 x2(n)');
xlim([-0.5, N-0.5]);
ylim([0, max(x3)+2]);
set(gca, 'XTick', m);
grid on;
```

> **Resultado esperado:** `x3 = [18, 19, 15, 16, 22]`
