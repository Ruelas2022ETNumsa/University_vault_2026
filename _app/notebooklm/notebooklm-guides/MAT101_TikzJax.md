---
title: TikZJax — Guía unificada para Obsidian
galaxy_body: beacon
scope: vault
tool: tikzjax-plugin
audience:
  - usuario
  - notebooklm
  - claude
tags:
  - beacon
  - tikzjax
  - infraestructura
date_created: 2026-06-30
date_updated: 2026-07-01
status: en-proceso
---

# ⚡ GUÍA UNIFICADA DE TIKZJAX PARA OBSIDIAN (MAT101)

> Plugin: `obsidian-tikzjax` — renderiza LaTeX/TikZ como SVG directamente en tus notas usando WebAssembly.
> Guía específica de Cálculo 1. Para circuitos electrónicos y otras materias ver `tikzjax_guide.md` (guía general).
> Este documento está organizado en tres bloques: **Reglas de sintaxis (N1–N10)**, **Checklist (N11)**, y **Biblioteca de ejemplos por tema MAT101 (N12–N19)**.

---

# 🤖 SECCIÓN NOTEBOOKLM

Instrucciones para que NotebookLM genere bloques TikzJax correctos listos para copiar
en Obsidian. Cuando el usuario pida una gráfica, responder con un bloque de código
— no con imagen ni enlace.

### Defaults — cuando el usuario no especifica

- Entorno: `tikzpicture` simple si es geometría/conjuntos; `axis` (pgfplots) si es una función 2D con ejes numéricos precisos.
- Escala: `scale=1.2` como punto de partida para diagramas de conjuntos o geometría.
- Color de curva principal: `teal`; secundaria: `orange` (consistente con los ejemplos ya usados en las notas de T1).
- Ejes: incluir siempre flechas `->` y etiquetas `node[right]{$x$}` / `node[above]{$y$}` cuando el diagrama tiene sistema de ejes.

### Reglas base — siempre obligatorias

Antes de generar cualquier bloque, seguir este orden:
1. ¿Qué tipo de diagrama? (geometría/conjuntos → `tikzpicture` · función con ejes → `pgfplots axis` · circuito → no aplica en MAT101, ver `tikzjax_guide.md`)
2. ¿Qué paquete necesita? (ver N2)
3. ¿Escala y tamaño? (ver N6)
4. ¿Qué colores? (ver N7)
5. ¿Qué nivel de detalle requiere? (ver N10) — pocos elementos/curva simple → Desmos; varios elementos relacionados o anotaciones → TikZJax. En caso de duda, revisar si el tipo de gráfico ya tiene precedente en la biblioteca de ejemplos (Bloque C) de esta guía o de `MAT101_desmos.md`.

---

## BLOQUE A — SINTAXIS Y REGLAS

---

### N1. ESTRUCTURA OBLIGATORIA DEL BLOQUE

**Sin `\begin{document}` el plugin no renderiza nada. Sin `\end{document}` el bloque queda abierto y falla.**

```
\usepackage{PAQUETE}
\begin{document}
  \begin{ENTORNO}[OPCIONES]
    ...
  \end{ENTORNO}
\end{document}
```

Reglas:
- Identificador del bloque: ` ```tikz ` — nunca `latex`, nunca `tikzjax`
- `\begin{document}` y `\end{document}` siempre presentes
- `\documentclass{standalone}` **nunca se incluye** — el plugin lo agrega automáticamente
- Paquetes con `\usepackage{}` **antes** de `\begin{document}`

❌ Incorrecto — sin document:
```
\begin{tikzpicture}
\draw (0,0) -- (1,1);
\end{tikzpicture}
```

✅ Correcto:
```tikz
\begin{document}
\begin{tikzpicture}
\draw (0,0) -- (1,1);
\end{tikzpicture}
\end{document}
```

---

### N2. PAQUETES DISPONIBLES PARA MAT101

| Paquete | Para qué | Uso en MAT101 |
|---------|---------|----------------|
| (ninguno) | Dibujo geométrico básico — `tikzpicture` puro | Conjuntos, funciones a mano alzada, circunferencia trigonométrica, funciones por tramos |
| `pgfplots` | Gráficas matemáticas 2D/3D de precisión | Funciones trigonométricas, exponenciales, logarítmicas, superficies 3D |
| `amsmath` | Fracciones y notación avanzada en nodos | Obligatorio si se usa `\tfrac`, `\dfrac`, sistemas — ver N8 |
| `amssymb` | Símbolos matemáticos extendidos | Conjuntos, relaciones |
| `tikz-3dplot` | Coordenadas y perspectiva 3D | Superficies, volúmenes de revolución (T6) |

> `circuitikz` y `chemfig` no aplican a MAT101 — son para electrónica/química. Ver `tikzjax_guide.md` (guía general) si se necesitan para otra materia.

---

### N3. ENTORNOS SEGÚN TIPO DE DIAGRAMA

| Tipo de diagrama | Entorno |
|-------------------|---------|
| Geometría, conjuntos, diagramas de flechas (composición, relación) | `tikzpicture` |
| Función con ejes numéricos, dominio/rango preciso, cuadrícula | `pgfplots` → `\begin{axis}[...]` dentro de `tikzpicture` |
| Superficie o volumen 3D | `pgfplots` con `\addplot3` |
| Circunferencia trigonométrica, función inversa con espejo `y=x` | `tikzpicture` con coordenadas manuales |

---

### N4. SINTAXIS BÁSICA DE DIBUJO (tikzpicture)

```
% Ejes con flecha y etiqueta
\draw[->] (-3,0) -- (3,0) node[right] {$x$};
\draw[->] (0,-2) -- (0,2) node[above] {$y$};

% Curva por función explícita
\draw[thick, teal, domain=-2:2, samples=100] plot (\x,{\x^2});

% Punto sólido con etiqueta
\fill (1,1) circle (0.05);
\node[above] at (1,1) {$(1,1)$};

% Línea punteada / auxiliar
\draw[dashed, gray] (-1,0) -- (1,0);

