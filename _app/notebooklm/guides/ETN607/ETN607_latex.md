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
date_updated: 2026-08-13
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

Versores de coordenadas cilíndricas y esféricas con subíndice:

```latex
\( \mathbf{e}_r \)        ← versor radial
\( \mathbf{e}_\theta \)   ← versor angular (cilíndricas / esféricas)
\( \mathbf{e}_\phi \)     ← versor azimutal (esféricas)
\( \mathbf{e}_z \)        ← versor axial (cilíndricas)
```

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

%%
# galaxy-links

%%
