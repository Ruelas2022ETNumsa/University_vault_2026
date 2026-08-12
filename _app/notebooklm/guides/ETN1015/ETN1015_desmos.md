---
title: Desmos — Guía unificada para ETN1015
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
  - ETN1015
date_created: 2026-08-12
date_updated: 2026-08-12
status: activo
---

# 📈 GUÍA UNIFICADA DE DESMOS PARA ETN1015

> Plugin: `obsidian-desmos` — renderiza gráficas directamente en Obsidian.
> Organizado en tres bloques: **Reglas de sintaxis (N1–N10)**, **Checklist (N11)**, y **Biblioteca de ejemplos por tema ETN1015 (N12–N19)**.

---

# 🤖 SECCIÓN NOTEBOOKLM

Cuando el usuario pida una gráfica, responder con un bloque de código listo para copiar en Obsidian — no con imagen ni enlace.

### Defaults — cuando el usuario no especifica

- Tamaño: `width=300; height=200;`
- Color de primera curva: `#005F73`
- Ventana: `left=-5; right=5; bottom=-3; top=3;` como punto de partida, ajustar según la señal
- Siempre incluir `---` aunque no haya configuración

### Reglas base — siempre obligatorias

Antes de generar cualquier bloque, seguir este orden:
1. ¿Qué tipo de gráfica? (señal en tiempo / espectro / respuesta en frecuencia / Bode)
2. ¿Qué tamaño? (elegir de la tabla en N2 según el tipo)
3. ¿Cuál es la ventana? (ajustar left/right/bottom/top según la señal)
4. ¿Qué ecuaciones y en qué orden? (constantes → ecuaciones → puntos)
5. ¿Qué colores? (paleta en N5 según el rol de cada curva)

Reglas que nunca se omiten:
- Identificador: tres backticks seguidos de `desmos-graph` en la misma línea
- El `---` es siempre obligatorio, incluso sin parámetros
- Orden de parámetros: ventana → tamaño → `---` → ecuaciones
- Colores siempre en hex — ver paleta completa en N5
- Restricciones sin llaves: `|0<=x<=3|` nunca `|{0<=x<=3}|`

---

## BLOQUE A — SINTAXIS Y REGLAS

---

### N1. REGLA CRÍTICA — EL `---` ES SIEMPRE OBLIGATORIO + ESTRUCTURA

**Sin `---` el plugin no renderiza nada.** No importa si hay configuración o no.

#### Estructura obligatoria del bloque

```
desmos-graph
[parámetros de ventana: left right bottom top]
[parámetros de tamaño: width height]
---
[ecuaciones con modificadores]
```

**Orden de parámetros — siempre este orden, sin excepción:**

1. Primero `left`, `right`, `bottom`, `top` — definen la ventana
2. Después `width`, `height` — definen el tamaño del canvas

❌ Incorrecto — sin `---`:
```
desmos-graph
width=300; height=200;
y=\sin(x)|#005F73
```

❌ Incorrecto — orden de parámetros invertido:
```
desmos-graph
width=350; height=120;
left=-6; right=6; bottom=-1; top=1;
---
y=\sin(x)|#005F73
```

✅ Correcto — con configuración:
```
desmos-graph
left=-6; right=6; bottom=-1; top=1;
width=350; height=120;
---
y=\sin(x)|#005F73
```

✅ Correcto — sin configuración, el `---` igual va:
```
desmos-graph
---
y=\sin(x)|#005F73
```

---

### N2. PARÁMETROS DE CONFIGURACIÓN

| Parámetro | Qué hace           | Valor típico |
| --------- | ------------------ | ------------ |
| `left`    | Límite izquierdo x | `-5`         |
| `right`   | Límite derecho x   | `5`          |
| `bottom`  | Límite inferior y  | `-3`         |
| `top`     | Límite superior y  | `3`          |
| `width`   | Ancho en px        | ver tabla    |
| `height`  | Alto en px         | ver tabla    |

**Tamaños estándar confirmados:**

| Tipo           | width | height | Uso                                          |
| -------------- | ----- | ------ | -------------------------------------------- |
| Pequeño        | 300   | 200    | Señales simples, un solo tramo               |
| Mediano        | 400   | 350    | Señales con múltiples tramos, espectros      |
| Grande         | 550   | 450    | Múltiples curvas, etiquetas, regiones        |
| Cornell        | 320   | 250    | Máximo dentro de bloque multi-column         |
| Panorámico     | 550   | 200    | Señales periódicas, respuestas en frecuencia |
| Plano cuadrado | 500   | 500    | Plano complejo aproximado, regiones          |

