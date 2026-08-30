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
  - ETN1015
date_created: 2026-08-12
date_updated: 2026-08-12
status: en-proceso
---

# ⚡ GUÍA UNIFICADA DE TIKZJAX PARA OBSIDIAN (ETN1015)

> Plugin: `obsidian-tikzjax` — renderiza LaTeX/TikZ como SVG directamente en tus notas usando WebAssembly.
> Guía específica de Procesamiento Digital de Señales — ETN1015, siguiendo el libro base Rao.
> Para cálculo y funciones reales ver `MAT101_TikzJax.md` en `_app/notebooklm/guides/MAT101/`.
> Este documento está organizado en tres bloques: **Reglas de sintaxis (N1–N10)**, **Checklist (N11)**, y **Biblioteca de ejemplos por capítulo Rao (N12–N19)**.

---

# 🤖 SECCIÓN NOTEBOOKLM

Instrucciones para que NotebookLM genere bloques TikzJax correctos listos para copiar
en Obsidian. Cuando el usuario pida un diagrama, responder con un bloque de código
— no con imagen ni enlace.

### Defaults — cuando el usuario no especifica

- Entorno: `tikzpicture` con bloques rectangulares si es diagrama de sistemas; `axis` (pgfplots) si es plano complejo s/z o espectro de frecuencia.
- Escala: `scale=1.2` como punto de partida para diagramas de bloques.
- Color de bloque principal: `teal`; señal de entrada/salida: `orange`; polos: `teal`; ceros: `orange`.
- Ejes en plano complejo: siempre con flechas `->` y etiquetas `node[right]{$\sigma$}` / `node[above]{$j\omega$}` (continuo) o `node[right]{$\text{Re}$}` / `node[above]{$\text{Im}$}` (discreto Z).

### Reglas base — siempre obligatorias

Antes de generar cualquier bloque, seguir este orden:
1. ¿Qué tipo de diagrama? (bloques → `tikzpicture` con rectángulos · plano complejo → `pgfplots axis` · tallo discreto → `pgfplots axis` con `ycomb` · flujo de señal → `tikzpicture` con nodos circulares)
2. ¿Qué paquete necesita? (ver N2)
3. ¿Escala y tamaño? (ver N6)
4. ¿Qué colores? (ver N7)
5. ¿Qué nivel de detalle requiere? (ver N10) — señal continua simple o espectro → Desmos; diagrama de bloques, polos/ceros, estructura de filtro → TikZJax. En caso de duda, revisar si el tipo ya tiene precedente en el Bloque C de esta guía o de `ETN1015_desmos.md`.

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
\draw (0,0) -- (1,0);
\end{tikzpicture}
```

✅ Correcto:
```tikz
\begin{document}
\begin{tikzpicture}
\draw (0,0) -- (1,0);
\end{tikzpicture}
\end{document}
```

---

### N2. PAQUETES DISPONIBLES PARA ETN1015

| Paquete | Para qué | Uso en ETN1015 |
|---------|---------|----------------|
| (ninguno) | Dibujo geométrico básico — `tikzpicture` puro | Diagramas de bloques, flujo de señal, LTI cajas |
| `pgfplots` | Gráficas 2D de precisión con ejes numéricos | Plano complejo s/z, espectros, señales discretas (tallo) |
| `amsmath` | Fracciones y notación avanzada en nodos | Obligatorio si se usa `\tfrac`, `\dfrac`, `H(s)`, `H(z)` dentro de nodos — ver N8 |
| `amssymb` | Símbolos matemáticos extendidos | Conjuntos $\mathbb{Z}$, $\mathbb{R}$, operadores |

> `circuitikz`, `chemfig` y `tikz-3dplot` no aplican a ETN1015.

---

### N3. ENTORNOS SEGÚN TIPO DE DIAGRAMA

| Tipo de diagrama | Entorno |
|-------------------|---------|
| Diagrama de bloques (sistemas LTI, filtros, estructuras) | `tikzpicture` con `\draw` + `\node` rectangulares |
| Diagrama de flujo de señal (SFG) | `tikzpicture` con nodos `circle` y flechas con etiquetas |
| Plano complejo s (Laplace) o z (Transformada Z) | `pgfplots` → `\begin{axis}[...]` con `axis lines=middle` |
| Señal discreta — diagrama de tallo | `pgfplots` → `\addplot[ycomb, ...]` |
| Señal continua simple (pocos elementos, esquemático) | `tikzpicture` con `plot` manual |
| Espectro de frecuencia (magnitud/fase discreto) | `pgfplots` → `\addplot[ycomb, ...]` |

---

### N4. SINTAXIS BASE PARA DIAGRAMAS DE BLOQUES

Los diagramas de bloques son el tipo más frecuente en ETN1015. Patrón estándar:

```tikz
\usepackage{amsmath}
\begin{document}
\begin{tikzpicture}[scale=1.2, >=latex]

% Señal de entrada
\draw[->] (-1.5,0) -- (-0.5,0);
\node[left] at (-1.5,0) {$x(t)$};

% Bloque sistema
\draw[thick] (-0.5,-0.4) rectangle (0.5,0.4);
\node at (0,0) {$H(s)$};

% Señal de salida
\draw[->] (0.5,0) -- (1.5,0);
\node[right] at (1.5,0) {$y(t)$};

\end{tikzpicture}
\end{document}
```

Elementos recurrentes:

```
% Flecha de señal
\draw[->, thick] (A) -- (B);

% Bloque rectangular etiquetado
\draw[thick] (x0-0.6, y0-0.4) rectangle (x0+0.6, y0+0.4);
\node at (x0, y0) {$H$};

% Sumador (círculo con +/-)
\draw[thick] (0,0) circle (0.25);
\draw (−0.25,0) -- (0.25,0);   % línea horizontal interna
\draw (0,−0.25) -- (0,0.25);   % línea vertical interna
\node[above right, font=\tiny] at (0.18,0.18) {$+$};

