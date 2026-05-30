---
title: "TikZJax — Guía unificada para Obsidian"
galaxy_body: beacon
scope: vault
tool: tikzjax
audience: [usuario, notebooklm, claude]
tags: [beacon, tikzjax, circuitikz, infraestructura]
date_created: 2026-05-30
date_updated: 2026-05-30
status: activo
---

# ⚡ GUÍA UNIFICADA DE TIKZJAX PARA OBSIDIAN

> Plugin: `obsidian-tikzjax` — renderiza LaTeX/TikZ como SVG directamente en tus notas usando WebAssembly.
> Este documento tiene tres secciones según quién lo usa: **Usuario**, **NotebookLM** y **Claude**.
> Sistema Graph: [[_graph-system]]

---

# 👤 SECCIÓN USUARIO

Referencia rápida para escribir bloques TikZJax en Obsidian.

---

## U1. ESTRUCTURA OBLIGATORIA

Todo bloque TikZJax se escribe así:

````
```tikz
\usepackage{paquete}
\begin{document}
  \begin{tikzpicture}[opciones]
    ...comandos TikZ...
  \end{tikzpicture}
\end{document}
```
````

**Reglas:**
- El identificador del bloque es `tikz` — no `latex`, no `tikzjax`
- `\begin{document}` y `\end{document}` son **siempre obligatorios**
- `\documentclass{standalone}` **no se incluye** — el plugin lo usa automáticamente
- Los paquetes se cargan con `\usepackage{}` antes de `\begin{document}`

---

## U2. PAQUETES DISPONIBLES

| Paquete | Para qué |
|---------|---------|
| `circuitikz` | Circuitos electrónicos — resistencias, fuentes, capacitores, inductores, transistores, amplificadores |
| `pgfplots` | Gráficas matemáticas 2D y 3D de precisión — funciones, superficies, curvas de nivel |
| `tikz-cd` | Diagramas conmutativos — álgebra abstracta, categorías |
| `chemfig` | Estructuras químicas y fórmulas moleculares |
| `amsmath` | Matemáticas avanzadas — matrices, sistemas de ecuaciones |
| `amssymb` | Símbolos matemáticos extendidos |
| `tikz-3dplot` | Coordenadas y perspectiva 3D para TikZ |

---

## U3. CIRCUITOS ELECTRÓNICOS — circuitikz

### Estilos de norma

```tikz
% Estilo americano (IEEE)
\begin{circuitikz}[american]

% Estilo europeo (IEC)
\begin{circuitikz}[european]
```

### Componentes más comunes

| Componente                     | Código `to[...]` | Símbolo        |     |     |
| ------------------------------ | ---------------- | -------------- | --- | --- |
| Resistencia                    | `R`              | —▭—            |     |     |
| Capacitor                      | `C`              | —              |     | —   |
| Inductor                       | `L`              | —⌇⌇⌇—          |     |     |
| Fuente de voltaje DC           | `battery1`       | —⊣             | —   |     |
| Fuente de voltaje AC           | `sV`             | —○—            |     |     |
| Fuente de corriente            | `isource`        | —◯→—           |     |     |
| Fuente de voltaje controlada   | `cV`             | —◇—            |     |     |
| Fuente de corriente controlada | `cI`             | —◇→—           |     |     |
| Tierra (ground)                | `ground`         | ⏚              |     |     |
| Cortocircuito/cable            | `short`          | ———            |     |     |
| Diodo                          | `D`              | —▷             | —   |     |
| LED                            | `led`            | —▷             | —   |     |
| Transistor NPN                 | `npn`            | transistor NPN |     |     |
| Op-amp                         | `op amp`         | amplificador   |     |     |

### Etiquetas en componentes

```tikz
\draw (0,0) to[R, l=$R_1$, v=$V_R$] (3,0);
%              ↑ nombre    ↑ tensión (flecha)

\draw (0,0) to[R, l^=$R_1$] (3,0);   % etiqueta arriba
\draw (0,0) to[R, l_=$R_1$] (3,0);   % etiqueta abajo (default)
```

### Estructura básica de un circuito

```tikz
\usepackage{circuitikz}
\begin{document}
\begin{circuitikz}[american]
  % Malla principal: dibujada en sentido horario
  \draw (0,0)
    to[battery1, l=$V_s$]   (0,3)   % fuente → sube
    to[short]               (3,3)   % cable → derecha
    to[R, l=$R_1$]          (3,0)   % resistencia → baja
    to[short]               (0,0);  % cable → izquierda (cierra)
\end{circuitikz}
\end{document}
```

### Circuito con múltiples ramas

