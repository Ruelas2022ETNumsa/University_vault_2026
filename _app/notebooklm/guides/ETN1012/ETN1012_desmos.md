---
title: Desmos — Guía de gráficas de ocupación para ETN1012
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
  - ETN1012
date_created: 2026-09-28
date_updated: 2026-09-28
status: activo
---

# 📈 GUÍA DE DESMOS PARA ETN1012 — OCUPACIONES INDIVIDUAL Y SIMULTÁNEA

> Plugin: `obsidian-desmos` — renderiza gráficas directamente en Obsidian.
> Guía exclusiva para los ejercicios de **Ingeniería de Tráfico Básico**: registro de ocupaciones individuales (un tramo por toma en cada circuito) y registro de ocupaciones simultáneas (número de circuitos ocupados vs. tiempo).
> Organizada en: **Sección NotebookLM**, **Bloque A — Reglas de sintaxis (N1–N7)**, **Bloque B — Procedimiento y fórmulas (N8–N10)**, **Bloque C — Plantillas y ejemplo resuelto (N11–N13)** y **Checklist (N14)**.

---

# 🤖 SECCIÓN NOTEBOOKLM

Cuando el usuario pida graficar la ocupación individual o simultánea de un ejercicio, responder con un bloque de código listo para copiar en Obsidian — no con imagen ni enlace.

### Qué gráficas cubre esta guía

1. **Ocupación individual:** una fila por circuito; cada toma es un segmento horizontal a la altura del número de circuito.
2. **Ocupación simultánea:** línea escalonada continua (segmentos horizontales unidos por segmentos verticales) que indica cuántos circuitos están ocupados a la vez.

### Defaults — cuando el usuario no especifica

- Tamaño: `width=550; height=300;`
- Color de los tramos individuales: `#005F73`
- Color de la línea de ocupación simultánea: `#C1121F` (rojo, como en las diapositivas)
- Línea de referencia de "todos ocupados": `#A3A2A4` con `DASHED`
- Ventana individual: `left=-4; right=T+3; bottom=0; top=N+1;`
- Ventana simultánea: `left=-3; right=T+3; bottom=-0.5; top=N+1;`
  donde `T` es el periodo de observación (normalmente 60 min) y `N` es el número de circuitos
- Siempre incluir `---`

### Orden de trabajo — siempre este orden

1. Leer del enunciado (imagen o tabla): número de circuitos `N`, periodo `T` y los tramos `[inicio, fin]` de cada circuito.
2. Armar la tabla de tramos por circuito y sumar el tiempo de ocupación de cada uno (ver N8).
3. Graficar la **ocupación individual** (plantilla N11) si el usuario la pide o si conviene mostrar el enunciado.
4. Calcular la **ocupación simultánea** por intervalos (ver N8) y graficarla (plantilla N12).
5. Verificar: $\sum k\,\Delta t = V$ y $A' \le N$ (ver N10).
6. Calcular con las fórmulas del formulario (ver N9).

Reglas que nunca se omiten:
- Identificador: tres backticks seguidos de `desmos-graph` en la misma línea
- El `---` es siempre obligatorio
- Orden de parámetros: ventana → tamaño → `---` → ecuaciones
- Colores siempre en hex
- Restricciones sin llaves: `|0<=x<=3|` nunca `|{0<=x<=3}|`
- Las constantes no se usan arriba del `---`: escribir los valores numéricos directamente

---

## BLOQUE A — SINTAXIS Y REGLAS

---

### N1. REGLA CRÍTICA — EL `---` ES SIEMPRE OBLIGATORIO + ESTRUCTURA

**Sin `---` el plugin no renderiza nada.**

```
[parámetros de ventana: left right bottom top]
[parámetros de tamaño: width height]
---
[puntos con etiquetas]
[segmentos]
```

- Todos los parámetros terminan en `;`
- Sin espacios alrededor de `|`
- Sin comentarios `//`

---

### N2. VENTANA Y TAMAÑO

| Gráfica | left | right | bottom | top | width | height |
|---|---|---|---|---|---|---|
| Individual | `-4` | `T+3` (63) | `0` | `N+1` | 550 | 300 |
| Simultánea | `-3` | `T+3` (63) | `-0.5` | `N+1` | 550 | 300 |

- Con `N` = 5 circuitos usar `height=250`; con `N` = 7 o más usar `height=300` o mayor.
- El margen izquierdo (`-4` en la individual) es el espacio donde van las etiquetas de circuito.
- Escribir el valor numérico (`63`), no la expresión `T+3`.

---

### N3. SEGMENTOS