% Punto de bifurcación (bullet)
\fill (x0,y0) circle (0.05);

% Etiqueta de señal en línea
\node[above] at (x_mid, y_mid) {$e(t)$};
```

`>=latex` en las opciones del entorno da puntas de flecha estilizadas — incluir siempre.

---

### N5. PLANO COMPLEJO CON PGFPLOTS

Para plano s (Laplace) y plano z (Transformada Z):

```tikz
\usepackage{pgfplots}
\begin{document}
\begin{tikzpicture}
\begin{axis}[
    axis lines=middle,
    xmin=-3, xmax=3,
    ymin=-3, ymax=3,
    xlabel={$\sigma$},
    ylabel={$j\omega$},
    width=8cm, height=8cm,
    xtick={-2,-1,0,1,2},
    ytick={-2,-1,0,1,2},
    tick style={thin, black}
]
% Polo: X en la posición
\node[teal, font=\Large] at (axis cs:-1, 1) {$\times$};
\node[teal, font=\Large] at (axis cs:-1,-1) {$\times$};

% Cero: círculo vacío en la posición
\draw[orange, thick] (axis cs:0,0) circle [radius=6pt];

% Región de convergencia (sombreado)
% ...

\end{axis}
\end{tikzpicture}
\end{document}
```

**Convenciones de símbolos:**
- Polos → `\times` o `$\times$` en `teal` (font=\Large para visibilidad)
- Ceros → `\draw circle [radius=6pt]` en `orange`
- Eje $j\omega$ (continuo): etiqueta `$j\omega$`; eje Im (discreto): etiqueta `$\text{Im}$`
- Eje $\sigma$ (continuo); eje Re (discreto): etiqueta `$\text{Re}$`
- Circunferencia unitaria (plano z): `\draw[dashed, gray] (axis cs:0,0) circle [radius=1cm]` — siempre incluir en plano z

Para el plano z, ajustar etiquetas:
```
xlabel={$\text{Re}\{z\}$},
ylabel={$\text{Im}\{z\}$},
```
Y agregar la circunferencia unitaria como referencia visual obligatoria.

---

### N6. ESCALA Y TAMAÑO

| Tipo | pgfplots (width/height) | tikzpicture (scale aprox.) | Uso |
|------|------------------------|---------------------------|-----|
| Pequeño | `width=6cm, height=4cm` | `scale=0.8` | Bloque LTI simple, un símbolo |
| Mediano | `width=8cm, height=7cm` | `scale=1` a `1.2` | Diagrama de 2–3 bloques, plano s/z básico |
| Grande | `width=11cm, height=9cm` | `scale=1` a `1.5` | Estructura de filtro compleja, SFG con muchos nodos |
| Cuadrado | `width=9cm, height=9cm` | `scale=1.3` | Plano complejo s/z con ROC sombreada |
| Panorámico | `width=12cm, height=5cm` | `scale=1` (ancho) | Señal discreta larga, espectro de frecuencia |

```
\begin{tikzpicture}[scale=1.2]         → escala el dibujo completo
\begin{axis}[width=8cm, height=7cm]    → tamaño fijo en pgfplots
```

Diagramas de bloques con más de 4 subsistemas en cascada: usar `scale=0.9` y fuente `\small` en los nodos para que el texto no desborde el bloque.

---

### N7. PALETA DE COLORES

Misma paleta que `MAT101_TikzJax.md` y `ETN1015_desmos.md` — consistencia visual entre herramientas.

TikZ no reconoce hex directamente — declarar con `xcolor`:
```
\usepackage{xcolor}
\definecolor{curvaPpal}{HTML}{005F73}
\draw[thick, curvaPpal] ...
```

Alternativa directa — nombres estándar TikZ (sin `xcolor`):
`teal` (señal/polo principal), `orange` (señal secundaria/cero), `olive` (auxiliar), `gray` (ejes, punteados).

#### Paleta para curvas y líneas (sólidas)
```
#005F73   → azul petróleo   (señal de entrada / polo principal)
#0A9396   → verde azulado   (señal interna / respuesta al impulso)
#EE9B00   → ámbar           (destaque / cero)
#BB3E03   → naranja quemado (señal de error / inestabilidad)
#629900   → verde oliva     (señal auxiliar / referencia)
#5A189A   → morado          (punto especial / eje de simetría)
#C1121F   → rojo            (señal de advertencia / polo inestable)
#DA627D   → rosa            (señal alternativa)
#FFD60A   → amarillo        (resaltado)
#474448   → gris antracita  (ejes, bordes, auxiliares, ROC borde)
```

#### Paleta para líneas segmentadas (50% color + 50% blanco)
```
#80AFB9   → azul petróleo segmentado
#85C9CB   → verde azulado segmentado
#F7CD80   → ámbar segmentado
#DD9F81   → naranja quemado segmentado
#B1CC80   → verde oliva segmentado
#A3A2A4   → gris antracita segmentado
```

#### Paleta para rellenos — ROC y regiones (25% color + 75% blanco)
```
#BFD7DC   → azul petróleo claro   (ROC región de convergencia principal)
#C2E4E5   → verde azulado claro   (ROC secundaria)
#F0C4C7   → rojo claro            (región inestable / fuera de ROC)
#D1D0D1   → gris claro            (región neutra)
```

---

### N8. LIMITACIONES CONOCIDAS DEL PLUGIN

- **`pgfplots fillbetween` no está soportado.** Para sombrear la ROC en el plano s/z: usar `\fill[color, opacity=0.2]` con un `\addplot coordinates{...}` en forma de polígono cerrado, o dibujar el relleno manualmente con `\fill` en `tikzpicture`.
- **`\tfrac{}{}` en nodos falla silenciosamente** sin `\usepackage{amsmath}`. Siempre cargar `amsmath` si hay fracciones en etiquetas de bloques (ej: `$\dfrac{1}{s+1}$`).
- **`\node` con `rectangle` requiere la librería `shapes`** si se usan formas distintas al rectángulo por defecto. Para bloques rectangulares estándar no es necesaria — basta con `\draw ... rectangle`.
- **Flechas con punta correcta:** usar `[>=latex, ->]` o `[->, >=stealth]` en las opciones del `tikzpicture` para consistencia visual.
- **`ycomb` para señales discretas:** disponible en `pgfplots` sin paquete extra. Producir con `\addplot[ycomb, thick, teal, mark=*, mark size=2pt]`.

---

### N9. ADVERTENCIA DE PRIMER RENDER

El plugin puede no mostrar el diagrama la primera vez que se abre la nota. Si el bloque aparece vacío o con error: cerrar Obsidian completamente y volver a abrirlo. Ocurre más seguido con diagramas complejos (muchos nodos, pgfplots con varios `\addplot`) en la primera carga del vault.

---

### N10. CÓMO DECIDIR ENTRE TIKZJAX Y DESMOS

El criterio es siempre el mismo: **¿qué herramienta produce el código más simple para este diagrama?**

**Usar Desmos cuando:**
- Señal continua $x(t)$, $h(t)$, $y(t)$ expresable como fórmula directa
- Espectro de magnitud o fase como función continua de $\omega$
- Curva de Bode (magnitud en dB vs $\omega$ en escala log)
- Respuesta en frecuencia $|H(j\omega)|$ o $\angle H(j\omega)$ como función
- Comparación de dos o tres señales continuas superpuestas

**Usar TikZJax cuando:**
- Diagrama de bloques de cualquier sistema LTI
- Plano complejo s (Laplace) o z (Transformada Z) con polos y ceros
- Diagrama de flujo de señal (SFG) con nodos y ramas
- Señal discreta $x[n]$ — diagrama de tallo exacto
- Estructura de filtro directo (forma I, II), traspuesta
- Representación en espacio de estados (bloques integradores)
- Cualquier diagrama estructural donde la geometría exacta importa

**Cuando no esté claro:** revisar si ese tipo ya tiene un ejemplo confirmado en el Bloque C de esta guía o en `ETN1015_desmos.md` — el precedente tiene prioridad. Esta sección no se actualiza por tema nuevo; los ejemplos van acumulándose en el Bloque C.

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
- [ ] Si hay fracciones en nodos (`\tfrac`, `\dfrac`, funciones de transferencia) → ¿está cargado `\usepackage{amsmath}`?
- [ ] Si es plano z → ¿incluye la circunferencia unitaria en punteado gris?
- [ ] Si hay área o ROC sombreada → ¿evita `fillbetween` y usa el patrón manual (N8)?
- [ ] ¿Los colores están en la paleta oficial (hex vía `\definecolor` o nombres estándar de TikZ)?
- [ ] Si es diagrama de bloques → ¿usa `>=latex` o `>=stealth` en las opciones del entorno?
- [ ] ¿El diagrama aporta algo que Desmos no puede dar (N10)? Si no, reconsiderar usar Desmos.
- [ ] Si el bloque es solo referencia de código (no debe renderizar) → quitar `tikz` del identificador, dejar ` ``` ` plano.

