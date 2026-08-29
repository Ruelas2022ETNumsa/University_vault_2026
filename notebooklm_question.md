# Snippets — preguntas para NotebookLM/Gemini (ETN825 AHPL N16)

> Copiar cada bloque y pegarlo en NotebookLM o Gemini con las fuentes cargadas.
> Capturar el output exacto — incluyendo errores de formato si los hay.
> Objetivo: obtener los pares pregunta→respuesta reales para construir N16 en ETN825_AHPL.md

---

## A — Módulo completo

```
Escribí un módulo AHPL completo para una interfaz simple.
El módulo debe:
- Esperar una señal de entrada llamada `start`
- Cuando `start = 1`: cargar el registro `DR[8]` desde el bus `IOBUS[8]`
- Activar la señal de salida `done` por un ciclo
- Terminar en DEAD END

Incluí todas las declaraciones (MODULE, MEMORY, OUTPUTS, INPUTS, COMBUS)
y la secuencia de control numerada completa.
Usá el formato de bloque de código para el módulo
y una tabla para la lectura paso a paso.
```

---

## B — Bucle de espera

```
Mostrá el patrón AHPL de un bucle de espera.
Necesito dos variantes en el mismo bloque de código:

Variante 1: el módulo espera mientras `ready = 0` y sale cuando `ready = 1`
Variante 2: el módulo espera mientras `wait = 1` y sale cuando `wait = 0`

Para cada variante mostrá el paso numerado exacto y explicá
cuál es la condición de retorno y cuál es la condición de salida.
```

---

## C — Bifurcación múltiple por bits

```
Escribí una bifurcación AHPL que evalúa los bits IR[0] e IR[1]
y salta a tres destinos distintos según la combinación de bits.

Mostrá el paso de bifurcación con formato → (condiciones)/(destinos)
donde las condiciones son mutuamente excluyentes.
Después explicá qué combinación de bits activa cada rama.
```

---

## D — Transferencia condicional con operador *

```
Mostrá cómo se escribe en AHPL una transferencia condicional
usando el operador * (asterisco).

Necesito exactamente estos dos ejemplos del libro (capítulo 4, p. 105):

Ejemplo 1: A recibe B solo si a = 0, y D recibe C solo si a = 1 — en el mismo paso
Ejemplo 2: D recibe uno de tres registros (A, B o C) según cuál de las señales f, g, h vale 1

Para cada ejemplo: mostrá el código AHPL exacto y explicá
qué hace el operador * y qué hace el operador ! en el ejemplo 2.
```

---

## E — Operador ! (row concatenate) aislado

```
En AHPL según Hill & Peterson Digital Systems 2ª ed.,
¿qué hace exactamente el operador ! (signo de exclamación)?

Explicá la diferencia entre:
- concatenación simple con coma: (X, Y)
- row concatenate con !: (A ! B)

Mostrá un ejemplo concreto del libro con número de página
donde aparezca el operador ! en una expresión real.
```

---

## F — Verificación de convención de negado en bloques de código

```
En los bloques de código AHPL del libro Hill & Peterson Digital Systems 2ª ed.
(las secuencias numeradas, no el texto matemático),
¿cómo se escribe el NOT de una señal?

¿Se usa tilde ~ como prefijo, barra superior sobre el símbolo, o NOT()?
Mostrá exactamente 2 ejemplos de secuencias numeradas del libro
con la señal negada dentro de una bifurcación → (cond)/(dest).
Indicá la página de cada ejemplo.
```

---

## G — Módulo PRINTER INTERFACE completo

```
Transcribí el módulo PRINTER INTERFACE completo de Hill & Peterson
Digital Systems 2ª ed., Example 9.3 (p. 349-350).

Incluí:
- Todas las declaraciones (MODULE, MEMORY, OUTPUTS, INPUTS, COMBUS)
- Todos los pasos numerados con sus subpasos si los hay
- El END SEQUENCE, la expresión combinacional CHAR = CR, y el END final

Usá bloque de código para el módulo completo
y una tabla para la lectura paso a paso con KaTeX inline para operadores.
```

---

## H — Prueba de formato puro

```
Escribí el siguiente módulo AHPL exactamente como aparecería
en un bloque de código estándar (texto plano con la notación del libro):

MODULE: TEST
MEMORY: AC[8]; flag
OUTPUTS: done
INPUTS: go
COMBUS: DBUS[8]

1. → (~go)/(1)
2. AC ← DBUS; flag ← 1
3. done = 1
4. DEAD END
END SEQUENCE
END

Después de el bloque de código, mostrá una tabla paso a paso
con KaTeX inline para los operadores (← y =).
No uses \begin{aligned}, no uses $$, no uses \begin{array}.
```

---

## Orden de consulta sugerido

1. **H primero** — prueba de formato puro. Si el output ya es correcto (bloque + tabla KaTeX inline sin `\begin{aligned}`), los demás probablemente también lo sean.
2. **G** — módulo conocido con fuente verificable en el libro. Permite comparar contra la respuesta real confirmada en sesiones anteriores.
3. **A, B, C, D** — patrones nuevos para N16.
4. **E, F** — si quedan dudas sobre operadores específicos después de ver los outputs anteriores.

---

## Qué registrar por output

Para cada respuesta capturada, anotar:
- ¿Usó bloque de código para el módulo AHPL? (sí/no)
- ¿Usó tabla con KaTeX inline para la lectura? (sí/no)
- ¿Apareció `\begin{aligned}` o `$$`? (sí/no)
- ¿Los operadores son correctos? (`←`, `=`, `~`, `∧`, `∨`, `!`, `*`)
- ¿Las declaraciones tienen tamaño entre corchetes? (`DR[18]`, no `DR`)
- Errores puntuales si los hay