Un segmento horizontal (una toma o un nivel de ocupación):

```
y=k|a<=x<=b|#hex
```

Un segmento vertical (conector entre dos niveles):

```
x=a|c<=y<=d|#hex
```

Reglas:
- `k` es el número de circuito (individual) o el número de circuitos ocupados (simultánea).
- Usar `<=` en ambos extremos para que los segmentos vecinos se toquen sin hueco.
- Un segmento por tramo — no unir tramos separados en una sola línea.
- Sin llaves `{}` en las restricciones.

---

### N4. ETIQUETAS

Las etiquetas solo funcionan en puntos. Para mostrar solo el texto (sin el punto) se agrega `hidden`:

```
(x,y)|label:texto|hidden|#474448
```

- Etiquetas de circuito (individual): en `x=-2`, una por circuito: `(-2,3)|label:3|hidden|#474448`
- Duración de un tramo de congestión (simultánea): sobre el nivel `N`, en el punto medio del tramo: `(7.5,7.4)|label:5|hidden|#474448` (`7.4` = `N + 0.4`)
- Marcas de tiempo (opcional, para imitar el eje de las diapositivas): `(5,-0.35)|label:5|hidden|#474448`
- `label:` imprime texto literal: no usar LaTeX ni `\frac`.

---

### N5. COLORES

```
#005F73   → tramos de ocupación individual
#C1121F   → línea de ocupación simultánea (rojo, igual que las diapositivas)
#A3A2A4   → línea de referencia (todos los circuitos ocupados), con DASHED
#474448   → etiquetas
#BB3E03   → (opcional) resaltar los tramos de congestión
```

Siempre hex. `DASHED` va en mayúsculas.

---

### N6. ORDEN DE DECLARACIÓN

1. Puntos de etiqueta (`hidden`)
2. Línea de referencia (simultánea)
3. Segmentos, en orden de circuito (individual) o de tiempo (simultánea)

---

### N7. ERRORES COMUNES

- Olvidar los **conectores verticales** en la simultánea: sin ellos se ve una serie de trazos sueltos y no una curva escalonada.
- Poner un conector cuando el nivel no cambia (no hace falta).
- Dibujar un conector de cierre en `x=T`: en las diapositivas la línea simplemente termina.
- Olvidar el conector inicial `x=0|0<=y<=k1`: las diapositivas arrancan desde el eje, en 0.
- Usar `<` en los extremos: deja huecos entre segmentos consecutivos.
- Usar una etiqueta con `\frac` o LaTeX: se imprime literal.
- No revisar la suma: si $\sum k\,\Delta t \ne V$, algún tramo se leyó mal.

---

## BLOQUE B — PROCEDIMIENTO Y FÓRMULAS

---

### N8. CÓMO OBTENER LA OCUPACIÓN SIMULTÁNEA A PARTIR DE LA INDIVIDUAL

**Paso 1 — Tabla de tramos por circuito.** Anotar los tramos `[inicio, fin]` de cada circuito y sumar sus duraciones:

| Circuito | Tramos | $\sum t_j$ (min) |
|:-:|---|:-:|
| 1 | a–b, c–d, … | suma |

La suma de la última columna es el volumen de tráfico $V$. El número total de tramos es el número de tomas $n$.

**Paso 2 — Puntos de corte.** Reunir todos los inicios y fines de todos los circuitos, sin repetir, y ordenarlos: $t_0 = 0 < t_1 < \dots < t_m = T$.

**Paso 3 — Nivel de cada intervalo.** Para cada intervalo $[t_i,\,t_{i+1}]$ tomar su punto medio y contar cuántos circuitos tienen un tramo que lo contiene. Ese número $k_i$ es el nivel de ocupación del intervalo.

**Paso 4 — Segmentos horizontales.** Uno por intervalo: `y=k_i|t_i<=x<=t_{i+1}|#C1121F`. Si dos intervalos consecutivos tienen el mismo nivel, pueden unirse en uno solo.

**Paso 5 — Conectores verticales.** En cada punto de corte $t_i$ donde el nivel cambia de $k_{i-1}$ a $k_i$: `x=t_i|min<=y<=max|#C1121F`, con `min` y `max` el menor y el mayor de los dos niveles. Al inicio: `x=0|0<=y<=k_0|#C1121F`.

**Paso 6 — Congestión.** Los intervalos con $k = N$ (todos los circuitos ocupados) suman el tiempo $t$ de congestión. Marcar cada uno con una etiqueta con su duración (N4).

---

### N9. FÓRMULAS DEL FORMULARIO (INGENIERÍA DE TRÁFICO BÁSICO)