Para señales en tiempo usar ratio panorámico (3:1). Para espectros ratio 4:3.

---

### N3. SINTAXIS DE ECUACIONES

| Matemática          | Código Desmos              |
| ------------------- | -------------------------- |
| y = k (constante)   | `y=2`, `y=-1`, `y=0`       |
| y = A·sin(ωx + φ)   | `y=A\sin(\omega x+\phi)`   |
| y = A·cos(ωx + φ)   | `y=A\cos(\omega x+\phi)`   |
| y = eˣ              | `y=e^x`                    |
| y = e^{-ax}         | `y=e^{-a*x}`               |
| y = e^{-ax}·sin(ωx) | `y=e^{-a*x}\sin(\omega x)` |
| y = 1/x             | `y=1/x`                    |
| y = 1/(1+x²)        | `y=1/(1+x^2)`              |
| y = \|x\|           | `y=\abs(x)`                |
| y = x^{1/2}         | `y=x^{1/2}`                |
| y = ln(x)           | `y=\ln(x)`                 |

#### Notación funcional

| Matemática            | Código Desmos        |          |
| --------------------- | -------------------- | -------- |
| f(x) = expresión      | `f(x)=e^{-x}\sin(x)` |          |
| f(x) con dominio fijo | `f(x)=e^{-x}         | 0<=x<=5` |
| Constante declarada   | `a=2` / `b=0.5`      |          |

---

### N4. CONSTANTES Y FUNCIONES DEFINIDAS POR EL USUARIO

Desmos permite declarar constantes con cualquier letra **excepto `x` e `y`**:

```
desmos-graph
---
a=2
b=0.5
w=3.1416
```

Luego se usan directamente en ecuaciones y restricciones:

```
desmos-graph
---
a=2
w=2
y=a*e^{-a*x}\sin(w*x)|0<=x<=5|#005F73
```

> **Importante:** las constantes **no pueden usarse en la configuración** (arriba del `---`). `left=a` no funciona — escribir siempre el valor numérico.

#### El valor de π

Desmos reconoce `\pi` como constante nativa (debajo del `---`):

```
desmos-graph
---
y=\sin(x)|-\pi<=x<=\pi|#005F73
```

`\pi` no funciona en la configuración — usar valor numérico: `left=-3.1416;`

---

### N5. MODIFICADORES Y COLORES

```
desmos-graph
---
y=\sin(x)|#005F73
y=\cos(x)|#0A9396|DASHED
y=\sin(x)+1|#EE9B00|DOTTED
(0,1)|open|#C1121F
(3.1416,0)|cross|#5A189A
```

```
|#hex          → color (SIEMPRE usar hex)
|SOLID         → línea sólida (default)
|DASHED        → línea segmentada
|DOTTED        → línea punteada
|0<=x<=1       → restricción de dominio
|hidden        → ocultar curva
|open          → punto vacío / discontinuidad abierta
|cross         → punto con cruz
(x,y)|#hex    → punto sólido (default)
```

#### ⚠️ Orden de declaración obligatorio
constantes (a=2) → ecuaciones (y=...) → puntos ((1,1))

#### ⚠️ Regla de color: SIEMPRE hex, NUNCA nombres en mayúsculas

Los modificadores `DASHED`, `SOLID`, `DOTTED` sí van en mayúsculas — es la sintaxis correcta.

#### Paleta para curvas y líneas (sólidas)

```
#005F73   → azul petróleo   (señal principal / x(t))
#0A9396   → verde azulado   (señal secundaria / y(t))
#EE9B00   → ámbar           (destaque / h(t))
#BB3E03   → naranja quemado (advertencia)
#629900   → verde oliva     (auxiliar)
#5A189A   → morado          (punto especial)
#C1121F   → rojo            (error / evento)
#DA627D   → rosa            (curva alternativa)
#FFD60A   → amarillo        (resaltado)
#474448   → gris antracita  (ejes, bordes, auxiliares)
```

#### Paleta para líneas segmentadas

```
#80AFB9   → azul petróleo segmentado
#85C9CB   → verde azulado segmentado
#F7CD80   → ámbar segmentado
#DD9F81   → naranja quemado segmentado
#B1CC80   → verde oliva segmentado
#A3A2A4   → gris antracita segmentado
```

#### Paleta para rellenos

```
#BFD7DC   → azul petróleo claro   (región principal)
#C2E4E5   → verde azulado claro   (región secundaria)
#FBE6BF   → ámbar claro
#F0C4C7   → rojo claro            (región de evento)
```

---

