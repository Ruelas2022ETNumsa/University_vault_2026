# CONTEXTO DE TRABAJO — PROCESOS ESTOCÁSTICOS 806

## INSTRUCCIÓN INMEDIATA — LEER AL CARGAR ESTE ARCHIVO

Cuando el usuario comparta este archivo, Claude debe hacer lo siguiente **antes de responder cualquier otra cosa**:

1. Leer el archivo `E:\University_vault_2026\Formulario_806_ii.md` completo.
2. Confirmar al usuario con un mensaje breve: *"Contexto cargado. Formulario leído. Listo para revisar ejercicios."*

No esperar a que el usuario pida revisar un ejercicio. La lectura del formulario es el primer paso obligatorio al iniciar la conversación con este contexto.

---

## PROPÓSITO DE ESTE DOCUMENTO

Este documento describe el flujo de trabajo completo para resolver, revisar y graficar ejercicios de **Variables Aleatorias Continuas Múltiples** (Procesos Estocásticos 806). Define qué notas existen, qué rol cumple cada una, y cómo debe actuar Claude en cada etapa.

---

## NOTAS DEL SISTEMA

| Nota | Ubicación | Rol |
|------|-----------|-----|
| `Formulario_806_ii.md` | `E:\University_vault_2026\` | Fuente de verdad matemática. Contiene todas las fórmulas, definiciones y procedimientos válidos para el curso. |
| `desmoslm.md` | `E:\University_vault_2026\_app\_appnotes\` | Instrucciones para generar bloques `desmos-graph` compatibles con Obsidian. |
| `E1.md`, `E2.md`, `E3.md`, ... | `E:\University_vault_2026\` | Ejercicios resueltos por NotebookLM. Cada archivo contiene un enunciado y su resolución por incisos. Claude los revisa y corrige. |

---

## FLUJO DE TRABAJO

```
1. El usuario pide a NotebookLM resolver un ejercicio
         ↓
2. NotebookLM genera la respuesta (enunciado + resolución por incisos)
         ↓
3. El usuario guarda esa respuesta en Obsidian como E1.md, E2.md, etc.
         ↓
4. El usuario le pide a Claude que revise el archivo
         ↓
5. Claude lee el ejercicio y lo verifica contra el Formulario_806_ii.md
         ↓
6. Claude agrega correcciones debajo de cada inciso usando callouts
         ↓
7. Si hay gráficas mal ubicadas, Claude las separa por inciso y las reubica
```

---

## ROL DE CLAUDE EN LA REVISIÓN

Cuando el usuario pida revisar un ejercicio `E1.md`, `E2.md`, etc., Claude debe:

### 1. Verificar contra el formulario

El formulario ya fue leído al iniciar la sesión. Usarlo como única fuente de verdad matemática para verificar procedimientos, fórmulas y resultados.

### 2. Revisar inciso por inciso

Recorrer el ejercicio inciso por inciso (a, b, c, ...) y en cada uno verificar:

- Que el planteamiento de la integral sea correcto (límites, orden de integración, región).
- Que la fórmula aplicada corresponda al formulario.
- Que el desarrollo algebraico sea correcto paso a paso.
- Que el resultado final sea correcto.
- Que los límites de integración sean consistentes con la región del problema.

### 3. Agregar correcciones con callout

Si un inciso tiene errores, agregar **debajo del inciso** (sin borrar ni modificar el contenido original) un bloque callout en este formato:

```
> [!correction] Corrección
> **Error identificado:** [descripción del error]
>
> **Corrección:**
> [desarrollo correcto paso a paso]
>
> **Resultado correcto:** [resultado final]
```

Si el inciso está correcto, agregar:

```
> [!check] Correcto
> Procedimiento y resultado verificados con el formulario.
```

### 4. No sobreescribir el contenido original

Claude NUNCA borra ni modifica el texto original del ejercicio. Solo agrega callouts debajo de cada inciso. El usuario debe poder ver el original y la corrección en paralelo.

---

## MANEJO DE GRÁFICAS DESMOS EN LOS EJERCICIOS

### Problema frecuente

NotebookLM tiende a generar todas las gráficas del ejercicio en un solo bloque `desmos-graph` al final del archivo, mezclando ecuaciones de distintos incisos.

### Lo que Claude debe hacer

Cuando encuentre gráficas mal ubicadas (todas juntas al final), debe:

1. **Identificar** a qué inciso pertenece cada ecuación o región graficada.
2. **Separar** el bloque original en bloques individuales, uno por inciso.
3. **Reubicar** cada bloque dentro del inciso correspondiente, inmediatamente después del desarrollo matemático de ese inciso.
4. **Eliminar** el bloque original acumulado al final.

### Formato correcto para cada gráfica

Cada gráfica debe ir dentro de su inciso con una etiqueta clara:

```
#### Gráfica — inciso [letra]

