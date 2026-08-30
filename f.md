En los bloques de código AHPL (secuencias numeradas) del libro *Digital Systems: Hardware Organization and Design* (2ª ed.) de Hill & Peterson, el **NOT** de una señal o expresión **se escribe exclusivamente con una barra superior (overbar)** sobre el símbolo o la expresión correspondiente (por ejemplo, \( \overline{X} \)). 

**No se utiliza** la tilde `~` como prefijo ni tampoco la función `NOT()` en el texto impreso original del libro. Sin embargo, en las transcripciones de texto plano y en la sintaxis aceptada para compiladores de AHPL, **se suele emplear la tilde `~` como sustituto tipográfico** para representar dicha barra superior en bloques de código estándar.

A continuación se muestran exactamente **dos ejemplos reales** tomados de las secuencias numeradas del libro, representados tanto en formato de texto plano con tilde `~` como en su notación tipográfica original con barra superior:

---

### Ejemplo 1: Página 225
En el capítulo 7, sección 7.2 ("Starting, Stepping, and Resetting"), dentro del módulo de nivel único sincronizado **`MODULE: SL(a)`**:

**Bloque de código (sustitución tipográfica):**
```
1. → (~SL(SYN(start))) / (1)
```

**Notación original del libro impreso (KaTeX inline):**
\( 1. \rightarrow ( \overline{SL(SYN(start))} ) / (1) \)

*Explicación:* La barra superior cubre toda la expresión de la señal de entrada condicional. Si la señal es falsa (\( 0 \)), el control realiza un bucle de espera retornando al paso 1; cuando se hace verdadera (\( 1 \)), sale del bucle continuando al siguiente paso.

---

### Ejemplo 2: Página 289
En el capítulo 7, sección 7.8 ("A Complete Design Example"), dentro del secuenciamiento del módulo de almacenamiento de prioridad **`PRIORITY STORE`**:

**Bloque de código (sustitución tipográfica):**
```
1. (a, b) * (inreq ∨ outreq) ← 1, 0
   → (~(inreq ∨ outreq), inreq, ~inreq ∧ outreq) / (1, 2, 5)
```

**Notación original del libro impreso (KaTeX inline):**
\( 1. \; (a, b) * (inreq \lor outreq) \leftarrow 1, 0 \)
\( \quad \rightarrow ( \overline{inreq \lor outreq},\; inreq,\; \overline{inreq} \land outreq ) / (1, 2, 5) \)

*Explicación:* En la bifurcación condicional de este paso se aprecian dos aplicaciones de la barra superior:
1. \( \overline{inreq \lor outreq} \): Niega la disyunción completa (si no hay solicitud de entrada ni de salida, se mantiene en el paso 1).
2. \( \overline{inreq} \): Niega la señal individual de solicitud de entrada en la condición de prioridad \( \overline{inreq} \land outreq \) (si no hay solicitud de entrada pero sí de salida, salta a atender la salida en el paso 5).

---

💡 ¿Te gustaría que analicemos cómo se realiza la síntesis o compilación de hardware para alguna de estas bifurcaciones negadas basándonos en las tablas de control y compuertas lógicas del libro?