% Flecha entre dos nodos (diagramas de conjuntos/composición)
\draw[->, thick, orange] (a1) -- (b5);
\draw[->, thick, orange] (a1) .. controls (-1,1.5) and (1,-1.5) .. (b6);
```

`domain` y `samples` controlan el rango y la resolución de la curva — más `samples` = curva más suave.

---

### N5. GRÁFICAS CON PGFPLOTS

```tikz
\usepackage{pgfplots}
\begin{document}
\begin{tikzpicture}
\begin{axis}[
    axis lines=middle,
    xmin=-4, xmax=4,
    ymin=-2, ymax=2,
    xlabel={$x$}, ylabel={$y$},
    xtick={-1,0,1}, ytick={-1,0,1}
]
\addplot[very thick, teal, domain=-4:4, samples=200] {sin(deg(x))};
\end{axis}
\end{tikzpicture}
\end{document}
```

- Trigonométricas: usar `deg(x)` dentro de `sin()`, `cos()`, `tan()` — sin este ajuste pgfplots interpreta el argumento en radianes y da resultados incorrectos.
- `axis lines=middle` centra los ejes en el origen — preferido para funciones sin restricción de dominio.
- Puntos clave: `\fill[orange] (axis cs:X,Y) circle (2pt) node[above right] {$texto$};`

---

### N6. ESCALA Y TAMAÑO

Mismas 6 categorías que `MAT101_desmos.md` (N2 de esa guía — incluyendo Panorámico), valores adaptados a TikZ:

| Tipo           | pgfplots (width/height)  | tikzpicture (scale aprox.) | Uso                                    |
| -------------- | ------------------------ | -------------------------- | -------------------------------------- |
| Pequeño        | `width=6cm, height=4cm`  | `scale=0.7`                | Rectas numéricas, intervalos, un punto |
| Mediano        | `width=8cm, height=7cm`  | `scale=1` a `1.2`          | Funciones, parábolas                   |
| Grande         | `width=11cm, height=9cm` | `scale=0.9` a `1.5`        | Múltiples curvas, etiquetas, regiones  |
| Cornell        | `width=6cm, height=5cm`  | `scale=0.85`               | Máximo dentro de bloque multi-column   |
| Plano cuadrado | `width=9cm, height=9cm`  | `scale=1.3`                | Regiones, geometría, área entre curvas |
| Panorámico     | `width=12cm, height=5cm` | `scale=1` (ancho)          | Funciones trigonométricas, periódicas  |

```
\begin{tikzpicture}[scale=1.2]         → escala el dibujo completo
\begin{axis}[width=8cm, height=7cm]    → tamaño fijo en pgfplots
```

- `scale` no tiene equivalente px exacto — depende del rango de coordenadas del dibujo. La columna de la tabla es punto de partida, no valor fijo.
- Diagramas de conjuntos/composición (elipses, nodos, flechas): usar fila "Mediano" o "Grande" según cantidad de elementos.
- Circunferencia trigonométrica: `scale=2` como excepción documentada — necesita más espacio para etiquetas de segmentos.

---

### N7. PALETA DE COLORES

Los hex de abajo son los mismos usados en `MAT101_desmos.md`, para mantener consistencia visual entre ambas herramientas. TikZ no reconoce estos hex directamente — hay que declararlos con `xcolor`:

```
\usepackage{xcolor}
\definecolor{curvaPpal}{HTML}{005F73}
...
\draw[thick, curvaPpal] ...
```

Alternativa más simple — nombres estándar de TikZ (ya usados en los ejemplos existentes de T1): `teal`, `orange`, `olive`, `gray`. Válidos cuando no hace falta coincidencia exacta de color con Desmos.

> **Excepción para familias de funciones con 4 curvas:** `violet`, `purple` y `red!70!black` están reservados para diagramas que necesitan una cuarta serie (ej. función potencial, exponencial). No usar como color general en diagramas de 1–3 curvas.

#### Paleta para curvas y líneas (sólidas)

```
#005F73   → azul petróleo   (curva principal)
#0A9396   → verde azulado   (curva secundaria)
#EE9B00   → ámbar           (destaque)
#BB3E03   → naranja quemado (curva de advertencia)
#629900   → verde oliva     (curva auxiliar)
#5A189A   → morado          (punto especial)
#C1121F   → rojo            (curva de error / evento)
#DA627D   → rosa            (curva alternativa)
#FFD60A   → amarillo        (resaltado)
#474448   → gris antracita  (ejes, bordes, auxiliares)
```

#### Paleta para líneas segmentadas (50% color + 50% blanco)
```
#80AFB9   → azul petróleo segmentado
#85C9CB   → verde azulado segmentado
#F7CD80   → ámbar segmentado
#DD9F81   → naranja quemado segmentado
#B1CC80   → verde oliva segmentado
#AD8CCD   → morado segmentado
#E0898F   → rojo segmentado
#EDB1BE   → rosa segmentado
#FFEB85   → amarillo segmentado
#A3A2A4   → gris antracita segmentado
```

#### Paleta para rellenos (áreas sombreadas — 25% color + 75% blanco)
```
#BFD7DC   → azul petróleo claro   (región principal)
#C2E4E5   → verde azulado claro   (región secundaria)
#FBE6BF   → ámbar claro           (región de destaque)
#EECFC0   → naranja quemado claro (región de advertencia)
#D8E6BF   → verde oliva claro     (región auxiliar)
#D6C5E6   → morado claro          (región auxiliar)
#F0C4C7   → rojo claro            (región de evento)
#F6D8DF   → rosa claro            (región alternativa)
#FFF5C2   → amarillo claro        (región de resaltado)
#D1D0D1   → gris claro            (región neutra)
```

---

### N8. LIMITACIONES CONOCIDAS DEL PLUGIN

- **`pgfplots fillbetween` no está soportado.** Para rellenar el área entre dos curvas $f(x)$ y $g(x)$ en $[a,b]$: (1) rellenar bajo $f(x)$ con el color deseado usando `\closedcycle`, (2) rellenar bajo $g(x)$ con blanco para borrar el exceso, (3) dibujar las curvas encima. El relleno blanco debe ir *antes* que las curvas.
- **`\tfrac{}{}` en nodos falla silenciosamente** (no renderiza nada) sin `\usepackage{amsmath}` cargado. Alternativa segura sin dependencia: usar el valor decimal directo (`0.5` en vez de `\tfrac{1}{2}`).
- **`chemfig` es inestable** — evitar en MAT101 salvo necesidad puntual.

---

### N9. ADVERTENCIA DE PRIMER RENDER

El plugin puede no mostrar el diagrama la primera vez que se abre la nota. Si el bloque aparece vacío o con error: cerrar Obsidian completamente y volver a abrirlo. Ocurre más seguido con diagramas complejos en la primera carga del vault.

---

### N10. CÓMO DECIDIR ENTRE TIKZJAX Y DESMOS

No se decide por tema, sino por **nivel de detalle** del diagrama solicitado. La pregunta es siempre la misma sin importar el tema de MAT101: ¿cuántos elementos hay y cómo se relacionan entre sí?

- **Curva o región simple** (una función, área bajo una curva, comparación de 2-3 curvas sin anotaciones extra) → **Desmos**. Más rápido de generar y calcular.
- **Múltiples elementos relacionados, anotaciones densas, o precisión geométrica** (conjuntos con flechas de relación/composición, circunferencia trigonométrica con segmentos y puntos etiquetados, función inversa con espejo `y=x`, figuras con medidas exactas, superficies o volúmenes 3D) → **TikZJax**. Permite el nivel de control que Desmos no ofrece.

Cuando no esté claro cuál usar: revisar si ese tipo de gráfico ya tiene un ejemplo confirmado en el Bloque C de esta guía o en el de `MAT101_desmos.md` — el precedente ya resuelto tiene prioridad sobre reevaluar el criterio desde cero. Esta sección no se actualiza por tema nuevo; los ejemplos concretos van acumulándose en el Bloque C de cada guía.

---

## BLOQUE B — CHECKLIST

---

### N11. CHECKLIST ANTES DE RESPONDER

Antes de entregar un bloque TikZJax verificar:

- [ ] ¿Usa el identificador exacto ` ```tikz `? (nunca `latex`, nunca `tikzjax`)
- [ ] ¿Tiene `\begin{document}` y `\end{document}`?
- [ ] ¿NO incluye `\documentclass`?
- [ ] ¿Los paquetes necesarios están cargados con `\usepackage{}` antes de `\begin{document}`?
- [ ] ¿Todas las expresiones matemáticas están entre `$...$`?
- [ ] Si hay fracciones en nodos (`\tfrac`, `\dfrac`) → ¿está cargado `\usepackage{amsmath}`?
- [ ] Si hay área entre curvas → ¿evita `fillbetween` y usa el patrón manual de relleno (N8)?
- [ ] ¿Los colores están en la paleta oficial (hex vía `\definecolor` o nombres estándar de TikZ) — nunca negro puro para curvas?
- [ ] ¿El diagrama aporta algo que Desmos no puede dar (N10)? Si no, reconsiderar usar Desmos.
- [ ] Si el bloque es solo referencia de código (no debe renderizar) → quitar `tikz` del identificador, dejar ` ``` ` plano.

---

## BLOQUE C — BIBLIOTECA DE EJEMPLOS POR TEMA (MAT101)

---

### N12. T0 — NÚMEROS REALES Y DESIGUALDADES

> Primer parcial. Rectas numéricas, intervalos, valor absoluto básico, inecuaciones.

*(Agregar ejemplos confirmados aquí)*

---

### N13. T1 — FUNCIONES REALES

> Primer parcial. Dominio, imagen, gráficas de familias de funciones, transformaciones.

### Relación vs. función (diagramas de conjuntos)

> Contexto para NotebookLM: estos tres ejemplos muestran cómo distinguir una relación cualquiera de una función usando diagramas de flechas entre dos conjuntos. Usar este tipo de gráfica cuando el usuario pida representar dominio/codominio con elementos discretos y sus correspondencias.

Analizar si $f$ es o no función.

#### a)

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.2] % N6: Mediano

\draw (-4,0) ellipse (1 and 2);
\draw (4,0) ellipse (1 and 2);

\node at (-4,2.6) {$D$};
\node at (4,2.6) {$R$};
\node at (0,2.8) {$f$};

\node (a1) at (-4,1) {$1$};
\node (a2) at (-4,0) {$2$};
\node (a3) at (-4,-1) {$3$};

\node (b4) at (4,1) {$4$};
\node (b5) at (4,0) {$5$};
\node (b6) at (4,-1) {$6$};

\draw[->, thick, orange]
(a1) .. controls (-1,1.5) and (1,-1.5) .. (b6);

\draw[->, thick, teal]
(a2) -- (b5);

\draw[->, thick, olive]
(a3) .. controls (-1,-1.5) and (1,1.5) .. (b4);

\end{tikzpicture}
\end{document}
```


$f$ sí es función.

$$  D_f=\{1,2,3\}  $$
$$R_f=\{4,5,6\}=rango,\ recorrido,\ codominio ,\text{ conjunto de imágenes}$$
  $$f={(1,6),(2,5),(3,4)}$$

- $\forall x$ del $D$ debe tener imagen.
- El $D$ debe ser único y no debe repetirse.
    
---

#### b)

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.2] % N6: Mediano

\draw (-4,0) ellipse (1 and 2);
\draw (4,0) ellipse (1 and 2);

\node at (-4,2.6) {$D$};
\node at (4,2.6) {$R$};
\node at (0,2.8) {$f$};

\node (a1) at (-4,1) {$1$};
\node (a2) at (-4,0) {$2$};
\node (a3) at (-4,-1) {$3$};

\node (b4) at (4,1) {$4$};
\node (b5) at (4,0) {$5$};
\node (b6) at (4,-1) {$6$};

\draw[->, thick, olive]
(a1) .. controls (-1,1.2) and (1,0.6) .. (b5);

\draw[->, thick, teal]
(a2) -- (b5);

\draw[->, thick, orange]
(a3) .. controls (-1,-1.2) and (1,-0.6) .. (b5);

\end{tikzpicture}
\end{document}
```

La relación **sí** es función porque:
$$D_f=\{1,2,3\}$$  $$R=\{4,5,6\} = codominio$$
$$R_{f}=\{5\}= \text{imagen o rango}$$
Todas las flechas llegan a 5.

---

#### c)

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.2] % N6: Mediano

\draw (-4,0) ellipse (1 and 2);
\draw (4,0) ellipse (1 and 2);

\node at (-4,2.6) {$D$};
\node at (4,2.6) {$R$};
\node at (0,2.8) {$f$};

\node (a1) at (-4,1) {$1$};
\node (a2) at (-4,0) {$2$};
\node (a3) at (-4,-1) {$3$};

\node (b4) at (4,1) {$4$};
\node (b5) at (4,0) {$5$};
\node (b6) at (4,-1) {$6$};

% 1 -> 4
\draw[->, thick, olive]
(a1) .. controls (-1,2) and (1,2) .. (b4);

% 3 -> 5
\draw[->, thick, teal]
(a3) .. controls (-1,-0.4) and (1,-0.2) .. (b5);

% 3 -> 6
\draw[->, thick, orange]
(a3) .. controls (-1,-2) and (1,-2) .. (b6);

\end{tikzpicture}
\end{document}
```

