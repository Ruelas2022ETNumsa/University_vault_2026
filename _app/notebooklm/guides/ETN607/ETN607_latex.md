---
title: KaTeX — Guía de notación para NotebookLM (ETN607)
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
  - ETN607
date_created: 2026-08-13
date_updated: 2026-08-19
status: activo
---

# Guía de notación KaTeX para NotebookLM — ETN607

Esta guía define la notación que NotebookLM debe usar al generar ecuaciones para ETN607 (Mecánica Clásica / Lagrange).
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

## 2. Derivadas temporales — notación de punto

Derivada primera respecto al tiempo: punto sobre la variable.
Derivada segunda: dos puntos.

```latex
\( \dot{q} \)        ← dq/dt
\( \ddot{q} \)       ← d²q/dt²
\( \dot{\theta} \)   ← dθ/dt
\( \ddot{x} \)       ← d²x/dt²
```

Usar siempre notación de punto para derivadas temporales — nunca \(\dfrac{d}{dt}\) salvo que se esté deduciendo una expresión.

---

## 3. Derivadas parciales

```latex
\( \dfrac{\partial L}{\partial q} \)

\( \dfrac{\partial L}{\partial \dot{q}} \)

\( \dfrac{d}{dt}\left(\dfrac{\partial L}{\partial \dot{q}}\right) \)
```

Usar `\dfrac` siempre — nunca `\frac` solo.

---

## 4. Vectores y versores

Vectores con flecha arriba:

```latex
\( \vec{r} \)     ← vector posición
\( \vec{v} \)     ← vector velocidad
\( \vec{F} \)     ← vector fuerza
```

Versores de coordenadas cilíndricas y esféricas con sombrero y negrita:

```latex
\( \hat{\mathbf{e}}_r \)        ← versor radial
\( \hat{\mathbf{e}}_\theta \)   ← versor angular (cilíndricas / esféricas)
\( \hat{\mathbf{e}}_\phi \)     ← versor azimutal (esféricas)
\( \hat{\mathbf{e}}_z \)        ← versor axial (cilíndricas)
\( \hat{\mathbf{e}}_\ell \)     ← versor radial (esféricas — notación del docente: ℓ)
```

El apunte usa sombrero (`^`) sobre los versores — usar siempre `\hat{\mathbf{e}}`, nunca `\mathbf{e}` solo.

Versores cartesianos:

```latex
\( \mathbf{e}_x \),  \( \mathbf{e}_y \),  \( \mathbf{e}_z \)
```

---

## 5. Coordenadas generalizadas

```latex
\( q_i \)          ← coordenada generalizada i
\( \dot{q}_i \)    ← velocidad generalizada i
\( Q_i \)          ← fuerza generalizada i
\( n \)            ← número de grados de libertad
```

---

## 6. Ecuación de Lagrange

Forma estándar:

```latex
\[
\dfrac{d}{dt}\left(\dfrac{\partial L}{\partial \dot{q}_i}\right) - \dfrac{\partial L}{\partial q_i} = Q_i
\]
```

Con función potencia (sistemas disipativos):

```latex
\[
\dfrac{d}{dt}\left(\dfrac{\partial L}{\partial \dot{q}_i}\right) - \dfrac{\partial L}{\partial q_i} + \dfrac{\partial F}{\partial \dot{q}_i} = 0
\]
```

Lagrangiano:

```latex
\( L = T - V \)
```

---

## 7. Energía cinética y potencial

```latex
\( T \)   ← energía cinética
\( V \)   ← energía potencial
\( F \)   ← función potencia (Rayleigh)
```

Forma general de T:

```latex
\[
T = \dfrac{1}{2} m \left( \dot{x}^2 + \dot{y}^2 + \dot{z}^2 \right)
\]
```

En coordenadas cilíndricas:

```latex
\[
T = \dfrac{1}{2} m \left( \dot{r}^2 + r^2\dot{\theta}^2 + \dot{z}^2 \right)
\]
```

En coordenadas esféricas:

```latex
\[
T = \dfrac{1}{2} m \left( \dot{\ell}^2 + \ell^2\dot{\theta}^2 + \ell^2\dot{\phi}^2\sin^2\theta \right)
\]
```

---

## 8. Producto punto y producto vectorial

```latex
\( \vec{A} \cdot \vec{B} \)      ← producto punto
\( \vec{A} \times \vec{B} \)     ← producto vectorial
```

---

## 9. Desarrollos multilínea

Usar `\begin{array}{rcl}` con `\\` para saltar de línea:

```latex
\[
\begin{array}{rcl}
T & = & \dfrac{1}{2}m\dot{r}^2 + \dfrac{1}{2}mr^2\dot{\theta}^2 \\
  & = & \dfrac{1}{2}m\left(\dot{r}^2 + r^2\dot{\theta}^2\right)
\end{array}
\]
```

