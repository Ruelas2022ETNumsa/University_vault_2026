```ahpl
1. -> (~IR(0) /\ ~IR(1), ~IR(0) /\ IR(1), IR(0))/(5, 8, 12)
```

### **Explicación de las ramas y combinaciones**

Las tres condiciones especificadas en la bifurcación son **mutuamente excluyentes** y cubren la totalidad del espacio de estados de los dos bits evaluados:

1. **Primera rama (Destino `5`):** 
   * **Condición:** \( \overline{IR}_{0} \land \overline{IR}_{1} \) (en el bloque de código: `~IR(0) /\ ~IR(1)`).
   * **Combinación activa:** Se activa únicamente cuando **`IR(0) = 0` e `IR(1) = 0`** (combinación binaria **`00`**).

2. **Segunda rama (Destino `8`):** 
   * **Condición:** \( \overline{IR}_{0} \land IR_{1} \) (en el bloque de código: `~IR(0) /\ IR(1)`).
   * **Combinación activa:** Se activa únicamente cuando **`IR(0) = 0` e `IR(1) = 1`** (combinación binaria **`01`**).

3. **Tercera rama (Destino `12`):** 
   * **Condición:** \( IR_{0} \) (en el bloque de código: `IR(0)`).
   * **Combinación activa:** Se activa cuando **`IR(0) = 1`**, sin importar el estado del bit `IR(1)`. Esto agrupa y resuelve de manera simplificada las combinaciones binarias **`10`** y **`11`**.