| Magnitud | Fórmula | Unidad |
|---|---|---|
| Volumen de tráfico | $V = \sum_{j=1}^{n} t_j$ | minutos-Erlang |
| Tasa de tomas | $i = \dfrac{n}{T}$ | tomas/minuto |
| Tiempo medio de ocupación | $t' = \dfrac{V}{n}$ | minutos/toma |
| Tráfico cursado | $A' = \dfrac{V}{T} = i\,t'$ | Erlangs |
| Congestión en el tiempo | $E = \dfrac{t}{T}$ | adimensional (%) |
| Congestión en las llamadas | $B = \dfrac{P}{N}$ | adimensional (%) |

- $t$ = suma de los periodos en que todos los circuitos están ocupados a la vez.
- $P$ = número de intentos de llamada que encuentran todos los circuitos ocupados.
- En $B = P/N$, $N$ = llamadas cursadas + intentos perdidos (no es el número de circuitos).
- En las diapositivas el tráfico cursado se escribe $A'$.

---

### N10. VERIFICACIONES

- $V = \sum_j t_j$ (por circuitos) debe coincidir con $\sum_i k_i\,\Delta t_i$ (por intervalos).
- El tráfico cursado no puede superar el número de circuitos: $A' \le N$.
- Ningún nivel puede superar $N$.
- Si el enunciado da $V$ o $A'$ y no coinciden con lo leído, revisar la lectura de los tramos antes de graficar.

---

## BLOQUE C — PLANTILLAS Y EJEMPLO RESUELTO

Todos los ejemplos de esta sección corresponden al Ejercicio 4 del primer parcial ETN-1012 (marzo 2022): 7 circuitos, $T = 60$ min.

---

### N11. PLANTILLA — OCUPACIÓN INDIVIDUAL

> Contexto para NotebookLM: una etiqueta por circuito en `x=-2` y un segmento por cada tramo. Cambiar `N` (top = N+1) y los tramos según el ejercicio.

```desmos-graph
left=-4; right=63; bottom=0; top=8;
width=550; height=300;
---
(-2,1)|label:1|hidden|#474448
(-2,2)|label:2|hidden|#474448
(-2,3)|label:3|hidden|#474448
(-2,4)|label:4|hidden|#474448
(-2,5)|label:5|hidden|#474448
(-2,6)|label:6|hidden|#474448
(-2,7)|label:7|hidden|#474448
y=7|0<=x<=10|#005F73
y=7|15<=x<=20|#005F73
y=7|30<=x<=40|#005F73
y=7|50<=x<=60|#005F73
y=6|5<=x<=20|#005F73
y=6|25<=x<=35|#005F73
y=6|40<=x<=50|#005F73
y=5|0<=x<=10|#005F73
y=5|15<=x<=25|#005F73
y=5|30<=x<=35|#005F73
y=5|50<=x<=60|#005F73
y=4|5<=x<=20|#005F73
y=4|30<=x<=40|#005F73
y=4|45<=x<=55|#005F73
y=3|0<=x<=10|#005F73
y=3|15<=x<=20|#005F73
y=3|25<=x<=35|#005F73
y=3|45<=x<=55|#005F73
y=2|5<=x<=20|#005F73
y=2|25<=x<=35|#005F73
y=2|40<=x<=45|#005F73
y=2|50<=x<=60|#005F73
y=1|0<=x<=10|#005F73
y=1|15<=x<=20|#005F73
y=1|30<=x<=40|#005F73
y=1|45<=x<=50|#005F73
y=1|55<=x<=60|#005F73
```

Tabla de tramos del ejemplo:

| Circuito | Tramos (min) | $\sum t_j$ |
|:-:|---|:-:|
| 1 | 0–10, 15–20, 30–40, 45–50, 55–60 | 35 |
| 2 | 5–20, 25–35, 40–45, 50–60 | 40 |
| 3 | 0–10, 15–20, 25–35, 45–55 | 35 |
| 4 | 5–20, 30–40, 45–55 | 35 |
| 5 | 0–10, 15–25, 30–35, 50–60 | 35 |
| 6 | 5–20, 25–35, 40–50 | 35 |
| 7 | 0–10, 15–20, 30–40, 50–60 | 35 |

$V = 250$ minutos-Erlang, $n = 27$ tomas.

---

### N12. PLANTILLA — OCUPACIÓN SIMULTÁNEA (LÍNEA ESCALONADA)

