| Identificador | Sección | Tamaño | Rol |
| :--- | :--- | :--- | :--- |
| `DR` | MEMORY | `(8)` | Registro interno de almacenamiento de datos |
| `done` | OUTPUTS | escalar | Señal de salida para notificar que la transferencia ha concluido |
| `start` | INPUTS | escalar | Señal de entrada que inicia la operación cuando está activa |
| `IOBUS` | COMBUS | `(8)` | Bus combinacional externo desde el cual se lee el dato |

```ahpl
MODULE: SIMPLE_INTERFACE
MEMORY: DR(8)
INPUTS: start
OUTPUTS: done
COMBUS: IOBUS(8)

1. -> (~start)/(1)
2. DR <- IOBUS
3. done = 1
4. DEAD END
END SEQUENCE
END
```

| Paso | Operación                        | Condición                     | Estado resultante                                                                                                                     |
| :--- | :------------------------------- | :---------------------------- | :------------------------------------------------------------------------------------------------------------------------------------ |
| `1.` | \( \rightarrow (1) \)            | \( \overline{\text{start}} \) | Bucle de polling. Retorna al paso 1 mientras \( \text{start} = 0 \). Habilita el paso 2 al flanco de reloj si \( \text{start} = 1 \). |
| `2.` | \( DR \leftarrow \text{IOBUS} \) | —                             | Carga síncrona. El registro \( DR(8) \) se carga con el valor del bus \( \text{IOBUS}(8) \) en el flanco de reloj de subida.          |
| `3.` | \( \text{done} = 1 \)            | —                             | Conexión combinacional. La línea de salida \( \text{done} \) se activa por un ciclo de reloj para notificar el fin de la carga.       |
| `4.` | \( \text{DEAD END} \)            | —                             | Terminación. Finaliza la secuencia de control y apaga todos los flip-flops de estado del módulo.                                      |