---

## BLOQUE C — BIBLIOTECA DE EJEMPLOS POR CAPÍTULO (ETN1015 — RAO)

---

### N12. CAP. 1 — INTRODUCCIÓN A SEÑALES Y SISTEMAS

> Operaciones elementales sobre señales, clasificación, señales básicas.

#### Sistema LTI — bloque básico

> Contexto para NotebookLM: usar cuando el usuario pida representar un sistema genérico con entrada y salida. Bloque rectangular `H` en `teal`, flecha de entrada $x(t)$ en `orange`, flecha de salida $y(t)$ en `teal`.

```tikz
\usepackage{amsmath}
\begin{document}
\begin{tikzpicture}[scale=1.2, >=latex]

% Flecha entrada
\draw[->, thick, orange] (-2,0) -- (-0.6,0);
\node[left, orange] at (-2,0) {$x(t)$};

% Bloque
\draw[thick, teal] (-0.6,-0.4) rectangle (0.6,0.4);
\node[teal] at (0,0) {$H$};

% Flecha salida
\draw[->, thick, teal] (0.6,0) -- (2,0);
\node[right, teal] at (2,0) {$y(t)$};

\end{tikzpicture}
\end{document}
```

---

#### Operaciones sobre señales — desplazamiento temporal

> Contexto para NotebookLM: usar para mostrar $x(t)$, $x(t-t_0)$ y $x(t+t_0)$ en el mismo plano. Tres curvas distintas, leyenda con descripción de cada desplazamiento.

```tikz
\usepackage{pgfplots}
\begin{document}
\begin{tikzpicture}
\begin{axis}[
    axis lines=middle,
    xmin=-4, xmax=6,
    ymin=-0.3, ymax=1.4,
    xlabel={$t$},
    ylabel={},
    width=11cm, height=5cm,
    xtick={-3,-2,-1,0,1,2,3,4,5},
    ytick={0,1},
    tick style={thin, black}
]

% x(t) — pulso rectangular entre 0 y 2
\addplot[very thick, teal, const plot]
    coordinates {(-4,0)(0,0)(0,1)(2,1)(2,0)(6,0)};

% x(t - 2) — desplazado 2 a la derecha
\addplot[very thick, orange, dashed, const plot]
    coordinates {(-4,0)(2,0)(2,1)(4,1)(4,0)(6,0)};

% x(t + 1) — desplazado 1 a la izquierda
\addplot[very thick, olive, dotted, const plot]
    coordinates {(-4,0)(-1,0)(-1,1)(1,1)(1,0)(6,0)};

% Leyenda manual
\draw[very thick, teal]        (axis cs:3.5,1.2) -- (axis cs:4.5,1.2)
    node[right, font=\small] {$x(t)$};
\draw[very thick, orange, dashed] (axis cs:3.5,1.05) -- (axis cs:4.5,1.05)
    node[right, font=\small] {$x(t-2)$};
\draw[very thick, olive, dotted] (axis cs:3.5,0.9) -- (axis cs:4.5,0.9)
    node[right, font=\small] {$x(t+1)$};

\end{axis}
\end{tikzpicture}
\end{document}
```

