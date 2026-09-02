# Transformación de Coordenadas — Rotación y Traslación

**Subtema:** Transformación de coordenadas (Rotación y Traslación)

---

## Enunciado

Una partícula sufre primero una **traslación** de vector $\vec{T} = (2, 1, -3)$ y luego una **rotación de 30°** alrededor del eje $z$, llegando al punto final $P_f = (2, 1, -1)$.

**Hallar:** La posición inicial $P_0$ de la partícula.

---

## Estrategia de resolución

Para encontrar $P_0$ se invierten las transformaciones en **orden inverso**:

$$P_f \xrightarrow{R_z^T(30°)} P_{int} \xrightarrow{-\vec{T}} P_0$$

1. Deshacer la rotación aplicando $R_z^T(30°)$ sobre $P_f$
2. Deshacer la traslación restando $\vec{T}$ al resultado

> **Fundamento:** Las matrices de rotación son ortogonales, por lo tanto $R^{-1} = R^T$

---

## Paso 1 — Deshacer la rotación de 30° alrededor del eje z

La inversa de $R_z(30°)$ es su transpuesta:

$$R_z^T(30°) = \begin{pmatrix} \cos 30° & \sin 30° & 0 \\ -\sin 30° & \cos 30° & 0 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} \dfrac{\sqrt{3}}{2} & \dfrac{1}{2} & 0 \\[6pt] -\dfrac{1}{2} & \dfrac{\sqrt{3}}{2} & 0 \\[6pt] 0 & 0 & 1 \end{pmatrix}$$

Se aplica sobre $P_f = (2,\ 1,\ -1)$:

$$\begin{bmatrix} x_{int} \\ y_{int} \\ z_{int} \end{bmatrix} = \begin{bmatrix} \dfrac{\sqrt{3}}{2} & \dfrac{1}{2} & 0 \\[6pt] -\dfrac{1}{2} & \dfrac{\sqrt{3}}{2} & 0 \\[6pt] 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 2 \\ 1 \\ -1 \end{bmatrix}$$

**Componente x:**

$$x_{int} = \frac{\sqrt{3}}{2}(2) + \frac{1}{2}(1) = \sqrt{3} + \frac{1}{2} = \frac{2\sqrt{3}+1}{2}$$

**Componente y:**

$$y_{int} = -\frac{1}{2}(2) + \frac{\sqrt{3}}{2}(1) = -1 + \frac{\sqrt{3}}{2} = \frac{\sqrt{3}-2}{2}$$

**Componente z:**

$$z_{int} = -1$$

**Punto intermedio (antes de la rotación, después de la traslación):**

$$P_{int} = \left(\frac{2\sqrt{3}+1}{2},\ \frac{\sqrt{3}-2}{2},\ -1\right)$$

---

## Paso 2 — Deshacer la traslación

Se resta el vector de traslación $\vec{T} = (2, 1, -3)$:

$$\begin{bmatrix} x_0 \\ y_0 \\ z_0 \end{bmatrix} = \begin{bmatrix} \dfrac{2\sqrt{3}+1}{2} \\ \dfrac{\sqrt{3}-2}{2} \\ -1 \end{bmatrix} - \begin{bmatrix} 2 \\ 1 \\ -3 \end{bmatrix}$$

**Componente x:**

$$x_0 = \frac{2\sqrt{3}+1}{2} - 2 = \frac{2\sqrt{3}+1-4}{2} = \frac{2\sqrt{3}-3}{2} = \sqrt{3} - \frac{3}{2}$$

**Componente y:**

$$y_0 = \frac{\sqrt{3}-2}{2} - 1 = \frac{\sqrt{3}-2-2}{2} = \frac{\sqrt{3}-4}{2}$$

**Componente z:**

$$z_0 = -1 - (-3) = -1 + 3 = 2$$

---

## Resultado

$$\boxed{P_0 = \left(\sqrt{3} - \frac{3}{2},\ \frac{\sqrt{3}-4}{2},\ 2\right)}$$

---

## Verificación del proceso

| Paso | Operación | Entrada | Salida |
|------|-----------|---------|--------|
| 1 (directo) | $+\vec{T} = (2,1,-3)$ | $P_0$ | $P_{int}$ |
| 2 (directo) | $R_z(30°)$ | $P_{int}$ | $P_f = (2,1,-1)$ ✓ |
| — | — | — | — |
| 1 (inverso) | $R_z^T(30°)$ | $P_f = (2,1,-1)$ | $P_{int}$ |
| 2 (inverso) | $-\vec{T}$ | $P_{int}$ | $P_0$ ✓ |

---

## Notas clave

- La rotación $R_z$ **no altera la componente z**, por eso el cambio en $z$ proviene íntegramente de la traslación: $z_0 = z_{int} - T_z = -1 - (-3) = 2$
- La inversa de cualquier matriz de rotación es su **transpuesta** (propiedad de matrices ortogonales: $R^T R = I$)
- El orden de inversión es **obligatoriamente inverso** al orden de aplicación

---

*Tags: #transformaciones #rotación #traslación #álgebra-lineal #mecánica*