$f$ no es función.

- $2\in D$ no tiene imagen $\nexists, y\in R$.
- $3\in D$ tiene doble imagen $\nexists !, y\in R$.

---

### Función par

$y=f(x)$ es par si verifica

$$
f(-x)=f(x)
$$

La gráfica de $y=f(x)$ es simétrica respecto al eje $y$.

```tikz
\usepackage{amsmath}
\begin{document}
\begin{tikzpicture}[scale=1.5] % N6: Grande

% Ejes
\draw[->] (-2.2,0) -- (2.2,0) node[right] {$x$};
\draw[->] (0,-0.2) -- (0,1.8) node[above] {$y$};

% Curva
\draw[thick, teal, domain=-1.35:1.35, samples=120]
  plot (\x,{(\x)^4-(\x)^2+0.5});

% Segmento de simetría
\draw[dashed] (-1,0.5) -- (1,0.5);

% Puntos
\fill (-1,0.5) circle (0.05);
\fill (1,0.5) circle (0.05);

% Etiquetas de puntos
\node[above] at (-1,0.5) {$(-1, 0.5)$};
\node[above] at (1,0.5) {$(1, 0.5)$};

% Marcas en eje x
\node[below] at (-1,0) {$-1$};
\node[below] at (1,0) {$1$};

% Etiqueta de función
\node[right] at (1.1,1.55) {$y=x^4-x^2+0.5$};

% Eje de simetría
\node at (0,-0.35) {Eje de sim\'etria};

\end{tikzpicture}
\end{document}
```
> Contexto para NotebookLM: la gráfica muestra $y=x^4-x^2+0.5$, simétrica respecto al eje $y$ — los puntos $(-1, 0.5)$ y $(1, 0.5)$ ilustran esa simetría. Usar cuando el usuario pida graficar una función par o mostrar simetría axial respecto al eje $y$.

---

### Función impar

$y=f(x)$ es impar si cumple:

$$
f(-x)=-f(x)
$$

La gráfica de $y=f(x)$ impar es simétrica respecto al origen $(0,0)$.

```tikz
\usepackage{amsmath}
\begin{document}
\begin{tikzpicture}[scale=1.2] % N6: Mediano

% Ejes
\draw[->] (-1.8,0) -- (1.8,0) node[right] {$x$};
\draw[->] (0,-1.2) -- (0,1.2) node[above] {$y$};

% Curva
\draw[thick, teal, domain=-1.5:1.5, samples=200]
  plot (\x,{(\x)^3-(\x)});

% Segmento que muestra la simetría respecto al origen
\draw[dashed] (-1,0) -- (1,0);

% Puntos simétricos
\fill (-0.5,0.375) circle (0.05);
\fill (0.5,-0.375) circle (0.05);

% Etiquetas de puntos
\node[above left] at (-0.5,0.375) {$(-0.5,\;0.375)$};
\node[below right] at (0.5,-0.375) {$(0.5,\;-0.375)$};



% Etiqueta de función
\node[right] at (0.8,0.9) {$y=x^3-x$};

% Centro de simetría
\fill (0,0) circle (0.05);
\node[below left] at (0,0) {$O(0,0)$};

\end{tikzpicture}
\end{document}
```

> Contexto para NotebookLM: la gráfica muestra $y=x^3-x$, simétrica respecto al origen — los puntos $(-0.5, 0.375)$ y $(0.5, -0.375)$ ilustran esa simetría puntual.

### Función periódica

$y=f(x)$ es periódica con período $p$ si cumple

$$
f(x+p)=f(x)
$$

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.5] % N6: Grande

% Ejes
\draw[->] (-0.5,0) -- (7.2,0) node[right] {$x$};
\draw[->] (0,-0.2) -- (0,1.4) node[above] {$y$};

% Curva y = sen²(x)
\draw[thick, teal, domain=0:6.283, samples=200]
  plot (\x,{sin(\x r)*sin(\x r)});

% Marcas
\node[below] at (0,0) {$0$};
\node[below] at (1.57,0) {$\frac{\pi}{2}$};
\node[below] at (3.14,0) {$\pi$};
\node[below] at (4.71,0) {$\frac{3\pi}{2}$};
\node[below] at (6.28,0) {$2\pi$};

% Máximos
\fill (1.57,1) circle (0.04);
\fill (4.71,1) circle (0.04);

% Etiqueta
\node[right] at (6.3,0.5) {$y=\sin^2 x$};

% Periodo
\draw[dashed] (0,1) -- (6.28,1);
\node[above] at (1.57,1.2) {$p=\pi$};

\end{tikzpicture}
\end{document}
```

> Contexto para NotebookLM: usar cuando el usuario pida mostrar una función periódica. El ejemplo usa $y=\sin^2 x$ con período $p=\pi$. Incluir siempre la línea horizontal del período y los puntos de máximo marcados.

- La gráfica en $p$ unidades se repite indefinidamente.


### Función inversa

Si $y=f(x)$ es inyectiva, existe $f^{-1}(x)$ tal que $f^{-1}(f(x))=x$. La gráfica de $f^{-1}$ es el reflejo de la gráfica de $f$ respecto a la recta $y=x$.

> Contexto para NotebookLM: usar esta gráfica cuando el usuario pida mostrar una función junto a su inversa. Muestra tres curvas: $f(x)$, $f^{-1}(x)$, y la recta $y=x$ como eje de simetría entre ambas.

```tikz
\usepackage{pgfplots}
\begin{document}

\begin{tikzpicture}
\begin{axis}[
    axis lines=middle,
    xmin=-5, xmax=5,
    ymin=-5, ymax=5,
    width=11cm,
    height=9cm,
    xlabel={$x$},
    ylabel={$y$},
    xtick={-5,-4,...,5},
    ytick={-5,-4,...,5},
    clip=true
]

% Recta y=x
\addplot[
    domain=-5:5,
    dashed,
    gray,
    thick
]
{x};

% y=f^{-1}(x)=x^3+1
\addplot[
    domain=-1.8:1.6,
    samples=200,
    very thick,
    teal
]
{x^3+1};

% y=f(x)=\sqrt[3]{x-1}
\addplot[
    domain=-1.8:1.6,
    samples=200,
    very thick,
    orange
]
({x^3+1},{x});

\node[teal] at (axis cs:-2.2,1.2)
{$y=f^{-1}(x)$};

\node[orange] at (axis cs:2,-1.8)
{$y=f(x)$};

\node[gray] at (axis cs:4,3.2)
{$y=x$};

\end{axis}
\end{tikzpicture}

\end{document}
```

---

### Composición de funciones

**Def.** Sean las funciones
$$f:B\to C$$
$$g:A\to B$$
donde
$$y=f(x)$$

- Se define
$$(f \circ g)(x) = f(g(x))$$

("f compuesta con g en x")
$$(f\circ g)(x)=f\bigl(g(x)\bigr)$$
$$D_{f\circ g}=
\{\,x\in D_g \;:\; g(x)\in D_f\,\}
$$



```tikz
\begin{document}
\begin{tikzpicture}[scale=1.2] % N6: Mediano

% Conjuntos
\draw (-3.5,0) ellipse (1 and 1.5);
\draw (0,0) ellipse (1 and 1.5);
\draw (3.5,0) ellipse (1 and 1.5);

% Nombres de conjuntos (debajo)
\node at (-3.5,-2.1) {$A$};
\node at (0,-2.1) {$B$};
\node at (3.5,-2.1) {$C$};

% Elementos
\node (x) at (-3.5,0) {$x$};
\node (gx) at (0,0) {$g(x)$};
\node (fgx) at (3.5,0) {$f(g(x))$};

% Flecha g
\draw[->, thick, teal]
(x) .. controls (-2.0,0.8) and (-1.2,0.8) .. (gx);

\node at (-1.75,1.05) {$g$};

% Flecha f
\draw[->, thick, orange]
(gx) .. controls (1.2,0.8) and (2.0,0.8) .. (fgx);

\node at (1.75,1.05) {$f$};

\end{tikzpicture}
\end{document}
```

> Contexto para NotebookLM: usar cuando el usuario pida diagrama de composición $f\circ g$. Tres elipses en línea representando los conjuntos $A$, $B$, $C$; flecha `teal` para $g$ y flecha `orange` para $f$, ambas por encima de los conjuntos.

> donde el dominio de $f \circ g$ es el conjunto de todos los $x$ en el dominio de $g$ tales que $g(x)$ esté en el dominio de $f$.

---

### Características generales de las principales funciones reales

#### Función de 1er grado (recta)

La función de primer grado tiene la forma:

$$f(x)=ax+b$$

donde:
- $D_{f}=\mathbb{R} \, , \, R_{f}=\mathbb{R}$

ademas:

- $a=\text{tg}(\alpha)$ es la pendiente de la recta.
- $b$ es la ordenada en el origen.

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.2] % N6: Mediano

% Ejes
\draw[->] (-0.5,0) -- (4.5,0) node[right] {$x$};
\draw[->] (0,-0.5) -- (0,4) node[above] {$y$};

% Recta f(x)=ax+b con b=1
\draw[very thick,color=teal] (0,1) -- (4,4);

% Marca de b
\draw (-0.08,1) -- (0.08,1);
\node[left] at (0,1) {$b$};

% Triángulo para la pendiente
\draw[dashed] (1,1.75) -- (2,1.75);
\draw[dashed] (2,1.75) -- (2,2.5);

\node[below] at (1.5,1.75) {$1$};
\node[right] at (2,2.1) {$a$};

% Ángulo alfa
\draw (1.7,1.8) arc[start angle=0,end angle=37,radius=0.5];
\node at (1.4,1.9) {$\alpha$};

% Etiquetas
\node[color=teal] at (3.2,2.5) {$f(x)=ax+b$};
\node at (3.2,1.5) {$\mathrm{tg}(\alpha)=a$};

\end{tikzpicture}
\end{document}
```

