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
  - ETN825
date_created: 2026-08-27
date_updated: 2026-08-27
status: activo
---

# ⚡ GUÍA UNIFICADA DE TIKZJAX PARA OBSIDIAN (ETN825)

> Plugin: `obsidian-tikzjax` — renderiza LaTeX/TikZ como SVG directamente en tus notas usando WebAssembly. Guía específica de Arquitectura de Computadores (ETN825). Para guía de notación AHPL ver `ETN825_AHPL.md`. Este documento está organizado en tres bloques: **Reglas de sintaxis (N1–N9)**, **Checklist (N10)**, y **Biblioteca de ejemplos por tipo ETN825 (N11–N15)**.

---

# 🤖 SECCIÓN NOTEBOOKLM

Instrucciones para que NotebookLM genere bloques TikzJax correctos listos para copiar en Obsidian. Cuando el usuario pida un diagrama, responder con un bloque de código — no con imagen ni enlace.

### Defaults — cuando el usuario no especifica

- Entorno: `tikzpicture` para todos los tipos de diagrama de ETN825.
- Escala: `scale=1.2` como punto de partida.
- Color principal de señal/módulo activo: `teal`; señal de control/handshake: `orange`; bus/dato: `violet`; referencia/auxiliar: `gray`.
- Líneas de señal: grosor `thick`. Flechas de bus: `very thick`.
- Módulos (cajas negras): rectángulo `draw=teal, thick` con nombre en negrita dentro.
- Registros internos: rectángulo `draw=gray` más pequeño dentro del módulo.

### Reglas base — siempre obligatorias

Antes de generar cualquier bloque, seguir este orden:

1. ¿Qué tipo de diagrama? (flujo · tiempo · caja negra · paquete de bits)
2. ¿Qué paquetes necesita? (ver N2)
3. ¿Escala y tamaño? (ver N5)
4. ¿Qué colores? (ver N6)
5. ¿Qué nivel de complejidad? (ver N9) — si el diagrama existe en el resumen del docente o en un libro fuente → citar; si hay que construirlo exacto para el apunte → TikZJax.

---

## BLOQUE A — SINTAXIS Y REGLAS

---

### N1. ESTRUCTURA OBLIGATORIA DEL BLOQUE

**Sin `\begin{document}` el plugin no renderiza nada. Sin `\end{document}` el bloque queda abierto y falla.**

```
\usepackage{PAQUETE}
\usetikzlibrary{LIBRERÍA}
\begin{document}
  \begin{tikzpicture}[OPCIONES]
    ...
  \end{tikzpicture}
\end{document}
```

Reglas:

- Identificador del bloque: ` ```tikz ` — nunca `latex`, nunca `tikzjax`
- `\begin{document}` y `\end{document}` siempre presentes
- `\documentclass{standalone}` **nunca se incluye** — el plugin lo agrega automáticamente
- Paquetes con `\usepackage{}` **antes** de `\begin{document}`
- Librerías TikZ con `\usetikzlibrary{}` también **antes** de `\begin{document}`

❌ Incorrecto:
```
\begin{tikzpicture}
\draw[->] (0,0) -- (1,0) node[right]{ready};
\end{tikzpicture}
```

✅ Correcto:
```tikz
\begin{document}
\begin{tikzpicture}
\draw[->] (0,0) -- (1,0) node[right]{ready};
\end{tikzpicture}
\end{document}
```

---

### N2. PAQUETES DISPONIBLES PARA ETN825

| Paquete / Librería | Para qué | Uso en ETN825 |
|---|---|---|
| (ninguno) | Dibujo geométrico básico | Cajas negras, buses, flechas |
| `\usetikzlibrary{shapes.geometric}` | Rombos de decisión | **Obligatorio** en diagramas de flujo |
| `\usetikzlibrary{arrows.meta}` | Puntas de flecha personalizadas | Buses con flecha doble, señales |
| `\usetikzlibrary{positioning}` | Posicionamiento relativo de nodos | Diagramas de flujo con muchos nodos |
| `\usetikzlibrary{calc}` | Coordenadas calculadas | Conexiones con puntos intermedios |
| `\usepackage{amsmath}` | Subíndices/superíndices en nodos | Si se usa `$IR_{8:17}$`, `$AC_{10:17}$` |

> `circuitikz` no aplica a ETN825 — los diagramas de la materia no son circuitos eléctricos.

---

### N3. TIPOS DE DIAGRAMA EN ETN825

| Tipo | Descripción | Entorno | Sección |
|---|---|---|---|
| Diagrama de flujo | Flujograma de secuencia AHPL — rombos de decisión, rectángulos de operación, saltos numerados | `tikzpicture` + `shapes.geometric` | N11, N15 |
| Diagrama de tiempo | Señales digitales (Clock, ready, datavalid, accept, SCN) con niveles alto/bajo y etiquetas | `tikzpicture` | N12 |
| Caja negra | Módulo con registros internos, entradas/salidas, buses (IOBUS, CSBUS) | `tikzpicture` | N13 |
| Paquete de bits | Formato de instrucción/registro — campos etiquetados con índices de bit | `tikzpicture` | N14 |

---

### N4. SINTAXIS BASE PARA ETN825

```
% Rombo de decisión (diagrama de flujo)
\node[diamond, draw=teal, thick, aspect=2, inner sep=1pt]
    (nombre) at (x,y) {\small condición?};

% Rectángulo de operación (diagrama de flujo)
\draw[draw=teal, thick] (x1,y1) rectangle (x2,y2);
\node at (cx,cy) {$AC \leftarrow DR$};

% Nodo de salto numerado (círculo con número)
\node[circle, draw=gray, thick, inner sep=2pt] at (x,y) {\small 24};

% Señal digital alta (diagrama de tiempo)
\draw[thick, teal] (x1,y_low) -- (x1,y_high) -- (x2,y_high) -- (x2,y_low);

% Bus ancho (dos líneas paralelas con flecha)
\draw[very thick, violet, ->] (x1,y+0.05) -- (x2,y+0.05);
\draw[very thick, violet] (x1,y-0.05) -- (x2,y-0.05);

% Módulo caja negra
\draw[draw=teal, thick] (x1,y1) rectangle (x2,y2);
\node[font=\bfseries] at (cx,cy) {INTERFACE};

% Registro interno dentro de módulo
\draw[draw=gray] (x1,y1) rectangle (x2,y2);
\node[font=\small] at (cx,cy) {DR(18)};