---

#### Señal escalón unitario $u(t)$ y rampa $r(t)$

> Contexto para NotebookLM: usar cuando el usuario pida graficar señales básicas en tiempo continuo. Dos subfiguras: escalón a la izquierda, rampa a la derecha, en un mismo `tikzpicture`.

```tikz
\usepackage{pgfplots}
\begin{document}
\begin{tikzpicture}

% --- Escalón unitario u(t) ---
\begin{axis}[
    at={(0,0)},
    axis lines=middle,
    xmin=-2, xmax=3,
    ymin=-0.3, ymax=1.5,
    xlabel={$t$},
    ylabel={$u(t)$},
    width=6cm, height=5cm,
    xtick={-1,0,1,2},
    ytick={0,1},
    tick style={thin, black}
]
\addplot[very thick, teal, const plot]
    coordinates {(-2,0)(0,0)(0,1)(3,1)};
\fill[teal] (axis cs:0,1) circle (2pt);
\draw[teal, fill=white, thick] (axis cs:0,0) circle (2pt);
\end{axis}

% --- Rampa r(t) = t·u(t) ---
\begin{axis}[
    at={(220pt,0)},
    axis lines=middle,
    xmin=-1, xmax=3,
    ymin=-0.3, ymax=3,
    xlabel={$t$},
    ylabel={$r(t)$},
    width=6cm, height=5cm,
    xtick={0,1,2},
    ytick={0,1,2},
    tick style={thin, black}
]
\addplot[very thick, orange, domain=0:2.8, samples=3]
    {x};
\addplot[very thick, orange, domain=-1:0, samples=2]
    {0};
\fill[orange] (axis cs:0,0) circle (2pt);
\end{axis}

\end{tikzpicture}
\end{document}
```

---

### N13. CAP. 2 — SISTEMAS EN TIEMPO CONTINUO

> Integral de convolución, sistemas LTI, respuesta al impulso, ecuaciones diferenciales.

#### Sistema en cascada

> Contexto para NotebookLM: usar cuando el usuario pida representar la composición de dos sistemas LTI en serie. La función de transferencia equivalente $H = H_1 \cdot H_2$ se puede agregar como etiqueta debajo.

```tikz
\usepackage{amsmath}
\begin{document}
\begin{tikzpicture}[scale=1.2, >=latex]

% Entrada
\draw[->, thick, orange] (-2.5,0) -- (-1.1,0);
\node[left, orange] at (-2.5,0) {$x(t)$};

% Bloque H1
\draw[thick, teal] (-1.1,-0.4) rectangle (0.1,0.4);
\node[teal] at (-0.5,0) {$H_1$};

% Señal intermedia
\draw[->, thick] (0.1,0) -- (0.9,0);
\node[above, font=\small] at (0.5,0) {$w(t)$};

% Bloque H2
\draw[thick, teal] (0.9,-0.4) rectangle (2.1,0.4);
\node[teal] at (1.5,0) {$H_2$};

% Salida
\draw[->, thick, orange] (2.1,0) -- (3,0);
\node[right, orange] at (3,0) {$y(t)$};

% Equivalente
\node[gray, font=\small] at (0.5,-0.9) {Equivalente: $H = H_1 \cdot H_2$};

\end{tikzpicture}
\end{document}
```

---

### N_CAP2_PALANI. CAP. 2 — DFT Y CONVOLUCIÓN CIRCULAR (PALANI)

---

#### Convolución circular — pasos del método gráfico (círculos concéntricos)

> Contexto para NotebookLM: usar para ilustrar cada paso $m = 0, 1, \ldots, N-1$ del método gráfico de Palani (Fig. 2.11).
>
> **Reglas generales — válidas para cualquier N:**
> - Los N valores se distribuyen uniformemente sobre cada círculo — distancia angular igual entre puntos consecutivos: $\Delta\theta = 360°/N$
> - Siempre se inicia en 0° (derecha)
> - Círculo exterior x₁(n): sentido antihorario desde 0° — nunca rota
> - Círculo interior x₂(n): sentido horario desde 0° — en cada paso m rota hasta coincidir con el siguiente punto en sentido antihorario (es decir, avanza $\Delta\theta$ CCW por paso)
>
> **Ejemplo N=4 — $\Delta\theta = 90°$:**
>
> Disposición fija — círculo exterior x₁(n), antihorario desde 0°:
> - n=0 → 0°   (derecha)    x₁(0)=2
> - n=1 → 90°  (arriba)     x₁(1)=1
> - n=2 → 180° (izquierda)  x₁(2)=2
> - n=3 → 270° (abajo)      x₁(3)=1
>
> Círculo interior x₂, horario desde 0°, m=0 sin rotar:
> - n=0 → 0°   (derecha)    x₂(0)=1
> - n=1 → 270° (abajo)      x₂(1)=2
> - n=2 → 180° (izquierda)  x₂(2)=3
> - n=3 → 90°  (arriba)     x₂(3)=4
>
> **Ejemplo N=5 — $\Delta\theta = 72°$:**
>
> Disposición fija — círculo exterior x₁(n), antihorario desde 0°:
> - n=0 → 0°   x₁(0)
> - n=1 → 72°  x₁(1)
> - n=2 → 144° x₁(2)
> - n=3 → 216° x₁(3)
> - n=4 → 288° x₁(4)
>
> Círculo interior x₂, horario desde 0°, m=0 sin rotar:
> - n=0 → 0°   x₂(0)
> - n=1 → 288° x₂(1)
> - n=2 → 216° x₂(2)
> - n=3 → 144° x₂(3)
> - n=4 → 72°  x₂(4)
>
> **Cada paso m: el interior rota $\Delta\theta$ CCW hasta alinear el siguiente punto con 0°. El exterior nunca cambia.**
>
> Patrón por paso (N=4):
> - $m=0$: interior sin rotar → $x_3(0) = 2\times1 + 1\times4 + 2\times3 + 1\times2 = 14$
> - $m=1$: interior rota 90° CCW → der=x₂(1)=2, arriba=x₂(2)=3, izq=x₂(3)=4, abajo=x₂(0)=1 → $x_3(1) = 2\times2 + 1\times1 + 2\times4 + 1\times3 = 16$
> - $m=2$: interior rota 90° CCW → der=x₂(2)=3, arriba=x₂(3)=4, izq=x₂(0)=1, abajo=x₂(1)=2 → $x_3(2) = 2\times3 + 1\times2 + 2\times1 + 1\times4 = 14$
> - $m=3$: interior rota 90° CCW → der=x₂(3)=4, arriba=x₂(0)=1, izq=x₂(1)=2, abajo=x₂(2)=3 → $x_3(3) = 2\times4 + 1\times3 + 2\times2 + 1\times1 = 16$

