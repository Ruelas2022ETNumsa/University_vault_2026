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
date_created: 2026-08-07
date_updated: 2026-08-19
status: activo
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

#### Péndulo invertido sobre carro móvil (Figura 1.1)

> Contexto para NotebookLM: usar para el ejemplo clásico de péndulo invertido — masa $m$ unida por varilla al carro $M$ que se desplaza horizontalmente. Ángulo $\theta$ respecto a la vertical. Este diagrama NO es el péndulo simple — la masa está arriba del pivote.

```tikz
\usetikzlibrary{patterns}
\begin{document}
\begin{tikzpicture}[scale=1.3]

% Suelo con rayas
\fill[pattern=north east lines] (-1,-0.5) rectangle (3,-0.2);
\draw[thick] (-1,-0.2) -- (3,-0.2);

% Ruedas
\fill[gray] (0.3,-0.2) circle (0.15);
\fill[gray] (1.3,-0.2) circle (0.15);

% Carro M
\draw[fill=teal!15, draw=teal, thick] (0,0) rectangle (1.6,0.5);
\node at (0.8,0.25) {$M$};

% Pivote
\fill (0.8,0.5) circle (0.07);

% Varilla (péndulo invertido: masa arriba)
\draw[thick, gray] (0.8,0.5) -- (1.5,2.2);

% Masa m
\fill[orange!80!black] (1.5,2.2) circle (0.15);
\node[right] at (1.65,2.2) {$m$};

% Vertical de referencia (punteada)
\draw[dashed, gray] (0.8,0.5) -- (0.8,2.5);

% Ángulo theta
\draw (0.8,1.0) arc (90:70:0.5);
\node at (1.05,1.05) {$\theta$};

% Coordenada x del carro
\draw[->, violet, thick] (0,-0.6) -- (1.6,-0.6);
\node[below, violet] at (0.8,-0.6) {$x$};

\end{tikzpicture}
\end{document}
```

---

#### Desplazamiento vectorial — límite de $\Delta\vec{R}$ (Figura 1.9)

> Contexto para NotebookLM: usar para ilustrar la definición de velocidad vectorial como límite del cociente $\Delta\vec{R}/\Delta t$. Triángulo de vectores $\vec{R}_0$, $\vec{R}_f$, $\Delta\vec{R}$.

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.4]

% Origen
\fill (0,0) circle (0.06);
\node[below left] at (0,0) {O};

% Vector R0
\draw[->, thick, teal] (0,0) -- (1.5,0.5);
\node[below, teal] at (0.75,0.25) {$\vec{R}_0$};

% Vector Rf
\draw[->, thick, violet] (0,0) -- (2.2,1.8);
\node[above left, violet] at (1.1,0.9) {$\vec{R}_f$};

% Delta R
\draw[->, thick, orange] (1.5,0.5) -- (2.2,1.8);
\node[right, orange] at (1.9,1.15) {$\Delta\vec{R}$};

% Extremos
\fill[teal] (1.5,0.5) circle (0.06);
\fill[violet] (2.2,1.8) circle (0.06);

% Fórmula
\node[gray] at (1.4,-0.3)
{$\vec{v} =
\displaystyle
\lim_{\Delta t\to0}
\frac{\Delta\vec{R}}{\Delta t}$};

\end{tikzpicture}
\end{document}
```

---

#### Coordenadas cilíndricas 3D — versores (Figuras 1.10–1.11)

> Contexto para NotebookLM: usar para ilustrar el sistema de coordenadas cilíndricas con los tres versores $\hat{e}_r$, $\hat{e}_\theta$, $\hat{e}_z$ en perspectiva 2D proyectada. El versor $\hat{e}_z$ no depende de $\theta$; $\hat{e}_r$ y $\hat{e}_\theta$ sí.

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.4]

% Ejes principales (perspectiva isométrica manual)
% Eje z (vertical)
\draw[->, thick, gray] (0,0) -- (0,2.5) node[above]{$z$};
% Eje x (diagonal izquierda)
\draw[->, thick, gray] (0,0) -- (-1.5,-0.8) node[below left]{$x$};
% Eje y (diagonal derecha)
\draw[->, thick, gray] (0,0) -- (2.0,-0.5) node[below right]{$y$};

% Punto P en el espacio
\fill[teal] (1.2,1.5) circle (0.08);
\node[right] at (1.25,1.5) {$P$};

% Radio r (proyección en plano xy)
\draw[dashed, gray] (0,0) -- (1.2,0.2);
\draw[dashed, gray] (1.2,0.2) -- (1.2,1.5);
\node[gray, font=\small] at (0.5,-0.05) {$r$};

% Ángulo theta
\draw (0.5,-0.12) arc (-14:0:0.5);
\node[gray, font=\small] at (0.7,-0.25) {$\theta$};

% Versor e_r (radial, en el plano)
\draw[->, very thick, orange] (1.2,0.2) -- (1.85,0.37);
\node[orange, right] at (1.85,0.37) {$\hat{e}_r$};

% Versor e_theta (tangencial, perpendicular a e_r en plano)
\draw[->, very thick, violet] (1.2,0.2) -- (0.85,0.9);
\node[violet, left] at (0.85,0.9) {$\hat{e}_\theta$};

% Versor e_z (vertical)
\draw[->, very thick, teal] (1.2,1.5) -- (1.2,2.2);
\node[teal, right] at (1.2,2.2) {$\hat{e}_z$};

% Vector R
\draw[->, thick, teal, dashed] (0,0) -- (1.2,1.5);
\node[teal, above left] at (0.6,0.75) {$\vec{R}$};

\end{tikzpicture}
\end{document}
```

---

#### Coordenadas esféricas 3D — versores (Figura 1.12)

> Contexto para NotebookLM: usar para el sistema de coordenadas esféricas con $\ell$, $\theta$, $\phi$ y los tres versores $\hat{e}_\ell$, $\hat{e}_\theta$, $\hat{e}_\phi$. La sombra en el plano $xy$ ayuda a visualizar $\phi$.

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.4]

% Ejes (perspectiva manual)
\draw[->, thick, gray] (0,0) -- (0,2.8) node[above]{$z$};
\draw[->, thick, gray] (0,0) -- (-1.4,-0.7) node[below left]{$x$};
\draw[->, thick, gray] (0,0) -- (2.2,-0.4) node[below right]{$y$};

