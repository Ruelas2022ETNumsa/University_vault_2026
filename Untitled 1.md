### Tabla de Declaraciones

| Identificador | Sección | Tamaño | Rol |
| :--- | :--- | :--- | :--- |
| `AC` | MEMORY | `` | Registro de acumulación que almacena el dato recibido. |
| `flag` | MEMORY | escalar | Flip-flop que se activa tras completar la carga. |
| `done` | OUTPUTS | escalar | Señal de salida de finalización combinacional. |
| `go` | INPUTS | escalar | Señal de entrada que actúa como habilitador del proceso. |
| `DBUS` | COMBUS | `` | Bus combinacional que suministra el dato externo. |

### Código AHPL del Módulo

```ahpl
MODULE: CARGAGO
MEMORY: AC; flag
INPUTS: go
OUTPUTS: done
COMBUS: DBUS

1. -> (~go)/(1)
2. AC <- DBUS; flag <- 1
3. done = 1
4. DEAD END
END
```

### Tabla de Pasos

| Paso | Operación | Condición | Estado resultante |
| :--- | :--- | :--- | :--- |
| `1.` | \( \rightarrow (\overline{go})/(1) \) | \( \overline{go} \) | **Bucle de espera (polling)**. El control permanece retenido en el paso 1 mientras la señal de entrada sea igual a 0. |
| `2.` | \( AC \leftarrow DBUS \) ; \( flag \leftarrow 1 \) | — | **Transferencia síncrona**. En el flanco de bajada del reloj, \( AC \) se carga con el valor actual del bus \( DBUS \) y el flip-flop \( flag \) se pone en 1. |
| `3.` | \( done = 1 \) | — | **Conexión combinacional**. La salida \( done \) se mantiene activa en nivel alto durante este ciclo de reloj sin intervención del flip-flop. |
| `4.` | \( DEAD\ END \) | — | **Término**. Detiene la secuencia del circuito de control. |

💡 **Sugerencia:** ¿Te gustaría que adaptemos este módulo básico para realizar una transferencia condicional utilizando el operador asterisco (`*`) o para simular un protocolo de handshake?
---
copia con el cursor y pegar:

Tabla de declaraciones:IdentificadorSecciónTamañoRolACMEMORY7Registro acumulador interno de destinoDBUSINPUTS7Bus de entrada con el dato externogoINPUTSescalarSeñal de habilitación de la cargareadyOUTPUTSescalarSeñal de salida que indica que el dato ha sido cargadoBloque de código:MODULE: RECEPTOR
MEMORY: AC[7]
INPUTS: DBUS[7]; go
OUTPUTS: ready

1. ready = 0
   -> (~go)/(1)
2. AC <- DBUS; ready = 1
   DEAD END
END
Tabla de pasos:PasoOperaciónCondiciónEstado resultante1.$ ready = 0 $$ \overline{go} = 1 $Realiza polling. Si $ go = 0 $, vuelve al paso 1 en el siguiente ciclo de reloj. Si $ go = 1 $, continúa al paso 2.2.$ AC \leftarrow DBUS $ <br> $ ready = 1 $—Carga el contenido de las líneas de entrada en el registro $ AC $, levanta la señal de listo y termina el proceso.💡 Siguiente paso sugerido: ¿Te gustaría ver cómo se modifica este código para realizar una transferencia bidireccional usando un bus combinacional (COMBUS) en lugar de entradas directas?
