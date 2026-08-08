---
title: TikZJax — Guía unificada para Obsidian 
galaxy_body: beacon 
scope: vault tool: 
tikzjax-plugin audience:
- usuario
- notebooklm
- claude 
tags:
- beacon
- tikzjax
- infraestructura
date_created: 2026-08-07
date_updated: 2026-08-07
status: en-proceso
---

# ⚡ GUÍA UNIFICADA DE TIKZJAX PARA OBSIDIAN (ETN607)

> Plugin: `obsidian-tikzjax` — renderiza LaTeX/TikZ como SVG directamente en tus notas usando WebAssembly. Guía específica de Mecánica Aplicada — Dinámica Clásica (ETN607). Para funciones matemáticas y cálculo ver `MAT101_TikzJax.md`. Este documento está organizado en tres bloques: **Reglas de sintaxis (N1–N10)**, **Checklist (N11)**, y **Biblioteca de ejemplos por tema ETN607 (N12–N19)**.

---

# 🤖 SECCIÓN NOTEBOOKLM

Instrucciones para que NotebookLM genere bloques TikzJax correctos listos para copiar en Obsidian. Cuando el usuario pida una gráfica, responder con un bloque de código — no con imagen ni enlace.

### Defaults — cuando el usuario no especifica

- Entorno: `tikzpicture` simple para diagramas de cuerpo libre, sistemas mecánicos, coordenadas generalizadas y trayectorias; `axis` (pgfplots) solo si se pide una curva numérica con ejes (potencial, energía vs. tiempo, fase).
- Escala: `scale=1.2` como punto de partida para diagramas de cuerpo libre simples.
- Color de fuerza/vector principal: `teal`; fuerza de reacción/restricción: `orange`; aceleración: `violet`; gravedad: `olive`.
- Vectores: siempre con flecha `->` y etiqueta en nodo. Grosor estándar `thick`.
- Masas: rectángulos rellenos o círculos con `fill=teal!20, draw=teal`.
- Suelo/pared: patrón `north east lines` con `\usetikzlibrary{patterns}` — obligatorio para cualquier diagrama con apoyo fijo.

### Reglas base — siempre obligatorias

Antes de generar cualquier bloque, seguir este orden:

1. ¿Qué tipo de diagrama? (cuerpo libre → `tikzpicture` · curva energía/fase → `pgfplots axis` · sistema con resorte/amortiguador → `tikzpicture` + decorations)
2. ¿Qué paquetes necesita? (ver N2)
3. ¿Escala y tamaño? (ver N6)
4. ¿Qué colores? (ver N7)
5. ¿Qué nivel de detalle? (ver N10) — un vector aislado o esquema topológico → citar figura del libro; sistema completo con múltiples cuerpos y fuerzas → TikZJax.

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
- Librerías TikZ con `\usetikzlibrary{}` también **antes** de `\begin{document}`

❌ Incorrecto — sin document:

```
\begin{tikzpicture}
\draw[->] (0,0) -- (1,0) node[right]{$F$};
\end{tikzpicture}
```

✅ Correcto:

```tikz
\usetikzlibrary{patterns}
\begin{document}
\begin{tikzpicture}
\draw[->] (0,0) -- (1,0) node[right]{$F$};
\end{tikzpicture}
\end{document}
```

---

### N2. PAQUETES DISPONIBLES PARA ETN607

|Paquete / Librería|Para qué|Uso en ETN607|
|---|---|---|
|(ninguno)|Dibujo geométrico básico|Vectores, puntos, ángulos, coordenadas|
|`\usetikzlibrary{patterns}`|Relleno de suelo/pared con rayas|**Obligatorio** en todo diagrama con apoyo fijo|
|`\usetikzlibrary{decorations.pathmorphing}`|Resortes (zigzag) y cuerdas|Sistemas masa-resorte (T5, T6)|
|`\usetikzlibrary{decorations.markings}`|Amortiguadores|Sistemas disipación (T6)|
|`\usetikzlibrary{angles,quotes}`|Ángulos con arco y etiqueta|Péndulos, planos inclinados, ángulos $\theta$|
|`\usetikzlibrary{calc}`|Coordenadas calculadas|Posiciones relativas complejas|
|`pgfplots`|Curvas de potencial, espacio de fases|Gráficas $V(q)$, $\dot{q}$ vs $q$, energía vs tiempo|
|`amsmath`|Fracciones en nodos|Si se usa `\tfrac`, `\dfrac` en etiquetas|