> Contexto para NotebookLM: un segmento horizontal por intervalo y un conector vertical por cada cambio de nivel. Empieza con el conector desde 0. La línea gris punteada marca el nivel `N`. Las etiquetas numéricas sobre el nivel `N` indican la duración de cada tramo de congestión.

Niveles del ejemplo (intervalos de 5 min): 4, 7, 3, 7, 1, 3, 7, 3, 2, 4, 5, 4.

| Intervalo (min) | 0–5 | 5–10 | 10–15 | 15–20 | 20–25 | 25–30 | 30–35 | 35–40 | 40–45 | 45–50 | 50–55 | 55–60 |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Circuitos ocupados | 4 | 7 | 3 | 7 | 1 | 3 | 7 | 3 | 2 | 4 | 5 | 4 |

```desmos-graph
left=-3; right=63; bottom=-0.5; top=8;
width=550; height=300;
---
y=7|0<=x<=60|#A3A2A4|DASHED
x=0|0<=y<=4|#C1121F
y=4|0<=x<=5|#C1121F
x=5|4<=y<=7|#C1121F
y=7|5<=x<=10|#C1121F
x=10|3<=y<=7|#C1121F
y=3|10<=x<=15|#C1121F
x=15|3<=y<=7|#C1121F
y=7|15<=x<=20|#C1121F
x=20|1<=y<=7|#C1121F
y=1|20<=x<=25|#C1121F
x=25|1<=y<=3|#C1121F
y=3|25<=x<=30|#C1121F
x=30|3<=y<=7|#C1121F
y=7|30<=x<=35|#C1121F
x=35|3<=y<=7|#C1121F
y=3|35<=x<=40|#C1121F
x=40|2<=y<=3|#C1121F
y=2|40<=x<=45|#C1121F
x=45|2<=y<=4|#C1121F
y=4|45<=x<=50|#C1121F
x=50|4<=y<=5|#C1121F
y=5|50<=x<=55|#C1121F
x=55|4<=y<=5|#C1121F
y=4|55<=x<=60|#C1121F
(7.5,7.4)|label:5|hidden|#474448
(17.5,7.4)|label:5|hidden|#474448
(32.5,7.4)|label:5|hidden|#474448
```

Patrón general por intervalo $[t_i,\,t_{i+1}]$ con nivel $k_i$ y nivel anterior $k_{i-1}$:

```
x=t_i|min(k_{i-1},k_i)<=y<=max(k_{i-1},k_i)|#C1121F
y=k_i|t_i<=x<=t_{i+1}|#C1121F
```

(sustituir los valores numéricos; el patrón está escrito con símbolos solo como referencia.)

---

### N13. RESULTADO DEL EJEMPLO

$$
V = \sum_{j=1}^{n} t_j = 35 + 40 + 35 + 35 + 35 + 35 + 35 = 250\ \text{minutos-Erlang}
$$

$$
A' = \frac{V}{T} = \frac{250}{60} = 4{,}167\ \text{Erlangs}
$$

Verificación: $\sum k\,\Delta t = 5\,(4+7+3+7+1+3+7+3+2+4+5+4) = 5 \times 50 = 250$.

Los 7 circuitos están ocupados a la vez en 5–10, 15–20 y 30–35 min: $t = 15$ min.

$$
E = \frac{t}{T} = \frac{15}{60} = 0{,}25 \quad (25\%)
$$

---

## CHECKLIST — ANTES DE RESPONDER

### N14.

- [ ] ¿Dice exactamente tres backticks seguidos de `desmos-graph` en la línea de apertura?
- [ ] ¿Tiene `---` y los parámetros en orden ventana → tamaño?
- [ ] ¿Todos los parámetros terminan en `;` y no hay espacios alrededor de `|`?
- [ ] ¿La ventana usa `top = N+1` y `right = T+3` con valores numéricos?
- [ ] ¿Un segmento por tramo, con `<=` en ambos extremos?
- [ ] Simultánea: ¿hay un conector vertical en cada cambio de nivel y uno inicial desde 0?
- [ ] Simultánea: ¿sin conector de cierre en `x=T` y sin conectores donde el nivel no cambia?
- [ ] ¿Etiquetas con `hidden` y texto plano (sin LaTeX)?
- [ ] ¿Colores en hex (`#005F73` individual, `#C1121F` simultánea) y `DASHED` en mayúsculas?
- [ ] ¿$\sum k\,\Delta t = V$ y $A' \le N$?
- [ ] ¿Fórmulas con la notación del formulario ($V$, $i$, $t'$, $A'$, $E$, $B$)?

---

%%
# galaxy-links
[[_app/_config/_galaxy-system.md]]
[[_app/_config/_note-system.md]]
%%