> Contexto para NotebookLM: usar para $f(x)=ax+b$. Mostrar triángulo de pendiente con catetos `1` y `a`, marca de $b$ en eje $y$, y ángulo $\alpha$ en la recta.

**Función constante**

Cuando:
$$a=0$$

la función queda:
$$f(x)=b$$

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.2]

\draw[->] (-0.5,0) -- (4,0) node[right] {$x$};
\draw[->] (0,-0.5) -- (0,3) node[above] {$y$};

\draw[very thick,color=teal] (-0.2,2) -- (3.5,2);

\node[left] at (0,2) {$b$};
\node[above right] at (2.5,2) {$f(x)=b$};

\end{tikzpicture}
\end{document}
```

> Contexto para NotebookLM: usar para $f(x)=b$ con $a=0$. Recta horizontal, sin triángulo de pendiente, etiqueta $b$ en eje $y$.

**Recta vertical**

La ecuación:

$$x=c$$

representa una recta vertical.

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.2] % N6: Mediano

% Ejes
\draw[->] (-1,0) -- (3.5,0);
\draw[->] (0,-1) -- (0,3.5);

% Recta vertical x=c
\draw[very thick,color=orange] (2,-0.8) -- (2,3);

% Etiquetas
\node at (2,-0.3) {$c$};
\node at (2.7,2.5) {$x=c$};

\end{tikzpicture}
\end{document}
```

> Contexto para NotebookLM: usar para $x=c$. Recta vertical en `orange` — no es función. Útil para ilustrar por qué falla el test de la recta vertical.

La recta vertical no representa una función.


**Función lineal**

$$y=f(x)=ax \, ; \, a\in \mathbb{R}$$
$$D_{f}=\mathbb{R} \, ; \, R_{f}=\mathbb{R}$$


```tikz
\begin{document}
\begin{tikzpicture}[scale=1.2] % N6: Mediano

% Ejes
\draw[->] (-0.5,0) -- (4.5,0) node[right] {$x$};
\draw[->] (0,-0.5) -- (0,3.5) node[above] {$y$};

% Recta
\draw[very thick,color=teal] (0,0) -- (4,3);



% Etiquetas
\node[right] at (2,1.15) {$a$};

% Ángulo alfa
\draw (0.6,0) arc[start angle=0,end angle=37,radius=0.6];
\node at (0.95,0.25) {$\alpha$};

% Fórmula
\node[below right] at (2.6,1.9) {recta en el origen};

\end{tikzpicture}
\end{document}
```

> Contexto para NotebookLM: usar para $f(x)=ax$ (recta en el origen). Mostrar ángulo $\alpha$ en la base y etiqueta de pendiente $a$ sobre la recta.

**Ejemplo — test de la recta vertical**

```tikz
\usepackage{pgfplots}
\begin{document}
\begin{tikzpicture}
\begin{axis}[
    axis lines=middle,
    xmin=-0.5, xmax=13,
    ymin=-1.5, ymax=1.5,
    width=8cm,
    height=7cm,
    xlabel={$x$},
    ylabel={$y$},
    xtick=\empty,
    ytick={-1,0,1}
]

% Curva senoidal
\addplot[
    very thick,
    teal,
    domain=0:12.56,
    samples=200
]
{sin(deg(x))};

% Rectas verticales
\draw[dashed,gray] (axis cs:1, -1.3) -- (axis cs:1, 1.3);
\draw[dashed,gray] (axis cs:4, -1.3) -- (axis cs:4, 1.3);
\draw[dashed,gray] (axis cs:7, -1.3) -- (axis cs:7, 1.3);
\draw[dashed,gray] (axis cs:10, -1.3) -- (axis cs:10, 1.3);

% Puntos de intersección
\fill[orange] (axis cs:1,{sin(deg(1))}) circle (2pt);
\fill[orange] (axis cs:4,{sin(deg(4))}) circle (2pt);
\fill[orange] (axis cs:7,{sin(deg(7))}) circle (2pt);
\fill[orange] (axis cs:10,{sin(deg(10))}) circle (2pt);

\end{axis}
\end{tikzpicture}
\end{document}
```

> Contexto para NotebookLM: usar para ilustrar el test de la recta vertical en una función. Rectas verticales punteadas en distintos $x$, cada una corta la curva en exactamente un punto — confirma que es función. Si en cambio una vertical corta en más de un punto, la gráfica no es función (ver ejemplo $y^2=x+1$ abajo).

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.2] % N6: Mediano

% Ejes
\draw[->] (-2,0) -- (6,0) node[right] {$x$};
\draw[->] (0,-3) -- (0,3) node[above] {$y$};

% Ticks eje x
\foreach \x in {-1,1,2,3,4,5}
    \draw (\x,0.05) -- (\x,-0.05) node[below, font=\small] {\x};

% Ticks eje y
\foreach \y in {-2,-1,1,2}
    \draw (0.05,\y) -- (-0.05,\y) node[left, font=\small] {\y};

% Parábola y²=x+1 → x=y²-1, graficada con y como parámetro
\draw[very thick, teal, smooth, samples=100, domain=-2.7:2.7]
    plot ({(\x)^2 - 1}, {\x});

% Recta vertical x=2
\draw[dashed, gray, thick] (2,-2.7) -- (2,2.7);

% Puntos de intersección
\fill[orange] (2, 1.732) circle (0.07);
\fill[orange] (2,-1.732) circle (0.07);

% Etiquetas curva y recta
\node[teal] at (4.8, 2) {$y^2=x+1$};
\node[gray]  at (2.6, 2.4) {$x=2$};



% Vértice
\fill[teal] (-1,0) circle (0.07);
\node[teal, above left, font=\small] at (-1,0) {$(-1,0)$};

\end{tikzpicture}
\end{document}
```

> Contexto para NotebookLM: usar para ilustrar el test de la recta vertical en una relación que NO es función. La parábola $y^2=x+1$ (horizontal) y la vertical $x=2$ cortan en dos puntos — confirma que no es función.

---

#### Función de 2do grado (parabólica)

$$y=f(x)=ax^{2}+bx+c \quad ; \quad a,b,c\in\mathbb{R}$$

$$D_f=\mathbb{R}$$

$$R_f=\text{según coeficientes } a,b,c$$



- para $a>0$


```tikz
\begin{document}
\begin{tikzpicture}[scale=1.2]

% Ejes
\draw[->] (-0.5,0) -- (5,0) node[right] {$x$};
\draw[->] (0,-0.5) -- (0,3.5) node[above] {$y$};

% Parábola: y = a(x-h)² + k  con h=2, k=1, a=0.5
\draw[very thick, teal, smooth, samples=100, domain=-0.2:4.2]
    plot ({\x}, {0.5*(\x-2)^2 + 1});

% Vértice
\fill[teal] (2,1) circle (0.06);
\node[below right, font=\small] at (2,1) {$V(2,1)$};

% Líneas guía punteadas
\draw[dashed, gray] (2,0) -- (2,1);
\draw[dashed, gray] (0,1) -- (2,1);

% Etiquetas ejes
\node[below] at (2,0) {$2$};
\node[left]  at (0,1) {$1$};

% Etiquetas
\node[teal, right, font=\small] at (3.2,2.6) {$y=a(x-2)^2+1$};
\node[right, font=\small] at (0.3,0.3) {$a>0$};

\end{tikzpicture}
\end{document}
```

> Contexto para NotebookLM: usar para parábola cóncava arriba ($a>0$). Mostrar vértice $V$ con líneas guía punteadas al eje $x$ e $y$. Etiqueta de la ecuación en forma vértice.

- para $a<0$

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.2]

% Ejes
\draw[->] (-0.5,0) -- (5,0) node[right] {$x$};
\draw[->] (0,-0.5) -- (0,4) node[above] {$y$};

% Parábola: y = a(x-h)² + k  con h=2, k=2.5, a=-0.5
\draw[very thick, teal, smooth, samples=100, domain=-0.5:4.5]
    plot ({\x}, {-0.5*(\x-2)^2 + 2.5});

% Vértice
\fill[teal] (2,2.5) circle (0.06);
\node[above right, font=\small] at (2,2.5) {$V(2,\,2.5)$};

% Líneas guía punteadas
\draw[dashed, gray] (2,0) -- (2,2.5);
\draw[dashed, gray] (0,2.5) -- (2,2.5);

% Etiquetas ejes
\node[below] at (2,0) {$2$};
\node[left]  at (0,2.5) {$2.5$};

% Etiquetas
\node[teal, right, font=\small] at (3.0,0.5) {$y=a(x-2)^2+2.5$};
\node[right, font=\small] at (0.3,3.5) {$a<0$};

\end{tikzpicture}
\end{document}
```

> Contexto para NotebookLM: usar para parábola cóncava abajo ($a<0$). Misma estructura que $a>0$: vértice $V$ con líneas guía. El vértice es máximo en este caso.

Se reconoce las graficas identificando

- Vértice $$V=(h,k)$$.
    
- Eje de simetría: $$x=h$$
---

**Ejemplo**
$y-\frac{11}{2}=-2\left(x-\frac32\right)^{2}$

Como (a<0), la parábola abre hacia abajo.