```tikz
\usepackage{circuitikz}
\begin{document}
\begin{circuitikz}[american]
  % Rama izquierda
  \draw (0,0) to[battery1, l=$V_s$] (0,4)
              to[short] (4,4);
  % Rama derecha
  \draw (4,4) to[R, l=$R_1$] (4,2)
              to[R, l=$R_2$] (4,0)
              to[short] (0,0);
  % Nodo intermedio etiquetado
  \draw (4,2) node[right] {$V_x$};
\end{circuitikz}
\end{document}
```

### Nodos y conexiones

```tikz
% Punto de conexión visible
\draw (2,2) node[circ] {};

% Punto de conexión invisible (solo intersección)
\draw (2,2) node[coordinate] (A) {};

% Etiqueta en un nodo
\draw (2,2) node[above] {$V_A$};
\draw (2,2) node[below right] {$+$};
```

---

## U4. GRÁFICAS MATEMÁTICAS — pgfplots

```tikz
\usepackage{pgfplots}
\begin{document}
\begin{tikzpicture}
\begin{axis}[
  xlabel={$x$}, ylabel={$f(x)$},
  xmin=-3, xmax=3,
  ymin=-1, ymax=5,
  grid=major,
  width=8cm, height=6cm
]
  \addplot[blue, thick, domain=-3:3, samples=100] {x^2};
  \addplot[red, thick, domain=-3:3, samples=100] {x};
\end{axis}
\end{tikzpicture}
\end{document}
```

---

## U5. DIBUJO GEOMÉTRICO BÁSICO — tikzpicture

```tikz
\begin{document}
\begin{tikzpicture}
  % Línea
  \draw (0,0) -- (3,0);

  % Flecha
  \draw[->] (0,0) -- (3,0) node[right] {$x$};

  % Rectángulo
  \draw (0,0) rectangle (2,1);

  % Círculo
  \draw (1,1) circle (0.5);

  % Región rellena
  \fill[blue!20] (0,0) -- (2,0) -- (1,1) -- cycle;
  \draw (0,0) -- (2,0) -- (1,1) -- cycle;

  % Texto matemático
  \node at (1,0.3) {$\Omega$};
\end{tikzpicture}
\end{document}
```

---

## U6. ESCALA Y TAMAÑO

```tikz
% Escalar el dibujo completo
\begin{circuitikz}[scale=1.5, american]

% Escalar solo el texto
\begin{circuitikz}[american, font=\small]

% Tamaño fijo con pgfplots
\begin{axis}[width=10cm, height=7cm]
```

---

## U7. ADVERTENCIA — PRIMER RENDER

El plugin puede no mostrar el diagrama al primer render. Si el bloque aparece vacío o con error:
1. Cerrar Obsidian completamente
2. Reabrir Obsidian
3. El diagrama debería renderizar correctamente

Esto ocurre especialmente con `circuitikz` en la primera carga del vault.

---

---

# 🤖 SECCIÓN NOTEBOOKLM

Instrucciones para que NotebookLM genere bloques TikZJax correctos listos para copiar en Obsidian.

---

## N1. ESTRUCTURA OBLIGATORIA

```
```tikz
\usepackage{PAQUETE}
\begin{document}
  \begin{ENTORNO}[OPCIONES]
    ...
  \end{ENTORNO}
\end{document}
```
```

**Sin `\begin{document}` el plugin no renderiza nada.**
**Sin `\end{document}` el bloque queda abierto y falla.**
**No incluir `\documentclass` — el plugin lo agrega automáticamente.**

---

## N2. SELECCIÓN DE PAQUETE Y ENTORNO

| Tipo de diagrama | Paquete | Entorno |
|-----------------|---------|---------|
| Circuito electrónico | `circuitikz` | `\begin{circuitikz}[american]` |
| Gráfica matemática 2D/3D | `pgfplots` | `\begin{axis}[...]` dentro de `tikzpicture` |
| Diagrama geométrico | (ninguno) | `\begin{tikzpicture}` |
| Diagrama conmutativo | `tikz-cd` | `\begin{tikzcd}` |

---

## N3. CIRCUITOS — REGLAS DE SINTAXIS

```
\draw (X1,Y1) to[COMPONENTE, OPCIONES] (X2,Y2);
```

- Las coordenadas son en cm por defecto
- Los componentes se dibujan de inicio a fin según la dirección
- `to[short]` para cables sin componente
- Cerrar siempre el circuito (el último punto debe llegar al primero)

Componentes frecuentes:
```
R         → resistencia
C         → capacitor
L         → inductor
battery1  → fuente DC
sV        → fuente AC
isource   → fuente de corriente
D         → diodo
short     → cable
ground    → tierra
```

Etiquetas:
```
l=$R_1$     → etiqueta del componente
v=$V_R$     → tensión con flecha
i=$I_R$     → corriente con flecha
```

