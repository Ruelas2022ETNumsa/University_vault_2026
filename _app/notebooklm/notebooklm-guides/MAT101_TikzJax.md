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
date_updated: 2026-06-30
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

```
\begin{tikzpicture}[scale=1.2]         → escala el dibujo completo
\begin{axis}[width=8cm, height=6cm]    → tamaño fijo en pgfplots
```

Referencia rápida:
- Diagramas de conjuntos/composición: `scale=1` a `1.5`
- Funciones con detalle (parábolas, trigonométricas con puntos etiquetados): `scale=1.2` a `2`
- Gráficas pgfplots: `width=8cm; height=6cm;` como punto de partida

---

### N7. PALETA DE COLORES

Los hex de abajo son los mismos usados en `MAT101_desmos.md`, para mantener consistencia visual entre ambas herramientas. TikZ no reconoce estos hex directamente — hay que declararlos con `xcolor`:

```
\usepackage{xcolor}
\definecolor{curvaPpal}{HTML}{005F73}
...
\draw[thick, curvaPpal] ...
```

Alternativa más simple — nombres estándar de TikZ (ya usados en los ejemplos existentes de T1): `teal`, `orange`, `violet`, `purple`, `olive`, `gray`, `red`. Válidos cuando no hace falta coincidencia exacta de color con Desmos.

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

-xxx




-xxx

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
