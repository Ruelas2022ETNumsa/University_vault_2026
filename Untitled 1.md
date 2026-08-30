## Secuencia de Control en AHPL

##### Ej. Escribir un módulo AHPL simple que espera la señal go, carga AC desde DBUS y finaliza.

**Resolución**
Diseñamos un secuenciador de 3 pasos para controlar la carga de un registro con bucle de espera asíncrono.

1) Tabla de declaraciones

| Identificador | Sección | Tamaño | Rol |
|---|---|---|---|
| `AC` | MEMORY | `(18)` | Registro acumulador principal |
| `DBUS` | INPUTS | `(18)` | Bus de datos de entrada |
| `go` | INPUTS | `escalar` | Señal de inicio de transferencia |
| `ready` | OUTPUTS | `escalar` | Indicador de disponibilidad del módulo |

2) Bloque de código
```ahpl
MODULE: CARGADOR
MEMORY: AC(18)
INPUTS: DBUS(18); go
OUTPUTS: ready
1. ready = 1
   -> (~go)/(1)
2. AC <- DBUS
3. DEAD END
END
```

3) Tabla de pasos

| Paso | Operación | Condición | Estado resultante |
|---|---|---|---|
| `1.` | \( ready = 1 \) | — | Conexión combinacional del indicador \( ready \) |
| | \( \rightarrow (1) \) | \( \overline{go} = 1 \) | Bucle de espera asíncrono sobre la señal \( go \) |
| `2.` | \( AC \leftarrow DBUS \) | — | Carga del bus \( DBUS \) en el acumulador \( AC \) |
| `3.` | \( \text{DEAD END} \) | — | Terminación del flujo de control (Halt) |