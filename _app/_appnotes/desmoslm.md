# INSTRUCCIONES PARA NOTEBOOKLM: Generación de Código Desmos para Obsidian

## PROPÓSITO DE ESTE DOCUMENTO

Este documento le enseña a NotebookLM cómo generar bloques de código Desmos compatibles con el plugin `obsidian-desmos`. Cuando el usuario pida graficar una ecuación o ejercicio, NotebookLM debe responder con un bloque de código listo para copiar y pegar en Obsidian, NO con una imagen ni un enlace externo.

---

## REGLA CRÍTICA NÚMERO 1 — EL SEPARADOR `---` ES OBLIGATORIO SIEMPRE

**El separador `---` es OBLIGATORIO en absolutamente todos los bloques, sin excepción.**
No importa si hay configuración o no. No importa si el bloque es simple o complejo.
**Sin `---` el plugin no renderiza la gráfica.**

### INCORRECTO — bloque sin `---` (NUNCA hacer esto):

```
```desmos-graph
width=500; height=500
y=x^2|BLUE
```
```

### CORRECTO — separador `---` siempre presente:

```
```desmos-graph
width=500; height=500;
---
y=x^2|BLUE
```
```

### CORRECTO — incluso sin configuración, el `---` va igual:

```
```desmos-graph
---
y=x^2|BLUE
```
```

**Regla absoluta: la línea `---` siempre está presente, separa configuración de ecuaciones.**

---

## ESTRUCTURA OBLIGATORIA DEL BLOQUE

```
```desmos-graph
[parámetros de configuración terminados en ;]
---
[ecuaciones, una por línea]
```
```

- **Línea 1:** ` ```desmos-graph `
- **Sección de configuración:** parámetros como `left=`, `right=`, `width=`, etc., cada uno terminado en `;`
- **Línea separadora:** `---` (SIEMPRE, sin excepción)
- **Sección de ecuaciones:** una ecuación por línea, con sus modificadores
- **Última línea:** ` ``` `

---

## PARÁMETROS DE CONFIGURACIÓN

Van **antes** del `---`, separados por `;` o saltos de línea. Cada parámetro termina en `;`.

| Parámetro | Qué hace | Valor típico |
|-----------|----------|--------------|
| `left` | Límite izquierdo del eje x | `-5` |
| `right` | Límite derecho del eje x | `5` |
| `bottom` | Límite inferior del eje y | `-3` |
| `top` | Límite superior del eje y | `3` |
| `width` | Ancho en píxeles | `500` |
| `height` | Alto en píxeles | `400` |
| `grid` | Mostrar cuadrícula | `true` o `false` |
| `degreeMode` | Modo ángulos | `degrees` o `radians` |

---

## SINTAXIS DE ECUACIONES

Las ecuaciones usan formato LaTeX matemático estándar. Van **después** del `---`.

### Ecuaciones básicas

| Matemática | Código a escribir |
|------------|-------------------|
| y = x² | `y=x^2` |
| y = √x | `y=\sqrt{x}` |
| y = 1/x | `y=\frac{1}{x}` |
| y = eˣ | `y=e^x` |
| y = sin(x) | `y=\sin(x)` |
| y = cos(x) | `y=\cos(x)` |
| y = ln(x) | `y=\ln(x)` |
| x² + y² = r² | `x^2+y^2=r^2` (circunferencia) |
| x = a | `x=a` (línea vertical) |
| y = b | `y=b` (línea horizontal) |

### Funciones definidas por el usuario

```
f(x)=2x+1
g(x)=x^2-3
```

Para graficar la derivada de una función definida:
```
f(x)=x^2|hidden
f'(x)|BLUE
```

El modificador `|hidden` oculta la curva base pero la mantiene disponible para usar.

---

## MODIFICADORES — COLOR, ESTILO Y RESTRICCIONES

Después de cada ecuación se agregan modificadores separados por `|`.

### Colores disponibles

```
|RED       → Rojo
|BLUE      → Azul
|GREEN     → Verde
|ORANGE    → Naranja
|PURPLE    → Morado
|YELLOW    → Amarillo
|MAGENTA   → Magenta
|CYAN      → Cian
|BLACK     → Negro
|WHITE     → Blanco
|#42ddf5   → Cualquier color hexadecimal
```

Colores claros recomendados para rellenos de área:
- `#a5d8ff` → Azul claro
- `#b2f2bb` → Verde claro
- `#ffd8a8` → Naranja claro
- `#d0bfff` → Morado claro

### Estilos de línea

