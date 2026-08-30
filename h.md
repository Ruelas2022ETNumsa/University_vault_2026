```text
MODULE: TEST
MEMORY: AC(8); flag
OUTPUTS: done
INPUTS: go
COMBUS: DBUS(8)

1. → (~go)/(1)
2. AC ← DBUS; flag ← 1
3. done = 1
4. DEAD END
END SEQUENCE
END
```

| Paso | Operación                                          | Condición           | Estado resultante                                                                                                                                                           |
| :--- | :------------------------------------------------- | :------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `1.` | \( \rightarrow (\overline{go})/(1) \)              | \( \overline{go} \) | Bucle de espera. Retorna al paso 1 mientras \( go = 0 \); transiciona al paso 2 cuando \( go = 1 \).                                                                        |
| `2.` | \( AC \leftarrow DBUS \) ; \( flag \leftarrow 1 \) | —                   | Transferencia síncrona. Al flanco de reloj, el registro \( AC(8) \) se carga con el valor de \( DBUS(8) \) y el flip-flop \( flag \) se establece en 1 de forma simultánea. |
| `3.` | \( done = 1 \)                                     | —                   | Conexión combinacional. La salida de bus \( done \) se activa en nivel alto sin sincronización de reloj durante este ciclo de control.                                      |
| `4.` | \( DEAD\ END \)                                    | —                   | Fin de secuencia. Se detiene la propagación del nivel de control.                                                                                                           |


---

copiando con el puntero

MODULE: TEST
MEMORY: AC(8); flag
OUTPUTS: done
INPUTS: go
COMBUS: DBUS(8)

1. → (~go)/(1)
2. AC ← DBUS; flag ← 1
3. done = 1
4. DEAD END
END SEQUENCE
END
``` [1]

| Paso | Operación | Condición | Estado resultante |
| :--- | :--- | :--- | :--- |
| `1.` | \( \rightarrow (\overline{go})/(1) \) | \( \overline{go} \) | Bucle de espera. Retorna al paso 1 mientras \( go = 0 \); transiciona al paso 2 cuando \( go = 1 \) [1]. |
| `2.` | \( AC \leftarrow DBUS \) ; \( flag \leftarrow 1 \) | — | Transferencia síncrona. Al flanco de reloj, el registro \( AC(8) \) se carga con el valor de \( DBUS(8) \) y el flip-flop \( flag \) se establece en 1 de forma simultánea [1]. |
| `3.` | \( done = 1 \) | — | Conexión combinacional. La salida de bus \( done \) se activa en nivel alto sin sincronización de reloj durante este ciclo de control [1]. |
| `4.` | \( DEAD\ END \) | — | Fin de secuencia. Se detiene la propagación del nivel de con