% Punto P
\fill[teal] (1.1,1.8) circle (0.08);
\node[right] at (1.18,1.8) {$P$};

% Vector ell (radio esférico)
\draw[->, thick, teal] (0,0) -- (1.1,1.8);
\node[teal, left] at (0.55,0.9) {$\ell$};

% Sombra en plano xy
\draw[dashed, gray] (0,0) -- (1.1,0.15);
\draw[dashed, gray] (1.1,0.15) -- (1.1,1.8);
\node[gray, font=\small] at (0.8,-0.1) {$\ell\sin\theta$};

% Ángulo theta (con eje z)
\draw[gray] (0,0.7) arc (90:58:0.7);
\node[gray, font=\small] at (0.35,0.85) {$\theta$};

% Ángulo phi (en plano xy)
\draw[gray] (0.45,-0.06) arc (-8:0:0.45);
\node[gray, font=\small] at (0.7,-0.2) {$\phi$};

% Versor e_ell (radial esférico)
\draw[->, very thick, teal] (1.1,1.8) -- (1.65,2.65);
\node[teal, right] at (1.65,2.65) {$\hat{e}_\ell$};

% Versor e_theta (meridional)
\draw[->, very thick, violet] (1.1,1.8) -- (1.75,1.2);
\node[violet, right] at (1.75,1.2) {$\hat{e}_\theta$};

% Versor e_phi (azimutal)
\draw[->, very thick, orange] (1.1,1.8) -- (0.4,2.1);
\node[orange, left] at (0.4,2.1) {$\hat{e}_\phi$};

\end{tikzpicture}
\end{document}
```

---

#### Coordenadas no lineales $(A, \theta)$ — plano $xy$ (pág. 6)

> Contexto para NotebookLM: usar para el sistema de coordenadas no lineales donde $A = xy/2$ y $\tan\theta = y/x$. Punto $P$ definido por su posición en el plano con los ejes y el ángulo $\theta$ marcado.

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.3]

% Ejes
\draw[->, thick, gray] (-0.3,0) -- (3,0) node[right]{$x$};
\draw[->, thick, gray] (0,-0.3) -- (0,2.5) node[above]{$y$};
\node[below left] at (0,0) {$O$};

% Punto P
\fill[teal] (2.2,1.5) circle (0.08);
\node[right] at (2.3,1.5) {$P$};

% Proyecciones punteadas
\draw[dashed, gray] (2.2,0) -- (2.2,1.5);
\draw[dashed, gray] (0,1.5) -- (2.2,1.5);
\node[below, gray] at (2.2,0) {$x$};
\node[left, gray] at (0,1.5) {$y$};

% Radio A (desde origen)
\draw[->, thick, violet] (0,0) -- (2.2,1.5);
\node[violet, above left] at (1.1,0.75) {$A$};

% Ángulo theta
\draw (0.7,0) arc (0:34:0.7);
\node at (0.85,0.22) {$\theta$};

% Cuadrícula auxiliar (hash en origen)
\draw[thick] (-0.15,-0.15) -- (0.15,0.15);
\draw[thick] (0.15,-0.15) -- (-0.15,0.15);

\end{tikzpicture}
\end{document}
```

---

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

#### E1 — Bloque $m_1$ con resorte $K$, polea y sistema vertical $m_2$–resorte $K'$–$m_3$ guiado por pared (P2)

> Contexto para NotebookLM: bloque $m_1$ sobre piso horizontal conectado a la pared izquierda por resorte $K$; una cuerda horizontal parte de $m_1$, pasa por una polea fija y desciende verticalmente. Del cable vertical cuelga el bloque $m_2$, conectado hacia abajo por resorte $K'$ al bloque $m_3$; ambos guiados por una pared vertical lateral. Coordenada $x_1$: posición horizontal del centro de $m_1$ desde la pared izquierda. Coordenada $y_2$: desplazamiento vertical del centro de $m_2$ desde la altura del centro de $m_1$. Coordenada $y_3$: desplazamiento vertical del centro de $m_3$ desde la misma referencia.

```tikz
\usetikzlibrary{patterns,decorations.pathmorphing}

\begin{document}

\begin{tikzpicture}[scale=1.0, >=latex]

\colorlet{maincolor}{teal}
\colorlet{accentcolor}{orange}

% PARED IZQUIERDA
\fill[pattern=north east lines] (-0.5,0) rectangle (0,2);
\draw[thick] (0,0) -- (0,2);

% PISO HORIZONTAL
\fill[pattern=north east lines] (0,-0.2) rectangle (5.5,0);
\draw[thick] (0,0) -- (5.5,0);

% RESORTE K
\draw[decorate, decoration={coil, aspect=0.3, segment length=2mm, amplitude=3mm}, maincolor, thick]
    (0,0.7) -- (1.5,0.7);
\node[above, maincolor] at (0.75,0.9) {$K$};

% BLOQUE m1
\draw[fill=teal!10, draw=maincolor, thick] (1.5,0) rectangle (2.8,1.4);
\node[maincolor] at (2.15,0.7) {$m_1$};

% CUERDA HORIZONTAL
\draw[thick] (2.8,1.0) -- (5.2,1.0);

% POLEA
\draw[thick, fill=gray!20] (5.5,0.7) circle (0.3);
\fill (5.5,0.7) circle (0.05);
\draw[thick] (5.5,0) -- (5.5,0.4);

% CUERDA VERTICAL
\draw[thick] (5.8,0.7) -- (5.8,-1.0);

% PARED VERTICAL LATERAL
\fill[pattern=north east lines] (4.5,-4) rectangle (5,0);
\draw[thick] (5,-4) -- (5,0);

% BLOQUE m2
\draw[fill=teal!10, draw=maincolor, thick] (5,-1.7) rectangle (6,-1.0);
\node[maincolor] at (5.5,-1.35) {$m_2$};

% RESORTE K'
\draw[decorate, decoration={coil, aspect=0.3, segment length=2mm, amplitude=2.5mm}, accentcolor, thick]
    (5.5,-1.7) -- (5.5,-2.8);
\node[right, accentcolor] at (5.7,-2.25) {$K'$};

% BLOQUE m3
\draw[fill=orange!10, draw=accentcolor, thick] (5,-3.5) rectangle (6,-2.8);
\node[accentcolor] at (5.5,-3.15) {$m_3$};

% COORDENADA x1
\draw[<->, maincolor, thick] (0,2.1) -- (2.15,2.1) node[midway, above] {$x_1$};
\draw[dotted] (0,1.8) -- (0,2.3);
\draw[dotted] (2.15,0.7) -- (2.15,2.3);

% COORDENADA y2
\draw[<->, maincolor, thick] (6.7,0.7) -- (6.7,-1.35) node[midway, right] {$y_2$};
\draw[dotted] (2.15,0.7) -- (6.7,0.7);
\draw[dotted] (5.5,-1.35) -- (6.7,-1.35);

% COORDENADA y3
\draw[<->, accentcolor, thick] (7.5,0.7) -- (7.5,-3.15) node[midway, right] {$y_3$};
\draw[dotted] (2.15,0.7) -- (7.5,0.7);
\draw[dotted] (5.5,-3.15) -- (7.5,-3.15);

\end{tikzpicture}

\end{document}
```

