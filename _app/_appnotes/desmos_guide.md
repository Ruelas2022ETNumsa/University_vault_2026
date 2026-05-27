---
title: "Desmos — Guía unificada para Obsidian"
galaxy_body: beacon
scope: vault
tool: desmos-plugin
audience: [usuario, notebooklm, claude]
tags: [beacon, desmos, infraestructura]
date_created: 2026-01-01
status: activo
---

# 📈 GUÍA UNIFICADA DE DESMOS PARA OBSIDIAN

> Plugin: `obsidian-desmos` — renderiza gráficas de [desmos.com](https://www.desmos.com/calculator) directamente en tus notas.
> Este documento tiene tres secciones según quién lo usa: **Usuario**, **NotebookLM** y **Claude**.

---

# 👤 SECCIÓN USUARIO

Referencia rápida para escribir bloques Desmos a mano en Obsidian.

---

## U1. ESTRUCTURA BÁSICA

Todo bloque Desmos se escribe así:

````
```desmos-graph
[configuración opcional]
---
[ecuaciones]
```
````

- La sección antes del `---` es **configuración** (límites, tamaño).
- La sección después del `---` son las **ecuaciones y curvas**.
- El `---` es **siempre obligatorio**.

---

## U2. CONFIGURACIÓN — LÍMITES Y TAMAÑO

| Parámetro | Descripción | Ejemplo |
|-----------|-------------|---------|
| `left` | Límite izquierdo del eje x | `left=-5` |
| `right` | Límite derecho del eje x | `right=5` |
| `bottom` | Límite inferior del eje y | `bottom=-3` |
| `top` | Límite superior del eje y | `top=3` |
| `width` | Ancho en píxeles | `width=500` |
| `height` | Alto en píxeles | `height=400` |
| `grid` | Mostrar/ocultar cuadrícula | `grid=false` |
| `degreeMode` | Modo de ángulos | `degreeMode=degrees` |

> 💡 Para gráficas de estudio usa `width=500; height=400`. Para plano xy cuadrado usa `width=500; height=500`.

---

## U3. ECUACIONES — SINTAXIS LaTeX

| Lo que quieres | Código |
|----------------|--------|
| $y = x^2$ | `y=x^2` |
| $y = \sqrt{x}$ | `y=\sqrt{x}` |
| $y = \frac{1}{x}$ | `y=\frac{1}{x}` |
| $y = e^x$ | `y=e^x` |
| $y = \sin(x)$ | `y=\sin(x)` |
| $y = \ln(x)$ | `y=\ln(x)` |
| $x^2 + y^2 = 1$ | `x^2+y^2=1` |
| $x = 2$ (vertical) | `x=2` |
| $y = 3$ (horizontal) | `y=3` |

---

## U4. COLORES

Agregar `|COLOR` después de la ecuación.

| Nombre | Uso recomendado |
|--------|-----------------|
| `RED`, `BLUE`, `GREEN`, `ORANGE`, `PURPLE` | Curvas y líneas |
| `BLACK` | Bordes, ejes, puntos de referencia |
| `DASHED`, `DOTTED` | Líneas auxiliares |
| `#a5d8ff` | Relleno azul claro |
| `#b2f2bb` | Relleno verde claro |
| `#ffd8a8` | Relleno naranja claro |
| `#ff7b7b` | Relleno rojo claro |
| `#d0bfff` | Relleno morado claro |

---

## U5. RESTRICCIONES DE DOMINIO

```
y=x^2|0<=x<=3
y=\sqrt{x}|x>=0
x=2|0<=y<=5
```

---

## U6. ÁREAS SOMBREADAS

Usar inecuaciones. Para intersección de condiciones, todo en **una sola línea** separado por `|`:

```
y<2-x|y>x|x>=0|x<=1|#a5d8ff
```

### ⚠️ Rectángulos sombreados

Para sombrear un rectángulo **no usar** `y<=cte|y>=cte` solo — hay que incluir también las restricciones en x. Sintaxis correcta:

```
x>=0|x<=1|y>=0|y<=1|#a5d8ff
```

Esto es equivalente a decir: "la región donde x está entre 0 y 1, e y está entre 0 y 1". Si se omite alguna condición, Desmos extiende el relleno infinitamente en esa dirección.

---

## U7. PUNTOS Y ETIQUETAS

```
(1,2)                   → Punto sólido
(1,2)|OPEN              → Punto hueco
(1,2)|label:texto|BLACK → Punto con etiqueta
```

---

## U8. FUNCIONES OCULTAS

```
f(x)=x^2|hidden
f'(x)|BLUE
```

---

## U9. CHEATSHEET RÁPIDO

```
left=; right=; bottom=; top=;   ← ventana del plano
width=; height=;                 ← tamaño en px
---
y=ec                             ← curva básica
y=ec|COLOR|DASHED                ← con color y estilo
y=ec|0<=x<=1|COLOR               ← con restricción de dominio
y<ec|y>otra|#hexcolor            ← área sombreada entre curvas
x>=a|x<=b|y>=c|y<=d|#hexcolor   ← rectángulo sombreado
(x,y)|label:texto|COLOR          ← punto etiquetado
f(x)=ec|hidden                   ← función oculta
```

---

## U10. RECURSOS

| Recurso | URL |
|---------|-----|
| Desmos Calculator | https://www.desmos.com/calculator |
| Plugin GitHub | https://github.com/nigecat/obsidian-desmos |
| Learn Desmos | https://learn.desmos.com |

---

---

# 🤖 SECCIÓN NOTEBOOKLM

Instrucciones para que NotebookLM genere bloques Desmos correctos listos para copiar en Obsidian. Cuando el usuario pida una gráfica, responder con un bloque de código — no con imagen ni enlace.

---

## N1. REGLA CRÍTICA — EL `---` ES SIEMPRE OBLIGATORIO

**Sin `---` el plugin no renderiza nada.** No importa si hay configuración o no.

❌ Incorrecto:
```
```desmos-graph
width=500; height=500;
y=x^2|BLUE
```
```

✅ Correcto:
```
```desmos-graph
width=500; height=500;
---
y=x^2|BLUE
```
```

✅ Sin configuración, el `---` igual va:
```
```desmos-graph
---
y=x^2|BLUE
```
```

---

## N2. ESTRUCTURA OBLIGATORIA

```
```desmos-graph
[parámetros terminados en ;]
---
[ecuaciones con modificadores]
```
```

---

## N3. PARÁMETROS DE CONFIGURACIÓN

| Parámetro | Qué hace | Valor típico |
|-----------|----------|--------------|
| `left` | Límite izquierdo x | `-5` |
| `right` | Límite derecho x | `5` |
| `bottom` | Límite inferior y | `-3` |
| `top` | Límite superior y | `3` |
| `width` | Ancho en px | `500` |
| `height` | Alto en px | `400` |

Usar `width=500; height=500` para plano cuadrado (probabilidad, geometría).

---

## N4. SINTAXIS DE ECUACIONES

| Matemática | Código |
|------------|--------|
| y = x² | `y=x^2` |
| y = √x | `y=\sqrt{x}` |
| y = 1/x | `y=\frac{1}{x}` |
| y = eˣ | `y=e^x` |
| y = sin(x) | `y=\sin(x)` |
| x² + y² = r² | `x^2+y^2=r^2` |

---

## N5. MODIFICADORES

```
|RED, |BLUE, |GREEN, |ORANGE, |PURPLE, |BLACK   → color de curva
|SOLID, |DASHED, |DOTTED                         → estilo de línea
|0<=x<=1                                         → restricción de dominio
|hidden                                          → ocultar curva
```

Colores para rellenos (usar hexadecimal, no nombre):
```
#a5d8ff → azul claro
#b2f2bb → verde claro
#ffd8a8 → naranja claro
#ff7b7b → rojo claro
#d0bfff → morado claro
```

---

## N6. ÁREAS SOMBREADAS

Usar inecuaciones con todas las condiciones en **una sola línea**:

```
y<2-x|y>x|x>=0|x<=1|#a5d8ff
```

### ⚠️ Rectángulos sombreados

Para sombrear una región rectangular incluir SIEMPRE las cuatro restricciones en una sola línea:

```
x>=0|x<=1|y>=0|y<=1|#a5d8ff
```

No usar `y<=1|y>=0` sin las restricciones de x — Desmos extenderá el relleno fuera del rectángulo.

---

## N7. PUNTOS

```
(1,2)|label:(1,2)|BLACK
(1,2)|OPEN|label:(1,2)|BLACK
```

---

## N8. EJEMPLOS COMPLETOS

### Función simple
```
```desmos-graph
left=-4; right=4; bottom=-2; top=6;
width=500; height=400;
---
y=x^2|BLUE
```
```

### Región triangular (probabilidad)
```
```desmos-graph
left=-0.2; right=1.5; bottom=-0.2; top=2.5;
width=500; height=500;
---
y=x|0<=x<=1|RED|SOLID
y=2-x|0<=x<=1|BLUE|SOLID
x=0|0<=y<=2|BLACK|DASHED
y<2-x|y>x|x>=0|x<=1|#a5d8ff
(0,0)|label:(0,0)|BLACK
(1,1)|label:(1,1)|RED
(0,2)|label:(0,2)|BLUE
```
```

### Rectángulo sombreado (soporte cuadrado)
```
```desmos-graph
left=-0.2; right=1.3; bottom=-0.2; top=1.3;
width=500; height=500;
---
x>=0|x<=1|y>=0|y<=1|#a5d8ff
x=1|0<=y<=1|BLUE|DASHED
y=1|0<=x<=1|BLUE|DASHED
(0,0)|label:(0,0)|BLACK
(1,1)|label:(1,1)|BLACK
```
```

### Región entre curva y recta
```
```desmos-graph
left=-0.1; right=1.3; bottom=-0.1; top=1.3;
width=500; height=500;
---
y=x|0<=x<=1|RED|SOLID
y=\sqrt{x}|0<=x<=1|GREEN|SOLID
y<\sqrt{x}|y>x|0<=x<=1|#b2f2bb
(0,0)|label:(0,0)|BLACK
(1,1)|label:(1,1)|BLACK
```
```

---

## N9. CHECKLIST ANTES DE RESPONDER

Antes de entregar un bloque Desmos verificar:
- [ ] ¿Tiene `---`?
- [ ] ¿Todos los parámetros terminan en `;`?
- [ ] ¿Sin espacios alrededor de `|`?
- [ ] ¿Sin llaves `{}`en restricciones?
- [ ] ¿Sin comentarios `//`?
- [ ] ¿Rectángulos sombreados con las 4 condiciones `x>=|x<=|y>=|y<=`?
- [ ] ¿Rellenos con color hexadecimal, no con nombre?

---

---

# 🧠 SECCIÓN CLAUDE

Reglas y patrones que Claude debe aplicar al generar o corregir bloques Desmos en archivos `.md` del vault. Esta sección es la referencia de trabajo activa para Claude.

---

## C1. REGLAS ABSOLUTAS DE SINTAXIS

Estas reglas no tienen excepciones. Cualquier bloque que las viole debe corregirse:

| Regla | Correcto | Incorrecto |
|-------|----------|------------|
| Separador `---` siempre presente | `width=500;\n---\ny=x` | `width=500;\ny=x` |
| Sin espacios alrededor de `\|` | `y=x\|RED` | `y = x \| RED` |
| Sin llaves `{}` en restricciones | `y=x\|0<=x<=1` | `y=x\|{0<=x<=1}` |
| Sin comentarios `//` | — | `y=x^2 // parábola` |
| Raíces con `\sqrt{x}` | `y=\sqrt{x}` | `y=sqrt(x)` |
| Fracciones con `\frac{a}{b}` | `y=\frac{3}{8}x` | `y=(3/8)x` |
| Pi con `\pi` | `y=\frac{1}{\pi}` | `y=1/pi` |
| Restricciones de líneas con dominio | `y=x\|0<=x<=2\|BLUE` | `y=x\|BLUE` (se desborda) |
| Rellenos con hex, no nombre | `\|#a5d8ff` | `\|BLUE` (saturado) |

---

## C2. RECTÁNGULOS SOMBREADOS

Para sombrear una región rectangular usar las **cuatro condiciones en una sola línea**:

```
x>=a|x<=b|y>=c|y<=d|#a5d8ff
```

**Ejemplo — soporte cuadrado [0,1]×[0,1]:**
```
x>=0|x<=1|y>=0|y<=1|#a5d8ff
```

**Nunca** usar solo `y<=1|y>=0|#a5d8ff` — Desmos extiende el relleno fuera del rectángulo porque no conoce los límites en x.

Para agregar los bordes del rectángulo como líneas encima del relleno:
```
x>=0|x<=1|y>=0|y<=1|#a5d8ff
x=1|0<=y<=1|BLUE|DASHED
y=1|0<=x<=1|BLUE|DASHED
```

---

## C3. CUÁNDO INCLUIR GRÁFICA

Incluir gráfica solo si aporta claridad visual que el texto no puede dar:

✅ Incluir cuando:
- El soporte tiene geometría no obvia (triángulo, semicírculo, valor absoluto, curva).
- Se pide probabilidad sobre una región con fronteras curvas o partidas.
- La densidad marginal tiene forma visual relevante para entender el problema.
- El enunciado pide explícitamente dibujar la región.

❌ No incluir cuando:
- El resultado es un número (varianza, covarianza, probabilidad simple).
- La conclusión es algebraica (independencia, normalización).
- El soporte es un cuadrado simple y la conclusión no depende de verlo.
- Ya hay una gráfica suficiente en ese inciso.

---

## C4. UNA GRÁFICA POR INCISO

Cada inciso tiene su propio bloque `desmos-graph` independiente. Nunca mezclar ecuaciones de distintos incisos en un solo bloque.

Si el archivo tiene todas las gráficas juntas al final:
1. Identificar a qué inciso pertenece cada ecuación.
2. Crear un bloque por inciso y ubicarlo después del desarrollo de ese inciso.
3. Eliminar el bloque acumulado al final.

---

## C5. NOTA SOBRE ESTE ARCHIVO

Los bloques de código Desmos en **este documento** usan ` ```desmos-graphx ` (con x al final) o se muestran como texto plano para que Obsidian no los renderice y se pueda leer el ejemplo.

En los archivos de ejercicios (`ETN806-*.md`, etc.) usar siempre ` ```desmos-graph ` **sin la x**.

---

## C6. FLUJO DE CORRECCIÓN DE UN BLOQUE EXISTENTE

Cuando Claude encuentra un bloque Desmos con errores:

1. Identificar todos los errores (ver C1).
2. Corregir directamente en el archivo con Filesystem — no mostrar el bloque corregido en el chat.
3. Si el bloque usa ` ``` ` genérico en lugar de ` ```desmos-graph `, corregir el tipo también.
4. Si la gráfica no aporta al inciso, eliminarla (ver C3).

---

## C7. PLANTILLA BASE PARA REGIONES DE PROBABILIDAD

```desmos-graphx
left=-0.2; right=X; bottom=-0.2; top=Y;
width=500; height=500;
---
[fronteras del dominio con restricciones de dominio y colores]
[región sombreada como inecuación con todas las condiciones en una línea]
[puntos clave con label]
```

Ajustar `right` y `top` según el tamaño del soporte más un margen de ~20%.

---

## C8. PALETA DE COLORES RECOMENDADA POR ROL

| Rol visual | Color |
|------------|-------|
| Soporte / región principal | `#a5d8ff` (azul claro) |
| Región de evento / probabilidad | `#ff7b7b` (rojo claro) |
| Región secundaria | `#b2f2bb` (verde claro) |
| Frontera superior del dominio | `BLUE` |
| Frontera inferior / diagonal | `RED` |
| Curva de evento | `PURPLE` |
| Líneas auxiliares | `BLACK|DASHED` |
| Puntos clave | `BLACK` o el color de la curva asociada |

%%
galaxy-links
[[_galaxy-system]]
[[convencion-notas]]
%%