```tikz
\begin{document}
\begin{tikzpicture}[scale=0.7] % N6: Pequeño

% Ejes
\draw[->] (-1,0) -- (4,0) node[right] {$x$};
\draw[->] (0,-1) -- (0,7) node[above] {$y$};

% Ticks eje x
\foreach \x in {-1,1,2,3}
    \draw (\x,0.05) -- (\x,-0.05) node[below, font=\small] {\x};

% Ticks eje y
\foreach \y in {1,2,3,4,5,6}
    \draw (0.05,\y) -- (-0.05,\y) node[left, font=\small] {\y};

% Parábola: y = -2(x - 3/2)² + 11/2
\draw[very thick, teal, smooth, samples=150, domain=-0.45:3.45]
    plot ({\x}, {-2*(\x - 1.5)^2 + 5.5});

% Vértice V(3/2, 11/2)
\fill[teal] (1.5, 5.5) circle (0.07);
\node[above right, font=\small] at (1.5, 5.5) {$V\!\left(\frac{3}{2},\frac{11}{2}\right)$};

% Líneas guía punteadas al vértice
\draw[dashed, gray] (1.5, 0) -- (1.5, 5.5);
\draw[dashed, gray] (0, 5.5) -- (1.5, 5.5);

% Tick vértice eje x y y
\node[below, font=\small] at (1.5,-0.05) {$\frac{3}{2}$};
\node[left,  font=\small] at (-0.3, 5.5) {$\frac{11}{2}$};

% Raíces: x = 3/2 ± √(11/4) = 3/2 ± √11/2
% x₁ ≈ -0.158   x₂ ≈ 3.158
\fill[orange] (-0.158, 0) circle (0.07);
\fill[orange] ( 3.158, 0) circle (0.07);
\node[below right, orange, font=\small] at (-2, 1) {$\frac{3-\sqrt{11}}{2}$};
\node[below left,  orange, font=\small] at ( 5.158, 0) {$\frac{3+\sqrt{11}}{2}$};

% Intersección eje y: x=0 → y = -2(9/4)+11/2 = 7/2
\fill[violet] (0, 3.5) circle (0.07);
\node[right, violet, font=\small] at (-0.1, 3.5) {$\frac{7}{2}$};

% Etiqueta ecuación
\node[teal, font=\small] at (3.3, 1.5) {$y-\frac{11}{2}=-2\!\left(x-\frac{3}{2}\right)^{\!2}$};

\end{tikzpicture}
\end{document}
```


> Contexto para NotebookLM: usar cuando el usuario dé una ecuación concreta de parábola. Mostrar vértice, raíces en `orange` con etiquetas exactas, e intersección con eje $y$ en `purple`.

$D_{f}=\mathbb{R}\quad ; \quad  R_{f}=\left]-\infty,\frac{11}{2}\right]$

---

#### Función potencial generalizada

$$y=f(x)=x^{n} \quad ; \quad n=2,3,4,5,\ldots$$

donde 
$$D_f=\mathbb{R}$$

$$
R_f=
\begin{cases}
\mathbb{R}^{+}\cup\{0\}, & \text{si } n \text{ es par} \\
\mathbb{R}, & \text{si } n \text{ es impar}
\end{cases}
$$

Ejemplo

```tikz
\begin{document}
\begin{tikzpicture}[scale=0.7] % N6: Pequeño

% Cuadrícula
%\draw[gray!25, thin, step=1] (-5,-5) grid (5,5);

% Ejes
\draw[->] (-5.3,0) -- (5.3,0) node[right] {$x$};
\draw[->] (0,-5.3) -- (0,5.3) node[above] {$y$};

% Ticks eje x
\foreach \x in {-5,-4,-3,-2,-1,1,2,3,4,5}
   \draw (\x,0.07) -- (\x,-0.07) node[below, font=\tiny] {\x};

% Ticks eje y
%\foreach \y in {-5,-4,-3,-2,-1,1,2,3,4,5}
%   \draw (0.07,\y) -- (-0.07,\y) node[left, font=\tiny] {\y};

% n=2  y=x^2   dominio recortado para no salir de y=5 → |x|≤√5≈2.236
\draw[very thick, teal, smooth, samples=120, domain=-2.236:2.236]
    plot ({\x}, {\x*\x});

% n=3  y=x^3   |x|≤∛5≈1.71
\draw[very thick, orange, smooth, samples=120, domain=-1.71:1.71]
    plot ({\x}, {\x*\x*\x});

% n=4  y=x^4   |x|≤5^(1/4)≈1.495
\draw[very thick, violet, smooth, samples=120, domain=-1.495:1.495]
    plot ({\x}, {\x*\x*\x*\x});

% n=5  y=x^5   |x|≤5^(1/5)≈1.38
\draw[very thick, red!70!black, smooth, samples=120, domain=-1.38:1.38]
    plot ({\x}, {\x*\x*\x*\x*\x});

% Leyenda
\draw[very thick, teal]          (1.8, 4.8) -- (2.8, 4.8) node[right, font=\small] {$f(x)=x^2$};
\draw[very thick, orange]        (1.8, 4.1) -- (2.8, 4.1) node[right, font=\small] {$f(x)=x^3$};
\draw[very thick, violet]        (1.8, 3.4) -- (2.8, 3.4) node[right, font=\small] {$f(x)=x^4$};
\draw[very thick, red!70!black]  (1.8, 2.7) -- (2.8, 2.7) node[right, font=\small] {$f(x)=x^5$};

% Origen
\fill[black] (0,0) circle (0.07);

\end{tikzpicture}
\end{document}
```

> Contexto para NotebookLM: usar cuando el usuario pida comparar $x^n$ para distintos $n$. Cuatro curvas en un mismo sistema: $x^2$ (`teal`), $x^3$ (`orange`), $x^4$ (`violet`), $x^5$ (`red!70!black`). Todas pasan por el origen.

---

#### Función exponencial

$$
y=f(x)=a^x
$$

con:

$$
a>0,\qquad a\neq 1
$$

$$
D_f=\mathbb{R}
$$

$$
R_f=\mathbb{R}^{+}
$$

- a>0

```tikz
\begin{document}
\begin{tikzpicture}[scale=0.9]

% Cuadrícula
%\draw[gray!25, thin, step=1] (-5,-1) grid (5,5);

% Ejes
\draw[->] (-5.3,0) -- (3,0) node[right] {$x$};
\draw[->] (0,-1.3) -- (0,5.3) node[above] {$y$};

% Ticks eje x
\foreach \x in {-5,-4,-3,-2,-1}
    \draw (\x,0.07) -- (\x,-0.07) node[below, font=\tiny] {\x};

% Ticks eje y
\foreach \y in {1,2,3,4,5}
    \draw (0.07,\y) -- (-0.07,\y) node[left, font=\tiny] {\y};

% Asíntota horizontal y=0
\draw[dashed, gray!60, thin] (-5.3,0) -- (5.3,0);

% a=2  y=2^x
% y=5 → x=log2(5)≈2.322   y=-1 → x=log2(-1) no existe, x→-∞ asíntota
\draw[very thick, teal, smooth, samples=150, domain=-5:2.322]
    plot ({\x}, {2^\x});

% a=3  y=3^x
% y=5 → x=log3(5)≈1.465
\draw[very thick, orange, smooth, samples=150, domain=-5:1.465]
    plot ({\x}, {3^\x});

% a=5  y=5^x
% y=5 → x=1
\draw[very thick, violet, smooth, samples=150, domain=-5:1]
    plot ({\x}, {5^\x});

% a=10  y=10^x
% y=5 → x=log10(5)≈0.699
\draw[very thick, red!70!black, smooth, samples=150, domain=-5:0.699]
    plot ({\x}, {10^\x});

% Punto común (0,1) para todas
\fill[black] (0,1) circle (0.07);
\node[below right, font=\small] at (0,1) {$(0,1)$};




% Leyenda
\draw[very thick, teal]         (-4.8, 4.8) -- (-3.8, 4.8) node[right, font=\small] {$y=2^x$};
\draw[very thick, orange]       (-4.8, 4.1) -- (-3.8, 4.1) node[right, font=\small] {$y=3^x$};
\draw[very thick, violet]       (-4.8, 3.4) -- (-3.8, 3.4) node[right, font=\small] {$y=5^x$};
\draw[very thick, red!70!black] (-4.8, 2.7) -- (-3.8, 2.7) node[right, font=\small] {$y=10^x$};

% Etiqueta asíntota
\node[gray, font=\small] at (3.5,-0.6) {asíntota $y=0$};

\end{tikzpicture}
\end{document}
```


> Contexto para NotebookLM: usar para familia $a^x$ con $a>1$ (creciente). Cuatro curvas con distintas bases, punto común $(0,1)$, asíntota horizontal $y=0$. Leyenda en esquina superior izquierda.

- 0<a<1