% Campo de paquete de bits
\draw[thick] (x1,0) rectangle (x2,0.6);
\node[font=\small] at (cx,0.3) {OP};
\node[font=\scriptsize, gray] at (x1,0.8) {0};
\node[font=\scriptsize, gray] at (x2,0.8) {4};
```

---

### N5. ESCALA Y TAMAÑO

| Tipo | Scale aprox. | Ancho típico | Uso |
|---|---|---|---|
| Paquete de bits simple | `scale=1` | 10–12 cm | Formato de instrucción con pocos campos |
| Caja negra simple | `scale=1` | 9–11 cm | Módulo con 3–5 señales |
| Caja negra con buses | `scale=0.9` | 12–14 cm | Módulo + IOBUS + CSBUS + señales |
| Diagrama de tiempo (pocas señales) | `scale=1` | 10 cm | 2–4 señales, 1 intervalo |
| Diagrama de tiempo (complejo) | `scale=0.85` | 12 cm | 4+ señales, intervalos asíncronos |
| Diagrama de flujo (pequeño) | `scale=0.9` | — | 5–10 nodos |
| Diagrama de flujo (complejo) | `scale=0.7` | — | 10+ nodos, múltiples ramas |

> Para diagramas de flujo muy complejos (como el de la secuencia INT de 70–84 pasos): dividir en sub-diagramas por bloque funcional y hacer un TikZJax por sección. No intentar el diagrama completo en un solo bloque.

---

### N6. PALETA DE COLORES

```
teal    → módulos, rectángulos de operación, señal principal, reloj
orange  → señales de handshake (ready, accept, csrdy), operaciones de control
violet  → buses de datos (IOBUS, CSBUS), transferencias de datos
gray    → nodos auxiliares, saltos numerados, líneas de referencia, registros internos
```

Roles fijos por tipo de diagrama:

| Diagrama | teal | orange | violet | gray |
|---|---|---|---|---|
| Flujo | rectángulos operación | señales de condición | — | rombos, saltos |
| Tiempo | Clock, señal activa | ready/accept/handshake | datavalid, dato | líneas base, etiquetas |
| Caja negra | borde módulo, registros | señales de control | buses | auxiliares |
| Paquete de bits | campos de op/dato | campos de control | — | índices, tabla |

---

### N7. CONVENCIONES DE DIAGRAMA DE FLUJO AHPL

- **Rombos** (`diamond`): condiciones booleanas — etiqueta con `?` al final. Ramas `Yes`/`No` etiquetadas.
- **Rectángulos**: operaciones AHPL — contenido en notación AHPL (`$AC \leftarrow DR$`, `$IBUS = AC$`).
- **Círculos**: saltos numerados — número de paso entre paréntesis o solo el número.
- **Flechas**: `->` estándar. Nunca flechas dobles en flujo.
- **Flujo principal**: de arriba hacia abajo. Bucles: salida por la derecha o izquierda, retorno con línea horizontal.
- **Subrutinas**: indicar con `(nombre seq)` en nodo redondeado o entre paréntesis.

---

### N8. CONVENCIONES DE DIAGRAMA DE TIEMPO

- **Eje horizontal**: tiempo, sin escala numérica — se dibuja como línea base para cada señal.
- **Señales digitales**: nivel bajo = `y=0`, nivel alto = `y=0.5` (o `y=1` si hay espacio). Transiciones verticales instantáneas.
- **Clock**: pulsos regulares — patrón repetido de subida/bajada. Siempre la primera señal (arriba).
- **Intervalo asíncrono**: línea punteada vertical al inicio del intervalo + etiqueta `Long asynchronous interval`.
- **Flechas de dependencia** (diagrama (b) del libro): arcos curvos entre señales — usar `\draw[->] (x1,y1) .. controls .. (x2,y2)`. Solo si el diagrama lo requiere explícitamente.
- **Etiquetas**: a la izquierda de cada señal en `node[left]`. Usar `\textit{}` para nombres en cursiva (ready, datavalid, accept).

---

### N9. CUÁNDO USAR TIKZJAX VS CITAR FUENTE

- **Diagrama disponible en resumen del docente o libro fuente** → citar figura (nombre archivo, página si disponible). Más fiel al material real.
- **Diagrama que hay que construir exacto** (combina señales específicas, campos de instrucción del temario, módulo con registros del apunte) → TikZJax.
- **Diagrama de flujo complejo** (más de 15 nodos) → evaluar dividir en partes o citar figura del libro.
- **Diagramas de tiempo con flechas de dependencia** (tipo handshake asíncrono, diagrama (b)) → TikZJax con `\draw` curvos. Nunca inventar las dependencias — solo si están en el fuente.

Cuando no esté claro: revisar si el tipo ya tiene ejemplo en el Bloque C. El precedente confirmado tiene prioridad.

---

## BLOQUE B — CHECKLIST

---

### N10. CHECKLIST ANTES DE RESPONDER

Antes de entregar un bloque TikZJax verificar:

- [ ] ¿Usa el identificador exacto ` ```tikz `? (nunca `latex`, nunca `tikzjax`)
- [ ] ¿Tiene `\begin{document}` y `\end{document}`?
- [ ] ¿NO incluye `\documentclass`?
- [ ] ¿Los paquetes y librerías necesarios están cargados **antes** de `\begin{document}`?
- [ ] ¿Si hay rombos de decisión → `\usetikzlibrary{shapes.geometric}` cargado?
- [ ] ¿Todas las expresiones AHPL entre `$...$`? (`$AC \leftarrow DR$`, `$IR_{8:17}$`)
- [ ] ¿Los colores siguen los roles fijos de N6?
- [ ] ¿Las ramas Yes/No de los rombos están etiquetadas?
- [ ] ¿Las señales del diagrama de tiempo tienen etiqueta a la izquierda?
- [ ] ¿Los campos del paquete de bits tienen índices de bit sobre el rectángulo?
- [ ] ¿El diagrama aporta algo que no está en la figura del fuente (N9)? Si no, citar fuente.

---

## BLOQUE C — BIBLIOTECA DE EJEMPLOS POR TIPO (ETN825)

---

### N11. DIAGRAMA DE FLUJO — SECUENCIA AHPL

> Flujogramas de secuencias de control AHPL. Rombos de decisión, rectángulos de operación, nodos de salto numerados.

#### Fragmento de flujo — secuencia con decisión y operación

> Contexto para NotebookLM: usar como base para cualquier fragmento de flujograma AHPL. Patrón: entrada numerada → rombo de decisión → rama Yes (operación) → rama No (salto o continuación). Adaptar nodos y etiquetas según la secuencia real del apunte.

```tikz
\usetikzlibrary{shapes.geometric, arrows.meta, positioning}
\begin{document}
\begin{tikzpicture}[
    scale=0.9,
    decision/.style={diamond, draw=gray, thick, aspect=2.2,
                     inner sep=1pt, font=\small},
    operation/.style={draw=teal, thick, minimum width=2.8cm,
                      minimum height=0.6cm, font=\small},
    jump/.style={circle, draw=gray, thick, inner sep=2pt, font=\small}
]

% Nodo de entrada (salto desde paso anterior)
\node[jump] (n24) at (0,0) {24};

% Rombo 1
\node[decision] (mri) at (0,-1.4) {MRI?};
\node[font=\small, gray] at (-1.2,-1.4) {Nox};
\node[font=\small, gray] at (0.2,-2.1) {Yes};

% Salto Yes hacia (6)
\node[jump] (n6) at (0,-2.8) {6};

% Rombo 2 (rama No del primero)
\node[decision] (opr) at (2.8,-1.4) {OPR?};
\node[font=\small, gray] at (4.1,-1.4) {No};
\node[font=\small, gray] at (2.8,-2.1) {Yes};

% Salto Yes hacia (26)
\node[jump] (n26) at (2.8,-2.8) {26};

% Operación (rama No de OPR)
\node[operation] (op1) at (5.8,-1.4) {$CSR \leftarrow IR_{8:17}$};

% Conexiones
\draw[->, thick] (n24) -- (mri);
\draw[->, thick] (mri) -- node[left, font=\small]{Yes} (n6);
\draw[->, thick] (mri) -- node[above, font=\small]{No} (opr);
\draw[->, thick] (opr) -- node[left, font=\small]{Yes} (n26);
\draw[->, thick] (opr) -- node[above, font=\small]{No} (op1);

\end{tikzpicture}
\end{document}
```

---

#### Fragmento de flujo — bucle con condición de salida

> Contexto para NotebookLM: usar para secuencias AHPL con bucle de espera (polling). Patrón: rombo de condición → si No, volver al mismo rombo (bucle); si Yes, continuar con operación. Típico para espera de `ready`, `accept`, `datavalid`.

```tikz
\usetikzlibrary{shapes.geometric, arrows.meta, calc}
\begin{document}
\begin{tikzpicture}[
    scale=1,
    decision/.style={diamond, draw=gray, thick, aspect=2.2,
                     inner sep=1pt, font=\small},
    operation/.style={draw=teal, thick, minimum width=3cm,
                      minimum height=0.6cm, font=\small},
    jump/.style={circle, draw=gray, thick, inner sep=2pt, font=\small}
]

% Operación previa
\node[operation] (op75) at (0,0) {$MD \leftarrow AC$};

% Rombo ready
\node[decision] (ready) at (0,-1.5) {ready?};

% Operación si Yes
\node[operation] (op77) at (0,-3.2) {$IOBUS = MD$\\$datavalid \leftarrow 1$};

% Rombo accept
\node[decision] (accept) at (0,-4.8) {accept?};

% Salto si Yes
\node[jump] (n24b) at (0,-6.2) {24};

% Conexiones principales
\draw[->, thick] (op75) -- (ready);
\draw[->, thick] (ready) -- node[right, font=\small]{Yes} (op77);
\draw[->, thick] (op77) -- (accept);
\draw[->, thick] (accept) -- node[right, font=\small]{Yes} (n24b);

% Bucle No de ready (vuelve al rombo)
\draw[thick] (ready) -- node[above, font=\small]{No} ++(-1.8,0)
    -- ++(0,1.5) -- (0,0 |- ready) ;

% Bucle No de accept (vuelve al rombo)
\draw[thick] (accept) -- node[above, font=\small]{No} ++(1.8,0)
    -- ++(0,1.5) -- (0,0 |- accept);

% Etiquetas de paso
\node[gray, font=\scriptsize] at (-2.2,-1.0) {76};
\node[gray, font=\scriptsize] at (2.2,-4.3) {77};

\end{tikzpicture}
\end{document}
```