### N6. ESTRUCTURA DE UNA LÍNEA DE ECUACIÓN

Cada línea debajo del `---` se divide en segmentos separados por `|`:

```
expresión | modificador_2 | modificador_3 | ... | #color
    1     |      2       |      3        |     |   n
```

#### ⚠️ Llaves `{}` — solo válidas en el segmento 1

Las llaves `{}` **solo funcionan en el segmento 1**. En segmentos 2+ producen error sin aviso.

❌ No funciona:
```
desmos-graph
---
y=e^{-x}|x>=0|y^{1/2}>0|#BFD7DC
```

✅ Solución — declarar constante:
```
desmos-graph
---
n=0.5
y=e^{-x}|x>=0|y>0|#BFD7DC
```

---

### N7. SEÑALES POR TRAMOS Y ÁREAS SOMBREADAS

Las condiciones de sombreado van todas en **una sola línea**, separadas por `|`.

#### Señal por tramos — forma preferida

```
desmos-graph
---
y=0|x<0|#005F73
y=e^{-x}|x>=0|#005F73
(0,1)|label:(0,1)|#005F73
```

Alternativa válida con llaves escapadas:

```
desmos-graph
---
y=e^{-x}\{x>=0\}|#005F73
```

> `\{` y `\}` son llaves escapadas — el backslash es obligatorio.
> `{...}` sin backslash NO funciona en el plugin.

#### Área bajo la curva

```
desmos-graph
---
y=e^{-x}|x>=0|#005F73
y<=e^{-x}|x>=0|y>=0|#BFD7DC
```

#### ⚠️ Rectángulos sombreados — cuatro condiciones obligatorias

```
desmos-graph
---
x>=0|x<=1|y>=0|y<=1|#BFD7DC
```

---

### N8. PUNTOS Y ETIQUETAS

```
desmos-graph
---
(1,1)|label:(1,1)|#005F73
(2,2)|open|label:(2,2)|#0A9396
(3,3)|cross|label:(3,3)|#EE9B00
```

#### Fracciones y LaTeX en etiquetas

`\frac{}{}` no renderiza en `label:` — usar equivalente ASCII:

✅ `(1,0)|label:T/2|#C1121F`
❌ `(1,0)|label:\frac{T}{2}|#C1121F`

---

### N9. VALOR ABSOLUTO

```
desmos-graph
---
y=\abs(x)|#005F73
y=\abs(\sin(x))|#0A9396
```

Para regiones sombreadas usar tramos — `\abs()` no funciona en condiciones de relleno:

```
desmos-graph
---
y=\abs(x)|hidden
y>=x|y>=-x|y<=3|#C2E4E5
```

---

### N10. RAÍZ CUADRADA — TRES FORMAS VÁLIDAS

Usar en orden de preferencia:

**Forma 1:** `y=x^{1/2}` ← primera opción
**Forma 2:** `y=\sqrt{x}`
**Forma 3:** `x=y^2|y>=0`

❌ Nunca usar: `sqrt(x)` · `\sqrt(x)` · `sqrt{x}`

---

## BLOQUE B — CHECKLIST

---

### N11. CHECKLIST ANTES DE RESPONDER

- [ ] ¿El bloque abre con tres backticks seguidos de `desmos-graph`?
- [ ] ¿Tiene `---`?
- [ ] ¿Todos los parámetros terminan en `;`?
- [ ] ¿Sin espacios alrededor de `|`?
- [ ] ¿Sin llaves `{}` en restricciones inline?
- [ ] ¿Sin comentarios `//`?
- [ ] ¿Rectángulos sombreados con las 4 condiciones `x>=a|x<=b|y>=c|y<=d`?
- [ ] ¿Colores en hex? Los modificadores `DASHED`, `SOLID`, `DOTTED` sí van en mayúsculas.
- [ ] ¿Rellenos con hex pastel?
- [ ] ¿Señales por tramos usan `y=k|a<x<b|#hex` como forma preferida?
- [ ] ¿Sin `y=|x|` ni `y=abs(x)` en condiciones de relleno?
- [ ] ¿Raíz cuadrada usa `x^{1/2}`?
- [ ] ¿Llaves escapadas `\{` `\}` llevan backslash obligatorio?

---

## BLOQUE C — BIBLIOTECA DE EJEMPLOS POR TEMA (ETN1015)

Todos los ejemplos de esta sección han sido confirmados y renderizan correctamente.