```tikz
\usepackage{amsmath}
\begin{document}
\begin{tikzpicture}[scale=1.9]

% Círculo exterior — x1(n) fijo, antihorario desde 0°
% n=0 → der (0°), n=1 → arriba (90°), n=2 → izq (180°), n=3 → abajo (270°)
\draw[thick, teal] (0,0) circle (1.4);
\fill[orange] ( 1.4,  0)   circle (0.08);  % n=0
\fill[orange] ( 0,    1.4) circle (0.08);  % n=1
\fill[orange] (-1.4,  0)   circle (0.08);  % n=2
\fill[orange] ( 0,   -1.4) circle (0.08);  % n=3
\node[teal] at ( 1.85, 0)   {$x_1(0)=2$};   % 0°
\node[teal] at ( 0,    1.7) {$x_1(1)=1$};   % 90°
\node[teal] at (-1.85, 0)   {$x_1(2)=2$};   % 180°
\node[teal] at ( 0,   -1.7) {$x_1(3)=1$};   % 270°

% Círculo interior — x2(n) horario desde 0°, m=0 sin rotar
% x2(0) → der (0°), x2(1) → abajo (270°), x2(2) → izq (180°), x2(3) → arriba (90°)
\draw[thick, orange] (0,0) circle (0.85);
\fill[teal] ( 0.85,  0)   circle (0.08);  % x2(0)
\fill[teal] ( 0,    -0.85) circle (0.08);  % x2(1)
\fill[teal] (-0.85,  0)   circle (0.08);  % x2(2)
\fill[teal] ( 0,     0.85) circle (0.08);  % x2(3)
\node[orange] at ( 1.1,  0)    {$x_2(0)=1$};   % 0°
\node[orange] at ( 0,   -1.05) {$x_2(1)=2$};   % 270°
\node[orange] at (-1.1,  0)    {$x_2(2)=3$};   % 180°
\node[orange] at ( 0,    1.05) {$x_2(3)=4$};   % 90°

% Flecha rotación interior (sentido horario — CW — para graficar x2)
\draw[->, thick, orange, dashed] (0.2, 0.6) arc (70:-70:0.65);
\node[orange, font=\tiny] at (1.0, 0.55) {CW};

% Flecha rotación paso (CCW — cada m rota interior 1 pos CCW)
\draw[->, thick, gray] (-0.2, 0.6) arc (110:250:0.65);
\node[gray, font=\tiny] at (-1.0, 0.55) {CCW};

% Etiqueta m y resultado
\node[font=\small, teal] at (0, 2.2) {$m=0$};
\node[font=\small, gray] at (0,-2.3) {$x_3(0)=2{\times}1+1{\times}4+2{\times}3+1{\times}2=14$};

\end{tikzpicture}
\end{document}
```

> **Nota para NotebookLM:** generar un bloque TikZ por cada valor de $m$. En cada bloque rotar los valores del interior 1 posición CCW respecto al paso anterior — el exterior nunca cambia. Las etiquetas de los nodos del interior cambian de posición angular según la tabla de patrón arriba.

---

#### Sistema en paralelo

> Contexto para NotebookLM: usar para representar dos sistemas LTI en paralelo con sumador. La función equivalente $H = H_1 + H_2$ se puede agregar como etiqueta.

```tikz
\usepackage{amsmath}
\begin{document}
\begin{tikzpicture}[scale=1.2, >=latex]

% Entrada
\draw[->, thick, orange] (-3,0) -- (-2,0);
\node[left, orange] at (-3,0) {$x(t)$};

% Punto de bifurcación
\fill (-2,0) circle (0.06);

% Rama superior
\draw[->, thick] (-2,0) -- (-2,1) -- (-1,1);
\draw[thick, teal] (-1,0.6) rectangle (0,1.4);
\node[teal] at (-0.5,1) {$H_1$};
\draw[->, thick] (0,1) -- (1,1) -- (1,0.3);

% Rama inferior
\draw[->, thick] (-2,0) -- (-2,-1) -- (-1,-1);
\draw[thick, teal] (-1,-1.4) rectangle (0,-0.6);
\node[teal] at (-0.5,-1) {$H_2$};
\draw[->, thick] (0,-1) -- (1,-1) -- (1,-0.3);

% Sumador
\draw[thick] (1,0) circle (0.3);
\draw (0.7,0) -- (1.3,0);
\draw (1,-0.3) -- (1,0.3);
\node[above right, font=\tiny] at (1.1,0.1) {$+$};
\node[below right, font=\tiny] at (1.1,-0.1) {$+$};

% Salida
\draw[->, thick, orange] (1.3,0) -- (2.5,0);
\node[right, orange] at (2.5,0) {$y(t)$};

% Equivalente
\node[gray, font=\small] at (0,-2.2) {Equivalente: $H = H_1 + H_2$};

\end{tikzpicture}
\end{document}
```