```tikz
\begin{document}
\begin{tikzpicture}[scale=0.9]

% Ejes
\draw[->] (-3,0) -- (5.3,0) node[right] {$x$};
\draw[->] (0,-1.3) -- (0,5.3) node[above] {$y$};

% Ticks eje x
\foreach \x in {1,2,3,4,5}
    \draw (\x,0.07) -- (\x,-0.07) node[below, font=\tiny] {\x};

% Ticks eje y
\foreach \y in {1,2,3,4,5}
    \draw (0.07,\y) -- (-0.07,\y) node[left, font=\tiny] {\y};

% Asíntota horizontal y=0
\draw[dashed, gray!60, thin] (-3,0) -- (5.3,0);

% a=1/2  y=(1/2)^x
% y=5 → x=log_{1/2}(5)=-log2(5)≈-2.322
\draw[very thick, teal, smooth, samples=150, domain=-2.322:5]
    plot ({\x}, {(0.5)^\x});

% a=1/3  y=(1/3)^x
% y=5 → x=-log3(5)≈-1.465
\draw[very thick, orange, smooth, samples=150, domain=-1.465:5]
    plot ({\x}, {(0.333)^\x});

% a=1/5  y=(1/5)^x
% y=5 → x=-1
\draw[very thick, violet, smooth, samples=150, domain=-1:5]
    plot ({\x}, {(0.2)^\x});

% a=1/10  y=(1/10)^x
% y=5 → x=-log10(5)≈-0.699
\draw[very thick, red!70!black, smooth, samples=150, domain=-0.699:5]
    plot ({\x}, {(0.1)^\x});

% Punto común (0,1)
\fill[black] (0,1) circle (0.07);
\node[below left, font=\small] at (0,1) {$(0,1)$};

% Leyenda
\draw[very thick, teal]         (2.5, 4.8) -- (3.5, 4.8) node[right, font=\small] {$y=\left(\frac{1}{2}\right)^x$};
\draw[very thick, orange]       (2.5, 4.1) -- (3.5, 4.1) node[right, font=\small] {$y=\left(\frac{1}{3}\right)^x$};
\draw[very thick, violet]       (2.5, 3.4) -- (3.5, 3.4) node[right, font=\small] {$y=\left(\frac{1}{5}\right)^x$};
\draw[very thick, red!70!black] (2.5, 2.7) -- (3.5, 2.7) node[right, font=\small] {$y=\left(\frac{1}{10}\right)^x$};

% Etiqueta asíntota
\node[gray, font=\small] at (-1.5,-0.6) {asíntota $y=0$};

\end{tikzpicture}
\end{document}
```

> Contexto para NotebookLM: usar para familia $a^x$ con $0<a<1$ (decreciente). Misma estructura que $a>1$: cuatro curvas, punto común $(0,1)$, asíntota $y=0$. Leyenda en esquina superior derecha.

en general  $a=\dfrac{1}{b}$


$$f(x)=a^{x} = \left( \frac{1}{b}\right)^{x}= b^{-x} \quad ;\quad b>1$$

- Caso particular
$$a= e = 2,718281\dots \quad = \text{número de nepper}$$

```tikz
\begin{document}
\begin{tikzpicture}[scale=0.9]
% Ejes
\draw[->] (-5.3,0) -- (5.3,0) node[right] {$x$};
\draw[->] (0,-1.3) -- (0,5.3) node[above] {$y$};
% Ticks eje x
\foreach \x in {-5,-4,-3,-2,-1,1,2,3,4,5}
    \draw (\x,0.07) -- (\x,-0.07) node[below, font=\tiny] {\x};
% Ticks eje y
\foreach \y in {1,2,3,4,5}
    \draw (0.07,\y) -- (-0.07,\y) node[left, font=\tiny] {\y};
% f(x)=e^x
\draw[very thick, teal, smooth, samples=150, domain=-5:1.609]
    plot ({\x}, {exp(\x)});
% Tangente en (0,1): y = x + 1  →  pasa por (0,1) con pendiente 1
\draw[dashed, gray, thick] (-2.3,-1.3) -- (4,5);
\node[gray, font=\small] at (4.2,5.0) {$\frac{\pi}{4}$};
% Punto (0,1)
\fill[black] (0,1) circle (0.07);
\node[below right, font=\small] at (-1,1.7) {$(0,1)$};
% Leyenda
\draw[very thick, teal] (-4.8,4.8) -- (-3.8,4.8)
    node[right, font=\small] {$f(x)=e^x$};


\fill[black] (0,1) circle (0.07);
\node[below right, font=\small] at (-0.5,0.7) {$\alpha = 45^{\circ}$};

% Ángulo alfa
\draw (-0.5,0) arc[start angle=0,end angle=37,radius=0.6];
    
\end{tikzpicture}
\end{document}
```

> Contexto para NotebookLM: usar para el caso particular $f(x)=e^x$. Mostrar la tangente en $(0,1)$ con pendiente 1 ($\alpha=45°$) como rasgo distintivo de esta base.

---

#### Funciones logarítmicas

$y=f(x)=\log_{a}{x} \quad ; \quad a>0,\ a\neq 1 \qquad D_{f}=\mathbb{R}^{+},\ R_{f}=\mathbb{R}$

- $a>1$

```tikz
\begin{document}
\begin{tikzpicture}[scale=0.9]

% Ejes
\draw[->] (-1.3,0) -- (5.3,0) node[right] {$x$};
\draw[->] (0,-3.3) -- (0,5.3) node[above] {$y$};

% Ticks eje x
\foreach \x in {1,2,3,4,5}
    \draw (\x,0.07) -- (\x,-0.07) node[below, font=\tiny] {\x};
\draw (-1,0.07) -- (-1,-0.07) node[below, font=\tiny] {$-1$};

% Ticks eje y
\foreach \y in {-3,-2,-1,1,2,3,4,5}
    \draw (0.07,\y) -- (-0.07,\y) node[left, font=\tiny] {\y};

% f(x) = log_2(x)
\draw[very thick, teal, smooth, samples=200, domain=0.03:5]
    plot ({\x}, {ln(\x)/ln(2)});

% Asíntota vertical x=0 (referencia punteada)
\draw[dotted, gray!60] (0,-3.2) -- (0,5.2);

% Tangente en (1,0): derivada de log_2(x) es 1/(x*ln2), en x=1 es 1/ln(2)≈1.4427
% y - 0 = (1/ln2)(x - 1)  →  y = (x-1)/ln(2)
\draw[dashed, gray, thick, domain=-0.5:3.6]
    plot ({\x}, {(\x - 1)/ln(2)});

% Punto (1,0)
\fill[black] (1,0) circle (0.07);
\node[above right, font=\small] at (1,0) {$(1,0)$};

% Ángulo alfa en el origen de la tangente
\draw (1.55,0) arc[start angle=0,end angle=55,radius=0.55];
\node[font=\scriptsize] at (1.8,0.3) {$\alpha$};

% Etiqueta ángulo en grados aproximado
\node[below right, font=\small] at (2.5,0.4) {$\approx 55.3^\circ$};

% Leyenda
\draw[very thick, teal] (-0.8,4.8) -- (0.2,4.8)
    node[right, font=\small] {$f(x)=\log_2 x$};

% Asíntota label
\node[gray, font=\tiny] at (-0.45,-2.5) {$x=0$};

\end{tikzpicture}
\end{document}
```

> Contexto para NotebookLM: usar para $\log_a x$ con $a>1$ (creciente). Asíntota vertical $x=0$ punteada, tangente en $(1,0)$, ángulo $\alpha$ en ese punto.

- $0<a<1$


```tikz
\begin{document}
\begin{tikzpicture}[scale=0.9]

% Ejes
\draw[->] (-1.3,0) -- (5.3,0) node[right] {$x$};
\draw[->] (0,-3.3) -- (0,5.3) node[above] {$y$};

% Ticks eje x manualmente
\draw (1,0.07) -- (1,-0.07) node[below, font=\tiny] {$1$};
\draw (2,0.07) -- (2,-0.07) node[below, font=\tiny] {$2$};
\draw (3,0.07) -- (3,-0.07) node[below, font=\tiny] {$3$};
\draw (4,0.07) -- (4,-0.07) node[below, font=\tiny] {$4$};
\draw (5,0.07) -- (5,-0.07) node[below, font=\tiny] {$5$};

% Ticks eje y manualmente
\draw (0.07,1) -- (-0.07,1) node[left, font=\tiny] {$1$};
\draw (0.07,2) -- (-0.07,2) node[left, font=\tiny] {$2$};
\draw (0.07,3) -- (-0.07,3) node[left, font=\tiny] {$3$};
\draw (0.07,-1) -- (-0.07,-1) node[left, font=\tiny] {$-1$};
\draw (0.07,-2) -- (-0.07,-2) node[left, font=\tiny] {$-2$};
\draw (0.07,-3) -- (-0.07,-3) node[left, font=\tiny] {$-3$};

% f(x) = log_{1/2}(x) aproximada con puntos clave unidos
% log_{1/2}(x) = -log_2(x)
% Valores: (0.125, 3), (0.25, 2), (0.5, 1), (1, 0), (2,-1), (4,-2)
\draw[very thick, teal, smooth]
    (0.06,4.06) ..controls (0.1,3.5) and (0.2,2.5)..
    (0.25,2) ..controls (0.35,1.4) and (0.45,0.8)..
    (0.5,1) ..controls (0.7,0.4) and (0.85,0.1)..
    (1,0) ..controls (1.5,-0.6) and (1.8,-0.9)..
    (2,-1) ..controls (2.8,-1.4) and (3.5,-1.8)..
    (4,-2) ..controls (4.5,-2.2) and (4.9,-2.4)..
    (5,-2.32);

% Asintota vertical punteada
\draw[dotted, gray] (0,-3.2) -- (0,5.2);

% Tangente en (1,0): pendiente = -1/ln(2) ≈ -1.4427
% y = -1.4427*(x-1)
% en x=0: y=1.4427, en x=3: y=-2.885 (fuera), usamos x in [0, 2.8]
\draw[dashed, gray, thick] (0, 1.44) -- (2.8, -2.6);

% Punto (1,0)
\fill[black] (1,0) circle (0.07);
\node[above right, font=\small] at (1,0) {$(1,0)$};

% Puntos de referencia
\fill[black] (2,-1) circle (0.05);
\node[right, font=\tiny] at (2.05,-1) {$(2,-1)$};
\fill[black] (4,-2) circle (0.05);
\node[right, font=\tiny] at (4.05,-2) {$(4,-2)$};
\fill[black] (0.5,1) circle (0.05);
\node[right, font=\tiny] at (0.55,1) {$(1/2,1)$};

% Angulo en (1,0)
\draw (1.45,0) arc[start angle=0, end angle=125, radius=0.45];
\node[font=\scriptsize] at (0.75,0.38) {$\alpha$};

% Leyenda
\draw[very thick, teal] (0.2,4.8) -- (1.0,4.8);
\node[right, font=\small] at (1.05,4.8) {$f(x)=\log_{1/2} x$};

\end{tikzpicture}
\end{document}
```

