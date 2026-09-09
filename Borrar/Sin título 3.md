Basado en los textos de **Stallings (COA 11ª ed. y 7ª ed.)**, las preguntas clave que definen el funcionamiento y la arquitectura del **DMA** se centran en la delegación de control y la eficiencia del bus.

A continuación, se presentan preguntas de repaso (Nivel B) y un ejercicio de análisis de secuencia (Nivel C).

---

## Complemento nivel B: Cuestionario DMA (Guía Stallings)

1. **¿Qué información específica debe enviar el procesador al módulo de DMA para iniciar una transferencia?** [1-4].
2. **Defina el concepto de "Robo de Ciclo" (Cycle Stealing) y explique su impacto en el rendimiento del procesador.** [5-9].
3. **¿Cuáles son las tres configuraciones alternativas de interconexión para módulos de DMA y cuál es la más eficiente en términos de uso del bus del sistema?** [10-12].
4. **¿Por qué en la mayoría de los sistemas el acceso del módulo de DMA a la memoria principal tiene mayor prioridad que el acceso del procesador?** [13-15].
5. **¿Qué sucede con el procesador durante el tiempo en que el controlador de DMA mantiene el control de los buses?** [16-18].

**Idea clave (Stallings):** El DMA no es una interrupción convencional; el procesador no salva contexto, sino que se detiene (pausa) justo antes de necesitar el bus, permitiendo que el módulo de DMA ejecute la transferencia palabra por palabra [6, 7, 9].

---

## Complemento nivel C: Secuencia Buffer (DMA en SIC)

Este ejercicio analiza la implementación AHPL de la transferencia de entrada, fundamental para entender cómo el hardware gestiona el *handshake* sin intervención del software.

##### Ej. Describa la secuencia AHPL de entrada de datos en modo DMA (Pasos 103-106) del computador SIC.

**Resolución**
Se implementa un protocolo de *handshake* asíncrono donde el SIC espera la estabilidad del dato en el `IOBUS`.

1) Tabla de declaraciones
| Identificador | Sección | Tamaño | Rol |
| :--- | :--- | :--- | :--- |
| `MA` | MEMORY | `(12)` | Registro de dirección actual del área buffer. |
| `MD` | MEMORY | `(18)` | Registro de datos intermedio. |
| `M` | MEMORY | `(8192, 18)` | Matriz de memoria principal del SIC. |
| `IOBUS` | COMBUS | `(18)` | Bus de datos de entrada/salida. |
| `ready` | COMBUS | escalar | Señal de disponibilidad del SIC. |
| `datavalid` | COMBUS | escalar | Señal del periférico indicando dato estable. |
| `accept` | COMBUS | escalar | Señal de confirmación de recepción. |

2) Bloque de código AHPL
```ahpl
103. ready = 1
     → (~datavalid)/(103)
104. MD ← IOBUS
105. M * DCD(MA) ← MD
106. accept = 1
     → (datavalid)/(106)
```

3) Tabla de pasos
| Paso | Operación | Condición | Estado resultante |
| :--- | :--- | :--- | :--- |
| `103.` | $ready = 1$ | $\overline{datavalid}$ | **Espera:** El SIC indica que está listo y buclea hasta que el periférico valida el dato [19]. |
| `104.` | $MD \leftarrow IOBUS$ | — | **Captura:** Se carga la palabra del bus en el registro `MD` al flanco de reloj [19]. |
| `105.` | $M \times DCD(MA) \leftarrow MD$ | — | **Escritura:** El dato se almacena en la dirección de memoria apuntada por `MA` [19]. |
| `106.` | $accept = 1$ | $datavalid$ | **Cierre:** El SIC confirma la recepción y espera a que el periférico libere la línea `datavalid` [19]. |

---

## Ejercicio de Cálculo de Penalización (Stallings)

##### Ej. Un dispositivo transmite a 9600 bps mediante robo de ciclo a una CPU de 1 MIPS. ¿Cuánto se ralentiza el procesador? [13-15].

**Resolución**
Cálculo de la fracción de tiempo que el DMA "roba" el bus.


$$
\text{Velocidad de caracteres} = \frac{9600 \text{ bps}}{8 \text{ bits/char}} = 1200 \text{ caracteres/s}
$$


$$
\text{Ciclos robados por segundo} = 1200 \text{ ciclos/s}
$$


$$
\text{Ralentización} = \frac{\text{Ciclos robados}}{\text{Instrucciones por segundo}} = \frac{1200}{1,000,000}
$$


$$
\therefore\quad \color{orange}{0.12 \%}
$$


*Nota: La ralentización es despreciable (0.12%), lo que justifica la eficiencia del DMA frente a la E/S programada [13, 15].*