Alineación estándar: `{rcl}` — lado izquierdo · signo · lado derecho.
Nunca `\` simple para saltar — siempre `\\`.

---

## 10. Sistema de colores

Notación: `{\color{Color} contenido}`

| Color | Uso |
|---|---|
| NavyBlue | Valores intermedios que se usarán más adelante |
| TealBlue | Resultado final del desarrollo |
| YellowOrange | Valor nuevo tras una cancelación o sustitución |
| BrickRed | Error o término incorrecto |
| OliveGreen | Sustitución — reemplazo de variable por su valor |

```latex
{\color{TealBlue} L = T - V}
{\color{NavyBlue} T = \dfrac{1}{2}m\dot{r}^2}
{\color{OliveGreen} q_1 = r}
```

---

## 11. Cajas de resultado

```latex
\bbox[2px,border:2px solid #008080;background:white]{\color{#008080} L = T - V}

\bbox[2px,border:2px solid #FF4500;background:white]{\color{#FF4500} \ddot{q}_i = 0}

\boxed{T = \dfrac{1}{2}m\dot{q}^2}
```

| Tipo | Color hex | Uso |
|---|---|---|
| TD | `#008080` TealBlue | Resultado final del ejercicio |
| TA | `#FF4500` RedOrange | Resultado final de un inciso |
| B  | `#000080` NavyBlue | Valor intermedio con peso |
| `\boxed` | — | Resultado intermedio simple |

---

## 12. Flechas de transición

```latex
\( \longrightarrow \)   ← operación realizada, se pasa a la siguiente expresión
\( \Rightarrow \)       ← resultado alcanzado
```

---

## 13. Aceleración vectorial en coordenadas cilíndricas

Forma completa usada por el docente:

```latex
\[
\vec{a} = (\ddot{r} - r\dot{\theta}^2)\,\hat{\mathbf{e}}_r
        + (r\ddot{\theta} + 2\dot{r}\dot{\theta})\,\hat{\mathbf{e}}_\theta
        + \ddot{z}\,\hat{\mathbf{e}}_z
\]
```

Componente tangencial simplificada (pendulo, r = \ell = cte):

```latex
\( a_\theta = \ell\ddot{\theta} + 2(0)\dot{\theta} \)
```

---

## 14. Matrices de rotación

Usar `\begin{bmatrix}` para matrices. Columnas separadas con `&`, filas con `\\`:

```latex
\[
\begin{bmatrix} x \\ y \\ z \end{bmatrix}
=
\begin{bmatrix}
  \cos\mu & -\sin\mu & 0 \\
  \sin\mu &  \cos\mu & 0 \\
  0       &  0       & 1
\end{bmatrix}
\begin{bmatrix} u \\ v \\ w \end{bmatrix}
\]
```

Rotaciones sucesivas — producto de matrices, de derecha a izquierda:

```latex
\[
\begin{bmatrix} u \\ v \\ w \end{bmatrix}
=
\begin{bmatrix} \cos\beta & 0 & \sin\beta \\ 0 & 1 & 0 \\ -\sin\beta & 0 & \cos\beta \end{bmatrix}
\left(
\begin{bmatrix} \cos\mu & -\sin\mu & 0 \\ \sin\mu & \cos\mu & 0 \\ 0 & 0 & 1 \end{bmatrix}
\begin{bmatrix} x \\ y \\ z \end{bmatrix}
\right)
\]
```

---

## 15. Tangente — convención del apunte

El docente escribe $tg\,\theta$ (notación española). En la transcripción usar siempre `\tan`:

```latex
\( \tan\theta \)          ← correcto
\( tg\,\theta \)          ← NO usar — es la notación manuscrita del apunte
```

Ecuaciones de transformación que el docente escribe con $tg$:

```latex
\( \tan\theta = \dfrac{y}{x} \)
\( \tan\phi = \dfrac{y}{x} \)
```

---

## 16. Etiquetas $C_n$ del apunte

El docente marca resultados importantes con $C_1$, $C_2$, $C_3$ al margen derecho.
Transcribir como comentario inline al final del array, sin callout:

```latex
\[
\begin{array}{rcll}
v^2 & = & \dot{r}^2 + r^2\dot{\theta}^2 + \dot{z}^2 & C_2
\end{array}
\]
```

Usar columna extra `l` en el array para la etiqueta. No usar negrita ni color en $C_n$.

---

## 17. Notación valor[unidad]

El apunte usa corchetes para unidades: $50[\text{km/h}]$, $940[\text{V}]$.
Transcribir exactamente así — no convertir a notación estándar:

```latex
\( 50[\text{km/h}] \)
\( 940[\text{V}] \)
\( 470[\Omega] \)
```

---

%%
# galaxy-links

%%