---

### N12. DIAGRAMA DE TIEMPO

> Señales digitales con niveles alto/bajo. Clock, ready, datavalid, accept, SCN, csrdy.

#### Diagrama de tiempo — handshake sincrónico (tipo (a))

> Contexto para NotebookLM: usar para diagrama de tiempo con Clock y señales de handshake (ready, datavalid, accept) en intervalo sincrónico. Patrón de la imagen (a): Clock con pulsos regulares, ready alto durante toda la transacción, datavalid sube y baja, accept sube y baja desfasado. Incluye marcador de intervalo asíncrono con línea punteada si aplica.

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.0]

% --- Parámetros de layout ---
% y base de cada señal (de arriba abajo)
% Clock: y=4.5, ready: y=3.0, datavalid: y=1.5, accept: y=0

% Etiquetas señales
\node[left, font=\small] at (0,4.75) {Clock};
\node[left, font=\small, text=teal] at (0,3.0) {\textit{ready}};
\node[left, font=\small, text=violet] at (0,1.5) {\textit{datavalid}};
\node[left, font=\small, text=orange] at (0,0.0) {\textit{accept}};

% Líneas base
\draw[gray, thin] (0,4.5) -- (11,4.5);
\draw[gray, thin] (0,3.0) -- (11,3.0);
\draw[gray, thin] (0,1.5) -- (11,1.5);
\draw[gray, thin] (0,0.0) -- (11,0.0);

% --- CLOCK (pulsos regulares hasta x=4.5, luego punteado, luego retoma) ---
\foreach \x in {0.3, 0.9, 1.5, 2.1, 2.7, 3.3, 3.9} {
    \draw[thick, teal]
        (\x, 4.5) -- (\x, 4.9) -- (\x+0.3, 4.9) -- (\x+0.3, 4.5);
}
% Intervalo asíncrono punteado
\draw[dashed, gray] (4.5, 4.3) -- (4.5, 5.1);
\draw[dashed, thick, teal] (4.5, 4.7) -- (8.0, 4.7);
% Clock retoma
\foreach \x in {8.0, 8.6, 9.2, 9.8} {
    \draw[thick, teal]
        (\x, 4.5) -- (\x, 4.9) -- (\x+0.3, 4.9) -- (\x+0.3, 4.5);
}

% Etiqueta intervalo asíncrono
\node[font=\small, gray] at (6.2, 5.15) {Long asynchronous interval};

% --- READY (sube en x=0.5, baja en x=9.5) ---
\draw[thick, teal]
    (0, 3.0) -- (0.5, 3.0) -- (0.5, 3.4) -- (4.5, 3.4);
\draw[dashed, thick, teal] (4.5, 3.4) -- (8.0, 3.4);
\draw[thick, teal]
    (8.0, 3.4) -- (9.5, 3.4) -- (9.5, 3.0) -- (11, 3.0);

% --- DATAVALID (sube x=1.0, baja x=3.5) ---
\draw[thick, violet]
    (0, 1.5) -- (1.0, 1.5) -- (1.0, 1.9) -- (3.5, 1.9)
    -- (3.5, 1.5) -- (11, 1.5);

% --- ACCEPT (sube x=1.5, baja x=3.0) ---
\draw[thick, orange]
    (0, 0.0) -- (1.5, 0.0) -- (1.5, 0.4) -- (3.0, 0.4)
    -- (3.0, 0.0) -- (11, 0.0);

% Línea punteada vertical de referencia (punto de sincronía)
\draw[dashed, gray] (1.0, -0.3) -- (1.0, 5.1);

\end{tikzpicture}
\end{document}
```

---

#### Diagrama de tiempo — handshake asíncrono con dependencias (tipo (b))

> Contexto para NotebookLM: usar para el diagrama de handshake asíncrono donde las transiciones de cada señal dependen de la anterior (flechas curvas entre señales). Patrón: ready sube → datavalid sube → accept sube → datavalid baja → accept baja. Sin Clock. Las flechas indican causalidad.

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.1]

% Etiquetas
\node[left, font=\small, text=teal] at (0,4.0) {\textit{ready}};
\node[left, font=\small, text=violet] at (0,2.2) {\textit{datavalid}};
\node[left, font=\small, text=orange] at (0,0.4) {\textit{accept}};

% Líneas base
\draw[gray, thin] (0,4.0) -- (10,4.0);
\draw[gray, thin] (0,2.2) -- (10,2.2);
\draw[gray, thin] (0,0.4) -- (10,0.4);

% READY: sube x=1.0, baja x=7.5
\draw[thick, teal]
    (0,4.0) -- (1.0,4.0) -- (1.0,4.5) -- (7.5,4.5) -- (7.5,4.0) -- (10,4.0);

% DATAVALID: sube x=2.2, baja x=6.0
\draw[thick, violet]
    (0,2.2) -- (2.2,2.2) -- (2.2,2.7) -- (6.0,2.7) -- (6.0,2.2) -- (10,2.2);

% ACCEPT: sube x=3.5, baja x=7.0
\draw[thick, orange]
    (0,0.4) -- (3.5,0.4) -- (3.5,0.9) -- (7.0,0.9) -- (7.0,0.4) -- (10,0.4);

% Flechas de dependencia (causalidad entre transiciones)
% ready sube → datavalid sube
\draw[->, thick, gray]
    (1.0,4.5) .. controls (1.4,3.8) and (1.8,3.2) .. (2.2,2.7);

% datavalid sube → accept sube
\draw[->, thick, gray]
    (2.2,2.7) .. controls (2.7,2.0) and (3.0,1.4) .. (3.5,0.9);

% accept sube → datavalid baja
\draw[->, thick, gray]
    (3.5,0.9) .. controls (4.2,1.6) and (5.0,2.2) .. (6.0,2.7);

% datavalid baja → accept baja
\draw[->, thick, gray]
    (6.0,2.2) .. controls (6.3,1.5) and (6.6,1.0) .. (7.0,0.9);

\end{tikzpicture}
\end{document}
```

---

### N13. CAJA NEGRA — MÓDULO CON BUSES Y SEÑALES

> Módulos AHPL con registros internos, buses (IOBUS, CSBUS) y señales de control/datos.

#### Módulo INTERFACE — impresora con IOBUS y CSBUS

> Contexto para NotebookLM: usar para el módulo INTERFACE del ejemplo de impresora. Registros internos: DR(18), CR(8), busy, first. Buses: IOBUS (vertical, bidireccional), CSBUS (vertical, bidireccional). Señales salientes: print, feed, CHAR. Señales entrantes: wait. Señales de bus: accept, datavalid, ready, csrdy.

