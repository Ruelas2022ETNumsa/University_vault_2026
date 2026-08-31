El operador **`!`** representa la **concatenación de filas** (*row catenation*). Su función exacta en el hardware es agrupar múltiples registros o vectores horizontales de manera vertical para estructurar una matriz combinacional (colocando una fila sobre la otra). 

Físicamente, este operador no realiza una acción lógica por sí mismo (como una negación), sino que interconecta las salidas de los registros para formar las entradas de un multiplexor de bus.

---

### **Diferencia entre concatenación con coma `(X, Y)` y con exclamación `(A ! B)`**

* **Concatenación simple con coma `(X, Y)` (Column Catenation):**
  Une los vectores de forma **horizontal** para constituir un único vector plano más largo. Si la variable `\( X \)` posee un tamaño de `\( n \)` bits e `\( Y \)` de `\( m \)` bits, la expresión `\( (X, Y) \)` genera un nuevo vector continuo de `\( n + m \)` bits. Se suele emplear para operaciones de desplazamiento de bits, rotaciones o para empaquetar caracteres.

* **Row concatenate con exclamación `(A ! B)` (Row Catenation):**
  Apila los registros de forma **vertical** para construir una matriz sin alterar la longitud de palabra de los operandos. Si `\( A \)` y `\( B \)` son registros de `\( n \)` bits, la expresión `\( (A \mathop{!} B) \)` crea un arreglo de `\( 2 \times n \)` bits (una matriz de 2 filas). Se utiliza exclusivamente para la selección condicional de buses mediante multiplexores o decodificadores.

---

### **Ejemplo real del libro fuente**

En el libro de Hill & Peterson (*Digital Systems: Hardware Organization & Design*, 2ª ed., Sección 4.7, **página 105**), aparece la siguiente expresión de transferencia condicional con selección de origen:

```ahpl
D <- (A ! B ! C) * (f, g, h)
```

**Explicación del hardware descrito:**
1. Los tres registros de origen `\( A \)`, `\( B \)` y `\( C \)` se apilan mediante `!` para formar las filas de una matriz combinacional.
2. El operador condicional `*` actúa como el habilitador de las compuertas de enrutamiento.
3. Dependiendo de cuál de las señales de control mutuamente excluyentes `\( (f, g, h) \)` se active en `\( 1 \)`, la fila correspondiente de la matriz se propagará físicamente a través de las compuertas para cargarse en el registro de destino `\( D \)` al siguiente flanco de reloj.

---
💡 ¿Te gustaría que diseñemos el circuito esquemático con compuertas AND/OR y flip-flops que genera físicamente esta expresión combinacional `(A ! B) * (f, g)`?