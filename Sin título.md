Para realizar una gráfica con **anotaciones densas**, **múltiples elementos relacionados** o que requiera **precisión geométrica**, la guía unificada recomienda el uso de **TikZJax** sobre Desmos.

Un ejemplo clásico de un diagrama detallado en Cálculo I es la **circunferencia trigonométrica**, que permite visualizar simultáneamente las seis razones trigonométricas fundamentales en un solo esquema.

```tikz
\usepackage{amsmath}
\begin{document}
\begin{tikzpicture}[scale=2.5, >=stealth]
    % Ejes coordenados con etiquetas
    \draw[->] (-1.2,0) -- (1.5,0) node[right] {$x$};
    \draw[->] (0,-1.2) -- (0,1.5) node[above] {$y$};

    % Circunferencia unitaria
    \draw[thick, teal] (0,0) circle (1cm);

    % Líneas guía para tangentes (punteadas)
    \draw[gray, dashed] (1, -0.2) -- (1, 1.2);
    \draw[gray, dashed] (-0.2, 1) -- (1.2, 1);

    % Definición de puntos según el ángulo alpha (35 grados)
    \coordinate (O) at (0,0);
    \coordinate (P) at (35:1);
    \coordinate (Q) at (P |- O);
    \coordinate (T) at (1, {tan(35)});
    \coordinate (M) at ({1/tan(35)}, 1);

    % Radio de la circunferencia y arco del ángulo
    \draw[thick, orange] (O) -- (M);
    \draw[orange, ->] (0.3, 0) arc (0:35:0.3) node[midway, right, xshift=2pt] {$\alpha$};

    % Segmentos de las razones trigonométricas
    % Seno (segmento vertical PQ)
    \draw[very thick, teal] (P) -- (Q) node[midway, right] {$\text{sen}\,\alpha$};
    % Coseno (segmento horizontal OQ)
    \draw[very thick, orange] (O) -- (Q) node[midway, below] {$\text{cos}\,\alpha$};
    % Tangente (segmento vertical desde el eje x hasta el punto T)
    \draw[very thick, olive] (1,0) -- (T) node[midway, right] {$\text{tg}\,\alpha$};
    % Cotangente (segmento horizontal desde el eje y hasta el punto M)
    \draw[very thick, purple] (0,1) -- (M) node[midway, above] {$\text{ctg}\,\alpha$};

    % Etiquetas de puntos notables
    \fill (P) circle (0.8pt) node[above right] {$P$};
    \fill (T) circle (0.8pt) node[right] {$T$};
    \fill (M) circle (0.8pt) node[above] {$M$};
    \fill (O) circle (0.8pt) node[below left] {$O$};

    % Anotaciones adicionales de Secante y Cosecante
    \node[gray, left, rotate=35, font=\small] at (0.5, 0.4) {$\text{sec}\,\alpha$};
    \node[gray, above left, font=\small] at (0.8, 1.1) {$\text{cosec}\,\alpha$};

\end{tikzpicture}
\end{document}
```

> [!note] Detalles técnicos del diagrama
> 
> - **Escala**: Se utiliza `scale=2.5` (superior al default de 1.2) para permitir que las etiquetas de los segmentos sean legibles.
> - **Colores**: Se emplea la paleta estándar (`teal`, `orange`, `olive`, `purple`) para distinguir cada razón trigonométrica sin saturar visualmente el dibujo.
> - **Precisión**: TikZJax permite calcular las coordenadas de los puntos $T$ y $M$ mediante funciones matemáticas (`tan`), garantizando que los segmentos coincidan exactamente con la prolongación del radio.