```tikz
\usetikzlibrary{arrows.meta}
\begin{document}
\begin{tikzpicture}[scale=0.95]

% ---- MÓDULO INTERFACE (caja principal) ----
\draw[draw=teal, thick] (3,0) rectangle (8,7);
\node[font=\bfseries\small, teal] at (5.5,7.3) {INTERFACE};

% ---- REGISTROS INTERNOS ----
% DR(18)
\draw[draw=gray, thick] (3.4,5.6) rectangle (6.2,6.4);
\node[font=\small] at (4.8,6.0) {DR(18)};
% Triángulo (flip-flop D indicator)
\draw[gray] (3.4,5.85) -- (3.7,6.0) -- (3.4,6.15);

% CR(8)
\draw[draw=gray, thick] (3.4,3.8) rectangle (6.2,4.6);
\node[font=\small] at (4.8,4.2) {CR(8)};

% busy
\draw[draw=gray, thick] (3.4,2.4) rectangle (6.2,3.2);
\node[font=\small] at (4.8,2.8) {\textit{busy}};

% first
\draw[draw=gray, thick] (3.4,1.0) rectangle (6.2,1.8);
\node[font=\small] at (4.8,1.4) {\textit{first}};

% ---- BUS IOBUS (línea vertical a la izquierda del módulo) ----
\draw[very thick, violet] (1.5,-0.5) -- (1.5,7.5);
\node[font=\small, violet, rotate=90] at (1.1,3.5) {IOBUS};

% Conexiones bidireccionales módulo ↔ IOBUS
\draw[very thick, violet, {Latex[length=3mm]}-{Latex[length=3mm]}]
    (1.5,5.0) -- (3.0,5.0);
\draw[very thick, violet, {Latex[length=3mm]}-{Latex[length=3mm]}]
    (1.5,4.2) -- (3.0,4.2);
\draw[very thick, violet, {Latex[length=3mm]}-{Latex[length=3mm]}]
    (1.5,3.0) -- (3.0,3.0);

% ---- BUS CSBUS (línea vertical más a la izquierda) ----
\draw[very thick, violet] (0.2,-0.5) -- (0.2,7.5);
\node[font=\small, violet, rotate=90] at (-0.2,3.5) {CSBUS};

% Conexión módulo ↔ CSBUS
\draw[very thick, violet, {Latex[length=3mm]}-{Latex[length=3mm]}]
    (0.2,2.0) -- (3.0,2.0);

% ---- SEÑALES SALIENTES (derecha del módulo → impresora) ----
% print
\draw[->, thick] (8,6.2) -- (9.5,6.2);
\node[right, font=\small] at (9.5,6.2) {\textit{print}};

% feed
\draw[->, thick] (8,5.5) -- (9.5,5.5);
\node[right, font=\small] at (9.5,5.5) {\textit{feed}};

% CHAR (desde CR)
\draw[->, very thick, violet] (8,4.2) -- (9.5,4.2);
\node[right, font=\small, violet] at (9.5,4.2) {CHAR};

% ---- SEÑAL ENTRANTE (impresora → módulo) ----
% wait
\draw[->, thick] (9.5,2.8) -- (8,2.8);
\node[right, font=\small] at (9.5,2.8) {\textit{wait}};

% ---- ETIQUETA IMPRESORA ----
\draw[thick] (9.5,5.0) -- (10.5,5.8);
\draw[thick] (9.5,5.0) -- (10.5,4.2);
\node[font=\small] at (10.8,5.0) {IMPRESORA};
\node[font=\scriptsize, gray] at (10.8,4.7) {Dispositivo \#010};

% ---- SEÑALES DE BUS (izquierda del IOBUS) ----
\node[left, font=\small, orange] at (1.5,6.5) {\textit{accept}};
\draw[->, thick, orange] (0.6,6.5) -- (1.4,6.5);

\node[left, font=\small, violet] at (1.5,5.8) {\textit{datavalid}};
\draw[->, thick, violet] (1.4,5.8) -- (0.6,5.8);

\node[left, font=\small, teal] at (1.5,1.2) {\textit{ready}};
\draw[->, thick, teal] (1.4,1.2) -- (0.6,1.2);

% csrdy (bajo CSBUS)
\node[below, font=\small, orange] at (0.2,-0.5) {\textit{csrdy}};

\end{tikzpicture}
\end{document}
```

---

#### Caja negra simple — módulo genérico con entradas y salidas

> Contexto para NotebookLM: usar como base para cualquier módulo AHPL simple. Un rectángulo con nombre, entradas a la izquierda y salidas a la derecha. Adaptar nombre, señales y registros según el apunte.

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.0]

% Caja principal
\draw[draw=teal, thick] (2,0) rectangle (6,4);
\node[font=\bfseries\small, teal] at (4,4.3) {MODULO};

% Registro interno
\draw[draw=gray] (2.4,1.8) rectangle (5.6,2.8);
\node[font=\small] at (4.0,2.3) {REG(N)};

% Entradas (izquierda)
\draw[->, thick] (0,3.2) -- (2,3.2);
\node[left, font=\small] at (0,3.2) {entrada1};

\draw[->, thick] (0,2.0) -- (2,2.0);
\node[left, font=\small] at (0,2.0) {entrada2};

\draw[<-, thick] (0,0.8) -- (2,0.8);
\node[left, font=\small] at (0,0.8) {salida\_fb};

% Salidas (derecha)
\draw[->, thick] (6,3.2) -- (8,3.2);
\node[right, font=\small] at (8,3.2) {salida1};

\draw[->, thick] (6,1.5) -- (8,1.5);
\node[right, font=\small] at (8,1.5) {salida2};

% Bus (abajo)
\draw[very thick, violet] (0,-0.5) -- (8,-0.5);
\node[font=\small, violet] at (4,-0.85) {BUS};
\draw[very thick, violet, <->] (4,-0.5) -- (4,0);

\end{tikzpicture}
\end{document}
```

---

### N14. PAQUETE DE BITS — FORMATO DE INSTRUCCIÓN/REGISTRO

> Campos de instrucción o registro con índices de bit. Tabla de valores debajo si aplica.

#### Formato de instrucción INT

> Contexto para NotebookLM: usar para el formato de la instrucción INT del SIC. Campos: OP (bits 0–4, valor 1111), MR (bit 5), INTR (bit 6), intf (bit 7), enif (bit 8–9), MR or INTR (bits 10–17). Tabla debajo: combinaciones IR5/IR6 y su efecto sobre MR.

```tikz
\usepackage{amsmath}
\begin{document}
\begin{tikzpicture}[scale=1.0]

% ---- FILA DE BITS (rectángulos) ----
% Índices: 0-4=OP, 5=MR, 6=INTR, 7=intf, 8-9=enif, 10-17=MR or INTR

% Campo OP (bits 0–4): 5 celdas de ancho 0.7
\foreach \i in {0,1,2,3} {
    \draw[thick] (\i*0.7, 0) rectangle (\i*0.7+0.7, 0.7);
    \node[font=\small] at (\i*0.7+0.35, 0.35) {1};
}
\draw[thick] (4*0.7, 0) rectangle (4*0.7+0.7, 0.7);
\node[font=\small] at (4*0.7+0.35, 0.35) {1};

% Campo MR (bit 5)
\draw[thick] (3.5,0) rectangle (4.2,0.7);
\node[font=\small] at (3.85,0.35) {};

% Campo INTR (bit 6)
\draw[thick] (4.2,0) rectangle (4.9,0.7);

% Campo intf (bit 7)
\draw[thick] (4.9,0) rectangle (5.6,0.7);

% Campo enif (bits 8–9)
\draw[thick] (5.6,0) rectangle (6.3,0.7);
\draw[thick] (6.3,0) rectangle (7.0,0.7);

% Campo MR or INTR (bits 10–17): bloque ancho
\draw[thick] (7.0,0) rectangle (10.5,0.7);
\node[font=\small\itshape] at (8.75,0.35) {MR  or  INTR};

% ---- ÍNDICES DE BIT (encima) ----
\node[font=\scriptsize, gray] at (0,0.9) {0};
\node[font=\scriptsize, gray] at (2.8,0.9) {4};
\node[font=\scriptsize, gray] at (3.5,0.9) {5};
\node[font=\scriptsize, gray] at (4.2,0.9) {6};
\node[font=\scriptsize, gray] at (4.9,0.9) {7};
\node[font=\scriptsize, gray] at (5.6,0.9) {8};
\node[font=\scriptsize, gray] at (6.3,0.9) {9};
\node[font=\scriptsize, gray] at (7.0,0.9) {10};
\node[font=\scriptsize, gray] at (10.5,0.9) {17};

% ---- ETIQUETAS DE CAMPO (debajo) ----
% Llave OP
\draw[thick] (0,-0.1) -- (0,-0.3) -- (2.8,-0.3) -- (2.8,-0.1);
\node[font=\small] at (1.4,-0.6) {OP};

% Etiquetas individuales
\node[font=\small] at (3.85,-0.4) {MR};
\node[font=\small] at (4.55,-0.4) {INTR};
\node[font=\small] at (5.25,-0.4) {intf};
\node[font=\small] at (6.65,-0.55) {enif};