> Contexto para NotebookLM: usar para $\log_a x$ con $0<a<1$ (decreciente). Misma estructura que $a>1$: asíntota $x=0$, tangente en $(1,0)$, pero la curva desciende.

### Funciones trigonométricas

Se definen en la circunferencia trigonométrica.

```tikz
\begin{document}
\begin{tikzpicture}[scale=2]

% Ejes
\draw[->] (-1.2,0) -- (2.1,0) node[right] {$x$};
\draw[->] (0,-0.2) -- (0,1.4) node[above] {$y$};

% Semicircunferencia superior punteada
\draw[thick, dashed,teal] (1,0) arc (0:180:1);

% Recta L desde el origen (angulo 30 grados)
% pasa por P=(cos30,sin30), R=(1, tan30), M=(cot30, 1)
% tan(30)=1/sqrt(3) ~ 0.5774, cot(30)=sqrt(3) ~ 1.7321
\draw[thick, orange ] (0,0) -- (1.85,1.069);

% Recta tangente horizontal en N=(0,1)
\draw[thick,dashed] (-1.1,1) -- (1.85,1);

% Recta tangente vertical en T=(1,0)
\draw[thick,dashed] (1,-0.5) -- (1,1.3);

% Punto P = (cos30, sin30) = (0.866, 0.5)
\fill (0.866,0.5) circle (0.03);
\node[above left, font=\small] at (0.866,0.5) {$P$};

% Punto N = (0,1)
\fill (0,1) circle (0.03);
\node[left, font=\small] at (0.3,1.1) {$N$};

% Punto M = (sqrt(3), 1) ~ (1.7321, 1)
\fill (1.7321,1) circle (0.03);
\node[above, font=\small] at (1.7321,1) {$M$};

% Punto T = (1,0)
\fill (1,0) circle (0.03);
\node[below, font=\small] at (0.85,0) {$T$};

% Punto R = (1, tan30) = (1, 0.5774)
\fill (1,0.5774) circle (0.03);
\node[right, font=\small] at (1,0.5774) {$R$};

% Origen
\node[below left, font=\small] at (0,0) {$O$};

% Angulo 30 grados en el origen
\draw (0.25,0) arc (0:30:0.25);
\node[font=\small] at (0.36,0.08) {$x$};

% Labels de tangentes
\node[above, font=\small] at (-0.9,1) {Tangente en $N$};
\node[right, font=\small] at (1.1,-0.4) {Tangente en $T$};

% Labels lado derecho (+) 0 y (-) 360
\node[right, font=\small] at (1.05,0.05) {$(+)\ 0^\circ$};
\node[right, font=\small] at (1.05,-0.12) {$(-)\ 360^\circ$};

% Segmentos de referencia punteados
\draw[dotted] (0.866,0) -- (0.866,0.5);
\draw[dotted] (0,0.5) -- (0.866,0.5);

% Tick en x=1
\draw (1,0.04) -- (1,-0.04) node[below, font=\tiny] {$1$};

% Tick en y=1
\draw (0.04,1) -- (-0.04,1);

\end{tikzpicture}
\end{document}
```

Donde:

> Contexto para NotebookLM: usar cuando el usuario pida el diagrama de la circunferencia trigonométrica con los seis segmentos. Semicircunferencia en `teal` punteada, recta del ángulo en `orange`, tangentes verticales y horizontales como guías. Los puntos $P$, $T$, $R$, $M$, $N$ identifican cada razón trigonométrica según la tabla de abajo.

| $\sin{x}=\overline{PQ}$ | $\tan{x}=\overline{RT}$ | $\sec{x}=\overline{OR}$ |
| ----------------------- | ----------------------- | ----------------------- |
| $\cos{x}=\overline{OQ}$ | $\cot{x}=\overline{MN}$ | $\csc{x}=\overline{OM}$ |

---

#### Función seno

$$y=f(x)=\sin{x}$$

$$D_{f}=\mathbb{R} \quad ; \quad R_{f}=[-1,1]$$

Grafica :

```tikz
\usepackage{pgfplots}
\begin{document}
\begin{tikzpicture}
\begin{axis}[
    axis lines=middle,
    xmin=-3, xmax=13,
    ymin=-1.2, ymax=1.2,
    width=8cm,
    height=7cm,
    xlabel={$x$},
    ylabel={$y$},
    xtick=\empty,
    ytick={-1,0,1}
]

% Funcion
\addplot[
    very thick,
    teal,
    domain=-4:12.56,
    samples=200
]
{sin(deg(x))};

% Asintotas verticales - gruesas para tapar la linea falsa
\draw[dashed, gray, line width=1pt] (axis cs:-3, 1) -- (axis cs:13, 1);
\draw[dashed, gray, line width=1pt] (axis cs:-3, -1) -- (axis cs:13, -1);

% Puntos donde tan(x)=0
\fill[orange] (axis cs:0, 0) circle (2pt)node[above right] {$0$};
\fill[orange] (axis cs:3.14, 0) circle (2pt)node[above right] {$\pi$};
\fill[orange] (axis cs:6.28, 0) circle (2pt)node[above right] {$2\pi$};
\fill[orange] (axis cs:9.42, 0) circle (2pt)node[above right] {$3\pi$};


\end{axis}
\end{tikzpicture}
\end{document}
```

> Contexto para NotebookLM: usar para graficar $\sin x$. Mostrar al menos dos períodos, puntos en ceros con etiqueta ($0$, $\pi$, $2\pi$, $3\pi$) en `orange`, banda $y=\pm1$ en punteado gris.

>$f(x)=\sin x$ es periódico con $p=2\pi$ y es impar $\sin{-x}=-\sin{x}$

---

#### Función coseno

$$y=f(x)=\cos{x}$$

$$D_{f}=\mathbb{R} \quad ; \quad R_{f}=[-1,1]$$

Grafica :

```tikz
\usepackage{pgfplots}
\begin{document}
\begin{tikzpicture}
\begin{axis}[
    axis lines=middle,
    xmin=-3, xmax=13,
    ymin=-1.2, ymax=1.2,
    width=8cm,
    height=7cm,
    xlabel={$x$},
    ylabel={$y$},
    xtick=\empty,
    ytick={-1,0,1}
]

% Funcion
\addplot[
    very thick,
    teal,
    domain=-4:12.56,
    samples=200
]
{cos(deg(x))};

% Asintotas verticales - gruesas para tapar la linea falsa
\draw[dashed, gray, line width=1pt] (axis cs:-3, 1) -- (axis cs:13, 1);
\draw[dashed, gray, line width=1pt] (axis cs:-3, -1) -- (axis cs:13, -1);

% Puntos donde tan(x)=0
\fill[orange] (axis cs:1.57, 0) circle (2pt)node[above right] {$\frac{\pi}{2}$};
\fill[orange] (axis cs:4.71, 0) circle (2pt)node[above right] {$\frac{3\pi}{2}$};
\fill[orange] (axis cs:7.85, 0) circle (2pt)node[above right] {$\frac{5\pi}{2}$};
\fill[orange] (axis cs:10.99, 0) circle (2pt)node[above right] {$\frac{7\pi}{2}$};


\end{axis}
\end{tikzpicture}
\end{document}
```

> Contexto para NotebookLM: usar para graficar $\cos x$. Misma estructura que seno, puntos en ceros desplazados ($\pi/2$, $3\pi/2$, $5\pi/2$, $7\pi/2$) en `orange`.

>$f(x)=\cos x$ es periódico con $p=2\pi$ y es par $\cos{-x}=\cos{x}$

---

#### Función tangente

$$y=f(x)=\tan{x}=\dfrac{\sin x}{\cos x}$$

$$D_{f}=\mathbb{R} \quad \rightarrow \{ \; x / x = (2k+1)\frac{\pi}{2}\quad,\quad k\in \mathbb{Z} \; \}$$

$$R_{f}=\mathbb{R}$$

>$f(x)=\tan x$ es periódico con $p=2\pi$ y es impar $\tan{-x}=-\tan{x}$

Grafica :

```tikz
\usepackage{pgfplots}
\begin{document}
\begin{tikzpicture}
\begin{axis}[
    axis lines=middle,
    xmin=-3, xmax=13,
    ymin=-4, ymax=4,
    width=11cm,
    height=9cm,
    xlabel={$x$},
    ylabel={$y$},
    xtick=\empty,
    ytick={-1,0,1}
]

% Curva tangente
\addplot[
    very thick,
    teal,
    domain=-4:12.56,
    samples=200
]
{tan(deg(x))};

% Asintotas verticales - gruesas para tapar la linea falsa
\draw[dashed, gray, line width=3pt] (axis cs:-1.57, -4) -- (axis cs:-1.57, 4);

\draw[dashed, gray, line width=3pt] (axis cs:1.57, -4) -- (axis cs:1.57, 4);
\draw[dashed, gray, line width=3pt] (axis cs:4.71, -4) -- (axis cs:4.71, 4);
\draw[dashed, gray, line width=3pt] (axis cs:7.85, -4) -- (axis cs:7.85, 4);
\draw[dashed, gray, line width=3pt] (axis cs:10.99, -4) -- (axis cs:10.99, 4);

% Puntos donde tan(x)=0
\fill[orange] (axis cs:0, 0) circle (2pt)node[above right] {$0$};
\fill[orange] (axis cs:3.14, 0) circle (2pt)node[above right] {$\pi$};
\fill[orange] (axis cs:6.28, 0) circle (2pt)node[above right] {$2\pi$};
\fill[orange] (axis cs:9.42, 0) circle (2pt)node[above right] {$3\pi$};


\end{axis}
\end{tikzpicture}
\end{document}
```