---

#### Sistema con retroalimentación (feedback)

> Contexto para NotebookLM: usar para representar un sistema con lazo cerrado. Bloque directo $H_1$ en la rama hacia adelante, bloque $H_2$ en la rama de retroalimentación, sumador con signo negativo.

```tikz
\usepackage{amsmath}
\begin{document}
\begin{tikzpicture}[scale=1.1, >=latex]

% Sumador
\draw[thick] (-1,0) circle (0.3);
\draw (-1.3,0) -- (-0.7,0);
\draw (-1,-0.3) -- (-1,0.3);
\node[above right, font=\small] at (-0.85,0.1) {$+$};
\node[below right, font=\small] at (-0.85,-0.15) {$-$};

% Entrada
\draw[->, thick, orange] (-2.8,0) -- (-1.3,0);
\node[left, orange] at (-2.8,0) {$x(t)$};

% Señal de error e(t)
\draw[->, thick] (-0.7,0) -- (0.4,0);
\node[above, font=\small] at (-0.1,0) {$e(t)$};

% Bloque H1 (hacia adelante)
\draw[thick, teal] (0.4,-0.4) rectangle (1.8,0.4);
\node[teal] at (1.1,0) {$H_1(s)$};

% Salida
\draw[->, thick, orange] (1.8,0) -- (3.2,0);
\node[right, orange] at (3.2,0) {$y(t)$};

% Punto de bifurcación en la salida
\fill (2.5,0) circle (0.06);

% Rama de retroalimentación
\draw[->, thick] (2.5,0) -- (2.5,-1.2) -- (0.4,-1.2);
\draw[thick, teal] (0.4,-1.6) rectangle (1.8,-0.8);
\node[teal] at (1.1,-1.2) {$H_2(s)$};
\draw[->, thick] (-0.3,-1.2) -- (-1,-1.2) -- (-1,-0.3);

\end{tikzpicture}
\end{document}
```

---

### N14. CAP. 3 — FOURIER EN TIEMPO CONTINUO

> Series de Fourier, transformada de Fourier continua, respuesta en frecuencia.

#### Espectro de magnitud — serie de Fourier

> Contexto para NotebookLM: usar para mostrar el espectro bilateral de magnitud de una señal periódica. Tallos en frecuencias discretas $k\omega_0$, magnitudes simétricas respecto al origen. Usar `ycomb` en `pgfplots`.

```tikz
\usepackage{pgfplots}
\begin{document}
\begin{tikzpicture}
\begin{axis}[
    axis lines=middle,
    xmin=-4.5, xmax=4.5,
    ymin=-0.1, ymax=1.2,
    xlabel={$k\omega_0$},
    ylabel={$|c_k|$},
    width=11cm, height=5cm,
    xtick={-4,-3,-2,-1,0,1,2,3,4},
    xticklabels={$-4\omega_0$,$-3\omega_0$,$-2\omega_0$,$-\omega_0$,$0$,$\omega_0$,$2\omega_0$,$3\omega_0$,$4\omega_0$},
    ytick={0,0.5,1},
    tick style={thin, black}
]

\addplot[ycomb, very thick, teal, mark=*, mark size=3pt]
    coordinates {(-4,0.1)(-3,0.2)(-2,0.35)(-1,0.6)(0,1)(1,0.6)(2,0.35)(3,0.2)(4,0.1)};

\end{axis}
\end{tikzpicture}
\end{document}
```

---

### N15. CAP. 4 — TRANSFORMADA DE LAPLACE

> Región de convergencia (ROC), plano s, polos y ceros.

#### Plano s — polos, ceros y ROC

> Contexto para NotebookLM: usar cuando el usuario pida el diagrama de polos y ceros en el plano s con su región de convergencia. Polos con $\times$ en `teal`, ceros con círculo vacío en `orange`, ROC sombreada en azul claro.

```tikz
\usepackage{pgfplots}
\begin{document}
\begin{tikzpicture}
\begin{axis}[
    axis lines=middle,
    xmin=-3.5, xmax=2.5,
    ymin=-2.5, ymax=2.5,
    xlabel={$\sigma$},
    ylabel={$j\omega$},
    width=9cm, height=9cm,
    xtick={-3,-2,-1,0,1,2},
    ytick={-2,-1,0,1,2},
    tick style={thin, black}
]

% ROC — región a la derecha del polo más a la derecha
\fill[teal!15] (axis cs:-1,-2.5) rectangle (axis cs:2.5,2.5);
\node[font=\small, gray] at (axis cs:1.5,2) {ROC};

% Polos en -1 ± j
\node[teal, font=\Large, thick] at (axis cs:-1, 1) {$\times$};
\node[teal, font=\Large, thick] at (axis cs:-1,-1) {$\times$};
\node[teal, font=\small, left] at (axis cs:-1.15, 1.1) {$p_1$};
\node[teal, font=\small, left] at (axis cs:-1.15,-1.1) {$p_2$};

% Cero en el origen
\draw[orange, thick] (axis cs:0,0) circle [radius=7pt];
\node[orange, font=\small, above right] at (axis cs:0.1,0.1) {$z_1$};

% Línea eje jω (referencia ROC borde)
\draw[dashed, gray, thick] (axis cs:-1,-2.5) -- (axis cs:-1,2.5);
\node[gray, font=\small, above] at (axis cs:-1,2.4) {$\sigma=-1$};

\end{axis}
\end{tikzpicture}
\end{document}
```

---

