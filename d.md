## Transferencias Condicionales en AHPL con el Operador *

En el lenguaje AHPL, el **asterisco (\(*\))** se utiliza como el operador de condición para habilitar transferencias y conexiones lógicas. A continuación, se presentan los dos ejemplos exactos extraídos de la literatura oficial (Capítulo 4, pág. 105) junto con sus bloques de código estándar y explicaciones correspondientes:

### Ejemplo 1: Destino condicionado
**A recibe B solo si a = 0, y D recibe C solo si a = 1 — en el mismo paso**.

```
A * ~a <- B ; D * a <- C
```

*   **¿Qué hace el operador \(*\)?**
    En este ejemplo, el asterisco está ubicado a la **izquierda** de la asignación (asociado a los vectores de destino \(A\) y \(D\)). Cuando se coloca a la izquierda, las condiciones **controlan las entradas de reloj (*clock control*) de los flip-flops en los registros**.
    Esto significa que el pulso de reloj del sistema solo afectará a los flip-flops del registro destino si su correspondiente variable de control vale \(1\):
    *   El registro \(A\) recibirá el contenido de \(B\) si y solo si \(\overline{a} = 1\) (es decir, \(a = 0\)).
    *   El registro \(D\) recibirá el contenido de \(C\) si y solo si \(a = 1\).
    *   Al estar separados por un punto y coma `;` en un mismo paso, ambas transferencias condicionales se evalúan y ejecutan de manera **simultánea en el mismo ciclo de reloj**.

---

### Ejemplo 2: Origen seleccionado
**D recibe uno de tres registros (A, B o C) según cuál de las señales f, g, h vale 1**.

```
D <- (A ! B ! C) * (f, g, h)
```

*   **¿Qué hace el operador \(*\)?**
    En este caso, el asterisco está ubicado en el **lado derecho** de la asignación (afectando a los operandos de origen). Cuando se coloca a la derecha, las condiciones **especifican circuitos de bus para los vectores de datos**.
    Este esquema asume que las variables de control del vector \((f, g, h)\) son **mutuamente excluyentes** (solo una de ellas puede valer \(1\) a la vez), de manera que actúa como un multiplexor que selecciona el origen:
    *   Si \(f = 1\), se transfiere el registro \(A\) hacia \(D\).
    *   Si \(g = 1\), se transfiere el registro \(B\) hacia \(D\).
    *   Si \(h = 1\), se transfiere el registro \(C\) hacia \(D\).
    *   Si todas las señales de control valen \(0\) (\(f=g=h=0\)), no se selecciona ningún registro y **se transferirá un vector de ceros** hacia \(D\).

*   **¿Qué hace el operador \(!\)?**
    El operador **signo de exclamación (\(!\))** representa la operación de **concatenación de filas** (*row catenation*). En la sintaxis de AHPL, **no tiene una función de negación lógica o NOT booleana**. Su propósito es agrupar o encadenar horizontalmente los registros \(A\), \(B\) y \(C\) para conformar una matriz de vectores lógicos que el asterisco pueda indexar individualmente usando el vector condicional de control \((f, g, h)\).

---

💡 ¿Te gustaría que planteemos un ejercicio de examen resuelto aplicando este tipo de transferencias condicionales en un módulo interactivo?