% Flechas hacia etiquetas
\draw[->, gray, thin] (3.85,-0.2) -- (3.85,-0.3);
\draw[->, gray, thin] (4.55,-0.2) -- (4.55,-0.3);
\draw[->, gray, thin] (5.25,-0.2) -- (5.25,-0.3);
\draw[->, gray, thin] (6.65,-0.35) -- (6.65,-0.2);

% ---- TABLA DE VALORES (debajo) ----
\node[font=\small] at (0.5,-1.2) {$IR_5$};
\node[font=\small] at (1.5,-1.2) {$IR_6$};
\node[font=\small, align=left] at (5.0,-1.2) {};

% Filas
\foreach \y/\a/\b/\desc in {
    -1.7/0/0/No change in $MR$,
    -2.2/0/1/$MR \leftarrow IR_{10:17}$,
    -2.7/1/1/$MR \leftarrow AC_{10:17}$,
    -3.2/1/0/$AC_{10:17} \leftarrow MR$
} {
    \node[font=\small] at (0.5,\y) {\a};
    \node[font=\small] at (1.5,\y) {\b};
    \node[font=\small, anchor=west] at (2.5,\y) {\desc};
}

% Líneas de tabla
\draw[gray, thin] (0,-1.4) -- (10.5,-1.4);
\draw[gray, thin] (0,-1.4) -- (0,-3.45);
\draw[gray, thin] (2.0,-1.4) -- (2.0,-3.45);
\draw[gray, thin] (10.5,-1.4) -- (10.5,-3.45);
\draw[gray, thin] (0,-3.45) -- (10.5,-3.45);

\end{tikzpicture}
\end{document}
```

---

#### Paquete de bits simple — registro genérico

> Contexto para NotebookLM: usar como base para cualquier formato de registro o instrucción. Adaptar número de campos, anchos y etiquetas. N es el número total de bits.

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.0]

% Campos del registro (ajustar anchos según proporciones reales)
% Campo A (bits 0-3)
\draw[thick, teal] (0,0) rectangle (2.0,0.7);
\node[font=\small] at (1.0,0.35) {Campo A};

% Campo B (bits 4-7)
\draw[thick] (2.0,0) rectangle (4.0,0.7);
\node[font=\small] at (3.0,0.35) {Campo B};

% Campo C (bits 8-15)
\draw[thick] (4.0,0) rectangle (7.5,0.7);
\node[font=\small] at (5.75,0.35) {Campo C};

% Índices de bit
\node[font=\scriptsize, gray] at (0,0.9)   {0};
\node[font=\scriptsize, gray] at (2.0,0.9) {4};
\node[font=\scriptsize, gray] at (4.0,0.9) {8};
\node[font=\scriptsize, gray] at (7.5,0.9) {15};

% Etiquetas debajo
\node[font=\small, teal] at (1.0,-0.35) {opcode};
\node[font=\small]       at (3.0,-0.35) {modo};
\node[font=\small]       at (5.75,-0.35) {dirección};

\end{tikzpicture}
\end{document}
```

---

#### Paquete de bits — instrucción TST

> Contexto para NotebookLM: instrucción TST del SIC. Campos: OP (bits 0–5, valor `111100`), Test word (bits 6–17). La llave inferior agrupa bits 0–5 como OP. Usar como base para cualquier instrucción con campo OP de 6 bits seguido de un operando de 12 bits.

```tikz
\usepackage{amsmath}
\begin{document}
\begin{tikzpicture}[scale=1.0]

% ---- FILA DE BITS ----
% OP: bits 0-5 (6 celdas de 0.65 de ancho)
\foreach \i/\v in {0/1, 1/1, 2/1, 3/1, 4/0, 5/0} {
    \draw[thick] (\i*0.65, 0) rectangle (\i*0.65+0.65, 0.7);
    \node[font=\small] at (\i*0.65+0.325, 0.35) {\v};
}

% Test word: bits 6-17 (bloque ancho)
\draw[thick] (3.9, 0) rectangle (9.0, 0.7);
\node[font=\small] at (6.45, 0.35) {Test word};

% ---- ETIQUETA LABEL IZQUIERDA ----
\node[font=\small, left] at (0, 0.35) {TST};

% ---- ÍNDICES DE BIT ----
\node[font=\scriptsize, gray] at (0,   0.9) {0};
\node[font=\scriptsize, gray] at (3.9, 0.9) {6};
\node[font=\scriptsize, gray] at (9.0, 0.9) {17};

% ---- LLAVE OP (debajo de bits 0-5) ----
\draw[thick] (0,-0.12) -- (0,-0.35) -- (1.95,-0.35);
\draw[thick] (3.9,-0.12) -- (3.9,-0.35) -- (1.95,-0.35);
\draw[thick] (1.95,-0.35) -- (1.95,-0.55);
\node[font=\small] at (1.95,-0.8) {OP};

\end{tikzpicture}
\end{document}
```

---

#### Paquete de bits — instrucción IOT con anotaciones de campo

> Contexto para NotebookLM: instrucción IOT del SIC. Campos: OP (bits 0–5, valor `111101`), bits 6–8 de control (Command/Transfer, Status/Data, Command/Buffer), bit 9 (Input/Output), Device code **n** (bits 10–11), Control code (bits 12–17). Las llaves y flechas a la izquierda conectan los valores 1/0 con sus bits correspondientes. Es el diagrama más complejo de los tres — dividido en dos bloques: la fila de bits + índices, y las anotaciones.

```tikz
\usepackage{amsmath}
\begin{document}
\begin{tikzpicture}[scale=1.0]

% ---- FILA DE BITS ----
% OP: bits 0-5 (111101)
\foreach \i/\v in {0/1, 1/1, 2/1, 3/1, 4/0, 5/1} {
    \draw[thick] (\i*0.65, 0) rectangle (\i*0.65+0.65, 0.7);
    \node[font=\small] at (\i*0.65+0.325, 0.35) {\v};
}

% Bits 6,7,8 — control individual
\foreach \i in {6,7,8} {
    \draw[thick] (\i*0.65, 0) rectangle (\i*0.65+0.65, 0.7);
}

% Bit 9 — Input/Output
\draw[thick] (9*0.65, 0) rectangle (9*0.65+0.65, 0.7);

% Bits 10-11 — Device code (n)
\draw[thick] (10*0.65, 0) rectangle (10*0.65+0.65, 0.7);
\draw[thick] (11*0.65, 0) rectangle (11*0.65+0.65, 0.7);

% Bits 12-17 — Control code (bloque)
\draw[thick] (12*0.65, 0) rectangle (12*0.65+1.4, 0.7);

% ---- ETIQUETA LABEL IZQUIERDA ----
\node[font=\small, left] at (0, 0.35) {IOT};

% ---- ÍNDICES DE BIT ----
\foreach \pos/\lbl in {
    0/0, 3.9/6, 4.55/7, 5.2/8, 5.85/9, 6.5/10, 7.15/11, 7.8/12, 9.2/17
} {
    \node[font=\scriptsize, gray] at (\pos, 0.9) {\lbl};
}

% ---- ETIQUETAS DE CAMPO (sobre la fila) ----
\node[font=\scriptsize, align=center] at (5.53, 1.35)
    {Device};
\node[font=\scriptsize, align=center] at (5.53, 1.1)
    {code (\textbf{n})};
\draw[gray, thin, ->] (5.53, 1.0) -- (6.825, 0.75);

\node[font=\scriptsize] at (8.5, 1.35) {Control code};
\draw[gray, thin] (7.8, 1.1) -- (7.8, 0.75);
\draw[gray, thin] (9.2, 1.1) -- (9.2, 0.75);
\draw[gray, thin] (7.8, 1.1) -- (9.2, 1.1);

% ---- LLAVES Y ANOTACIONES IZQUIERDA (debajo) ----
% Llave OP (bits 0-5)
\draw[thick] (0,-0.12) -- (0,-0.32) -- (1.95,-0.32);
\draw[thick] (3.9,-0.12) -- (3.9,-0.32) -- (1.95,-0.32);
\draw[thick] (1.95,-0.32) -- (1.95,-0.52);
\node[font=\small] at (1.95,-0.72) {OP};

% Flecha y texto: bit 6 → 1=Command / 0=Transfer
\draw[->, gray, thin] (-1.8,-1.4) -- (4.225,-0.1);
\node[font=\scriptsize, align=left, anchor=east] at (-1.85,-1.3)
    {$1 = $ Command};
\node[font=\scriptsize, align=left, anchor=east] at (-1.85,-1.65)
    {$0 = $ Transfer};
% Llave izquierda agrupando las dos líneas
\draw[thick] (-1.6,-1.2) -- (-1.35,-1.2) -- (-1.35,-1.75) -- (-1.6,-1.75);

% Flecha y texto: bit 7 → 1=Status / 0=Data
\draw[->, gray, thin] (-1.8,-2.4) -- (4.875,-0.1);
\node[font=\scriptsize, align=left, anchor=east] at (-1.85,-2.3)
    {$1 = $ Status};
\node[font=\scriptsize, align=left, anchor=east] at (-1.85,-2.65)
    {$0 = $ Data};
\draw[thick] (-1.6,-2.2) -- (-1.35,-2.2) -- (-1.35,-2.75) -- (-1.6,-2.75);

% Flecha y texto: bit 8 → 1=Command / 0=Buffer
\draw[->, gray, thin] (-1.8,-3.4) -- (5.525,-0.1);
\node[font=\scriptsize, align=left, anchor=east] at (-1.85,-3.3)
    {$1 = $ Command};
\node[font=\scriptsize, align=left, anchor=east] at (-1.85,-3.65)
    {$0 = $ Buffer};
\draw[thick] (-1.6,-3.2) -- (-1.35,-3.2) -- (-1.35,-3.75) -- (-1.6,-3.75);

% Flecha y texto: bit 9 → 1=Input / 0=Output
\draw[->, gray, thin] (6.175,-0.6) -- (6.175,-1.1);
\node[font=\scriptsize, align=center] at (6.175,-1.35)
    {$1 = $ Input};
\node[font=\scriptsize, align=center] at (6.175,-1.7)
    {$0 = $ Output};

\end{tikzpicture}
\end{document}
```