---

#### Péndulo simple — coordenada generalizada θ

> Contexto para NotebookLM: usar para el diagrama estándar del péndulo simple. Pivote fijo, cuerda de longitud $\ell$, masa $m$, ángulo $\theta$ como coordenada generalizada. Fuerzas: tensión $T$ a lo largo de la cuerda, peso $mg$ vertical.

```tikz
\usetikzlibrary{angles,quotes,patterns}
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

#### E2 — Cuña deslizante con masa guiada verticalmente, resorte y posición $x_1$ (P2)

> Contexto para NotebookLM: bloque-cuña $m_1$ sobre piso horizontal conectado a la pared derecha por resorte $K$, cara izquierda inclinada a $60°$. Bloque $m_2$ guiado verticalmente por la pared izquierda, apoya su cara inclinada sobre la de $m_1$. Coordenada $x_1$: posición horizontal de $m_1$ desde la pared izquierda. Coordenada $y_2$: altura de $m_2$ sobre el piso. Cotas $B_1$ (ancho de $m_1$) y $B$ (distancia entre paredes).

```tikz
\usetikzlibrary{patterns,decorations.pathmorphing}
\begin{document}
\begin{tikzpicture}[scale=1.2, >=latex]
    \colorlet{maincolor}{teal}
    \colorlet{accentcolor}{orange}

    % Pared izquierda
    \fill[pattern=north east lines] (-0.3,0) rectangle (0,4);
    \draw[thick] (0,0) -- (0,4);

    % Piso horizontal
    \fill[pattern=north east lines] (0,-0.3) rectangle (7,0);
    \draw[thick] (0,0) -- (7,0);

    % Pared derecha
    \fill[pattern=north east lines] (7,0) rectangle (7.3,3);
    \draw[thick] (7,0) -- (7,3);

    % Bloque m1
    \draw[fill=teal!10, draw=maincolor, thick] (2.5,0) -- (5.5,0) -- (5.5,1.5) -- (3.366,1.5) -- cycle;
    \node[maincolor] at (4.5,0.7) {$m_1$};

    % Resorte K
    \draw[decoration={aspect=0.3, segment length=2mm, amplitude=3mm, coil}, decorate, maincolor, thick] (5.5,0.75) -- (7,0.75);
    \node[above, maincolor] at (6.25,0.95) {$K$};

    % Ángulo 60°
    \draw[thick, maincolor] (2.5,0) ++(0.5,0) arc (0:60:0.5);
    \node[maincolor] at (3.25,0.28) {$60^\circ$};

    % Bloque m2
    \draw[fill=orange!10, draw=accentcolor, thick] (0,1.5) -- (2.134,1.5) -- (3.0,3.0) -- (0,3.0) -- cycle;
    \node[accentcolor] at (1.0,2.3) {$m_2$};

    % Coordenada x1
    \draw[->, maincolor, thick] (0,-0.7) -- (2.5,-0.7) node[midway, below] {$x_1$};
    \draw[dotted] (0,0) -- (0,-0.9);
    \draw[dotted] (2.5,0) -- (2.5,-0.9);

    % Cota B1
    \draw[<->, maincolor] (2.5,-1.2) -- (5.5,-1.2) node[midway, below] {$B_1$};
    \draw[dotted] (5.5,0) -- (5.5,-1.4);

    % Cota B
    \draw[<->, accentcolor] (0,-1.7) -- (7,-1.7) node[midway, below] {$B$};

    % Coordenada y2
    \draw[->, accentcolor, thick] (-0.7,0) -- (-0.7,1.5) node[midway, left] {$y_2$};
    \draw[dotted] (0,0) -- (-0.9,0);
    \draw[dotted] (0,1.5) -- (-0.9,1.5);

