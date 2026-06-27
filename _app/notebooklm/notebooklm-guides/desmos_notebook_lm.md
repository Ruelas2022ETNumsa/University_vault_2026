---
title: Desmos — Guía unificada para Obsidian
galaxy_body: beacon
scope: vault
tool: desmos-plugin
audience:
  - usuario
  - notebooklm
  - claude
tags:
  - beacon
  - desmos
  - infraestructura
date_created: 2026-01-01
date_updated: 2026-06-05
status: activo
---

# 📈 GUÍA UNIFICADA DE DESMOS PARA OBSIDIAN

> Plugin: `obsidian-desmos` — renderiza gráficas de [desmos.com](https://www.desmos.com/calculator) directamente en tus notas.
> Este documento tiene tres secciones según quién lo usa: **Usuario**, **NotebookLM** y **Claude**.

---

# 🤖 SECCIÓN NOTEBOOKLM

Instrucciones para que NotebookLM genere bloques Desmos correctos listos para copiar en Obsidian. Cuando el usuario pida una gráfica, responder con un bloque de código — no con imagen ni enlace.

---

## N1. REGLA CRÍTICA — EL `---` ES SIEMPRE OBLIGATORIO

**Sin `---` el plugin no renderiza nada.** No importa si hay configuración o no.

❌ Incorrecto:

```desmos-graph
width=500; height=500;
y=x^2|BLUE
```

✅ Correcto:

```desmos-graph
width=500; height=500;
---
y=x^2|BLUE
```

✅ Sin configuración, el `---` igual va:

```desmos-graph
---
y=x^2|BLUE
```

---

## N2. ESTRUCTURA OBLIGATORIA

```desmos-graph
[parámetros terminados en ;]
---
[ecuaciones con modificadores]
```

---

## N3. PARÁMETROS DE CONFIGURACIÓN

| Parámetro | Qué hace           | Valor típico |
| --------- | ------------------ | ------------ |
| `left`    | Límite izquierdo x | `-5`         |
| `right`   | Límite derecho x   | `5`          |
| `bottom`  | Límite inferior y  | `-3`         |
| `top`     | Límite superior y  | `3`          |
| `width`   | Ancho en px        | ver tabla    |
| `height`  | Alto en px         | ver tabla    |

**Tamaños estándar confirmados:**

| Tipo | width | height | Uso |
|------|-------|--------|-----|
| Pequeño | 300 | 200 | Rectas numéricas, intervalos, un punto |
| Mediano | 400 | 350 | Funciones, parábolas, trigonométricas |
| Grande | 550 | 450 | Múltiples curvas, etiquetas, regiones |
| Cornell | 320 | 250 | Máximo dentro de bloque multi-column |
| Plano cuadrado | 500 | 500 | Probabilidad, geometría |

Para rectas numéricas usar ratio horizontal (3:1). Para funciones estándar ratio 4:3.

---

## N4. SINTAXIS DE ECUACIONES

| Matemática   | Código                |
| ------------ | ------------------- |
| y = x²       | `y=x^2`             |
| y = √x       | `x=y^2` + `y>=0`    |
| y = 1/x      | `y=1/x`             |
| y = eˣ       | `y=e^x`             |
| y = sin(x)   | `y=\sin(x)`         |
| x² + y² = r² | `x^2+y^2=r^2`       |

---

## N5. MODIFICADORES Y COLORES

```desmos-graph
|#hex                                            → color (SIEMPRE usar hex)
|SOLID, |DASHED, |DOTTED                         → estilo de línea
|0<=x<=1                                         → restricción de dominio
|hidden                                          → ocultar curva
```

### ⚠️ Regla de color: SIEMPRE hex, NUNCA nombres en mayúsculas

El plugin acepta nombres (`RED`, `BLUE`, etc.) pero producen colores saturados y duros. Usar siempre hex.

### Paleta para curvas y líneas

```desmos-graph
#c74440   → rojo medio      (curva principal / frontera)
#2d70b3   → azul medio      (curva secundaria)
#388c46   → verde medio     (curva terciaria)
#fa7e19   → naranja         (destaque)
#6042a6   → morado          (evento / probabilidad)
#000000   → negro           (ejes, bordes, auxiliares)
```

### Paleta para rellenos (áreas sombreadas)

```desmos-graph
#a5d8ff   → azul claro      (región / soporte principal)
#b2f2bb   → verde claro     (región secundaria)
#ffd8a8   → naranja claro   (región de advertencia)
#ff7b7b   → rojo claro      (región de evento)
#d0bfff   → morado claro    (región auxiliar)
```

> Los hex de curvas son los colores internos de Desmos web. Los de rellenos son sus versiones pastel.

---

## N6. ÁREAS SOMBREADAS

Usar inecuaciones con todas las condiciones en **una sola línea**:

```desmos-graph
y<3-x|y>x-3|x>=-4|x<=2|#a5d8ff
```


```desmos-graph
left=-0.5; right=5.5;
bottom=-1; top=24;
---
x<y<=x^2 \{2<=x<=4\}

y=x^2
y=x
```


### ⚠️ Rectángulos sombreados

Para sombrear una región rectangular incluir SIEMPRE las cuatro restricciones en una sola línea:

```desmos-graph
x>=0|x<=1|y>=0|y<=1|#a5d8ff
```

No usar `y<=1|y>=0` sin las restricciones de x — Desmos extenderá el relleno fuera del rectángulo.

---

## N7. PUNTOS

```desmos-graph
(1,2)|label:(1,2)|BLACK
(1,2)|OPEN|label:(1,2)|BLACK
```

### ⚠️ Fracciones en etiquetas — solo slash

`\frac{}{}` no renderiza en `label:` — aparece el texto literal. Usar siempre slash:

✅ `(3,0)|OPEN|label:(d-b)/(a-c)|#ff7b7b`
❌ `(3,0)|OPEN|label:\frac{d-b}{a-c}|#ff7b7b`

---

## N8. VALOR ABSOLUTO

El plugin soporta `\abs()` para valor absoluto simple. Usar `\abs()` es la forma más directa.

### Forma con `\abs()` — primera opción:

```desmos-graph
y=\abs(x)
y=\abs(2x-3)
y=\abs(x^{2}-4x+3)
y=\abs(x)\abs(x-4)
y=\abs(\abs(x^{2}-4)-4)
```

### Forma por tramos — cuando `\abs()` no es suficiente (regiones sombreadas):

Para sombrear regiones bajo y=|x|, `\abs()` no funciona en condiciones de relleno. Usar tramos:

```desmos-graph
y=x \{x>=0\}|#2d70b3
y=-x \{x<=0\}|#2d70b3
y=2|#000000|DASHED
-2<=x<=2|y<=2|y>=0|#a5d8ff
```

### ⚠️ Nunca en condiciones de relleno:

```desmos-graph
y=|x|
-|y|<=x<=|y|
y<=abs(x)
```

| Intención | Correcto (✅) | Incorrecto (❌) |
|-----------|--------------|----------------|
| Curva y=\|x\| | `y=\abs(x)` | `y=\|x\|` |
| Curva compuesta | `y=\abs(x^{2}-4x+3)` | `y=\|x^2-4x+3\|` |
| Región bajo y=\|x\| | tramos con cotas numéricas | `-\|y\|<=x<=\|y\|` |

---

## N9. RAÍZ CUADRADA — TRES FORMAS VÁLIDAS

El plugin soporta tres formas para $y = \sqrt{x}$. Usar en orden de preferencia:

**Forma 1 — primera opción:**
```desmos-graph
y=x^{1/2}|x>=0|#2d70b3
```

**Forma 2 — segunda opción:**
```desmos-graph
y=\sqrt{x}|x>=0|#2d70b3
```

**Forma 3 — tercera opción (relación implícita):**
```desmos-graph
x=y^2
y>=0
```

### ⚠️ Formas que NO funcionan — nunca usar:

```desmos-graph
y=sqrt(x)
y=\sqrt(x)
y=sqrt{x}
```

---

## N10. EJEMPLOS COMPLETOS

### Función simple

```desmos-graph
left=-4; right=4; bottom=-2; top=6;
width=500; height=400;
---
y=x^2|#2d70b3
```

### Región triangular (probabilidad)

```desmos-graph
left=-0.2; right=1.5; bottom=-0.2; top=2.5;
width=500; height=500;
---
y=x|0<=x<=1|#c74440|SOLID
y=2-x|0<=x<=1|#2d70b3|SOLID
x=0|0<=y<=2|#000000|DASHED
y<2-x|y>x|x>=0|x<=1|#a5d8ff
(0,0)|label:(0,0)|#000000
(1,1)|label:(1,1)|#c74440
(0,2)|label:(0,2)|#2d70b3
```

### Rectángulo sombreado (soporte cuadrado)

```desmos-graph
left=-0.2; right=1.3; bottom=-0.2; top=1.3;
width=500; height=500;
---
x>=0|x<=1|y>=0|y<=1|#a5d8ff
x=1|0<=y<=1|#2d70b3|DASHED
y=1|0<=x<=1|#2d70b3|DASHED
(0,0)|label:(0,0)|#000000
(1,1)|label:(1,1)|#000000
```

### Región entre curva y recta

```desmos-graph
left=-0.1; right=1.3; bottom=-0.1; top=1.3;
width=500; height=500;
---
y=x|0<=x<=1|#c74440|SOLID
y=\sqrt{x}|0<=x<=1|#388c46|SOLID
y<\sqrt{x}|y>x|0<=x<=1|#b2f2bb
(0,0)|label:(0,0)|#000000
(1,1)|label:(1,1)|#000000
```

### Valor absoluto con región sombreada

```desmos-graph
left=-5; right=5; bottom=-1; top=5;
width=500; height=300;
---
y=x \{x>=0\}|#2d70b3
y=-x \{x<=0\}|#2d70b3
y=2|#000000|DASHED
-2<=x<=2|y<=2|y>=0|#a5d8ff
(-2,2)|label:(-a,a)|#c74440
(2,2)|label:(a,a)|#c74440
```

---

## N11. CHECKLIST ANTES DE RESPONDER

Antes de entregar un bloque Desmos verificar:
- [ ] ¿Tiene `---`?
- [ ] ¿Todos los parámetros terminan en `;`?
- [ ] ¿Sin espacios alrededor de `|`?
- [ ] ¿Sin llaves `{}` en restricciones?
- [ ] ¿Sin comentarios `//`?
- [ ] ¿Rectángulos sombreados con las 4 condiciones `x>=|x<=|y>=|y<=`?
- [ ] ¿Colores de curvas en hex (`#c74440`, `#2d70b3`, etc.) y NO nombres en mayúsculas?
- [ ] ¿Rellenos con hex pastel (`#a5d8ff`, `#ff7b7b`, etc.)?
- [ ] ¿Funciones por tramos usan `y=k \{a<x<b\}` y NO `{a<x<b: k}`?
- [ ] ¿Sin `y=|x|`, `y=abs(x)` ni `|x|` en condiciones de relleno?
- [ ] ¿Raíz cuadrada usa `x=y^2` + `y>=0` como primera opción — NO `y=sqrt(x)` ni `y=\sqrt(x)`?

---

## N12. FUNCIONES POR TRAMOS Y VALORES EN INTERVALOS

### ⚠️ Sintaxis web `{intervalo: valor}` NO funciona en el plugin

Desmos web acepta `{a<x<b: 0.2}` para definir una función que vale 0.2 en ese intervalo. **El plugin de Obsidian no soporta esta sintaxis** — el bloque se renderiza vacío o no renderiza.

**Sintaxis correcta para el plugin:** usar `y=valor \{condición\}` con las llaves escapadas:

```desmos-graph
y=0.10 \{a<x<b\}|#2d70b3
```

Las llaves `\{...\}` actúan como restricción de dominio sobre la línea `y=valor`.

### Ejemplo completo — función escalonada con variables

Este bloque renderiza correctamente:

```desmos-graph
left=-1; right=7; bottom=-0.5; top=0.6;
width=600; height=180;
---
y=0

a=1
b=4
c=6

(a,0)|label:a
(b,0)|label:b
(c,0)|label:c

y=0.10 \{a<x<b\}|#2d70b3
y=0.20 \{b<x<c\}|#2d70b3
y=0.35 \{a<x<c\}|#c74440
```

Este bloque **no renderiza** (sintaxis web):

```desmos-graph
left=-2; right=8; bottom=-1; top=1;
width=500; height=100;
---
y=0|#000000
a=1
b=4
c=6
(a,0)|label:a|#2d70b3
(b,0)|label:b|#2d70b3
(c,0)|label:c|#2d70b3
{a<x<b: 0.1}|#2d70b3
{b<x<c: 0.1}|#2d70b3
{a<x<c: 0.3}|label:Transitividad|#c74440
```

### Patrón general

| Intención                             | Sintaxis plugin (✅)                         | Sintaxis web (❌)    |
| ------------------------------------- | ------------------------------------------- | ------------------- |
| Valor fijo en intervalo               | `y=k \{a<x<b\}\|#hex`                       | `{a<x<b: k}`        |
| Función en intervalo                  | `y=f(x) \{a<x<b\}\|#hex`                    | `{a<x<b: f(x)}`     |
| Variable definida, valor en intervalo | `y=k \{a<x<b\}\|#hex` con `a=1` etc. arriba | igual — no funciona |

### Nota sobre etiquetas en funciones por tramos

`label:` **no se puede poner en una línea de función** — solo funciona en puntos. Para etiquetar un tramo, agregar un punto con label en el centro del intervalo:

```desmos-graph
y=0.10 \{a<x<b\}|#2d70b3
(2.5, 0.10)|label:P(A)|#2d70b3
```

---

## N13. EJEMPLOS POR TIPO DE FUNCIÓN (Capítulo I)

Todos confirmados y renderizados correctamente.

**Reglas críticas de sintaxis:**
- Potencias siempre con `{}`: `x^{3/2}` nunca `x^(3/2)`
- Palabras reservadas con `\`: `\cos`, `\sin`, `\ln`, `\frac{}{}`
- Funciones especiales: `\abs()`, `\floor()`, `\operatorname{sgn}()`, `\operatorname{mod}()`

### Polinomios

```desmos-graph
width=300; height=200;
left=-3; right=3; bottom=-2; top=5;
---
y=x^4-4x^2+3
```

```desmos-graph
width=300; height=200;
left=-3; right=3; bottom=-4; top=4;
---
y=x^3-3x
```

### Potenciales generalizadas

```desmos-graph
width=300; height=200;
---
y=x^{3/2}
```

```desmos-graph
width=300; height=200;
left=-0.5; right=7; bottom=-0.5; top=5;
---
y=x^{-1/2}
```

```desmos-graph
width=300; height=200;
left=-10; right=10; bottom=-0.5; top=5;
---
y=x^{2/3}
```

```desmos-graph
width=300; height=200;
left=-5; right=5; bottom=-0.5; top=5;
---
y=x^{-2/3}
```

### Exponenciales y logarítmicas

```desmos-graph
width=300; height=200;
left=-5; right=3; bottom=-0.5; top=5;
---
y=2^x
```

```desmos-graph
width=300; height=200;
left=-5; right=3; bottom=-0.5; top=5;
---
y=e^x
```

```desmos-graph
width=300; height=200;
left=-0.5; right=3; bottom=-2; top=0.5;
---
y=\log(x)
```

```desmos-graph
width=300; height=200;
left=-0.5; right=3; bottom=-3; top=2;
---
y=\ln(x)
```

### Trigonométricas

```desmos-graph
width=300; height=200;
left=-3.14; right=3.14; bottom=-2; top=2;
---
y=\sin(x)
```

```desmos-graph
width=300; height=200;
left=-3.14; right=3.14; bottom=-2; top=2;
---
y=\cos(x)
```

```desmos-graph
width=400; height=350;
---
y=\tan(x)
```

### Trigonométricas inversas

```desmos-graph
left=-3; right=3; bottom=-3.5; top=3.5;
width=400; height=350;
---
y=\sin(x)|-3<=x<=3|#5E81AC|DASHED
y=x|-3<=x<=3|#777777|DASHED
y=-\arcsin(x)-3.1416|-1<=x<=1|#A65C59|dashed
y=-\arcsin(x)+3.1416|-1<=x<=1|#A65C59|dashed
y=\arcsin(x)|-1<=x<=1|#D97706|solid
(1,3.1416/2)|label:(1,pi/2)|#D97706|cross
(-1,-3.1416/2)|label:-(1,pi/2)|#D97706|cross
```

```desmos-graph
left=-3; right=3; bottom=-3.5; top=3.5;
width=400; height=350;
---
y=\cos(x)|-3<=x<=3|#5E81AC|DASHED
y=x|-3<=x<=3|#777777|DASHED
y=\arccos(x)|-1<=x<=1|#D97706|SOLID
y=-\arccos(x)|-1<=x<=1|#A65C59|DASHED
(1,0)|label:(1,0)|#D97706|cross
(0,1.5708)|label:(0,pi/2)|#D97706|cross
(-1,3.1416)|label:(-1,pi)|#D97706|cross
```

```desmos-graph
left=-3; right=3; bottom=-3; top=3;
width=400; height=350;
---
y=\tan(x)|-1.55<=x<=1.55|#5E81AC|DASHED
y=x|-7<=x<=7|#777777|DASHED
y=\arctan(x)|-7<=x<=7|#D97706|SOLID
x=-1.5708|-7<=y<=7|#5E81AC|DASHED
x=1.5708|-7<=y<=7|#5E81AC|DASHED
y=-1.5708|-7<=x<=7|#A65C59|DASHED
y=1.5708|-7<=x<=7|#A65C59|DASHED
(0,0)|label:(0,0)|#D97706|cross
```

### Hiperbólicas

```desmos-graph
width=300; height=200;
left=-2; right=2; bottom=-2; top=2;
---
y=\sinh(x)
```

```desmos-graph
width=300; height=200;
left=-2; right=2; bottom=-0.5; top=4;
---
y=\cosh(x)|#D97706
(0,1)|label:(0,1)|#D97706|cross
```

### Valor absoluto (`\abs()`)

```desmos-graph
width=300; height=200;
left=-2; right=2; bottom=-0.5; top=2;
---
y=\abs(x)
```

```desmos-graph
width=300; height=200;
left=-1; right=4; bottom=-0.5; top=4;
---
y=\abs(2x-3)
```

```desmos-graph
width=300; height=200;
left=-1; right=5; bottom=-0.5; top=3;
---
y=\abs(x^{2}-4x+3)
```

```desmos-graph
width=300; height=200;
left=-5; right=5; bottom=-0.5; top=6;
---
y=\abs(\abs(x^{2}-4)-4)
```

### Parte entera (`\floor()`)

```desmos-graph
width=300; height=200;
left=-4; right=4; bottom=-4; top=4;
---
y=\floor(x)
```

### Función distancia (`\operatorname{mod}`)

```desmos-graph
width=300; height=200;
left=-2; right=2; bottom=-0.5; top=1;
---
y=\min(\operatorname{mod}(x,1),1-\operatorname{mod}(x,1))
```

### Función signo

Forma directa (Desmos puede agregar segmentos verticales en discontinuidades — no son parte de la función matemática):

```desmos-graph
width=300; height=200;
left=-2; right=2; bottom=-2; top=2;
---
y=\operatorname{sgn}(x)|#D97706
(0,-1)|#D97706|open
(0,1)|#D97706|open
```

Alternativa gráficamente correcta (por tramos, sin segmentos verticales):

```desmos-graph
width=300; height=200;
left=-3; right=3; bottom=-2; top=2;
---
y=1|-3<=x<-2|#D97706
y=-1|-2<x<-1|#D97706
y=1|-1<x<1|#D97706
y=-1|1<x<2|#D97706
y=1|2<x<=3|#D97706
(-2,0)|label:(-2,0)|#D97706
(-1,0)|label:(-1,0)|#D97706
(1,0)|label:(1,0)|#D97706
(2,0)|label:(2,0)|#D97706
(-2,1)|#D97706|open
(-2,-1)|#D97706|open
(-1,1)|#D97706|open
(-1,-1)|#D97706|open
(1,1)|#D97706|open
(1,-1)|#D97706|open
(2,1)|#D97706|open
(2,-1)|#D97706|open
```

### Función escalón y por tramos

```desmos-graph
width=300; height=200;
left=-2; right=2; bottom=-1; top=2;
---
y=0|-2<=x<0|#D97706
y=1|0<=x<=2|#D97706
(0,0)|#D97706|open
(0,1)|label:(0,1)|#D97706
```

```desmos-graph
width=320; height=250;
left=-3; right=10; bottom=-2; top=15;
---
y=x|-3<=x<0|#D97706
y=3x|0<=x<4|#D97706
y=-3x+24|4<=x<8|#D97706
y=0|8<=x<=10|#D97706
(0,0)|label:(0,0)|#D97706
(4,12)|label:(4,12)|#D97706
(8,0)|label:(8,0)|#D97706
(0,0)|#D97706|open
(4,12)|#D97706|open
(8,0)|#D97706|open
```

%%
galaxy-links
[[_galaxy-system]]
[[_note-system]]
%%