### N16. CAP. 5 — FILTROS ANALÓGICOS

> Butterworth, Chebyshev, Elíptico, Bessel — polos en el plano s.

#### Polos de Butterworth de orden N

> Contexto para NotebookLM: usar para mostrar la ubicación de los polos de un filtro Butterworth de orden $N$ en el semiplano izquierdo. Los polos se distribuyen sobre una circunferencia de radio $\omega_c$ en el semiplano Re{s}<0.

```tikz
\usepackage{pgfplots}
\begin{document}
\begin{tikzpicture}
\begin{axis}[
    axis lines=middle,
    xmin=-2.2, xmax=2.2,
    ymin=-2.2, ymax=2.2,
    xlabel={$\sigma$},
    ylabel={$j\omega$},
    width=9cm, height=9cm,
    xtick={-2,-1,0,1,2},
    ytick={-2,-1,0,1,2},
    tick style={thin, black}
]

% Circunferencia de radio omega_c = 1.5
\draw[dashed, gray, thick] (axis cs:0,0) circle [radius=90pt];
\node[gray, font=\small] at (axis cs:1.2,1.4) {$\omega_c$};

% Polos Butterworth N=4 en el semiplano izquierdo
% Angulos: 135°, 165°, 195°, 225° — los del semiplano izquierdo
% cos/sin manualmente para r=1.5
% p1: 135° → (-1.06, 1.06)
% p2: 165° → (-1.45, 0.39)
% p3: 195° → (-1.45,-0.39)
% p4: 225° → (-1.06,-1.06)
\node[teal, font=\Large] at (axis cs:-1.06, 1.06) {$\times$};
\node[teal, font=\Large] at (axis cs:-1.45, 0.39) {$\times$};
\node[teal, font=\Large] at (axis cs:-1.45,-0.39) {$\times$};
\node[teal, font=\Large] at (axis cs:-1.06,-1.06) {$\times$};

% Etiquetas
\node[teal, font=\small, right] at (axis cs:-0.85, 1.1) {$p_1$};
\node[teal, font=\small, right] at (axis cs:-1.25, 0.45) {$p_2$};
\node[teal, font=\small, right] at (axis cs:-1.25,-0.5) {$p_3$};
\node[teal, font=\small, right] at (axis cs:-0.85,-1.1) {$p_4$};

% Nota N
\node[font=\small] at (axis cs:1.5,-1.8) {$N=4$};

\end{axis}
\end{tikzpicture}
\end{document}
```

---

### N17. CAP. 6 — SEÑALES Y SISTEMAS EN TIEMPO DISCRETO

> Señales discretas, sistemas LTI discretos, suma de convolución.

#### Señal discreta $x[n]$ — diagrama de tallo

> Contexto para NotebookLM: usar para representar una secuencia discreta arbitraria. Tallos en `teal`, puntos sólidos en los extremos. El origen $n=0$ marcado con un tick especial o etiqueta.

```tikz
\usepackage{pgfplots}
\begin{document}
\begin{tikzpicture}
\begin{axis}[
    axis lines=middle,
    xmin=-3.5, xmax=5.5,
    ymin=-0.5, ymax=2.5,
    xlabel={$n$},
    ylabel={$x[n]$},
    width=11cm, height=5cm,
    xtick={-3,-2,-1,0,1,2,3,4,5},
    ytick={0,1,2},
    tick style={thin, black}
]

\addplot[ycomb, very thick, teal, mark=*, mark size=3pt]
    coordinates {(-3,0)(-2,0)(-1,0.5)(0,1)(1,2)(2,1.5)(3,0.8)(4,0.3)(5,0)};

% Marca n=0
\draw[dashed, gray] (axis cs:0,-0.5) -- (axis cs:0,2.5);
\node[gray, font=\small, above] at (axis cs:0,2.4) {$n=0$};

\end{axis}
\end{tikzpicture}
\end{document}
```

---

#### Escalón discreto $u[n]$ e impulso $\delta[n]$

> Contexto para NotebookLM: usar para mostrar las dos señales básicas discretas en paralelo. Dos paneles `axis` en un mismo `tikzpicture`.

```tikz
\usepackage{pgfplots}
\begin{document}
\begin{tikzpicture}

% Impulso delta[n]
\begin{axis}[
    at={(0,0)},
    axis lines=middle,
    xmin=-3.5, xmax=3.5,
    ymin=-0.2, ymax=1.4,
    xlabel={$n$},
    ylabel={$\delta[n]$},
    width=6.5cm, height=4.5cm,
    xtick={-3,-2,-1,0,1,2,3},
    ytick={0,1},
    tick style={thin, black}
]
\addplot[ycomb, very thick, teal, mark=*, mark size=3pt]
    coordinates {(-3,0)(-2,0)(-1,0)(0,1)(1,0)(2,0)(3,0)};
\end{axis}

% Escalón u[n]
\begin{axis}[
    at={(230pt,0)},
    axis lines=middle,
    xmin=-3.5, xmax=3.5,
    ymin=-0.2, ymax=1.4,
    xlabel={$n$},
    ylabel={$u[n]$},
    width=6.5cm, height=4.5cm,
    xtick={-3,-2,-1,0,1,2,3},
    ytick={0,1},
    tick style={thin, black}
]
\addplot[ycomb, very thick, orange, mark=*, mark size=3pt]
    coordinates {(-3,0)(-2,0)(-1,0)(0,1)(1,1)(2,1)(3,1)};
\end{axis}

\end{tikzpicture}
\end{document}
```

---

#### Sistema LTI discreto — bloque básico

> Contexto para NotebookLM: usar para representar un sistema en tiempo discreto con entrada $x[n]$ y salida $y[n]$. Mismo patrón que el bloque continuo — solo cambia la notación de las señales.