> Contexto para NotebookLM: usar para graficar $\tan x$. Asíntotas verticales en $x=(2k+1)\pi/2$ con `line width=3pt` para tapar la línea falsa que pgfplots dibuja entre ramas. Puntos en ceros en `orange`.

---

**Funciones trigonométricas inversas**

#### Funcion $\arcsin$

$$y=f(x)=\arcsin{x}$$

$$D_{f}=[-1,1] \quad ; \quad R_{f}=\Big [-\frac{\pi}{2},\frac{\pi}{2}\Big ]$$

Grafica :

```tikz
\usepackage{pgfplots}
\begin{document}
\begin{tikzpicture}
\begin{axis}[
    axis lines=middle,
    xmin=-2, xmax=2,
    ymin=-2, ymax=2,
    width=11cm,
    height=9cm,
    xlabel={$x$},
    ylabel={$y$},
    xtick={-1,0,1},
    ytick={-1,0,1}
]

% Funcion seno
\addplot[
    dashed,
    very thick,
    teal,
    domain=-4:4,
    samples=200
]{sin(deg(x))};

% Linea espejo y=x
\draw[dashed, gray, line width=1pt] (axis cs:-4, -4) -- (axis cs:4, 4);

% Funcion arcoseno
\addplot[
    very thick,
    orange,
    domain=-1:1,
    samples=200
]{asin(x)/180*pi};

% Puntos clave arcoseno
\fill[orange] (axis cs:-1, -1.5708) circle (2pt) node[left] {$(-1,-\frac{\pi}{2})$};
\fill[orange] (axis cs:0, 0)        circle (2pt) node[above right] {$(0,0)$};
\fill[orange] (axis cs:1,  1.5708)  circle (2pt) node[right] {$(1,\frac{\pi}{2})$};
%asintotas
%||
\draw[dashed, gray, line width=1pt] (axis cs:1, -2) -- (axis cs:1, 2);
\draw[dashed, gray, line width=1pt] (axis cs:-1, -2) -- (axis cs:-1, 2);
%--
\draw[dashed, gray, line width=1pt] (axis cs:-2, -1.57) -- (axis cs:2, -1.57);
\draw[dashed, gray, line width=1pt] (axis cs:-2, 1.57) -- (axis cs:2, 1.57);

\end{axis}
\end{tikzpicture}
\end{document}
```


> Contexto para NotebookLM: usar para graficar $\arcsin x$. Mostrar $\sin x$ en `teal` punteado como referencia, espejo $y=x$ en gris, y la rama principal $\arcsin$ en `orange`. Puntos clave: $(-1,-\pi/2)$, $(0,0)$, $(1,\pi/2)$. Recuadro con asíntotas horizontales y verticales.

---

#### Funcion $\arccos$

$$y=f(x)=\arccos{x}$$

$$D_{f}=[-1,1] \quad ; \quad R_{f}= [0 ,\pi ]$$

Grafica :

```tikz
\usepackage{pgfplots}
\begin{document}
\begin{tikzpicture}
\begin{axis}[
    axis lines=middle,
    xmin=-2.5, xmax=3,
    ymin=-2, ymax=4,
    width=11cm,
    height=9cm,
    xlabel={$x$},
    ylabel={$y$},
    xtick={-1,0,1},
    ytick={0,1,2,3}
]

% Funcion coseno rama principal [0,pi]
\addplot[
    dashed,
    very thick,
    teal,
    domain=0:3.14,
    samples=100
]{cos(deg(x))};

% Linea espejo y=x
\draw[dashed, gray, line width=1pt] (axis cs:-2, -2) -- (axis cs:4, 4);

% Funcion arcocoseno
\addplot[
    very thick,
    orange,
    domain=-1:1,
    samples=200
]{acos(x)/180*pi};

% Puntos clave arcocoseno
\fill[orange] (axis cs:-1, 3.1416) circle (2pt) node[left] {$(-1,\pi)$};
\fill[orange] (axis cs:0, 1.5708)  circle (2pt) node[above right] {$(0,\frac{\pi}{2})$};
\fill[orange] (axis cs:1, 0)       circle (2pt) node[below right] {$(1,0)$};

% Lineas de referencia ||
\draw[dashed, gray, line width=1pt] (axis cs:1, -2) -- (axis cs:1, 4);
\draw[dashed, gray, line width=1pt] (axis cs:-1, -2) -- (axis cs:-1, 4);
% Lineas de referencia --
\draw[dashed, gray, line width=1pt] (axis cs:-2, 3.14) -- (axis cs:4, 3.14);
\draw[dashed, gray, line width=1pt] (axis cs:-2, 0) -- (axis cs:4, 0);

\end{axis}
\end{tikzpicture}
\end{document}
```


> Contexto para NotebookLM: usar para graficar $\arccos x$. Misma estructura que $\arcsin$: $\cos x$ en `teal` punteado (rama $[0,\pi]$), espejo $y=x$, $\arccos$ en `orange`. Puntos clave: $(-1,\pi)$, $(0,\pi/2)$, $(1,0)$.

---

#### Funcion $\arctan$

$$y=f(x)=\arctan{x}$$

$$D_{f}=\mathbb{R} \quad ; \quad R_{f}= \Big [ -\frac{\pi}{2},\frac{\pi}{2} \Big ]$$

Grafica :

```tikz
\usepackage{pgfplots}
\begin{document}
\begin{tikzpicture}
\begin{axis}[
    axis lines=middle,
    width=11cm,
    height=9cm,
    xmin=-4, xmax=4,
    ymin=-4, ymax=4,
    xlabel={$x$},
    ylabel={$y$},
    xtick={-1,0,1},
    ytick={-1,0,1}
]

% Tangente rama principal (-pi/2, pi/2)
\addplot[
    dashed,
    very thick,
    teal,
    domain=-1.47:1.47,
    samples=100
]{tan(deg(x))};

% Linea espejo y=x
\draw[dashed, gray, line width=1pt] (axis cs:-4, -4) -- (axis cs:4, 4);

% Arcotangente domain todos los reales
\addplot[
    very thick,
    orange,
    domain=-4:4,
    samples=200
]{atan(x)/180*pi};

% Puntos clave arctan
\fill[orange] (axis cs:-1, -0.7854) circle (2pt) node[below left] {$(-1,-\frac{\pi}{4})$};
\fill[orange] (axis cs:0, 0)        circle (2pt) node[above right] {$(0,0)$};
\fill[orange] (axis cs:1, 0.7854)   circle (2pt) node[above left] {$(1,\frac{\pi}{4})$};

% Asintotas horizontales de arctan en y=+-pi/2
\draw[dashed, gray, line width=1pt] (axis cs:-4,  1.5708) -- (axis cs:4,  1.5708);
\draw[dashed, gray, line width=1pt] (axis cs:-4, -1.5708) -- (axis cs:4, -1.5708);

% Asintotas verticales de tan en x=+-pi/2
\draw[dashed, gray, line width=1pt] (axis cs: 1.5708, -4) -- (axis cs: 1.5708, 4);
\draw[dashed, gray, line width=1pt] (axis cs:-1.5708, -4) -- (axis cs:-1.5708, 4);

\end{axis}
\end{tikzpicture}
\end{document}
```

> Contexto para NotebookLM: usar para graficar $\arctan x$. $\tan x$ en `teal` punteado (rama principal), espejo $y=x$, $\arctan$ en `orange` con asíntotas horizontales $y=\pm\pi/2$. Puntos clave: $(-1,-\pi/4)$, $(0,0)$, $(1,\pi/4)$.

---

### N14. T2 — LÍMITES Y CONTINUIDAD

> Primer parcial. Límites laterales, discontinuidades, comportamiento asintótico.

*(Agregar ejemplos confirmados aquí)*

---

### N15. T3 — DERIVACIÓN

> Segundo parcial. Pendiente de tangente, reglas de derivación, derivadas de funciones elementales.

*(Agregar ejemplos confirmados aquí)*

---

### N16. T4 — APLICACIONES DE LA DERIVACIÓN

> Segundo parcial. Máximos y mínimos, concavidad, optimización, teorema del valor medio.

*(Agregar ejemplos confirmados aquí)*

---

### N17. T5 — INTEGRACIÓN

> Tercer parcial. Integral definida, primitivas, regla de Barrow.

*(Agregar ejemplos confirmados aquí)*

---

### N18. T6 — APLICACIONES DE LA INTEGRACIÓN

> Tercer parcial. Área entre curvas, volúmenes de revolución.

*(Agregar ejemplos confirmados aquí)*

---

### N19. T7 — SERIES REALES (BONUS)

> Fuera de parciales. Series numéricas, criterios de convergencia.

*(Agregar ejemplos confirmados aquí)*

---

%%
galaxy-links
[[_galaxy-system]]
[[_note-system]]
%%