---

### N15. DIAGRAMAS DE FLUJO IOT — EJEMPLOS EXTENDIDOS

#### Flujo IOT — bloque de decodificación (pasos 5–51)

> Contexto para NotebookLM: bloque inicial del flujograma IOT. Desde el paso 4 (entrada), pasa por cuatro rombos de decisión en cadena: MRI (→6), OPR (→26), INT (→INT seq), TST (→TST seq). Si TST es No, continúa al paso 70. Este bloque es el tronco de decodificación de instrucciones OPR-extendidas del SIC.

```tikz
\usetikzlibrary{shapes.geometric, arrows.meta, positioning}
\begin{document}
\begin{tikzpicture}[
    scale=0.88,
    decision/.style={diamond, draw=gray, thick, aspect=2.4,
                     inner sep=0pt, font=\small},
    jump/.style={circle, draw=gray, thick, inner sep=2pt, font=\small},
    subseq/.style={draw=gray, thick, rounded corners=4pt,
                   minimum width=1.5cm, minimum height=0.6cm, font=\small}
]

% Entrada
\node[jump] (n4) at (0,0) {4};

% Rombo MRI
\node[decision] (mri) at (2.2,0) {MRI?};
\node[jump] (n6)  at (2.2,-1.5) {6};
\node[font=\scriptsize, gray] at (2.2,-0.75) {Yes};

% Número de paso 5
\node[font=\scriptsize, gray] at (1.8, 0.35) {5};

% Rombo OPR
\node[decision] (opr) at (4.8,0) {OPR?};
\node[jump] (n26) at (4.8,-1.5) {26};
\node[font=\scriptsize, gray] at (4.8,-0.75) {Yes};
\node[font=\scriptsize, gray] at (4.1, 0.35) {25};

% Rombo INT
\node[decision] (intd) at (7.4,0) {INT?};
\node[subseq]   (intseq) at (7.4,-1.5) {INT\\seq};
\node[font=\scriptsize, gray] at (7.4,-0.75) {Yes};
\node[font=\scriptsize, gray] at (6.7, 0.35) {50};

% Rombo TST
\node[decision] (tst) at (10.0,0) {TST?};
\node[subseq]   (tstseq) at (11.6,0) {TST\\seq};
\node[font=\scriptsize, gray] at (10.8, 0.25) {Yes};
\node[font=\scriptsize, gray] at (9.3, 0.35) {51};

% Salida No de TST → paso 70
\node[font=\scriptsize, gray] at (10.0,-0.75) {No};
\node[jump] (n70) at (10.0,-1.5) {70};

% Conexiones horizontales
\draw[->, thick] (n4) -- (mri);
\draw[->, thick] (mri) -- node[above, font=\scriptsize]{No} (opr);
\draw[->, thick] (opr) -- node[above, font=\scriptsize]{No} (intd);
\draw[->, thick] (intd) -- node[above, font=\scriptsize]{No} (tst);
\draw[->, thick] (tst) -- (tstseq);

% Salidas Yes (hacia abajo)
\draw[->, thick] (mri)  -- (n6);
\draw[->, thick] (opr)  -- (n26);
\draw[->, thick] (intd) -- (intseq);
\draw[->, thick] (tst)  -- (n70);

\end{tikzpicture}
\end{document}
```

---

#### Flujo IOT — bloque TST/CSR y decodificación COMMAND (pasos 70–75)

> Contexto para NotebookLM: bloque que sigue a la decodificación inicial cuando TST es No. Pasos 70–75: cargar CSR desde IR, poner CSBUS=CSR con csrdy=1, esperar accept (bucle), luego decidir COMMAND (→Transfer) y TYPE (Output→paso 75: MD←AC). Este bloque es la inicialización del canal CS antes de la transferencia.

```tikz
\usetikzlibrary{shapes.geometric, arrows.meta, calc}
\begin{document}
\begin{tikzpicture}[
    scale=0.9,
    decision/.style={diamond, draw=gray, thick, aspect=2.2,
                     inner sep=1pt, font=\small},
    operation/.style={draw=teal, thick, minimum width=3.2cm,
                      minimum height=0.65cm, font=\small, align=center},
    jump/.style={circle, draw=gray, thick, inner sep=2pt, font=\small}
]

% Entrada desde paso 70
\node[jump] (n70in) at (0,0) {70};

% Op 70: CSR ← IR_{8:17}
\node[operation] (op70) at (0,-1.0)
    {$CSR \leftarrow IR_{8:17}$};
\node[font=\scriptsize, gray, left] at (-1.6,-1.0) {70};

% Op 71: CSBUS=CSR / csrdy=1
\node[operation] (op71) at (0,-2.2)
    {$CSBUS = CSR$\\$csrdy \leftarrow 1$};
\node[font=\scriptsize, gray, left] at (-1.6,-2.2) {71};

% Rombo accept
\node[decision] (acc) at (0,-3.6) {accept?};
\node[font=\scriptsize, gray] at (0.2,-2.85) {0};
\node[font=\scriptsize, gray] at (0.2,-4.25) {1};

% Rombo COMMAND
\node[decision] (cmd) at (0,-5.1) {COMMAND?};
\node[font=\scriptsize, gray, left]  at (-0.1,-5.85) {No};
\node[font=\scriptsize, gray, right] at (0.1,-5.85) {(Transfer)};

% Rombo TYPE
\node[decision] (typ) at (0,-6.5) {TYPE?};
\node[font=\scriptsize, gray, left]  at (-1.5,-6.5) {Output};
\node[font=\scriptsize, gray, right] at ( 1.0,-6.5) {Input};

% Op 75: MD ← AC (Output)
\node[operation] (op75) at (-2.2,-6.5)
    {$MD \leftarrow AC$};
\node[font=\scriptsize, gray, left] at (-3.8,-6.5) {75};

% Salto Input → 78 (rama derecha)
\node[jump] (n78) at (1.8,-6.5) {78};

% Conexiones verticales principales
\draw[->, thick] (n70in) -- (op70);
\draw[->, thick] (op70)  -- (op71);
\draw[->, thick] (op71)  -- (acc);
\draw[->, thick] (acc)   -- node[right, font=\scriptsize]{1} (cmd);
\draw[->, thick] (cmd)   -- (typ);
\draw[->, thick] (typ)   -- (op75);
\draw[->, thick] (typ)   -- (n78);

% Bucle No de accept (vuelve al rombo)
\draw[thick] (acc) -- node[above, font=\scriptsize]{0} ++(-1.6,0)
    -- ++(0,1.45) -- (0,-2.15);

% Salto COMMAND Yes → (72)
\node[jump] (n72) at (2.2,-5.1) {72};
\draw[->, thick] (cmd) -- node[above, font=\scriptsize]{Yes} (n72);

\end{tikzpicture}
\end{document}
```