> `circuitikz` se usa en T7 (circuitos eléctricos equivalentes). Ver nota en N8 sobre su soporte en TikZJax. `chemfig` no aplica a ETN607.

---

### N3. ENTORNOS SEGÚN TIPO DE DIAGRAMA

|Tipo de diagrama|Entorno|
|---|---|
|Cuerpo libre, sistema de partículas, plano inclinado|`tikzpicture`|
|Péndulo simple, doble, esférico|`tikzpicture` con ángulos y cuerdas|
|Sistema masa-resorte(-amortiguador)|`tikzpicture` + `decorations.pathmorphing` / `decorations.markings`|
|Coordenadas generalizadas, espacio de configuración|`tikzpicture` con ejes y trayectoria|
|Cuerpo rígido en rotación, momento angular|`tikzpicture` con arcos y vectores|
|Curva de potencial $V(q)$, espacio de fases $(\dot{q},q)$|`pgfplots` → `\begin{axis}[...]`|
|Circuito eléctrico equivalente (T7)|`circuitikz` — ver N8|

---

### N4. SINTAXIS BASE PARA MECÁNICA

```
% Suelo con patrón de rayas (obligatorio en diagramas con apoyo fijo)
\fill[pattern=north east lines] (0,0) rectangle (3,-0.3);
\draw (0,0) -- (3,0);

% Masa como rectángulo relleno
\draw[fill=teal!20, draw=teal, thick] (1,-0.5) rectangle (2,0);
\node at (1.5,-0.25) {$m$};

% Vector fuerza con etiqueta
\draw[->, thick, orange] (1.5,-0.5) -- (1.5,-1.5) node[right]{$mg$};

% Vector reacción normal
\draw[->, thick, teal] (1.5,0) -- (1.5,1) node[right]{$N$};

% Resorte (requiere decorations.pathmorphing)
\draw[thick, decorate, decoration={zigzag, pre length=0.3cm, post length=0.3cm, segment length=6}]
    (0,0) -- (2,0);

% Arco de ángulo con etiqueta (requiere angles,quotes)
\draw pic["$\theta$", draw=gray, angle radius=0.6cm] {angle = A--O--B};

% Cuerda/hilo
\draw[thick, gray] (0,2) -- (1,0);

% Punto de pivote (articulación)
\fill (0,2) circle (0.08);
```

---

### N5. VECTORES Y NOTACIÓN LAGRANGIANA

```
% Coordenada generalizada q con flecha de desplazamiento
\draw[->] (0,0) -- (2,0) node[below right]{$q_1$};

% Velocidad generalizada q-dot
\node[right] at (2.2,0.3) {$\dot{q}_1$};

% Gradiente de potencial / fuerza generalizada
\draw[->, thick, violet] (2,0) -- (3,0.5) node[right]{$Q_1$};

% Trayectoria en espacio de configuración
\draw[teal, thick, ->] plot[smooth] coordinates {(0,0)(1,0.5)(2,1.2)(3,1.5)};

% Grado de libertad con etiqueta DoF
\node[gray, font=\small] at (1.5,-0.5) {$n=1$ DoF};
```

---

### N6. ESCALA Y TAMAÑO

|Tipo|pgfplots (width/height)|tikzpicture (scale aprox.)|Uso|
|---|---|---|---|
|Pequeño|`width=6cm, height=4cm`|`scale=0.7`|Vector único, punto de masa, ángulo|
|Mediano|`width=8cm, height=7cm`|`scale=1` a `1.2`|Cuerpo libre simple, péndulo, plano inclinado|
|Grande|`width=11cm, height=9cm`|`scale=0.9` a `1.5`|Sistemas con 2+ cuerpos, múltiples fuerzas|
|Cornell|`width=6cm, height=5cm`|`scale=0.85`|Dentro de bloque multi-column|
|Cuadrado|`width=9cm, height=9cm`|`scale=1.3`|Espacio de fases, coordenadas polares|
|Panorámico|`width=12cm, height=5cm`|`scale=1` (ancho)|Sistema extendido horizontal (masa-resorte-amortiguador)|

---

### N7. PALETA DE COLORES

