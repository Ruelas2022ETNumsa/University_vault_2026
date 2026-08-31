```ahpl
MODULE: TEST
MEMORY: AC(8); flag
INPUTS: go
OUTPUTS: done
COMBUS: DBUS(8)

1. -> (~go)/(1)
2. AC <- DBUS; flag <- 1
3. done = 1
4. DEAD END
END SEQUENCE
END
```

| Paso | Operación                                                | Condición           | Estado resultante                                                                                                                                                                                                                            |
| :--- | :------------------------------------------------------- | :------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `1.` | \( \rightarrow (1) \)                                    | \( \overline{go} \) | **Bucle de espera (polling).** El secuenciador permanece retenido en el paso 1 mientras \( go = 0 \) (\( \overline{go} = 1 \)). Al recibir \( go = 1 \), la bifurcación se hace falsa y se avanza al paso 2 en el siguiente flanco de reloj. |
| `2.` | \( AC \leftarrow \text{DBUS} \); \( flag \leftarrow 1 \) | —                   | **Transferencia síncrona.** Al flanco de subida de reloj, el registro \( AC(8) \) se carga con el valor presente en el bus \( \text{DBUS}(8) \). De manera simultánea, el flip-flop de un bit \( flag \) se establece en \( 1 \).            |
| `3.` | \( done = 1 \)                                           | —                   | **Conexión de bus combinacional.** La señal de salida \( done \) se conecta directamente a nivel lógico \( 1 \) de forma combinacional, activa únicamente durante el ciclo de reloj en el que el control reside en este paso.                |
| `4.` | \( \text{DEAD END} \)                                    | —                   | **Terminación.** Finaliza la propagación del nivel de control dentro del módulo, provocando el reset automático de todos los flip-flops de estado de la unidad de control.                                                                   |