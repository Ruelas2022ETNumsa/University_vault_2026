```text
MODULE: TEST
MEMORY: AC(8); flag
OUTPUTS: done
INPUTS: go
COMBUS: DBUS(8)

1. -> (~go)/(1)
2. AC <- DBUS; flag <- 1
3. done = 1
4. DEAD END
END SEQUENCE
END
```

| Paso | Operación                                         | Condición           | Estado resultante                                                                                                                                |
| :--- | :------------------------------------------------ | :------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------- |
| `1.` | \( \rightarrow (\overline{go})/(1) \)             | \( \overline{go} \) | Bucle de espera. Retorna al paso 1 mientras \( go = 0 \); continúa al paso 2 cuando \( go = 1 \).                                                |
| `2.` | \( AC \leftarrow DBUS \); \( flag \leftarrow 1 \) | —                   | Transferencia síncrona. El registro \( AC(8) \) se carga desde el bus \( DBUS(8) \) y el flip-flop \( flag \) se activa en 1 al flanco de reloj. |
| `3.` | \( done = 1 \)                                    | —                   | Conexión combinacional. La salida \( done \) se conecta a 1 de forma directa (sin reloj) durante este paso.                                      |
| `4.` | \( DEAD\ END \)                                   | —                   | Fin de la secuencia de control. El control se detiene.                                                                                           |