---

#### Flujo IOT — bloque Output (pasos 75–77)

> Contexto para NotebookLM: rama Output del flujograma IOT. Paso 75: MD←AC. Paso 76: bucle de espera ready. Paso 77: IOBUS=MD / datavalid←1, luego esperar accept. Si accept=1 → volver a paso 24. Patrón típico de transferencia de salida hacia dispositivo.

```tikz
\usetikzlibrary{shapes.geometric, arrows.meta, calc}
\begin{document}
\begin{tikzpicture}[
    scale=0.9,
    decision/.style={diamond, draw=gray, thick, aspect=2.2,
                     inner sep=1pt, font=\small},
    operation/.style={draw=teal, thick, minimum width=3.2cm,
                      minimum height=0.65cm, font=\small, align=center},
    jump/.style={circle, draw=gray, thick, inner sep=2pt, font=\small}
]

% Op 75
\node[operation] (op75) at (0,0) {$MD \leftarrow AC$};
\node[font=\scriptsize, gray, left] at (-1.6,0) {75};

% Rombo ready (bucle)
\node[decision] (rdy) at (0,-1.4) {ready?};

% Op 77: IOBUS=MD / datavalid←1
\node[operation] (op77) at (0,-3.0)
    {$IOBUS = MD$\\$datavalid \leftarrow 1$};
\node[font=\scriptsize, gray, left] at (-1.6,-3.0) {77};

% Rombo accept
\node[decision] (acc) at (0,-4.5) {accept?};

% Salto accept=1 → (24)
\node[jump] (n24) at (0,-6.0) {24};

% Conexiones
\draw[->, thick] (op75) -- (rdy);
\draw[->, thick] (rdy)  -- node[right, font=\scriptsize]{Yes} (op77);
\draw[->, thick] (op77) -- (acc);
\draw[->, thick] (acc)  -- node[right, font=\scriptsize]{Yes} (n24);

% Bucle No de ready
\draw[thick] (rdy) -- node[above, font=\scriptsize]{No} ++(-1.8,0)
    -- ++(0,1.45) -- (0,0.05);

% Bucle No de accept
\draw[thick] (acc) -- node[above, font=\scriptsize]{No} ++(1.8,0)
    -- ++(0,1.55) -- (0,-2.95);

\end{tikzpicture}
\end{document}
```

---

#### Flujo IOT — bloque Input / BUFFER / DATA (pasos 72–84)

> Contexto para NotebookLM: rama compleja del flujograma IOT. Desde paso 72 (COMMAND) y 73 (BUFFER). Rama Input (paso 78): espera ready=1, luego pregunta DATA: si Yes → MD←IOBUS / CSR←CSBUS, accept=1, luego chequea datavalid (bucle), DATA nuevamente, SKIP, PC←INC(PC). Si No → AC←MD (paso 82) y vuelve a 24. Patrón de transferencia de entrada con buffer y skip.

```tikz
\usetikzlibrary{shapes.geometric, arrows.meta, calc}
\begin{document}
\begin{tikzpicture}[
    scale=0.82,
    decision/.style={diamond, draw=gray, thick, aspect=2.2,
                     inner sep=1pt, font=\small},
    operation/.style={draw=teal, thick, minimum width=3.0cm,
                      minimum height=0.65cm, font=\small, align=center},
    jump/.style={circle, draw=gray, thick, inner sep=2pt, font=\small}
]

% Entradas
\node[jump] (n72) at (-2, 0)  {72};
\node[jump] (n73) at ( 2, 0)  {73};
\node[jump] (n85) at ( 2, 1.2) {85};

% Rombo COMMAND (72)
\node[font=\scriptsize, gray, above] at (-2,0.5) {COMMAND};

% Rombo BUFFER
\node[font=\small, draw=gray, thick,
      diamond, aspect=2.2, inner sep=1pt] (buf) at (0,-1.2) {BUFFER?};
\draw[->, thick] (n72) -- (buf);
\draw[->, thick] (n73) -- (buf);
\draw[->, thick] (n85) -- (n73);

% Salto BUFFER=Yes → (85) (vuelve arriba)
\node[font=\scriptsize, gray, right] at (0.2,-0.5) {Yes};
% flecha vuelve a n85
\draw[->, thick] (buf) -- ++(1.8,0) node[right, font=\scriptsize]{Yes}
    -- ++(0,2.5) -- (n85);

% Op 78: ready=1 (Input, BUFFER=No)
\node[operation] (op78) at (0,-2.8) {$ready \leftarrow 1$};
\node[font=\scriptsize, gray, left] at (-1.6,-2.8) {78};
\draw[->, thick] (buf) -- node[left, font=\scriptsize]{No (Input)} (op78);

% Rombo datavalid (bucle espera)
\node[font=\small, draw=gray, thick,
      diamond, aspect=2.2, inner sep=1pt] (dvw) at (0,-4.2) {datavalid?};
\draw[->, thick] (op78) -- (dvw);

% Rombo DATA (79 rama)
\node[font=\small, draw=gray, thick,
      diamond, aspect=2.2, inner sep=1pt] (dat1) at (0,-5.8) {DATA?};
\draw[->, thick] (dvw) -- node[right, font=\scriptsize]{Yes} (dat1);

% Bucle No de datavalid → vuelve
\draw[thick] (dvw) -- node[above, font=\scriptsize]{No} ++(-2.0,0)
    -- ++(0,1.45) -- (0,-2.75);

% Op 79 Yes: MD←IOBUS y CSR←CSBUS (simultáneo)
\node[operation] (op79) at (-2.2,-7.4)
    {$MD \leftarrow IOBUS$\\$CSR \leftarrow CSBUS$};
\node[font=\scriptsize, gray, left] at (-3.8,-7.4) {79};
\draw[->, thick] (dat1) -- node[left, font=\scriptsize]{Yes} (op79);

% accept=1
\node[operation] (accop) at (-2.2,-8.8) {$accept \leftarrow 1$};
\draw[->, thick] (op79) -- (accop);

% Rombo datavalid (80)
\node[font=\small, draw=gray, thick,
      diamond, aspect=2.2, inner sep=1pt] (dv80) at (-2.2,-10.2) {datavalid?};
\draw[->, thick] (accop) -- (dv80);
\node[font=\scriptsize, gray, left] at (-3.4,-10.2) {80};

% Rombo DATA (81)
\node[font=\small, draw=gray, thick,
      diamond, aspect=2.2, inner sep=1pt] (dat81) at (-2.2,-11.6) {DATA?};
\draw[->, thick] (dv80) -- node[right, font=\scriptsize]{No} (dat81);
\node[font=\scriptsize, gray, left] at (-3.4,-11.6) {81};

% Bucle Yes de dv80 → vuelve a op79
\draw[thick] (dv80) -- node[above, font=\scriptsize]{Yes} ++(-2.0,0)
    -- ++(0,2.9) -- (-2.2,-7.35);

% Rombo SKIP (83)
\node[font=\small, draw=gray, thick,
      diamond, aspect=2.2, inner sep=1pt] (sk) at (-2.2,-13.0) {SKIP?};
\draw[->, thick] (dat81) -- node[right, font=\scriptsize]{No} (sk);
\node[font=\scriptsize, gray, left] at (-3.4,-13.0) {83};

% Op 84: PC←INC(PC)
\node[operation] (op84) at (-2.2,-14.4) {$PC \leftarrow INC(PC)$};
\draw[->, thick] (sk) -- node[right, font=\scriptsize]{Yes} (op84);
\node[font=\scriptsize, gray, left] at (-3.8,-14.4) {84};

% Salida (24) desde 84
\node[jump] (n24a) at (-2.2,-15.6) {24};
\draw[->, thick] (op84) -- (n24a);

% SKIP No también → (24)
\node[jump] (n24b) at (0,-14.4) {24};
\draw[->, thick] (sk) -- node[above, font=\scriptsize]{No} (n24b);

% DATA 81 Yes → AC←MD (82)
\node[operation] (op82) at (1.5,-11.6) {$AC \leftarrow MD$};
\draw[->, thick] (dat81) -- node[above, font=\scriptsize]{Yes} (op82);
\node[font=\scriptsize, gray, right] at (3.1,-11.6) {82};

% AC←MD → (24)
\node[jump] (n24c) at (1.5,-13.0) {24};
\draw[->, thick] (op82) -- (n24c);

% DATA 79 No → AC←MD también (rama corta)
\node[operation] (op82b) at (2.2,-5.8) {$AC \leftarrow MD$};
\draw[->, thick] (dat1) -- node[above, font=\scriptsize]{No} (op82b);
\node[jump] (n24d) at (2.2,-7.2) {24};
\draw[->, thick] (op82b) -- (n24d);

\end{tikzpicture}
\end{document}
```

