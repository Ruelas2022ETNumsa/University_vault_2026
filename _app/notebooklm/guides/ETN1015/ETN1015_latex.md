---
title: KaTeX — Guía de notación para NotebookLM (ETN1015)
galaxy_body: beacon
scope: vault
tool: notebooklm
audience:
  - notebooklm
tags:
  - beacon
  - latex
  - katex
  - infraestructura
  - ETN1015
date_created: 2026-08-17
date_updated: 2026-08-17
status: activo
---

# Guía de notación KaTeX para NotebookLM — ETN1015

Esta guía define la notación que NotebookLM debe usar al generar ecuaciones para ETN1015 (Procesamiento Digital de Señales).
Las ecuaciones se entregan con delimitadores estándar: `\(...\)` para inline y `\[...\]` para display.
Obsidian las renderiza con KaTeX — seguir estos ejemplos exactamente.

---

## 1. Delimitadores

```
Inline:  \( expresión \)
Display: \[ expresión \]
```

Nunca usar `$...$` ni `$$...$$`.

---

## 2. Señales y secuencias discretas

```latex
\( x[n] \)            ← señal discreta genérica
\( x(t) \)            ← señal continua
\( h[n] \)            ← respuesta al impulso (sistema discreto)
\( y[n] \)            ← salida del sistema
\( \delta[n] \)       ← impulso unitario discreto
\( u[n] \)            ← escalón unitario discreto
```

Convolución discreta:

```latex
\[
y[n] = x[n] * h[n] = \sum_{k=-\infty}^{\infty} x[k]\, h[n-k]
\]
```

---

## 3. Transformada Z

Definición:

```latex
\[
X(z) = \sum_{n=-\infty}^{\infty} x[n]\, z^{-n}
\]
```

Par transformada:

```latex
\( x[n] \xleftrightarrow{\mathcal{Z}} X(z) \)
```

Transformada inversa Z:

```latex
\[
x[n] = \dfrac{1}{2\pi j} \oint_C X(z)\, z^{n-1}\, dz
\]
```

Región de convergencia:

```latex
\( \text{ROC}: r_1 < |z| < r_2 \)
```

---

## 4. DTFT — Transformada de Fourier en tiempo discreto

Definición:

```latex
\[
X\!\left(e^{j\omega}\right) = \sum_{n=-\infty}^{\infty} x[n]\, e^{-j\omega n}
\]
```

Transformada inversa:

```latex
\[
x[n] = \dfrac{1}{2\pi} \int_{-\pi}^{\pi} X\!\left(e^{j\omega}\right) e^{j\omega n}\, d\omega
\]
```

Par transformada:

```latex
\( x[n] \xleftrightarrow{\text{DTFT}} X\!\left(e^{j\omega}\right) \)
```

---

## 5. DFT — Transformada Discreta de Fourier

Definición (N-puntos):

```latex
\[
X[k] = \sum_{n=0}^{N-1} x[n]\, e^{-j\frac{2\pi}{N}kn}, \quad k = 0, 1, \ldots, N-1
\]
```

Transformada inversa (IDFT):

```latex
\[
x[n] = \dfrac{1}{N} \sum_{k=0}^{N-1} X[k]\, e^{j\frac{2\pi}{N}kn}, \quad n = 0, 1, \ldots, N-1
\]
```

Factor de giro:

```latex
\( W_N = e^{-j\frac{2\pi}{N}} \)
```

Forma compacta:

```latex
\[
X[k] = \sum_{n=0}^{N-1} x[n]\, W_N^{kn}
\]
```

---

## 6. Función de transferencia H(z)

Forma general:

```latex
\[
H(z) = \dfrac{Y(z)}{X(z)} = \dfrac{\displaystyle\sum_{k=0}^{M} b_k\, z^{-k}}{\displaystyle 1 + \sum_{k=1}^{N} a_k\, z^{-k}}
\]
```

Forma de polos y ceros:

```latex
\[
H(z) = G\, \dfrac{\displaystyle\prod_{k=1}^{M}(1 - c_k\, z^{-1})}{\displaystyle\prod_{k=1}^{N}(1 - d_k\, z^{-1})}
\]
```

---

## 7. Ecuación en diferencias

Forma general:

```latex
\[
y[n] = -\sum_{k=1}^{N} a_k\, y[n-k] + \sum_{k=0}^{M} b_k\, x[n-k]
\]
```

---

## 8. Respuesta en frecuencia

```latex
\[
H\!\left(e^{j\omega}\right) = \left|H\!\left(e^{j\omega}\right)\right| e^{j\angle H(e^{j\omega})}
\]
```

Magnitud y fase:

```latex
\( \left|H\!\left(e^{j\omega}\right)\right| \)    ← respuesta en magnitud
\( \angle H\!\left(e^{j\omega}\right) \)          ← respuesta en fase
```