---

## N4. CHECKLIST ANTES DE RESPONDER

- [ ] ¿Tiene `\begin{document}` y `\end{document}`?
- [ ] ¿El paquete está cargado con `\usepackage{}`?
- [ ] ¿No incluye `\documentclass`?
- [ ] ¿El circuito cierra (último punto = primero)?
- [ ] ¿Todas las matemáticas entre `$...$`?
- [ ] ¿El bloque usa el identificador `tikz`?

---

## N5. EJEMPLO COMPLETO — DIVISOR DE VOLTAJE

```tikz
\usepackage{circuitikz}
\begin{document}
\begin{circuitikz}[american]
  \draw (0,0)
    to[battery1, l=$V_s$]   (0,4)
    to[short]               (3,4)
    to[R, l=$R_1$, v=$V_1$] (3,2)
    to[R, l=$R_2$, v=$V_2$] (3,0)
    to[short]               (0,0);
  \draw (3,2) node[right] {$V_x$};
\end{circuitikz}
\end{document}
```

---

---

# 🧠 SECCIÓN CLAUDE

Reglas y patrones que Claude debe aplicar al generar o corregir bloques TikZJax en archivos `.md` del vault.

---

## C1. REGLAS ABSOLUTAS DE SINTAXIS

| Regla | Correcto | Incorrecto |
|-------|----------|------------|
| Identificador del bloque | ` ```tikz ` | ` ```latex `, ` ```tikzjax ` |
| `\begin{document}` siempre presente | ✅ | Omitirlo |
| `\end{document}` siempre presente | ✅ | Omitirlo |
| Sin `\documentclass` | No incluir | `\documentclass{standalone}` |
| Matemáticas entre `$...$` | `l=$R_1$` | `l=R_1` |
| Circuito cerrado | Último punto = primero | Circuito abierto |
| Paquete cargado con `\usepackage{}` | `\usepackage{circuitikz}` | Omitir el usepackage |

---

## C2. CUÁNDO INCLUIR DIAGRAMA TIKZJAX

Incluir solo si aporta precisión técnica que Desmos o texto no pueden dar:

✅ Incluir cuando:
- El enunciado involucra un circuito eléctrico o electrónico
- Se necesita un diagrama de bloques de sistema de control
- La figura requiere precisión geométrica con medidas exactas
- El contexto es electrónica, circuitos, señales o sistemas

❌ No incluir cuando:
- Una gráfica de función 2D es suficiente → usar Desmos
- El diagrama es conceptual y no requiere precisión → usar Excalidraw (observatory)
- El resultado es algebraico y no hay geometría visual relevante

---

## C3. CONVENCIÓN DE ESTILO

- Usar siempre `[american]` para circuitos salvo instrucción contraria
- Escalar con `[scale=1.2]` si el circuito es pequeño
- Etiquetar todos los componentes con `l=$...$`
- Etiquetar tensiones con `v=$...$` cuando el enunciado las pide
- Etiquetar corrientes con `i=$...$` cuando el enunciado las pide
- Agregar nodos etiquetados en los puntos de análisis (`node[right]{$V_A$}`)

---

## C4. FLUJO DE TRABAJO EN EL VAULT

1. El bloque `tikz` se escribe directamente en el cuerpo del `planet` o `comet` — no como nota separada.
2. Editar el archivo `.md` directamente con Filesystem — no mostrar el bloque completo en el chat salvo que el usuario lo pida.
3. Resumen en el chat: una línea indicando qué diagrama se agregó y en qué nota.
4. Si el diagrama no renderiza al primer intento → recordar al usuario el paso de cerrar y reabrir Obsidian.

---

## C5. PLANTILLA BASE PARA CIRCUITO SIMPLE

```tikz
\usepackage{circuitikz}
\begin{document}
\begin{circuitikz}[american, scale=1.2]
  \draw (0,0)
    to[FUENTE, l=$V_s$]     (0,3)
    to[short]               (4,3)
    to[COMPONENTE, l=$Z_1$] (4,0)
    to[short]               (0,0);
\end{circuitikz}
\end{document}
```

Reemplazar `FUENTE` y `COMPONENTE` según el circuito del enunciado.

---

## C6. NOTA SOBRE ESTE ARCHIVO

Los bloques de código TikZJax en **este documento** usan ` ```tikzx ` (con x al final) o se muestran como texto plano para que Obsidian no los renderice y se pueda leer el ejemplo.

En los archivos de ejercicios (`ETN806-*.md`, etc.) usar siempre ` ```tikz ` **sin la x**.

%%
galaxy-links
[[_graph-system]]
[[_galaxy-system]]
[[desmos_guide]]
%%