**Reglas críticas de sintaxis (recordatorio):**
- Potencias siempre con `{}`: `e^{-x}` nunca `e^(-x)`
- Llaves `{}` solo válidas en segmento 1 de cada línea — ver N6
- Palabras reservadas con `\`: `\cos`, `\sin`, `\ln`, `\abs()`
- Colores de la paleta oficial únicamente

---

### N12. CAP. 1 — SEÑALES BÁSICAS

> Señales elementales en tiempo continuo: escalón, rampa, impulso, exponencial.

#### Escalón unitario u(t)

> Contexto: tramo 0 para t<0, tramo 1 para t>=0. Punto de discontinuidad en (0,0) con `|open`.

```
desmos-graph
left=-3; right=5; bottom=-0.5; top=1.5;
width=400; height=200;
---
y=0|-3<=x<0|#005F73
y=1|0<=x<=5|#005F73
(0,0)|open|#005F73
(0,1)|#005F73
```

#### Escalón desplazado u(t - a)

> Contexto: escalón retrasado con salto en t=a.

```
desmos-graph
left=-2; right=8; bottom=-0.5; top=1.5;
width=400; height=200;
---
a=2
y=0|-2<=x<a|#005F73
y=1|a<=x<=8|#005F73
(a,0)|open|#005F73
(a,1)|label:t=a|#005F73
```

#### Rampa r(t) = t·u(t)

```
desmos-graph
left=-2; right=5; bottom=-0.5; top=5;
width=300; height=200;
---
y=0|-2<=x<0|#005F73
y=x|0<=x<=5|#005F73
(0,0)|#005F73
```

#### Exponencial decreciente x(t) = e^{-at}·u(t)

```
desmos-graph
left=-1; right=6; bottom=-0.5; top=1.5;
width=400; height=200;
---
a=1
y=0|-1<=x<0|#005F73
y=e^{-a*x}|0<=x<=6|#005F73
(0,1)|label:(0,1)|cross|#005F73
```

#### Exponencial creciente x(t) = e^{at}·u(-t)

```
desmos-graph
left=-6; right=1; bottom=-0.5; top=1.5;
width=400; height=200;
---
a=1
y=e^{a*x}|-6<=x<=0|#005F73
y=0|0<x<=1|#005F73
(0,1)|label:(0,1)|#005F73
```

#### Pulso rectangular Π(t)

```
desmos-graph
left=-3; right=3; bottom=-0.5; top=1.5;
width=400; height=200;
---
y=0|-3<=x<-1|#005F73
y=1|-1<=x<=1|#005F73
y=0|1<x<=3|#005F73
(-1,0)|open|#005F73
(-1,1)|#005F73
(1,1)|#005F73
(1,0)|open|#005F73
```

#### Señal senoidal x(t) = A·sin(ωt)

```
desmos-graph
left=-6.2832; right=6.2832; bottom=-2; top=2;
width=550; height=200;
---
A=1
w=1
y=A\sin(w*x)|#005F73
```

#### Señal exponencial compleja — Re e Im superpuestas

```
desmos-graph
left=-6.2832; right=6.2832; bottom=-1.5; top=1.5;
width=550; height=200;
---
w=1
y=\cos(w*x)|#005F73
y=\sin(w*x)|#0A9396|DASHED
```

---

### N13. CAP. 2 — SISTEMAS LTI EN TIEMPO CONTINUO

#### Respuesta al impulso h(t) = e^{-at}·u(t)

```
desmos-graph
left=-1; right=6; bottom=-0.5; top=1.5;
width=400; height=200;
---
a=1
y=0|-1<=x<0|#EE9B00
y=e^{-a*x}|0<=x<=6|#EE9B00
(0,1)|label:h(0)=1|cross|#EE9B00
```

#### Convolución gráfica — señales superpuestas

```
desmos-graph
left=-1; right=6; bottom=-0.5; top=1.5;
width=550; height=250;
---
a=1
y=e^{-a*x}|0<=x<=6|#005F73
y=e^{-a*(x-2)}|2<=x<=6|#0A9396|DASHED
(0,1)|label:x(t)|#005F73
(2,1)|label:h(t-2)|#0A9396
```

---

### N14. CAP. 3 — FOURIER CONTINUO

#### Espectro de amplitud — sinc

```
desmos-graph
left=-10; right=10; bottom=-0.5; top=1.5;
width=550; height=200;
---
y=\sin(x)/x|x!=0|#005F73
(0,1)|label:|X(0)|=1|cross|#005F73
```

#### Serie de Fourier — suma parcial onda cuadrada

```
desmos-graph
left=-6.2832; right=6.2832; bottom=-1.5; top=1.5;
width=550; height=200;
---
y=\sin(x)+\sin(3x)/3+\sin(5x)/5+\sin(7x)/7+\sin(9x)/9|#005F73
```

#### Respuesta en frecuencia |H(jω)| — primer orden

```
desmos-graph
left=-6; right=6; bottom=-0.5; top=1.5;
width=550; height=250;
---
y=1/(1+x^2)^{1/2}|#005F73
y=1/(2)^{1/2}|DASHED|#80AFB9
(1,0)|label:wc=1|open|#C1121F
(0,1)|label:|H(0)|=1|cross|#005F73
```

---

### N15. CAP. 4 — TRANSFORMADA DE LAPLACE

#### Respuesta transitoria — polo real negativo

```
desmos-graph
left=-0.5; right=6; bottom=-0.5; top=1.5;
width=400; height=200;
---
s=1
y=e^{-s*x}|0<=x<=6|#005F73
y=0|x<0|#005F73
(0,1)|label:(0,1)|cross|#005F73
```

#### Respuesta transitoria — par de polos complejos (subamortiguado)

```
desmos-graph
left=-0.5; right=8; bottom=-1.5; top=1.5;
width=550; height=250;
---
s=0.5
w=2
y=e^{-s*x}\sin(w*x)|0<=x<=8|#005F73
y=e^{-s*x}|0<=x<=8|#80AFB9|DASHED
y=-e^{-s*x}|0<=x<=8|#80AFB9|DASHED
y=0|x<0|#005F73
```

---

### N16. CAP. 5 — FILTROS ANALÓGICOS

#### Butterworth orden N — |H(jω)|

```
desmos-graph
left=-0.5; right=4; bottom=-0.5; top=1.2;
width=550; height=250;
---
N=2
y=1/(1+x^{2*N})^{1/2}|#005F73
y=1/2^{1/2}|DASHED|#80AFB9
(1,0)|label:wc|open|#C1121F
```

#### Bode — magnitud en dB

```
desmos-graph
left=0.01; right=100; bottom=-60; top=5;
width=550; height=250;
---
y=20\log(1/(1+x^2)^{1/2})|#005F73
y=-3|DASHED|#80AFB9
```

---

### N17. CAP. 6 — SEÑALES Y SISTEMAS EN TIEMPO DISCRETO

#### Exponencial discreta aproximada x[n] = a^n·u[n]

> Para diagramas de tallo exactos usar TikZ.

```
desmos-graph
left=-1; right=7; bottom=-0.5; top=1.5;
width=550; height=200;
---
a=0.7
y=a^{\floor(x)}|0<=x<=7|#005F73
y=0|x<0|#005F73
```

#### Proceso de muestreo — señal continua vs muestras

```
desmos-graph
left=-0.5; right=6.2832; bottom=-1.5; top=1.5;
width=550; height=250;
---
T=1
y=\sin(x)|#80AFB9|DASHED
y=\sin(\floor(x/T)*T)|0<=x<=6|#005F73
```

---

### N18. CAP. 7 — FOURIER DISCRETO (DTFT)

#### DTFT de x[n] = a^n·u[n] — magnitud

```
desmos-graph
left=-3.1416; right=3.1416; bottom=-0.5; top=4;
width=550; height=250;
---
a=0.7
y=1/(1-2*a*\cos(x)+a^2)^{1/2}|#005F73
```

#### Espectro periódico — repetición cada 2π

```
desmos-graph
left=-6.2832; right=6.2832; bottom=-0.5; top=4;
width=550; height=200;
---
a=0.7
y=1/(1-2*a*\cos(x)+a^2)^{1/2}|#005F73
```

---

### N19. CAP. 8 — TRANSFORMADA Z

#### Respuesta al escalón — sistema de primer orden discreto

```
desmos-graph
left=-0.5; right=10; bottom=-0.5; top=3;
width=550; height=250;
---
a=0.5
y=(1-a^{\floor(x)+1})/(1-a)|0<=x<=10|#005F73
y=1/(1-a)|DASHED|#80AFB9
y=0|x<0|#005F73
(0,1)|label:y[0]=1|cross|#005F73
```

#### Respuesta oscilatoria — polos complejos discretos

```
desmos-graph
left=-0.5; right=10; bottom=-1.5; top=1.5;
width=550; height=250;
---
r=0.9
w=1
y=r^x\sin(w*x)|0<=x<=10|#005F73
y=r^x|0<=x<=10|#80AFB9|DASHED
y=-r^x|0<=x<=10|#80AFB9|DASHED
y=0|x<0|#005F73
```

---

%%
# galaxy-links
[[_app/_config/_galaxy-system.md]]
[[_app/_config/_note-system.md]]
%%