Misma paleta base que `MAT101_TikzJax.md`. En ETN607 se asignan roles físicos fijos:

```
teal    → masa, cuerpo, sistema principal
orange  → fuerza de reacción, normal, restricción
olive   → gravedad (mg), peso
violet  → aceleración, coordenada generalizada, momento
gray    → suelo, pared, hilo, auxiliares
```

Declarar hex con `\usepackage{xcolor}` + `\definecolor{}` cuando se necesite coincidencia exacta:

```
\definecolor{masa}{HTML}{005F73}       % azul petróleo — cuerpo principal
\definecolor{fuerza}{HTML}{EE9B00}     % ámbar — fuerza aplicada
\definecolor{reaccion}{HTML}{BB3E03}   % naranja quemado — reacción/restricción
\definecolor{gravedad}{HTML}{629900}   % verde oliva — peso
\definecolor{accel}{HTML}{5A189A}      % morado — aceleración / coord. gen.
```

> Nunca negro puro para vectores — usar `gray` o `teal` según rol.

---

### N8. LIMITACIONES CONOCIDAS DEL PLUGIN

- **`pgfplots fillbetween` no está soportado.** Para rellenar región de potencial: usar `\closedcycle` + relleno blanco manual (mismo patrón que MAT101).
- **`\tfrac{}{}` en nodos falla sin `\usepackage{amsmath}`.**
- **`circuitikz` (T7):** soporte parcial en TikZJax — probar caso a caso. Si no renderiza, citar figura del libro fuente (nombre, capítulo, página) según las reglas del prompt ETN607. Resolución definitiva pendiente para otra sesión.
- **Decoraciones complejas (amortiguadores personalizados):** preferir la versión simple con rectángulo manual si `decorations.markings` falla.
- **`tikz-3dplot`:** disponible pero frágil — preferir perspectiva manual con coordenadas 2D proyectadas para cuerpos rígidos 3D.

---

### N9. ADVERTENCIA DE PRIMER RENDER

El plugin puede no mostrar el diagrama la primera vez que se abre la nota. Si el bloque aparece vacío o con error: cerrar Obsidian completamente y volver a abrirlo. Ocurre más seguido con diagramas complejos en la primera carga del vault.

---

### N10. CÓMO DECIDIR ENTRE TIKZJAX Y CITA DE FIGURA

No se decide por tema, sino por **complejidad del diagrama y disponibilidad en fuente**:

- **Diagrama simple disponible en libro fuente** (un péndulo, una masa en plano inclinado sin fuerzas múltiples) → **citar figura del libro** (nombre, capítulo, página). Más rápido y fiel al apunte.
- **Sistema con múltiples cuerpos, fuerzas etiquetadas, coordenadas generalizadas explícitas, o que no aparece exacto en ninguna fuente** → **TikZJax**. Permite construir exactamente lo que está en el apunte.
- **Curva de potencial, espacio de fases, gráfica energía vs tiempo** → **TikZJax con pgfplots** siempre — este tipo de gráfica raramente coincide exactamente con una figura del libro.

Cuando no esté claro cuál usar: revisar si ese tipo de diagrama ya tiene un ejemplo confirmado en el Bloque C de esta guía. El precedente resuelto tiene prioridad sobre reevaluar el criterio desde cero.

---

## BLOQUE B — CHECKLIST

---

### N11. CHECKLIST ANTES DE RESPONDER

Antes de entregar un bloque TikZJax verificar:

- [ ] ¿Usa el identificador exacto ` ```tikz `? (nunca `latex`, nunca `tikzjax`)
- [ ] ¿Tiene `\begin{document}` y `\end{document}`?
- [ ] ¿NO incluye `\documentclass`?
- [ ] ¿Los paquetes y librerías necesarios están cargados **antes** de `\begin{document}`?
- [ ] ¿Si hay suelo/pared → `\usetikzlibrary{patterns}` cargado?
- [ ] ¿Si hay resorte → `\usetikzlibrary{decorations.pathmorphing}` cargado?
- [ ] ¿Si hay ángulo con arco → `\usetikzlibrary{angles,quotes}` cargado?
- [ ] ¿Todas las expresiones matemáticas entre `$...$`?
- [ ] ¿Si hay `\tfrac` en nodos → `\usepackage{amsmath}` cargado?
- [ ] ¿Los colores siguen los roles físicos fijos de N7?
- [ ] ¿El diagrama aporta algo que no está en la figura del libro (N10)? Si no, citar fuente.
- [ ] Si el bloque es solo referencia de código → quitar `tikz` del identificador, dejar ` ``` ` plano.