---

---

#### Flujo DMA/Buffer — secuencia completa (pasos 90–111)

> Contexto para NotebookLM: flujograma del módulo de transferencia DMA con buffer. Entrada desde paso (2). Paso 90: bucle sobre `scan=1`. Paso 91: `CC←INC(CC)`. Pasos 92–95: fetch buffer word count a BWC. Pasos 95–96: fetch final buffer address a MD. Pasos 97–98: form current buffer address. Paso 99: bifurcación Input (1) / Output (0). Rama Output (100–102): fetch word from memory → transit via IOBUS, clear. Rama Input (103–106): obtain word via IOBUS → store, clear bus. Paso 107: buffer done? — Yes → 108 (`bufend=1`); No → 109 (`BUFRDY=1`) → 110–111 (store word count) → vuelve a (2). Fuente: Hill & Peterson Digital Systems 2ª ed., Fig. 11-13.

```tikz
\usetikzlibrary{shapes.geometric, arrows.meta, positioning, calc}
\begin{document}
\begin{tikzpicture}[
    scale=0.82,
    decision/.style={diamond, draw=gray, thick, aspect=2.4,
                     inner sep=0pt, font=\small},
    operation/.style={draw=teal, thick, minimum width=3.0cm,
                      minimum height=0.7cm, font=\small, align=center},
    terminal/.style={draw=orange, thick, minimum width=2.6cm,
                     minimum height=0.7cm, font=\small, align=center},
    jump/.style={circle, draw=gray, thick, inner sep=3pt, font=\small},
    conn/.style={circle, draw=gray, fill=gray, inner sep=2pt}
]

% ---- ENTRADA ----
\node[font=\small, above] (from2label) at (0,0.4) {From (2)};
\draw[->, thick] (0,0.4) -- (0,0);

% ---- PASO 90: rombo scan=1 ----
\node[decision] (scan) at (0,-1.0) {\textit{scan}: 1};
\node[font=\scriptsize, gray, left] at (-1.4,-0.4) {90};

% Rama distinto → paso 91 (derecha)
\node[operation] (op91) at (3.8,-1.0) {$CC \leftarrow INC(CC)$};
\node[font=\scriptsize, gray] at (3.8,-0.3) {91};
\draw[->, thick] (scan) -- node[above, font=\scriptsize]{$\neq$} (op91);
% Bucle: 91 vuelve a scan por arriba
\draw[->, thick] (op91.north) -- ++(0,0.7) -- ++(-3.8,0) -- (scan.north);

% ---- PASOS 92–95: Fetch buffer word count a BWC ----
\node[operation] (op9295) at (0,-3.0)
    {Fetch buffer word count\\to \textit{BWC}};
\node[font=\scriptsize, gray, left] at (-1.7,-3.0) {92--95};
\draw[->, thick] (scan.south) -- (op9295.north);

% ---- PASOS 95–96: Fetch final buffer address a MD ----
\node[operation] (op9596) at (0,-4.9)
    {Fetch final\\buffer address\\to \textit{MD}};
\node[font=\scriptsize, gray, left] at (-1.7,-4.9) {95--96};
\draw[->, thick] (op9295) -- (op9596);

% ---- PASOS 97–98: Form current buffer address ----
\node[operation] (op9798) at (0,-6.8)
    {Form current\\buffer address};
\node[font=\scriptsize, gray, left] at (-1.7,-6.8) {97--98};
\draw[->, thick] (op9596) -- (op9798);

% ---- PASO 99: rombo 1 or 0? ----
\node[decision] (inout) at (0,-8.4) {1 or 0?};
\node[font=\scriptsize, gray, left] at (-0.2,-7.7) {99};
\node[font=\scriptsize, gray, left]  at (-0.3,-9.2) {Input};
\node[font=\scriptsize, gray, right] at ( 0.3,-9.2) {Output};
\draw[->, thick] (op9798) -- (inout);

% ---- RAMA OUTPUT (derecha) ----
\node[operation] (op100) at (3.4,-8.4)
    {Fetch word\\from memory};
\node[font=\scriptsize, gray] at (3.4,-7.7) {100};
\draw[->, thick] (inout.east) -- node[above, font=\scriptsize]{0} (op100.west);

\node[operation] (op101) at (3.4,-10.3)
    {Transit via\\\textit{IOBUS} clear};
\node[font=\scriptsize, gray, right] at (5.0,-10.3) {101--102};
\draw[->, thick] (op100) -- (op101);

% ---- RAMA INPUT (izquierda) ----
\node[operation] (op103) at (-3.4,-8.4)
    {Obtain word\\via \textit{IOBUS}};
\node[font=\scriptsize, gray] at (-3.4,-7.7) {103--104};
\draw[->, thick] (inout.west) -- node[above, font=\scriptsize]{1} (op103.east);

\node[operation] (op105) at (-3.4,-10.3)
    {Store,\\clear bus};
\node[font=\scriptsize, gray, left] at (-5.0,-10.3) {105--106};
\draw[->, thick] (op103) -- (op105);

% ---- CONECTOR UNIÓN RAMAS ----
\node[conn] (join) at (0,-12.0) {};
\draw[thick] (op101.south) -- ++(0,-0.6) -| (join);
\draw[thick] (op105.south) -- ++(0,-0.6) -| (join);
\draw[->, thick] (join) -- ++(0,-0.4);

% ---- PASO 107: Buffer done? ----
\node[decision] (bufdone) at (0,-13.3) {Buffer\\done?};
\node[font=\scriptsize, gray, left] at (-0.2,-12.5) {107};
\draw[->, thick] (join) -- (bufdone);

% ---- RAMA YES → 108: bufend=1 ----
\node[terminal] (op108) at (-3.4,-13.3) {\textit{bufend} = 1};
\node[font=\scriptsize, gray] at (-3.4,-12.6) {108};
\draw[->, thick] (bufdone.west) -- node[above, font=\scriptsize]{Yes} (op108.east);

% ---- RAMA NO → 109: BUFRDY=1 ----
\node[terminal] (op109) at (3.4,-13.3) {\textit{BUFRDY} = 1};
\node[font=\scriptsize, gray] at (3.4,-12.6) {109};
\draw[->, thick] (bufdone.east) -- node[above, font=\scriptsize]{No} (op109.west);

% 110–111: Store word count
\node[operation] (op110) at (3.4,-15.0)
    {Store\\word count};
\node[font=\scriptsize, gray, right] at (5.0,-15.0) {110--111};
\draw[->, thick] (op109) -- (op110);

% ---- CONECTOR FINAL → (2) ----
\node[conn] (join2) at (0,-16.6) {};
\draw[thick] (op108.south) -- ++(0,-1.7) -| (join2);
\draw[thick] (op110.south) -- ++(0,-0.9) -| (join2);
\draw[->, thick] (join2) -- ++(0,-0.4);
\node[font=\small, below] at (0,-17.1) {(2)};

\end{tikzpicture}
\end{document}
```

%%
# galaxy-links
[[_app/notebooklm/guides/ETN607/ETN607_TikzJax.md]]
[[_app/notebooklm/guides/ETN825/ETN825_AHPL.md]]
%%