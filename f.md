En los bloques de código AHPL del libro de Hill & Peterson (*Digital Systems: Hardware Organization & Design*, 2ª ed.), el NOT de una señal **se escribe exclusivamente usando una barra superior (overbar) sobre el símbolo de la señal** (por ejemplo, \( \overline{X} \)).

**No se utiliza la tilde `~` ni la notación funcional `NOT()`** en las secuencias de control numeradas impresas del libro. El uso del prefijo `~` es únicamente una convención de sustitución tipográfica aceptada para transcribir el código a texto plano o markdown (como en compiladores y guías de sintaxis digitales).

A continuación se presentan exactamente dos ejemplos reales extraídos de las secuencias de control numeradas del libro:

---

### **Ejemplo 1: Página 248 (Capítulo 7, Sección 7.5)**
En la secuencia de ejemplo utilizada para explicar el proceso de compilación del hardware, el paso 2 realiza una bifurcación condicional de tres vías evaluando los bits del registro \( A \):

* **Representación tipográfica del libro físico:**
  \( 2. \rightarrow (A_0 \land \overline{A}_1 \land \overline{A}_2)/(1) \)
* **Transcripción estándar en texto plano:**
  ```ahpl
  2. -> (A0 /\ ~A1 /\ ~A2)/(1)
  ```
  *(Cita: Hill & Peterson 2ª ed., pág. 248)*

---

### **Ejemplo 2: Página 291 (Capítulo 7, Sección 7.3)**
En la sección donde se ilustra la mejora de circuitos y la simplificación de estructuras de control equivalentes, el paso 1 evalúa la señal de control \( a \) para decidir el salto:

* **Representación tipográfica del libro físico:**
  \( 1. \rightarrow (\overline{a}, a)/(2, 3) \)
* **Transcripción estándar en texto plano:**
  ```ahpl
  1. -> (~a, a)/(2, 3)
  ```
  *(Cita: Hill & Peterson 2ª ed., pág. 291)*

---
¿Te gustaría que analicemos la traducción de estas condiciones de bifurcación a compuertas lógicas (AND/OR e inversores) tal como se muestra en los diagramas de realización física del libro?