---

## BLOQUE C — BIBLIOTECA DE EJEMPLOS POR TEMA (ETN607)

---

### N12. T1–T2 — CONCEPTOS BÁSICOS: PARTÍCULA Y SISTEMA DE PARTÍCULAS

> Cinemática y dinámica de partícula. Métodos Newton, Lagrange, D'Alembert. Grados de libertad. Coordenadas generalizadas.

#### Cuerpo libre — partícula en plano inclinado

> Contexto para NotebookLM: usar cuando el usuario pida el diagrama de cuerpo libre de una masa sobre un plano inclinado con ángulo θ. Fuerzas: peso (olive), normal (orange), fricción si aplica (teal). Suelo con patrón rayas.

```tikz
\usetikzlibrary{patterns}
\begin{document}
\begin{tikzpicture}[scale=1.2]

% Suelo
\fill[pattern=north east lines] (0,0) rectangle (4,-0.3);
\draw (0,0) -- (4,0);

% Plano inclinado
\draw[thick] (0,0) -- (3,0) -- (3,2) -- cycle;
\node[below] at (1.5,0) {base};

% Ángulo theta
\draw (0.8,0) arc (0:33.7:0.8);
\node at (1.1,0.2) {$\theta$};

% Masa
\draw[fill=teal!20, draw=teal, thick, rotate around={33.7:(0,0)}]
    (1.2,0) rectangle (2,0.5);
\node[rotate=33.7] at (1.6,0.25) {$m$};

% Peso
\draw[->, thick, olive] (1.9,1.1) -- (1.9,0) node[right]{$mg$};

% Normal
\draw[->, thick, orange] (1.6,0.8) -- (0.9,1.5) node[right]{$N$};

\end{tikzpicture}
\end{document}
```

---

#### Coordenadas generalizadas — grados de libertad

> Contexto para NotebookLM: usar para ilustrar el concepto de coordenada generalizada $q$ y grado de libertad. Sistema simple: masa en riel curvo con $q$ como coordenada de arco.

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.3]

% Riel curvo
\draw[thick, gray] (-2,0) .. controls (-1,1) and (1,1) .. (2,0);

% Masa en el riel
\fill[teal] (0,1) circle (0.15);
\node[above right] at (0,1) {$m$};

% Coordenada generalizada
\draw[->, thick, violet, dashed] (-1.5,0.5) -- (0,1);
\node[below left, violet] at (-0.8,0.7) {$q$};

% Flecha de velocidad generalizada
\draw[->, thick, violet] (0,1) -- (0.6,1.3);
\node[above, violet] at (0.3,1.2) {$\dot{q}$};

% Referencia origen
\fill (0,0) circle (0.05);
\node[below] at (0,0) {$O$};

% Etiqueta DoF
\node[gray, font=\small] at (0,-0.4) {$n = 1$ grado de libertad};

\end{tikzpicture}
\end{document}
```

---

### N13. T3–T4 — ECUACIONES DE LAGRANGE: APLICACIÓN

> Derivación de ecuaciones de movimiento. Lagrangiano $L = T - V$. Fuerzas generalizadas. Energía cinética y potencial en coordenadas generalizadas.

#### Péndulo simple — coordenada generalizada θ

> Contexto para NotebookLM: usar para el diagrama estándar del péndulo simple. Pivote fijo, cuerda de longitud $\ell$, masa $m$, ángulo $\theta$ como coordenada generalizada. Fuerzas: tensión $T$ a lo largo de la cuerda, peso $mg$ vertical.

```tikz
\usetikzlibrary{angles,quotes}
\begin{document}
\begin{tikzpicture}[scale=1.4]

% Pivote
\fill[gray] (0,0) circle (0.08);
\draw[thick, gray] (-0.5,0.1) -- (0.5,0.1);
\fill[pattern=north east lines] (-0.5,0.1) rectangle (0.5,0.3);

% Cuerda
\draw[thick, gray] (0,0) -- (1.2,-2);