\end{tikzpicture}
\end{document}
```

---

#### E3 — Sistema de dos poleas en cadena con resortes $K$, $K'$ y masa $m_3$ (P2)

> Contexto para NotebookLM: polea $m_1$ suspendida del techo por resorte $K$; ramal izquierdo conectado al piso por resorte $K'$; ramal derecho sostiene la polea $m_2$ a distancia $a$ por debajo. Ramal izquierdo de $m_2$ fijo al piso; ramal derecho sostiene masa puntual $m_3$. Coordenadas $y_1$, $y_2$, $y_3$ desde el techo hacia abajo. Altura total $H$.

```tikz
\usetikzlibrary{patterns,decorations.pathmorphing}
\begin{document}
\begin{tikzpicture}[scale=1.0, >=latex]
    \colorlet{maincolor}{teal}
    \colorlet{accentcolor}{orange}

    % Techo
    \fill[pattern=north east lines] (-1,5.0) rectangle (4.5,5.3);
    \draw[thick] (-1,5.0) -- (4.5,5.0);

    % Piso
    \fill[pattern=north east lines] (-1,-0.3) rectangle (4.5,0);
    \draw[thick] (-1,0) -- (4.5,0);

    % Resorte K
    \draw[decoration={aspect=0.3, segment length=2mm, amplitude=2.5mm, coil}, decorate, maincolor, thick] (1.0,5.0) -- (1.0,3.7);
    \node[left, maincolor] at (0.75,4.35) {$K$};

    % Polea m1
    \draw[thick, fill=teal!10, draw=maincolor] (1.0,3.4) circle (0.3);
    \fill[maincolor] (1.0,3.4) circle (0.05);
    \node[left, maincolor] at (0.55,3.4) {$m_1$};

    % Ramal izquierdo de m1 + resorte K'
    \draw[thick, maincolor] (0.7,3.4) -- (0.7,1.8);
    \draw[decoration={aspect=0.3, segment length=2mm, amplitude=2mm, coil}, decorate, maincolor, thick] (0.7,1.8) -- (0.7,0);
    \node[left, maincolor] at (0.45,0.9) {$K'$};

    % Ramal derecho de m1
    \draw[thick, maincolor] (1.3,3.4) -- (1.3,2.0);

    % Polea m2
    \draw[thick, fill=orange!10, draw=accentcolor] (1.3,1.7) circle (0.3);
    \fill[accentcolor] (1.3,1.7) circle (0.05);
    \node[right, accentcolor] at (1.65,1.7) {$m_2$};

    % Ramal derecho de m2 a m3
    \draw[thick, accentcolor] (1.6,1.7) -- (1.6,0.6);
    \draw[thick, fill=accentcolor!30, draw=accentcolor] (1.6,0.45) circle (0.15);
    \node[right, accentcolor] at (1.8,0.45) {$m_3$};

    % Ramal izquierdo de m2 al piso
    \draw[thick, accentcolor] (1.0,1.7) -- (1.0,0);

    % Cota H
    \draw[<->, red, thick] (-0.6,0) -- (-0.6,5.0) node[midway, left] {$H$};

    % Coordenada y1
    \draw[->, maincolor, thick] (2.2,5.0) -- (2.2,3.4) node[midway, right] {$y_1$};
    \draw[dotted] (1.0,3.4) -- (2.3,3.4);
    \draw[dotted] (1.0,5.0) -- (2.3,5.0);

    % Coordenada y2
    \draw[->, accentcolor, thick] (2.9,5.0) -- (2.9,1.7) node[midway, right] {$y_2$};
    \draw[dotted] (1.3,1.7) -- (3.0,1.7);

    % Coordenada y3
    \draw[->, accentcolor, thick] (3.6,5.0) -- (3.6,0.45) node[midway, right] {$y_3$};
    \draw[dotted] (1.75,0.45) -- (3.7,0.45);

    % Cota a
    \draw[<->, maincolor, thick] (1.85,3.4) -- (1.85,1.7) node[midway, right] {$a$};
    \draw[dotted] (1.3,3.4) -- (2.0,3.4);

\end{tikzpicture}
\end{document}
```

---

#### E4 — Carro con péndulo articulado, coordenadas $(x, \theta)$ (P2)

> Contexto para NotebookLM: carro $M$ sobre piso horizontal sin fricción. Péndulo de varilla rígida sin masa, longitud $\ell$, masa puntual $m$ en el extremo, articulado en la parte superior del carro a altura $H$. Ángulo $\theta$ medido desde la vertical hacia arriba. Coordenada $x$: posición horizontal del pivote desde la pared izquierda.

```tikz
\usetikzlibrary{patterns,decorations.pathmorphing}
\begin{document}
\begin{tikzpicture}[scale=1.1, >=latex]
    \colorlet{maincolor}{teal}
    \colorlet{accentcolor}{orange}

    % Pared izquierda
    \fill[pattern=north east lines] (-0.3,0) rectangle (0,3.0);
    \draw[thick] (0,0) -- (0,3.0);

    % Piso
    \fill[pattern=north east lines] (0,-0.3) rectangle (6.0,0);
    \draw[thick] (0,0) -- (6.0,0);

    % Carro M
    \draw[fill=teal!10, draw=maincolor, thick] (1.8,0.35) rectangle (3.8,1.5);
    \node[maincolor] at (2.8,0.92) {$M$};

    % Ruedas
    \draw[thick, fill=gray!30] (2.2,0.18) circle (0.18);
    \draw[thick, fill=gray!30] (3.4,0.18) circle (0.18);

    % Pivote
    \fill[maincolor] (2.8,1.5) circle (0.06);

    % Vertical de referencia
    \draw[dashed, gray] (2.8,1.5) -- (2.8,2.8);

    % Varilla hacia arriba
    \draw[thick, accentcolor] (2.8,1.5) -- (4.1,2.65);
    \node[accentcolor, above right] at (3.45,2.1) {$\ell$};

    % Masa m
    \draw[thick, fill=orange!20, draw=accentcolor] (4.1,2.65) circle (0.2);
    \node[accentcolor, right=4pt] at (4.1,2.65) {$m$};

    % Ángulo theta
    \draw[->, accentcolor] (2.8,2.15) arc (90:55:0.65);
    \node[accentcolor] at (3.1,2.35) {$\theta$};

    % Cota H
    \draw[<->, gray] (4.8,0) -- (4.8,1.5) node[midway, right] {$H$};
    \draw[dotted] (3.8,1.5) -- (4.9,1.5);

    % Coordenada x
    \draw[->, maincolor, thick] (0,2.2) -- (2.8,2.2) node[midway, above] {$x$};
    \draw[dotted] (0,0) -- (0,2.4);
    \draw[dotted] (2.8,1.5) -- (2.8,2.4);

\end{tikzpicture}
\end{document}
```

---

#### E5 — Péndulo doble planar, coordenadas $(\theta, \phi)$, longitudes iguales (P2)

> Contexto para NotebookLM: péndulo doble con dos varillas de igual longitud $\ell$. Primera varilla articulada al techo, ángulo $\theta$ desde la vertical. Segunda articulada al extremo de la primera, ángulo $\phi$ desde la vertical que pasa por $m_1$. Masas $m_1$ y $m_2$ en los extremos.

```tikz
\usetikzlibrary{patterns,decorations.pathmorphing}
\begin{document}
\begin{tikzpicture}[scale=1.1, >=latex]
    \colorlet{maincolor}{teal}
    \colorlet{accentcolor}{orange}

    % Techo
    \fill[pattern=north east lines] (-1,0) rectangle (1,0.2);
    \draw[thick] (-1,0) -- (1,0);

    % Eje vertical
    \draw[dashed, gray] (0,0) -- (0,-3.5);

    % Primera varilla
    \draw[thick, maincolor] (0,0) -- (1.2,-1.8);
    \draw[fill=teal!20, draw=maincolor, thick] (1.2,-1.8) circle (0.18);
    \node[maincolor, right=2pt] at (1.2,-1.8) {$m_1$};
    \node[maincolor, above left] at (0.6,-0.9) {$\ell$};

    % Ángulo theta
    \draw[dashed, gray] (1.2,-1.8) -- (1.2,-3.8);
    \draw[->, maincolor, thick] (0,-1.0) arc (-90:-56:1.0);
    \node[maincolor] at (0.25,-1.2) {$\theta$};

    % Segunda varilla
    \draw[thick, accentcolor] (1.2,-1.8) -- (2.6,-3.2);
    \draw[fill=orange!20, draw=accentcolor, thick] (2.6,-3.2) circle (0.18);
    \node[accentcolor, right=2pt] at (2.6,-3.2) {$m_2$};
    \node[accentcolor, above left] at (1.9,-2.5) {$\ell$};

    % Ángulo phi
    \draw[->, accentcolor, thick] (1.2,-2.8) arc (-90:-45:1.0);
    \node[accentcolor] at (1.45,-3.0) {$\phi$};

\end{tikzpicture}
\end{document}
```

---

#### E10 — Tres poleas en cadena: resorte $K$ en techo, resorte $K'$ en ramal de $m_2$, masa $m_3$ (P2)

> Contexto para NotebookLM: polea $m_1$ suspendida del techo por resorte $K$; ramal izquierdo fijo al piso; ramal derecho sostiene polea $m_2$ a distancia $a$. Ramal izquierdo de $m_2$ conectado al piso por resorte $K'$; ramal derecho sostiene masa puntual $m_3$. Coordenadas $y_1$, $y_2$, $y_3$ desde el techo. Altura $H$.

```tikz
\usetikzlibrary{patterns,decorations.pathmorphing}
\begin{document}
\begin{tikzpicture}[scale=1.0, >=latex]
    \colorlet{maincolor}{teal}
    \colorlet{accentcolor}{orange}

    % Techo
    \fill[pattern=north east lines] (-1,5.3) rectangle (4.5,5.6);
    \draw[thick] (-1,5.3) -- (4.5,5.3);

    % Piso
    \fill[pattern=north east lines] (-1,-0.3) rectangle (4.5,0);
    \draw[thick] (-1,0) -- (4.5,0);

    % Resorte K
    \draw[decoration={aspect=0.3, segment length=2mm, amplitude=2.5mm, coil}, decorate, maincolor, thick] (1.0,5.3) -- (1.0,4.0);
    \node[left, maincolor] at (0.75,4.65) {$K$};

    % Polea m1
    \draw[thick, fill=teal!10, draw=maincolor] (1.0,3.7) circle (0.3);
    \fill[maincolor] (1.0,3.7) circle (0.05);
    \node[left, maincolor] at (0.5,3.7) {$m_1$};

    % Ramal izquierdo de m1 al piso
    \draw[thick, maincolor] (0.7,3.7) -- (0.7,0);

    % Ramal derecho de m1 a m2
    \draw[thick, maincolor] (1.3,3.7) -- (1.3,2.3);

    % Polea m2
    \draw[thick, fill=orange!10, draw=accentcolor] (1.3,2.0) circle (0.3);
    \fill[accentcolor] (1.3,2.0) circle (0.05);
    \node[right, accentcolor] at (1.7,2.0) {$m_2$};

    % Ramal izquierdo de m2 + resorte K'
    \draw[thick, accentcolor] (1.0,2.0) -- (1.0,1.4);
    \draw[decoration={aspect=0.3, segment length=2mm, amplitude=2mm, coil}, decorate, accentcolor, thick] (1.0,1.4) -- (1.0,0);
    \node[left, accentcolor] at (0.75,0.7) {$K'$};

    % Ramal derecho de m2 a m3
    \draw[thick, accentcolor] (1.6,2.0) -- (1.6,1.0);
    \draw[thick, fill=accentcolor!40, draw=accentcolor] (1.6,0.8) circle (0.15);
    \node[right, accentcolor] at (1.8,0.8) {$m_3$};

    % Cota H
    \draw[<->, red, thick] (-0.5,0) -- (-0.5,5.3) node[midway, left] {$H$};

    % y1
    \draw[->, maincolor, thick] (2.2,5.3) -- (2.2,3.7) node[midway, right] {$y_1$};
    \draw[dotted] (1.0,3.7) -- (2.3,3.7);
    \draw[dotted] (1.0,5.3) -- (2.3,5.3);

    % y2
    \draw[->, accentcolor, thick] (2.9,5.3) -- (2.9,2.0) node[midway, right] {$y_2$};
    \draw[dotted] (1.3,2.0) -- (3.0,2.0);

    % y3
    \draw[->, accentcolor, thick] (3.6,5.3) -- (3.6,0.8) node[midway, right] {$y_3$};
    \draw[dotted] (1.75,0.8) -- (3.7,0.8);

    % Cota a
    \draw[<->, maincolor, thick] (1.9,3.7) -- (1.9,2.0) node[midway, right] {$a$};
    \draw[dotted] (1.3,3.7) -- (2.1,3.7);

\end{tikzpicture}
\end{document}
```

---

#### E11 — Tres poleas en cadena: resorte $K$ en techo, cables fijos al piso, resorte $K'$ en ramal de $m_3$ (P2)

> Contexto para NotebookLM: polea $m_1$ suspendida del techo por resorte $K$; ramal izquierdo fijo al piso; ramal derecho sostiene $m_2$. Ramal izquierdo de $m_2$ fijo al piso; ramal derecho sostiene $m_3$. Ramal izquierdo de $m_3$ fijo al piso; ramal derecho conectado al piso por resorte $K'$. Coordenadas $y_1$, $y_2$, $y_3$ desde el techo. Cota $a$ de $m_1$ a $m_3$.

```tikz
\usetikzlibrary{patterns,decorations.pathmorphing}
\begin{document}
\begin{tikzpicture}[scale=1.0, >=latex]
    \colorlet{maincolor}{teal}
    \colorlet{accentcolor}{orange}

    % Techo
    \fill[pattern=north east lines] (-1,7.3) rectangle (5.5,7.6);
    \draw[thick] (-1,7.3) -- (5.5,7.3);

    % Piso
    \fill[pattern=north east lines] (-1,-0.3) rectangle (5.5,0);
    \draw[thick] (-1,0) -- (5.5,0);

    % Resorte K
    \draw[decoration={aspect=0.3, segment length=2mm, amplitude=2.5mm, coil}, decorate, maincolor, thick] (1.0,7.3) -- (1.0,6.0);
    \node[left, maincolor] at (0.75,6.65) {$K$};

    % Polea m1
    \draw[thick, fill=teal!10, draw=maincolor] (1.0,5.7) circle (0.3);
    \fill[maincolor] (1.0,5.7) circle (0.05);
    \node[left, maincolor] at (0.5,5.7) {$m_1$};

    \draw[thick, maincolor] (0.7,5.7) -- (0.7,0);
    \draw[thick, maincolor] (1.3,5.7) -- (1.3,3.7);

    % Polea m2
    \draw[thick, fill=accentcolor!10, draw=accentcolor] (1.3,3.4) circle (0.3);
    \fill[accentcolor] (1.3,3.4) circle (0.05);
    \node[left, accentcolor] at (0.8,3.4) {$m_2$};

    \draw[thick, accentcolor] (1.0,3.4) -- (1.0,0);
    \draw[thick, accentcolor] (1.6,3.4) -- (1.6,1.7);

    % Polea m3
    \draw[thick, fill=teal!20, draw=maincolor] (1.6,1.4) circle (0.3);
    \fill[maincolor] (1.6,1.4) circle (0.05);
    \node[left, maincolor] at (1.1,1.4) {$m_3$};

    \draw[thick, maincolor] (1.3,1.4) -- (1.3,0);
    \draw[thick, accentcolor] (1.9,1.4) -- (1.9,1.0);
    \draw[decoration={aspect=0.3, segment length=2mm, amplitude=2mm, coil}, decorate, accentcolor, thick] (1.9,1.0) -- (1.9,0);
    \node[right, accentcolor] at (2.1,0.5) {$K'$};

    % Cota H
    \draw[<->, red, thick] (-0.5,0) -- (-0.5,7.3) node[midway, left] {$H$};

    % y1
    \draw[->, maincolor, thick] (2.8,7.3) -- (2.8,5.7) node[midway, right] {$y_1$};
    \draw[dotted] (1.0,7.3) -- (2.9,7.3);
    \draw[dotted] (1.0,5.7) -- (2.9,5.7);

    % y2
    \draw[->, accentcolor, thick] (3.5,7.3) -- (3.5,3.4) node[midway, right] {$y_2$};
    \draw[dotted] (1.3,3.4) -- (3.6,3.4);

    % y3
    \draw[->, maincolor, thick] (4.2,7.3) -- (4.2,1.4) node[midway, right] {$y_3$};
    \draw[dotted] (1.9,1.4) -- (4.3,1.4);

    % Cota a
    \draw[<->, maincolor, thick] (2.1,5.7) -- (2.1,1.4) node[midway, right] {$a$};
    \draw[dotted] (1.3,5.7) -- (2.2,5.7);
    \draw[dotted] (1.9,1.4) -- (2.2,1.4);

\end{tikzpicture}
\end{document}
```

---

#### E12 — Cuatro masas: tres poleas en cadena + masa $m_4$ en ramal izquierdo de $m_1$, resorte $K'$ (P2)

> Contexto para NotebookLM: polea $m_1$ suspendida del techo por resorte $K$; ramal izquierdo sostiene bloque $m_4$; ramal derecho sostiene polea $m_2$. Ramal izquierdo de $m_2$ fijo al piso; ramal derecho sostiene polea $m_3$. Ramal izquierdo de $m_3$ fijo al piso; ramal derecho conectado al piso por resorte $K'$. Coordenadas $y_1$, $y_2$, $y_3$, $y_4$ desde el techo. Cota $a$ de $m_1$ a $m_3$.

```tikz
\usetikzlibrary{patterns,decorations.pathmorphing}
\begin{document}
\begin{tikzpicture}[scale=1.0, >=latex]
    \colorlet{maincolor}{teal}
    \colorlet{accentcolor}{orange}

    % Techo
    \fill[pattern=north east lines] (-1,7.3) rectangle (5.5,7.6);
    \draw[thick] (-1,7.3) -- (5.5,7.3);

    % Piso
    \fill[pattern=north east lines] (-1,-0.3) rectangle (5.5,0);
    \draw[thick] (-1,0) -- (5.5,0);

    % Resorte K
    \draw[decoration={aspect=0.3, segment length=2mm, amplitude=2.5mm, coil}, decorate, maincolor, thick] (1.0,7.3) -- (1.0,6.0);
    \node[left, maincolor] at (0.75,6.65) {$K$};

    % Polea m1
    \draw[thick, fill=teal!10, draw=maincolor] (1.0,5.7) circle (0.3);
    \fill[maincolor] (1.0,5.7) circle (0.05);
    \node[left, maincolor] at (0.5,5.7) {$m_1$};

    % Ramal izquierdo de m1 a m4
    \draw[thick, maincolor] (0.7,5.7) -- (0.7,4.3);
    \draw[thick, fill=teal!30, draw=maincolor] (0.4,3.7) rectangle (1.0,4.3);
    \node[maincolor] at (0.7,4.0) {$m_4$};

    % Ramal derecho de m1 a m2
    \draw[thick, maincolor] (1.3,5.7) -- (1.3,3.7);

    % Polea m2
    \draw[thick, fill=accentcolor!10, draw=accentcolor] (1.3,3.4) circle (0.3);
    \fill[accentcolor] (1.3,3.4) circle (0.05);
    \node[left, accentcolor] at (0.8,3.4) {$m_2$};

    \draw[thick, accentcolor] (1.0,3.4) -- (1.0,0);
    \draw[thick, accentcolor] (1.6,3.4) -- (1.6,1.7);

    % Polea m3
    \draw[thick, fill=teal!20, draw=maincolor] (1.6,1.4) circle (0.3);
    \fill[maincolor] (1.6,1.4) circle (0.05);
    \node[left, maincolor] at (1.1,1.4) {$m_3$};

    \draw[thick, maincolor] (1.3,1.4) -- (1.3,0);
    \draw[thick, accentcolor] (1.9,1.4) -- (1.9,1.0);
    \draw[decoration={aspect=0.3, segment length=2mm, amplitude=2mm, coil}, decorate, accentcolor, thick] (1.9,1.0) -- (1.9,0);
    \node[right, accentcolor] at (2.1,0.5) {$K'$};

    % Cota H
    \draw[<->, red, thick] (-0.5,0) -- (-0.5,7.3) node[midway, left] {$H$};

    % y1
    \draw[->, maincolor, thick] (2.8,7.3) -- (2.8,5.7) node[midway, right] {$y_1$};
    \draw[dotted] (1.0,7.3) -- (2.9,7.3);
    \draw[dotted] (1.0,5.7) -- (2.9,5.7);

    % y2
    \draw[->, accentcolor, thick] (3.5,7.3) -- (3.5,3.4) node[midway, right] {$y_2$};
    \draw[dotted] (1.3,3.4) -- (3.6,3.4);

    % y3
    \draw[->, maincolor, thick] (4.2,7.3) -- (4.2,1.4) node[midway, right] {$y_3$};
    \draw[dotted] (1.9,1.4) -- (4.3,1.4);

    % y4
    \draw[->, maincolor, thick] (4.9,7.3) -- (4.9,4.0) node[midway, right] {$y_4$};
    \draw[dotted] (0.7,4.0) -- (5.0,4.0);

    % Cota a
    \draw[<->, maincolor, thick] (2.1,5.7) -- (2.1,1.4) node[midway, right] {$a$};
    \draw[dotted] (1.0,5.7) -- (2.2,5.7);
    \draw[dotted] (1.6,1.4) -- (2.2,1.4);

\end{tikzpicture}
\end{document}
```

---

#### E13 — Dos poleas con resortes $K$, $K'$ y fuerza $F$ en ramal de $m_2$, coordenadas $(y_2, a)$ (P2)

> Contexto para NotebookLM: polea $m_1$ suspendida del techo por resorte $K$ en su centro; ramal izquierdo sostiene la polea $m_2$ por su centro; ramal derecho conectado al piso por resorte $K'$. Ramal izquierdo de $m_2$ fijo al piso; ramal derecho lleva la fuerza $F$ (flecha hacia abajo). Coordenadas $y_1$, $y_2$, $y_3$ desde el techo. Cota $a$: distancia de $m_2$ al punto de $F$.

```tikz
\usetikzlibrary{patterns,decorations.pathmorphing}
\begin{document}
\begin{tikzpicture}[scale=1.0, >=latex]
    \colorlet{maincolor}{teal}
    \colorlet{accentcolor}{orange}

    % Techo
    \fill[pattern=north east lines] (-1,7.3) rectangle (5.5,7.6);
    \draw[thick] (-1,7.3) -- (5.5,7.3);

    % Piso
    \fill[pattern=north east lines] (-1,-0.3) rectangle (5.5,0);
    \draw[thick] (-1,0) -- (5.5,0);

    % Resorte K
    \draw[decoration={aspect=0.3, segment length=2mm, amplitude=2.5mm, coil}, decorate, maincolor, thick] (1.2,7.3) -- (1.2,6.0);
    \node[left, maincolor] at (0.95,6.65) {$K$};

    % Polea m1
    \draw[thick, fill=teal!10, draw=maincolor] (1.2,5.7) circle (0.3);
    \fill[maincolor] (1.2,5.7) circle (0.05);
    \node[left, maincolor] at (0.7,5.7) {$m_1$};

    % Ramal izquierdo de m1 a m2
    \draw[thick, maincolor] (0.9,5.7) -- (0.9,3.4);

    % Ramal derecho de m1 a resorte K'
    \draw[thick, maincolor] (1.5,5.7) -- (1.5,2.0);
    \draw[decoration={aspect=0.3, segment length=2mm, amplitude=2mm, coil}, decorate, maincolor, thick] (1.5,2.0) -- (1.5,0);
    \node[right, maincolor] at (1.7,1.0) {$K'$};

    % Polea m2
    \draw[thick, fill=accentcolor!10, draw=accentcolor] (0.9,3.4) circle (0.3);
    \fill[accentcolor] (0.9,3.4) circle (0.05);
    \node[left, accentcolor] at (0.4,3.4) {$m_2$};

    % Ramal izquierdo de m2 al piso
    \draw[thick, accentcolor] (0.6,3.4) -- (0.6,0);

    % Ramal derecho de m2 a fuerza F
    \draw[thick, accentcolor] (1.2,3.4) -- (1.2,1.2);
    \draw[->, accentcolor, ultra thick] (1.2,1.2) -- (1.2,0.4) node[right, accentcolor] {$F$};
    \fill[accentcolor] (1.2,1.2) circle (0.06);

    % Cota H
    \draw[<->, red, thick] (-0.5,0) -- (-0.5,7.3) node[midway, left] {$H$};

    % y1
    \draw[->, maincolor, thick] (2.8,7.3) -- (2.8,5.7) node[midway, right] {$y_1$};
    \draw[dotted] (1.2,7.3) -- (2.9,7.3);
    \draw[dotted] (1.2,5.7) -- (2.9,5.7);

    % y2
    \draw[->, accentcolor, thick] (3.5,7.3) -- (3.5,3.4) node[midway, right] {$y_2$};
    \draw[dotted] (0.9,3.4) -- (3.6,3.4);

    % y3
    \draw[->, accentcolor, thick] (4.2,7.3) -- (4.2,1.2) node[midway, right] {$y_3$};
    \draw[dotted] (1.2,1.2) -- (4.3,1.2);

    % Cota a
    \draw[<->, accentcolor, thick] (2.1,3.4) -- (2.1,1.2) node[midway, right] {$a$};
    \draw[dotted] (0.9,3.4) -- (2.2,3.4);
    \draw[dotted] (1.2,1.2) -- (2.2,1.2);

\end{tikzpicture}
\end{document}
```

> Sistemas sin fricción. Integral de movimiento. Energía total constante $E = T + V$.

#### Curva de potencial $V(q)$

> Contexto para NotebookLM: usar cuando el usuario pida graficar la curva de energía potencial de un sistema conservativo. Mostrar: mínimo de $V$ (equilibrio estable), punto de inflexión (inestable), nivel de energía $E$ como línea horizontal, región de movimiento acotado.

```tikz
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

#### Diagrama de bloques — Simulink con rectángulos (Figura 1.5)

> Contexto para NotebookLM: bloques como rectángulos. Retroalimentación con dos `\draw` separados en la esquina para evitar artefactos visuales — nunca encadenar la esquina en un solo `\draw`.

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.1]

% Etiqueta entrada
\node[left] at (0,0) {$\ddot{\theta}$};

% Integrador 1
\draw[draw=teal, thick] (0.8,-0.4) rectangle (2.2,0.4);
\node at (1.5,0) {$1/s$};

% Etiqueta dot theta
\node[above] at (3.2,0) {$\dot{\theta}$};

% Integrador 2
\draw[draw=teal, thick] (3.8,-0.4) rectangle (5.2,0.4);
\node at (4.5,0) {$1/s$};

% Etiqueta theta
\node[above] at (6.2,0) {$\theta$};

% Scope (borde punteado)
\draw[draw=orange, thick, dashed] (6.5,-0.5) rectangle (8,0.5);
\node at (7.25,0) {Scope};

% Conexiones hacia adelante
\draw[->, thick] (0,0) -- (0.8,0);
\draw[->, thick] (2.2,0) -- (3.8,0);
\draw[->, thick] (5.2,0) -- (6.5,0);

% Rama de retroalimentacion: bajar desde theta
\draw[thick] (6.2,0) -- (6.2,-1.6);

% Bloque sin
\draw[draw=teal, thick] (3.8,-2.0) rectangle (5.2,-1.2);
\node at (4.5,-1.6) {$\sin$};

% Bloque ganancia
\draw[draw=teal, thick] (1.5,-2.0) rectangle (3.0,-1.2);
\node at (2.25,-1.6) {$-g/\ell$};

% Flechas retroalimentacion — esquina separada en dos draw
\draw[->, thick] (6.2,-1.6) -- (5.2,-1.6);
\draw[->, thick] (3.8,-1.6) -- (3.0,-1.6);
\draw[thick] (1.5,-1.6) -- (0,-1.6);
\draw[->, thick] (0,-1.6) -- (0,0);

\end{tikzpicture}
\end{document}
```

---

#### Diagrama de bloques — Simulink con triángulos (Figura 1.5 alt.)

> Contexto para NotebookLM: misma topología pero bloques como triángulos. Triángulo de ida: punta hacia la derecha `(x,0.5)--(x+1,1)--(x+1,0)--cycle`. Triángulo de retorno: punta hacia la izquierda `(x,1)--(x+1,0.5)--(x,0)--cycle`. Retroalimentación con dos `\draw` separados en esquinas.

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.1]

% Etiqueta entrada
\node[left] at (0,0.5) {$\ddot{\theta}$};

% Integrador 1 — triangulo ida (punta derecha)
\draw[draw=teal, thick] (1,0) -- (2,0.5) -- (1,1) -- cycle;
\node at (1.35,0.5) {$1/s$};

% Etiqueta dot theta
\node[above] at (2.8,0.5) {$\dot{\theta}$};

% Integrador 2 — triangulo ida (punta derecha)
\draw[draw=teal, thick] (3.5,0) -- (4.5,0.5) -- (3.5,1) -- cycle;
\node at (3.85,0.5) {$1/s$};

% Etiqueta theta
\node[above] at (5.3,0.5) {$\theta$};

% Scope (borde punteado)
\draw[draw=orange, thick, dashed] (5.6,0) rectangle (7,1);
\node at (6.3,0.5) {Scope};

% Conexiones hacia adelante
\draw[->, thick] (0,0.5) -- (1,0.5);
\draw[->, thick] (2,0.5) -- (3.5,0.5);
\draw[->, thick] (4.5,0.5) -- (5.6,0.5);

% Rama de retroalimentacion: bajar desde theta
\draw[thick] (5.3,0.5) -- (5.3,-1.6);

% Bloque sin — triangulo retorno (punta izquierda)
\draw[draw=teal, thick] (3.5,-1.6) -- (4.5,-1.1) -- (4.5,-2.1) -- cycle;
\node at (4.15,-1.6) {$\sin$};

% Bloque ganancia — triangulo retorno (punta izquierda)
\draw[draw=teal, thick] (1.5,-1.6) -- (2.5,-1.1) -- (2.5,-2.1) -- cycle;
\node at (2.15,-1.6) {$-g/\ell$};

% Flechas retroalimentacion — esquinas separadas
\draw[->, thick] (5.3,-1.6) -- (4.5,-1.6);
\draw[->, thick] (3.5,-1.6) -- (2.5,-1.6);
\draw[thick] (1.5,-1.6) -- (0,-1.6);
\draw[->, thick] (0,-1.6) -- (0,0.5);

\end{tikzpicture}
\end{document}
```

> **Nota:** las Figuras E1, E2, E3 (brazo robótico 3D, pág. 8) son IMA — no usar TikZJax para esas.

---

#### Péndulo doble — T3/T4

> Contexto para NotebookLM: usar para el péndulo doble como ejemplo de sistema con $n=2$ DoF y coordenadas generalizadas $\theta_1$, $\theta_2$. Masas $m_1$, $m_2$.

```tikz
\usetikzlibrary{patterns}
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

#### Espacio de fases $( \dot{q}, q )$ — retrato de fase del péndulo (separatriz correcta)

> Contexto para NotebookLM: versión corregida del retrato de fase para el péndulo simple ($\ddot{q} + \sin q = 0$). La separatriz homoclínica real tiene forma de "ojos" — dos ramas $\dot{q} = \pm 2\cos(q/2)$ que parten del equilibrio inestable en $q = \pm\pi$, cierran en $q = 0$ y vuelven. La curva anterior (`1.9*sin(deg(x/2))`) era una aproximación visual incorrecta.

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

% Separatriz correcta — rama superior: qdot = +2*cos(q/2)
\addplot[orange, very thick, domain=-3.14:3.14, samples=200]
    {2*cos(deg(x/2))};
% Separatriz correcta — rama inferior: qdot = -2*cos(q/2)
\addplot[orange, very thick, domain=-3.14:3.14, samples=200]
    {-2*cos(deg(x/2))};

% Punto de equilibrio estable (centro)
\fill[teal] (axis cs:0,0) circle (3pt);
\node[teal, above right] at (axis cs:0.1,0.1) {estable};

% Puntos de equilibrio inestable (silla) — en q = ±π donde la separatriz toca qdot=0
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