---

## 9. Fracciones y operadores

Usar `\dfrac` siempre — nunca `\frac` solo:

```latex
\( \dfrac{z}{z - a} \)

\( \dfrac{1}{1 - a\,z^{-1}} \)

\( \dfrac{b_0 + b_1 z^{-1}}{1 - a_1 z^{-1} - a_2 z^{-2}} \)
```

Operador de retardo:

```latex
\( z^{-1} \)    ← retardo de una muestra
\( z^{-k} \)    ← retardo de k muestras
```

---

## 10. Desarrollos multilínea

Usar `\begin{array}{rcl}` con `\\` para saltar de línea:

```latex
\[
\begin{array}{rcl}
Y(z) & = & H(z)\, X(z) \\
     & = & \dfrac{b_0 + b_1 z^{-1}}{1 - a_1 z^{-1}}\, X(z)
\end{array}
\]
```

Alineación estándar: `{rcl}` — lado izquierdo · signo · lado derecho.
Nunca `\` simple para saltar — siempre `\\`.

---

## 11. Sistema de colores

Notación: `{\color{Color} contenido}`

| Color | Uso |
|---|---|
| NavyBlue | Valores intermedios que se usarán más adelante |
| TealBlue | Resultado final del desarrollo |
| YellowOrange | Valor nuevo tras una cancelación o sustitución |
| BrickRed | Error o término incorrecto |
| OliveGreen | Sustitución — reemplazo de variable por su valor |

```latex
{\color{TealBlue} H(z) = \dfrac{1}{1 - a\,z^{-1}}}
{\color{NavyBlue} X(z) = \dfrac{z}{z-1}}
{\color{OliveGreen} z = e^{j\omega}}
```

---

## 12. Cajas de resultado

```latex
\bbox[2px,border:2px solid #008080;background:white]{\color{#008080} H(z) = \dfrac{z}{z-a}}

\bbox[2px,border:2px solid #FF4500;background:white]{\color{#FF4500} X[k] = 0 \text{ para } k \neq 0}

\boxed{y[n] = x[n] * h[n]}
```

| Tipo | Color hex | Uso |
|---|---|---|
| TD | `#008080` TealBlue | Resultado final del ejercicio |
| TA | `#FF4500` RedOrange | Resultado final de un inciso |
| B  | `#000080` NavyBlue | Valor intermedio con peso |
| `\boxed` | — | Resultado intermedio simple |

---

## 13. Flechas de transición y pares de transformada

```latex
\( \longrightarrow \)                              ← operación realizada
\( \Rightarrow \)                                  ← resultado alcanzado
\( \xleftrightarrow{\mathcal{Z}} \)                ← par Z
\( \xleftrightarrow{\text{DTFT}} \)                ← par DTFT
\( \xleftrightarrow{\text{DFT}} \)                 ← par DFT
```

---

## 14. Señales y sistemas en tiempo continuo

```latex
\( x(t) \)            ← señal continua genérica
\( h(t) \)            ← respuesta al impulso (sistema continuo)
\( y(t) \)            ← salida del sistema continuo
\( \delta(t) \)       ← impulso de Dirac
\( u(t) \)            ← escalón unitario continuo
```

Convolución continua:

```latex
\[
y(t) = x(t) * h(t) = \int_{-\infty}^{\infty} x(\tau)\, h(t-\tau)\, d\tau
\]
```

---

## 15. Transformada de Fourier continua (CTFT)

Definición:

```latex
\[
X(j\omega) = \int_{-\infty}^{\infty} x(t)\, e^{-j\omega t}\, dt
\]
```

Transformada inversa:

```latex
\[
x(t) = \dfrac{1}{2\pi} \int_{-\infty}^{\infty} X(j\omega)\, e^{j\omega t}\, d\omega
\]
```

Par transformada:

```latex
\( x(t) \xleftrightarrow{\mathcal{F}} X(j\omega) \)
```

Respuesta en frecuencia continua:

```latex
\( H(j\omega) = \left|H(j\omega)\right| e^{j\angle H(j\omega)} \)
```

---

## 16. Transformada de Laplace

Definición bilateral:

```latex
\[
X(s) = \int_{-\infty}^{\infty} x(t)\, e^{-st}\, dt
\]
```

Definición unilateral:

```latex
\[
X(s) = \int_{0^-}^{\infty} x(t)\, e^{-st}\, dt
\]
```

Par transformada:

```latex
\( x(t) \xleftrightarrow{\mathcal{L}} X(s) \)
```

Región de convergencia:

```latex
\( \text{ROC}: \sigma_1 < \text{Re}\{s\} < \sigma_2 \)
```

Función de transferencia continua:

```latex
\[
H(s) = \dfrac{Y(s)}{X(s)} = \dfrac{b_m s^m + \cdots + b_1 s + b_0}{s^n + a_{n-1} s^{n-1} + \cdots + a_1 s + a_0}
\]
```

Transformada inversa — fracciones parciales (forma típica):

```latex
\[
X(s) = \sum_{k=1}^{N} \dfrac{A_k}{s - p_k}
\]
```

---

## 17. Series de Fourier

### Continua (CTFS)

Síntesis (forma exponencial compleja):

```latex
\[
x(t) = \sum_{k=-\infty}^{\infty} c_k\, e^{jk\omega_0 t}
\]
```

Análisis — coeficientes:

```latex
\[
c_k = \dfrac{1}{T} \int_{T} x(t)\, e^{-jk\omega_0 t}\, dt
\]
```

Frecuencia fundamental:

```latex
\( \omega_0 = \dfrac{2\pi}{T} \)
```

Forma trigonométrica:

```latex
\[
x(t) = a_0 + \sum_{k=1}^{\infty} \left( a_k \cos(k\omega_0 t) + b_k \sin(k\omega_0 t) \right)
\]
```

### Discreta (DTFS)

Síntesis:

```latex
\[
x[n] = \sum_{k=\langle N \rangle} c_k\, e^{jk\omega_0 n}, \quad \omega_0 = \dfrac{2\pi}{N}
\]
```

Análisis:

```latex
\[
c_k = \dfrac{1}{N} \sum_{n=\langle N \rangle} x[n]\, e^{-jk\omega_0 n}
\]
```

---

## 18. Espacio de estados

### Sistema continuo

Ecuación de estado y salida:

```latex
\[
\dot{\mathbf{x}}(t) = \mathbf{A}\,\mathbf{x}(t) + \mathbf{B}\,u(t)
\]
\[
y(t) = \mathbf{C}\,\mathbf{x}(t) + \mathbf{D}\,u(t)
\]
```

### Sistema discreto

```latex
\[
\mathbf{x}[n+1] = \mathbf{A}\,\mathbf{x}[n] + \mathbf{B}\,u[n]
\]
\[
y[n] = \mathbf{C}\,\mathbf{x}[n] + \mathbf{D}\,u[n]
\]
```

Matrices del sistema:

```latex
\( \mathbf{A} \) ← matriz de estado (n×n)
\( \mathbf{B} \) ← matriz de entrada (n×1)
\( \mathbf{C} \) ← matriz de salida (1×n)
\( \mathbf{D} \) ← matriz de transmisión directa (escalar)
\( \mathbf{x}(t) \) ← vector de estado
```

Función de transferencia desde espacio de estados:

```latex
\[
H(s) = \mathbf{C}\,(s\mathbf{I} - \mathbf{A})^{-1}\mathbf{B} + \mathbf{D}
\]
```

Discreta:

```latex
\[
H(z) = \mathbf{C}\,(z\mathbf{I} - \mathbf{A})^{-1}\mathbf{B} + \mathbf{D}
\]
```

---

%%
# galaxy-links

%%

---

## 19. Convolución circular

Símbolo de convolución circular N-puntos:

```latex
\( x_3(m) = x_1(n) \circledast x_2(n) \)
```

Definición:

```latex
\[
x_3(m) = \sum_{n=0}^{N-1} x_1(n)\, x_2((m-n)\bmod N), \quad m = 0, 1, \ldots, N-1
\]
```

Matriz circulante — representación compacta:

```latex
\[
\begin{pmatrix} x_3(0) \\ x_3(1) \\ \vdots \\ x_3(N-1) \end{pmatrix}
=
\begin{pmatrix}
  x_1(0)   & x_1(N-1) & \cdots & x_1(1)   \\
  x_1(1)   & x_1(0)   & \cdots & x_1(2)   \\
  \vdots   & \vdots   & \ddots & \vdots   \\
  x_1(N-1) & x_1(N-2) & \cdots & x_1(0)
\end{pmatrix}
\begin{pmatrix} x_2(0) \\ x_2(1) \\ \vdots \\ x_2(N-1) \end{pmatrix}
\]
```

Ejemplo numérico — Palani Ej. 2.22, N=4:

```latex
\[
\begin{pmatrix} x_3(0) \\ x_3(1) \\ x_3(2) \\ x_3(3) \end{pmatrix}
=
\begin{pmatrix}
2 & 1 & 2 & 1 \\
1 & 2 & 1 & 2 \\
2 & 1 & 2 & 1 \\
1 & 2 & 1 & 2
\end{pmatrix}
\begin{pmatrix} 1 \\ 2 \\ 3 \\ 4 \end{pmatrix}
=
\begin{pmatrix} 14 \\ 16 \\ 14 \\ 16 \end{pmatrix}
\]
```

Relación con la DFT:

```latex
\[
x_1(n) \circledast x_2(n) \xleftrightarrow{\text{DFT}} X_1[k]\cdot X_2[k]
\]
```