% Masa
\fill[teal] (1.2,-2) circle (0.18);
\node[right] at (1.35,-2) {$m$};

% Ángulo theta (referencia vertical)
\draw[dashed, gray] (0,0) -- (0,-2.4);
\draw (0,-0.7) arc (-90:-59:0.7);
\node at (0.25,-0.9) {$\theta$};

% Longitud ell
\draw[<->, gray] (-0.2,0) -- (-0.2,-2);
\node[left, gray] at (-0.2,-1) {$\ell$};

% Peso
\draw[->, thick, olive] (1.2,-2) -- (1.2,-3) node[right]{$mg$};

% Tensión
\draw[->, thick, orange] (1.2,-2) -- (0.6,-0.8) node[right]{$T$};

\end{tikzpicture}
\end{document}
```

---

#### Sistema masa-resorte — Lagrangiano T5

> Contexto para NotebookLM: usar para sistema masa-resorte horizontal. Suelo con rayas, resorte en zigzag, masa, coordenada $x$ de desplazamiento. Este es el sistema prototipo de T5.

```tikz
\usetikzlibrary{patterns,decorations.pathmorphing}
\begin{document}
\begin{tikzpicture}[scale=1.2]

% Pared izquierda
\fill[pattern=north east lines] (-0.3,-0.5) rectangle (0,1);
\draw[thick] (0,-0.5) -- (0,1);

% Suelo
\fill[pattern=north east lines] (0,-0.5) rectangle (5,-0.2);
\draw[thick] (0,-0.2) -- (5,-0.2);

% Resorte
\draw[thick, decorate,
      decoration={zigzag, pre length=0.3cm, post length=0.3cm, segment length=5}]
    (0,0.3) -- (2,0.3);
\node[above] at (1,0.55) {$k$};

% Masa
\draw[fill=teal!20, draw=teal, thick] (2,-0.2) rectangle (3.2,0.8);
\node at (2.6,0.3) {$m$};

% Coordenada x
\draw[<->, violet] (2,-0.55) -- (3.2,-0.55);
\node[below, violet] at (2.6,-0.55) {$x$};

% Posición de equilibrio
\draw[dashed, gray] (2,1) -- (2,-0.7);
\node[gray, font=\small] at (2,1.15) {$x=0$};

\end{tikzpicture}
\end{document}
```

---

### N14. T5 — SISTEMAS CONSERVATIVOS

> Sistemas sin fricción. Integral de movimiento. Energía total constante $E = T + V$.

#### Curva de potencial $V(q)$

> Contexto para NotebookLM: usar cuando el usuario pida graficar la curva de energía potencial de un sistema conservativo. Mostrar: mínimo de $V$ (equilibrio estable), punto de inflexión (inestable), nivel de energía $E$ como línea horizontal, región de movimiento acotado.

```tikz
\usetikzlibrary{}
\usepackage{pgfplots}
\begin{document}
\begin{tikzpicture}
\begin{axis}[
    axis lines=middle,
    xmin=-0.5, xmax=5,
    ymin=-1, ymax=4,
    width=9cm, height=7cm,
    xlabel={$q$}, ylabel={$V(q)$},
    xtick=\empty, ytick=\empty
]

% Curva de potencial (tipo pozo + barrera)
\addplot[very thick, teal, domain=0.2:4.8, samples=200]
    {2*(x-1)^2*(x-4)^2/4 - 0.5};

% Nivel de energía E
\addplot[dashed, orange, thick, domain=0:5] {1.2};
\node[orange, right] at (axis cs:4.9,1.2) {$E$};

% Mínimo — equilibrio estable
\fill[teal] (axis cs:1,-0.5) circle (3pt);
\node[teal, below] at (axis cs:1,-0.5) {estable};

% Máximo — equilibrio inestable
\fill[orange] (axis cs:2.5,1.77) circle (3pt);
\node[orange, above] at (axis cs:2.5,1.85) {inestable};

% Región acotada
\draw[<->, gray] (axis cs:0.3,1.2) -- (axis cs:1.8,1.2);
\node[gray, above, font=\small] at (axis cs:1.05,1.25) {movimiento acotado};

