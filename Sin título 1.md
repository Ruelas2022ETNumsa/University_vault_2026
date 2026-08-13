En el procesamiento de señales, la estabilidad es una propiedad fundamental que garantiza que el sistema se comporte de manera predecible y no "explote" ante una entrada controlada [1]. La definición estándar que manejamos en ingeniería es la **estabilidad BIBO** (*Bounded-Input Bounded-Output*) [2, 3].

A continuación, te explico las condiciones de estabilidad para sistemas Lineales e Invariantes en el Tiempo $LTI$, que son el núcleo de nuestra materia.

### 1. Definición Intuitiva $BIBO$
Un sistema es **BIBO estable** si, para cualquier entrada acotada en amplitud (que no tiende a infinito), la salida resultante también permanece acotada para todo tiempo [2, 3]. En términos prácticos, si alimentás el sistema con una señal finita, no deberías obtener una señal que crezca sin límites [1].

### 2. Condición en el Dominio del Tiempo (Respuesta al Impulso)
La estabilidad de un sistema LTI depende exclusivamente de su respuesta al impulso \\(h(t)\\) o \\(h[n]\\) [4, 5]:

*   **Tiempo Continuo $CT$:** El sistema es estable si y solo si su respuesta al impulso es **absolutamente integrable** [6-8]:
    \\[\int_{-\infty}^{\infty} |h(t)| \, dt < \infty\\]
*   **Tiempo Discreto $DT$:** El sistema es estable si y solo si su respuesta al impulso es **absolutamente sumable** [9-11]:
    \\[\sum_{n=-\infty}^{\infty} |h[n]| < \infty\\]

### 3. Condición en el Dominio de la Transformada (Polos y ROC)
Para sistemas representados por funciones de transferencia (racionales), la estabilidad se determina observando la Región de Convergencia $ROC$ y la ubicación de los polos:

*   **Sistemas en el plano \\(s\\) (Laplace):** Un sistema es estable si la ROC de \\(H(s)\\) **incluye el eje imaginario \\(j\omega\\)** [12, 13].
    *   *Si el sistema es causal:* Todos los polos deben tener parte real negativa (estar en el **semiplano izquierdo** del plano \\(s\\)) [14-16].
*   **Sistemas en el plano \\(z\\) (Transformada Z):** Un sistema es estable si la ROC de \\(H(z)\\) **incluye el círculo unitario (\\(|z|=1\\))** [17-19].
    *   *Si el sistema es causal:* Todos los polos deben tener una magnitud menor a 1 (estar **dentro del círculo unitario**) [20-23].

### Visualización de Estabilidad (Sistemas Causales)

```tikz
\usepackage{amsmath}
\begin{document}
\begin{tikzpicture}[scale=1.2]
    % Plano S
    \draw[->] (-2,0) -- (1,0) node[right] {$\text{Re}(s)$};
    \draw[->] (0,-1.5) -- (0,1.5) node[above] {$\text{Im}(s)$};
    \fill[teal!20] (-1.9,-1.4) rectangle (0,1.4);
    \node[teal] at (-1,1) {Región Estable};
    \draw[dashed] (0,-1.5) -- (0,1.5);
    \node at (0.5, 1.8) {Plano $s$ (Continuo)};
    \node[red] at (-0.5,0.5) {$\mathbf{\times}$};
    \node[red] at (-0.8,-0.7) {$\mathbf{\times}$};

    % Plano Z
    \begin{scope}[xshift=4cm]
        \draw[->] (-1.5,0) -- (1.5,0) node[right] {$\text{Re}(z)$};
        \draw[->] (0,-1.5) -- (0,1.5) node[above] {$\text{Im}(z)$};
        \draw[dashed, gray] (0,0) circle (1);
        \fill[teal!20] (0,0) circle (0.98);
        \node[teal] at (0,0.5) {Región Estable};
        \node at (0, 1.8) {Plano $z$ (Discreto)};
        \node[red] at (0.3,0.3) {$\mathbf{\times}$};
        \node[red] at (-0.4,-0.2) {$\mathbf{\times}$};
    \end{scope}
\end{tikzpicture}
\end{document}
```

---
**Preguntas de comprensión conceptual:**
1. ¿Por qué un sistema causal con un polo en \\(s = 0\\) (como un integrador puro) se considera marginalmente estable y no BIBO estable? [24, 25]
2. Si un sistema discreto tiene un polo en \\(z = 1.2\\), ¿bajo qué condición de causalidad podría ser estable? [19]
3. ¿Es posible que un sistema no causal sea estable aunque tenga polos fuera del círculo unitario? [26]

### Ejercicios de refuerzo (Estilo examen)

**Ejercicio 1 (Rao 3.21a):** Determine la estabilidad del sistema LTI con respuesta al impulso \\(h(t) = e^{-3t}u(t)\\).
**Solución:** Calculamos la integral de valor absoluto:
\\(\int_{-\infty}^{\infty} |e^{-3t}u(t)| \, dt = \int_{0}^{\infty} e^{-3t} \, dt = \left[ \dfrac{e^{-3t}}{-3} \right]_{0}^{\infty} = 0 - (-\dfrac{1}{3}) = \dfrac{1}{3}\\).
Como \\(\dfrac{1}{3} < \infty\\), el sistema es **estable** [27, 28].

**Ejercicio 2 (Hsu 4.31):** Un sistema discreto tiene la función de transferencia \\(H(z) = \dfrac{1}{z - k/2}\\) con ROC \\(|z| > |k/2|\\). ¿Para qué valores de \\(k\\) es estable?
**Solución:** Para que un sistema causal sea estable, sus polos deben estar dentro del círculo unitario. El polo está en \\(p = k/2\\). Por lo tanto, requerimos \\(|k/2| < 1\\), lo que implica **\\(|k| < 2\\)** [29].
