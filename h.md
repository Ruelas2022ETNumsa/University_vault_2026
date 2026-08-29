```
MODULE: TEST
MEMORY: AC; flag
OUTPUTS: done
INPUTS: go
COMBUS: DBUS

1. → (~go)/(1)
2. AC ← DBUS; flag ← 1
3. done = 1
4. DEAD END
END SEQUENCE
END
```

| Paso | Operación                                         | Condición           | Estado resultante                                                                                                                                 |
| ---- | ------------------------------------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `1.` | \( \rightarrow 1 \)                               | \( \overline{go} \) | Bucle de espera (polling). Si la señal de entrada \( go \) es 0, el control retorna al paso 1; de lo contrario, avanza al paso 2.                 |
| `2.` | \( AC \leftarrow DBUS \); \( flag \leftarrow 1 \) | —                   | Transferencia activa por flanco de reloj. Se carga el valor del bus \( DBUS \) en el registro \( AC \) y el flip-flop \( flag \) se pone en 1.    |
| `3.` | \( done = 1 \)                                    | —                   | Conexión de bus combinacional. La señal de salida \( done \) se mantiene activa en nivel lógico alto sin intervención de reloj durante este paso. |
| `4.` | \( DEAD\ END \)                                   | —                   | Terminación de la secuencia de control. Se desactivan todos los flip-flops de control para detener la propagación.                                |