```
|SOLID     → Línea continua (por defecto)
|DASHED    → Línea discontinua
|DOTTED    → Línea punteada
```

### Restricción de dominio

```
y=x^2|0<=x<=3            → Parábola solo entre x=0 y x=3
y=\sqrt{x}|x>=0          → Raíz solo donde está definida
x=2|0<=y<=5              → Línea vertical entre y=0 y y=5
y=\sin(x)|-3<=x<=0       → Seno en parte negativa
```

### Combinación de modificadores

Se pueden combinar en cualquier orden:
```
y=x^2|RED|DASHED|0<=x<=3
```

---

## ÁREAS SOMBREADAS (INECUACIONES)

Para sombrear una región, usar una inecuación. Para la intersección de varias condiciones, ponerlas todas en una sola línea separadas por `|`:

```
y<x^2                         → Debajo de la parábola
y>x                           → Encima de y=x
x^2+y^2<4                     → Interior del círculo radio 2
y<2-x|y>x|x>=0|x<=1|#a5d8ff  → Intersección con color
```

**Nota:** Para rellenos usar siempre colores hexadecimales claros. Los colores con nombre (RED, BLUE, etc.) salen demasiado saturados en áreas sombreadas.

---

## PUNTOS Y ETIQUETAS

```
(1,2)                      → Punto sólido en (1,2)
(1,2)|OPEN                 → Punto hueco (límite excluido)
(1,2)|CROSS                → Punto en cruz
(1,2)|label:texto          → Punto con etiqueta
(1,2)|OPEN|label:(1,2)     → Combinación estilo + etiqueta
```

---

## EJEMPLOS COMPLETOS

Todos los ejemplos incluyen el `---` obligatorio.

### Ejemplo 1: Función cuadrática simple

```desmos-graph
left=-4; right=4; bottom=-2; top=6;
width=500; height=400;
---
y=x^2|BLUE
```

### Ejemplo 2: Varias funciones con colores

```desmos-graph
left=-5; right=5; bottom=-3; top=3;
width=500; height=400;
---
y=\sin(x)|BLUE|SOLID
y=\cos(x)|RED|DASHED
y=\frac{1}{2}x|GREEN|DOTTED
```

### Ejemplo 3: Región sombreada entre dos curvas

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

### Ejemplo 4: Región triangular (útil para probabilidad conjunta)

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

### Ejemplo 5: Función con derivada

```desmos-graph
left=-3; right=3; bottom=-5; top=5;
width=500; height=400;
---
f(x)=x^3-3x|hidden
f(x)|BLUE|SOLID
f'(x)|RED|DASHED
```

### Ejemplo 6: Densidad de probabilidad con media marcada

```desmos-graph
left=-0.2; right=1.2; bottom=-0.1; top=1.8;
width=600; height=400;
---
f(x)=6x(1-x)|0<=x<=1|BLUE|SOLID
x=0.5|0<=y<=1.5|GREEN|DASHED
(0.5,0)|label:mu=0.5|GREEN
```

---

## CÓMO RESPONDER CUANDO EL USUARIO PIDE UNA GRÁFICA

1. **Identificar** qué curvas, regiones o puntos hay que representar.
2. **Calcular** los límites adecuados del plano (que todas las curvas queden visibles con margen).
3. **Asignar** colores distintos a cada curva.
4. **Generar** el bloque `desmos-graph` completo con el `---` en su lugar.
5. **Explicar brevemente** qué representa cada línea del bloque.

### Reglas de buenas prácticas

- El separador `---` es SIEMPRE obligatorio, incluso si la sección de configuración está vacía.
- Todos los parámetros de configuración terminan en `;`.
- Usar `width=500; height=400` para funciones regulares y `width=500; height=500` para plano cuadrado.
- Usar restricciones de dominio cuando la función tenga dominio natural limitado.
- Usar colores hexadecimales claros para rellenos de área.
- Etiquetar los puntos clave con `|label:`.

---

## PLANTILLA UNIVERSAL

```
```desmos-graph
left=-5; right=5; bottom=-5; top=5;
width=500; height=500;
---
[ecuaciones aquí]
```
```

---

## RESUMEN DE SINTAXIS

```
[configuracion;]        ← parámetros antes del separador
---                     ← OBLIGATORIO SIEMPRE
y=ec|COLOR|ESTILO|rest  ← curva con modificadores
y<ec|y>otra|#hexcolor   ← área sombreada
(x,y)|OPEN|label:texto  ← punto etiquetado
f(x)=ec|hidden          ← función oculta reutilizable
```