\end{axis}
\end{tikzpicture}
\end{document}
```

---

### N15. T6 — SISTEMAS DISIPATIVOS

> Sistemas con fricción, amortiguamiento. Función de disipación de Rayleigh.

#### Sistema masa-resorte-amortiguador

> Contexto para NotebookLM: usar para sistema con amortiguador (dashpot) en paralelo con resorte. Amortiguador representado como rectángulo con línea central — versión simplificada compatible con TikZJax (ver N8 sobre `decorations.markings`).

```tikz
\usetikzlibrary{patterns,decorations.pathmorphing}
\begin{document}
\begin{tikzpicture}[scale=1.2]

% Pared
\fill[pattern=north east lines] (-0.3,-0.3) rectangle (0,2.3);
\draw[thick] (0,-0.3) -- (0,2.3);

% Suelo
\fill[pattern=north east lines] (0,-0.5) rectangle (5,-0.2);
\draw[thick] (0,-0.2) -- (5,-0.2);

% Resorte (arriba)
\draw[thick, decorate,
      decoration={zigzag, pre length=0.3cm, post length=0.3cm, segment length=5}]
    (0,1.6) -- (2.2,1.6);
\node[above] at (1.1,1.75) {$k$};

% Amortiguador (abajo) — versión simplificada
\draw[thick] (0,0.5) -- (0.9,0.5);
\draw[thick] (0.9,0.2) rectangle (1.8,0.8);
\draw[thick] (1.8,0.5) -- (2.2,0.5);
\node[above] at (1.1,0.85) {$c$};

% Conector vertical
\draw[thick] (2.2,0.5) -- (2.2,1.6);

% Masa
\draw[fill=teal!20, draw=teal, thick] (2.2,-0.2) rectangle (3.6,2);
\node at (2.9,0.9) {$m$};

% Fuerza aplicada
\draw[->, thick, orange] (3.6,0.9) -- (4.5,0.9) node[right]{$F(t)$};

% Coordenada x
\draw[<->, violet] (2.2,-0.65) -- (3.6,-0.65);
\node[below, violet] at (2.9,-0.65) {$x$};

\end{tikzpicture}
\end{document}
```

---

### N16. T7 — CIRCUITOS ELÉCTRICOS EQUIVALENTES

> Analogía eléctrico-mecánica. Circuitos RLC como sistemas lagrangianos.

> **NOTA:** `circuitikz` tiene soporte parcial en TikZJax — probar caso a caso. Si el bloque no renderiza en Obsidian, citar la figura equivalente de Wells Cap.7 o del libro fuente indicando nombre, capítulo y página. No inventar. Este bloque se completará con ejemplos confirmados en una sesión dedicada.

_(Agregar ejemplos confirmados aquí)_

---

### N17. T8 — CUERPO RÍGIDO

> Movimiento de cuerpo rígido. Tensor de inercia. Ecuaciones de Euler. Momento angular.

#### Cuerpo rígido en rotación — momento angular $\vec{L}$

> Contexto para NotebookLM: usar para ilustrar el vector momento angular $\vec{L}$, el vector $\vec{r}$ desde el eje al punto de masa, y la velocidad angular $\vec{\omega}$. Diagrama 2D con perspectiva manual.

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.3]

% Eje de rotación (vertical, punteado)
\draw[dashed, gray, thick] (0,-0.5) -- (0,3);
\node[gray, above] at (0,3) {eje};

% Cuerpo rígido (elipse simplificada)
\draw[fill=teal!10, draw=teal, thick] (0,1.2) ellipse (1.5 and 0.4);
\node[teal] at (0,1.2) {cuerpo rígido};

% Vector r (desde eje al CM)
\draw[->, thick, violet] (0,1.2) -- (1.5,1.2);
\node[violet, above] at (0.75,1.2) {$\vec{r}$};

% Velocidad angular omega
\draw[->, thick, orange, line width=1.5pt] (0,0.2) -- (0,1.0);
\node[orange, left] at (0,0.6) {$\vec{\omega}$};

% Momento angular L
\draw[->, thick, olive, line width=1.5pt] (0,1.5) -- (0,2.5);
\node[olive, right] at (0,2) {$\vec{L}$};

% Centro de masa
\fill[teal] (0,1.2) circle (0.07);
\node[below left, font=\small] at (0,1.2) {$CM$};

\end{tikzpicture}
\end{document}
```

---

### N18. DIAGRAMAS AUXILIARES — USO TRANSVERSAL