```desmos-graph
left=; right=; bottom=; top=;
width=500; height=500;
---
[ecuaciones del inciso]
```
```

### Reglas para generar/corregir bloques Desmos

- El separador `---` es SIEMPRE obligatorio.
- Cada inciso tiene su propio bloque independiente.
- Ajustar `left`, `right`, `bottom`, `top` para que la región del inciso quede bien visible.
- Usar colores hexadecimales claros para rellenos: `#a5d8ff`, `#b2f2bb`, `#ffd8a8`, `#d0bfff`.
- Etiquetar los puntos clave (vértices, intersecciones, medias) con `|label:`.
- Solo generar gráfica si aporta claridad visual al resultado. No todos los incisos la necesitan.

---

## TEMAS CUBIERTOS POR EL FORMULARIO

El formulario `Formulario_806_ii.md` cubre los siguientes temas. Claude debe verificar que los ejercicios usen correctamente:

1. **Función de densidad de probabilidad** — propiedades, normalización, $P(a \leq X \leq b)$
2. **Esperanza matemática** — $E[X]$, $E[g(X,Y)]$, linealidad
3. **Varianza** — $VAR[X] = E[X^2] - \mu_X^2$, desviación estándar
4. **Densidad conjunta** — propiedades, normalización doble, probabilidad en región $R$
5. **Función de distribución acumulativa conjunta** — $F_{X,Y}(x,y)$ y sus propiedades marginales
6. **Densidades marginales** — $f_X(x)$, $f_Y(y)$ por integración
7. **Independencia estadística** — verificación por $f_{X,Y} = f_X \cdot f_Y$
8. **Valor esperado de dos variables** — $E[W]$ con $W = g(X,Y)$
9. **Varianza de la suma y covarianza** — $VAR[X+Y]$, $COV[X,Y] = E[XY] - \mu_X\mu_Y$
10. **Coeficiente de correlación** — $\rho_{X,Y}$, rango $[-1, 1]$
11. **Densidad condicional** — dado evento $B$ y dado otra variable

---

## ERRORES COMUNES A VIGILAR

- **Límites de integración incorrectos** — región mal interpretada del enunciado (el error más común).
- **Orden de integración invertido** — integrar primero en $x$ cuando corresponde en $y$ o viceversa.
- **Constante $k$ mal calculada** — error al despejar $k$ de la condición de normalización.
- **Marginal con límites fijos en vez de variables** — usar números donde deberían ir expresiones en $x$ o $y$.
- **Independencia mal verificada** — concluir independencia sin hacer el producto $f_X \cdot f_Y$ explícitamente.
- **Covarianza mal calculada** — confundir $E[XY]$ con $E[X] \cdot E[Y]$.
- **Densidad condicional sin normalizar** — olvidar dividir por $P[B]$.
- **Gráficas de todos los incisos mezcladas en un solo bloque** — separar siempre por inciso.

---

## EJEMPLO DE ESTRUCTURA ESPERADA EN UN EJERCICIO EN.md

```markdown
# Ejercicio N — [título o descripción breve]

## Enunciado
[texto del enunciado]

## Inciso a)
[desarrollo de NotebookLM]

> [!correction] Corrección
> **Error identificado:** ...
> **Corrección:** ...
> **Resultado correcto:** ...

#### Gráfica — inciso a)
```desmos-graph
left=; right=; bottom=; top=;
width=500; height=500;
---
[ecuaciones del inciso a]
```

## Inciso b)
[desarrollo de NotebookLM]

> [!check] Correcto
> Procedimiento y resultado verificados con el formulario.
```

---

## NOTAS FINALES

- Si una fórmula del ejercicio no aparece en el formulario, señalarlo explícitamente.
- Si el enunciado es ambiguo (región no especificada, función incompleta), indicarlo antes de corregir.
- Los ejercicios `E1.md`, `E2.md`, etc. pueden tener cualquier combinación de temas. No asumir estructura fija.
