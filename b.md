```ahpl
1. -> (~ready)/(1)
2. -> (wait)/(2)
```

### **Variante 1: Espera activa en cero (Wait while 0)**
* **Paso numerado exacto:** 
  `1. -> (~ready)/(1)`
* **Condición de retorno:** **`~ready`** (equivalente a **`ready = 0`**). Mientras la señal de entrada sea `0`, el término evaluado es verdadero y el secuenciador bifurca hacia el mismo paso 1, manteniendo el bucle de espera.
* **Condición de salida:** **`ready = 1`**. Cuando la señal de entrada cambia a `1`, la condición de retorno `~ready` se vuelve falsa, interrumpiendo la bifurcación y permitiendo al módulo continuar automáticamente al paso de control inmediatamente posterior.

### **Variante 2: Espera activa en uno (Wait while 1)**
* **Paso numerado exacto:** 
  `2. -> (wait)/(2)`
* **Condición de retorno:** **`wait`** (equivalente a **`wait = 1`**). Mientras la señal de entrada permanezca en `1`, la condición se cumple y el control vuelve a cargarse en el flip-flop de control correspondiente al paso 2.
* **Condición de salida:** **`~wait`** (equivalente a **`wait = 0`**). En el instante en que la señal de entrada cae a `0`, la condición evaluada en la bifurcación se vuelve falsa, lo cual rompe el bucle y hace que el control avance al siguiente paso secuencial.