#### Péndulo doble — T3/T4

> Contexto para NotebookLM: usar para el péndulo doble como ejemplo de sistema con $n=2$ DoF y coordenadas generalizadas $\theta_1$, $\theta_2$. Masas $m_1$, $m_2$.

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.3]

% Pivote superior
\fill[gray] (0,0) circle (0.08);
\draw[thick, gray] (-0.5,0.1) -- (0.5,0.1);
\fill[pattern=north east lines] (-0.5,0.1) rectangle (0.5,0.3);

% Primera cuerda
\draw[thick, gray] (0,0) -- (0.8,-1.5);

% Masa 1
\fill[teal] (0.8,-1.5) circle (0.15);
\node[right] at (0.95,-1.5) {$m_1$};

% Segunda cuerda
\draw[thick, gray] (0.8,-1.5) -- (1.8,-2.8);

% Masa 2
\fill[orange!80!black] (1.8,-2.8) circle (0.15);
\node[right] at (1.95,-2.8) {$m_2$};

% Verticales de referencia
\draw[dashed, gray] (0,0) -- (0,-1.8);
\draw[dashed, gray] (0.8,-1.5) -- (0.8,-3);

% Ángulo theta1
\draw (0,-0.6) arc (-90:-62:0.6);
\node at (0.18,-0.75) {$\theta_1$};

% Ángulo theta2
\draw (0.8,-2.0) arc (-90:-55:0.5);
\node at (1.0,-2.15) {$\theta_2$};

% Longitudes
\draw[<->, gray] (-0.15,0) -- (-0.15,-1.5);
\node[left, gray] at (-0.15,-0.75) {$\ell_1$};
\draw[<->, gray] (0.65,-1.5) -- (0.65,-2.8);
\node[left, gray] at (0.65,-2.15) {$\ell_2$};

% DoF
\node[gray, font=\small] at (0,-3.2) {$n = 2$ DoF, $q = (\theta_1, \theta_2)$};

\end{tikzpicture}
\end{document}
```

---

### N19. ESPACIO DE FASES — USO TRANSVERSAL

#### Espacio de fases $(\dot{q}, q)$ — retrato de fase

> Contexto para NotebookLM: usar cuando el usuario pida el espacio de fases o retrato de fase de un sistema. Mostrar trayectorias cerradas (movimiento acotado), separatriz y trayectorias abiertas. Curvas representativas sin datos numéricos exactos.

```tikz
\usepackage{pgfplots}
\begin{document}
\begin{tikzpicture}
\begin{axis}[
    axis lines=middle,
    xmin=-3.5, xmax=3.5,
    ymin=-2.5, ymax=2.5,
    width=9cm, height=9cm,
    xlabel={$q$}, ylabel={$\dot{q}$},
    xtick=\empty, ytick=\empty
]

% Órbitas cerradas (movimiento acotado) — elipses concéntricas
\addplot[teal, thick, domain=0:360, samples=100]
    ({1.0*cos(x)},{0.7*sin(x)});
\addplot[teal, thick, domain=0:360, samples=100]
    ({1.8*cos(x)},{1.2*sin(x)});
\addplot[teal, thick, domain=0:360, samples=100]
    ({2.5*cos(x)},{1.8*sin(x)});

% Separatriz (órbita homoclínica) — aproximación manual
\addplot[orange, very thick, domain=-3.14:3.14, samples=200]
    {1.9*sin(deg(x/2))};

% Punto de equilibrio estable (centro)
\fill[teal] (axis cs:0,0) circle (3pt);
\node[teal, above right] at (axis cs:0.1,0.1) {estable};

% Punto de equilibrio inestable (silla)
\fill[orange] (axis cs:3.14,0) circle (3pt);
\fill[orange] (axis cs:-3.14,0) circle (3pt);

% Flechas de flujo
\draw[->, teal] (axis cs:1,0) -- (axis cs:1.01,0.1);
\draw[->, teal] (axis cs:-1,0) -- (axis cs:-1.01,-0.1);

\end{axis}
\end{tikzpicture}
\end{document}
```

---

%%

# galaxy-links

[[_app/_config/_galaxy-system.md]] [[_app/_config/_note-system.md]] [[_app/notebooklm/guides/MAT101/MAT101_TikzJax.md]] %%