| Identificador | Sección | Tamaño | Rol |
|---|---|---|---|
| `AC` | MEMORY | `(8)` | Registro acumulador; recibe el valor del bus `DBUS` al flanco de reloj |
| `flag` | MEMORY | escalar | Flip-flop escalar de control; se establece en 1 en el paso 2 |
| `done` | OUTPUTS | escalar | Señal de salida combinacional; activa en nivel alto durante el paso 3 |
| `go` | INPUTS | escalar | Señal de entrada de habilitación; controla el bucle de espera en el paso 1 |
| `DBUS` | COMBUS | `(8)` | Bus combinacional de entrada; fuente de datos para el registro `AC` |

```
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

| Paso | Operación | Condición | Estado resultante |
|---|---|---|---|
| `1.` | \( \rightarrow (\overline{go})/(1) \) | \( \overline{go} \) | Bucle de espera activa. Retorna al paso 1 mientras \( go = 0 \); avanza al paso 2 cuando \( go = 1 \). |
| `2.` | \( AC \leftarrow DBUS \); \( flag \leftarrow 1 \) | — | Transferencia síncrona. El registro \( AC(8) \) se carga desde el bus \( DBUS(8) \) y el flip-flop \( flag \) se establece en 1 de forma simultánea en el flanco de reloj. |
| `3.` | \( done = 1 \) | — | Conexión combinacional. La línea de salida \( done \) se conecta al nivel lógico 1 durante la duración de este paso. |
| `4.` | \( \text{DEAD END} \) | — | Fin de secuencia. Detiene definitivamente el secuenciador de control de este módulo. |