```tikz
\usepackage{amsmath}
\begin{document}
\begin{tikzpicture}[scale=1.2, >=latex]

% Flecha entrada
\draw[->, thick, orange] (-2,0) -- (-0.6,0);
\node[left, orange] at (-2,0) {$x[n]$};

% Bloque
\draw[thick, teal] (-0.6,-0.4) rectangle (0.6,0.4);
\node[teal] at (0,0) {$H$};

% Flecha salida
\draw[->, thick, teal] (0.6,0) -- (2,0);
\node[right, teal] at (2,0) {$y[n]$};

\end{tikzpicture}
\end{document}
```

---

### N18. CAP. 7 — FOURIER DISCRETO (DTFT Y MUESTREO)

> Transformada de Fourier en tiempo discreto, muestreo, reconstrucción.

#### Espectro DTFT — magnitud discreta

> Contexto para NotebookLM: usar para mostrar el espectro de magnitud de la DTFT. La frecuencia normalizada $\omega$ va de $-\pi$ a $\pi$. Curva continua (la DTFT es continua en $\omega$).

```tikz
\usepackage{pgfplots}
\begin{document}
\begin{tikzpicture}
\begin{axis}[
    axis lines=middle,
    xmin=-4, xmax=4,
    ymin=-0.2, ymax=1.4,
    xlabel={$\omega$},
    ylabel={$|X(e^{j\omega})|$},
    width=11cm, height=5cm,
    xtick={-3.14159,-1.5708,0,1.5708,3.14159},
    xticklabels={$-\pi$,$-\frac{\pi}{2}$,$0$,$\frac{\pi}{2}$,$\pi$},
    ytick={0,0.5,1},
    tick style={thin, black}
]

% Espectro ejemplo — lóbulo sinc discreto
\addplot[very thick, teal, domain=-3.5:3.5, samples=300]
    {abs(sin(deg(2.5*x))/(5*sin(deg(0.5*x)+0.0001)))};

% Marcas en +-pi
\draw[dashed, gray] (axis cs:-3.14159,0) -- (axis cs:-3.14159,1.3);
\draw[dashed, gray] (axis cs: 3.14159,0) -- (axis cs: 3.14159,1.3);

\end{axis}
\end{tikzpicture}
\end{document}
```

---

### N19. CAP. 8 — TRANSFORMADA Z

> Plano z, ROC, polos y ceros, sistemas discretos en dominio Z.

#### Plano z — polos, ceros y circunferencia unitaria

> Contexto para NotebookLM: usar para diagrama de polos y ceros en el plano z. La circunferencia unitaria en gris punteado es referencia obligatoria — la estabilidad de un sistema causal discreto requiere que los polos estén dentro de la circunferencia unitaria.

```tikz
\begin{document}
\begin{tikzpicture}[scale=2]
% Ejes
\draw[->] (-1.5,0) -- (1.5,0) node[right] {Re};
\draw[->] (0,-1.5) -- (0,1.5) node[above] {Im};
% Circunferencia unitaria
\draw[dashed, gray] (0,0) circle (1);
% Marcas de los ejes
\draw (-1,0.05) -- (-1,-0.05) node[below] {-1};
\draw (1,0.05) -- (1,-0.05) node[below] {1};
\draw (0.05,-1) -- (-0.05,-1) node[left] {-1};
\draw (0.05,1) -- (-0.05,1) node[left] {1};
% ROC
\fill[teal!15] (0,0) circle (1.4);
\fill[white] (0,0) circle (1);
% Polos
\node[teal] at (0.5, 0.5) {$\times$};
\node[teal] at (0.5,-0.5) {$\times$};
% Etiquetas de polos
\node[teal] at (0.72, 0.55) {p1};
\node[teal] at (0.72,-0.55) {p2};
% Cero
\draw[orange, thick] (0,0) circle (0.06);
\node[orange] at (0.13,0.13) {z1};
% Etiquetas
\node[gray] at (0.78,0.78) {$|z|=1$};
\node[teal!70] at (1.2,1.1) {ROC};
\end{tikzpicture}
\end{document}
```

---

#### Diagrama de flujo de señal (SFG) — sistema de 2do orden

> Contexto para NotebookLM: usar para representar la estructura interna de un sistema de segundo orden como SFG. Nodos circulares con etiquetas de señal, ramas con etiqueta de ganancia.

```tikz
\usepackage{amsmath}
\begin{document}
\begin{tikzpicture}[scale=1.3, >=latex]

% Nodos
\node[circle, draw, thick, minimum size=0.55cm] (x)  at (0,0)   {$x$};
\node[circle, draw, thick, minimum size=0.55cm] (w1) at (2,0)   {$w_1$};
\node[circle, draw, thick, minimum size=0.55cm] (w2) at (4,0)   {$w_2$};
\node[circle, draw, thick, minimum size=0.55cm] (y)  at (6,0)   {$y$};

% Ramas hacia adelante
\draw[->, thick, teal]  (x)  -- node[above, font=\small] {$1$} (w1);
\draw[->, thick, teal]  (w1) -- node[above, font=\small] {$1$} (w2);
\draw[->, thick, teal]  (w2) -- node[above, font=\small] {$1$} (y);

% Rama de retroalimentación desde w2 a w1
\draw[->, thick, orange] (w2) to [out=120, in=60]
    node[above, font=\small] {$a_1$} (w1);

% Rama de retroalimentación desde w2 a x
\draw[->, thick, orange] (w2) to [out=150, in=30]
    node[above, font=\small] {$a_2$} (x);

% Etiqueta de entrada
\draw[->, thick] (-1,0) -- (x);
\node[left] at (-1,0) {$x[n]$};

% Etiqueta de salida
\draw[->, thick] (y) -- (7,0);
\node[right] at (7,0) {$y[n]$};

\end{tikzpicture}
\end{document}
```

---

%%
# galaxy-links
[[_app/_config/_galaxy-system.md]]
[[_app/_config/_note-system.md]]
%%
