##### Ej. Módulo AHPL completo para una interfaz simple que espera la señal start, carga el registro DR(8) desde el bus IOBUS(8), activa done por un ciclo y termina en DEAD END.

**Resolución**
Diseño de una interfaz digital secuencial que realiza una espera activa (polling) sobre la señal start para cargar DR y activar de forma síncrona/combinacional done por un ciclo antes de detener el control.

| Identificador | Sección | Tamaño | Rol |
|---|---|---|---|
| `DR` | MEMORY | `(8)` | Registro de datos que almacena el byte recibido desde el bus de entrada |
| `start` | INPUTS | `escalar` | Señal de control externa que habilita la transferencia cuando es igual a 1 |
| `done` | OUTPUTS | `escalar` | Señal combinacional de salida que notifica la finalización de la carga |
| `IOBUS` | COMBUS | `(8)` | Bus de datos de entrada del sistema que sirve como fuente para cargar DR |

```ahpl
MODULE: SIMPLE_INTERFACE
MEMORY: DR(8)
INPUTS: start
OUTPUTS: done
COMBUS: IOBUS(8)
SEQUENCE
1. -> (~start)/(1)
2. DR <- IOBUS; done = 1
3. DEAD END
END SEQUENCE
END
```

| Paso | Operación                                 | Condición              | Estado resultante                                                                                                                                                                      |
| ---- | ----------------------------------------- | ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `1.` | \( \rightarrow (\overline{start})/(1) \)  | \( \overline{start} \) | Espera activa. El sistema permanece en el paso 1 mientras \( start = 0 \). Cuando \( start = 1 \), el nivel de control avanza al paso 2.                                               |
| `2.` | \( DR \leftarrow IOBUS \); \( done = 1 \) | —                      | Carga síncrona y conexión combinacional. Al flanco activo del reloj, \( DR(8) \) se carga con el valor de \( IOBUS(8) \) y la salida \( done \) se mantiene activa durante este ciclo. |
| `3.` | DEAD END                                  | —                      | Terminación. Se detiene la propagación del nivel de control en la secuencia principal.                                                                                                 |