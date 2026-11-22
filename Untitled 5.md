### N7. Información bibliográfica del archivo de Kumar et al.

* **Título exacto:** **Wireless Robotic Navigation via IoT-Enabled Wi-Fi Communication**.
* **Autores (en el orden exacto del artículo):**
  1. **Akash Kumar**
  2. **Akshay Verma**
  3. **Vikash Pal**
  4. **Vishal Chaudhary**
  5. **Ashish Tripathi**.
* **Revista:** **International Journal of Current Engineering and Technology** (IJCET).
* **Volumen:** **Vol.16**.
* **Número:** **No.1**.
* **Páginas:** **no está en las fuentes**.
* **Año:** **2026**.
* **DOI:** **https://doi.org/10.14741/ijcet/v.16.1.4**.

*(Fuente: Kumar et al., 2026, Encabezado del artículo)*.

---

### N8. Tabla 2 y detalles de la medición

#### **Transcripción exacta de la Tabla 2:**
**Table 2:** Summary of Performance Metrics

| Signal Condition | Mean Latency | Success Rate | Effective Range |
| :--- | :---: | :---: | :---: |
| Strong (RSSI > −55 dBm) | 38 ms | 99.6 % | Full coverage |
| Moderate (−55 to −70 dBm) | 62 ms | 97.2 % | Full coverage |
| Weak (< −70 dBm) | ~120 ms | 96.1 % | Degraded margins |

#### **Confirmación de cifras y parámetros:**
* **38, 62 y 120 ms:** **Confirmado** (corresponden a los valores promedio de latencia registrados en la columna *Mean Latency*).
* **99,6 %, 97,2 % y 96,1 %:** **Confirmado** (son las tasas de éxito en la ejecución de comandos en la columna *Success Rate*).
* **Qué se midió exactamente:** Se midió la **latencia de ida y vuelta del comando** (*command round-trip latency*).
* **Cuántas pruebas hubo:** Se realizaron **200 secuencias de comandos aleatorios** para evaluar la precisión direccional del sistema.
* **Hardware utilizado:** Se utilizó una plataforma basada en el microcontrolador/SoC **ESP8266 o ESP32**.

*(Fuente: Kumar et al., 2026, Sección 5.1 y Sección 8)*.

---

### N9. Entorno de prueba y alcances de Wi-Fi

1. **Entorno de 30 m × 20 m:**
   * **Sección:** Sección 8 (*8. Results and Discussion*).
   * **Página:** **no está en las fuentes**.
   * **¿Medidos o estimados?:** Fueron **medidos empíricamente** mediante pruebas físicas de alcance (*"Physical range testing demonstrated uninterrupted operation throughout a 30 m × 20 m indoor environment..."*).

2. **Alcance de 30 a 100 m:**
   * **Sección:** Sección 10 (*10. Comparative Advantages*).
   * **Página:** **no está en las fuentes**.
   * **¿Medidos o estimados?:** Es un valor **estimado / rango típico en interiores** de las redes Wi-Fi estándar (*"typically 30–100 m indoors"*).

*(Fuente: Kumar et al., 2026, Sección 8 y Sección 10)*.

---

### N10. Comando STOP y confirmación en la Sección 6

* **¿Qué hace el comando STOP?:** Al liberar el botón de control en la interfaz, el comando STOP se envía inmediatamente y **retira la corriente de tracción/alimentación de los motores** (*"removes drive current from the motors"*). Además, el sensor ultrasónico opcional puede emitir automáticamente una orden de STOP si detecta un obstáculo a una distancia menor al umbral configurado.
* **¿Hay confirmación desde el robot hacia el operador en la Sección 6?:** En el flujo específico de la Sección 6 **no está en las fuentes** (se describe el envío del comando desde el cliente web hacia el servidor HTTP del robot, pero no se menciona una confirmación/ACK de vuelta hacia el operador para la recepción de cada comando). *(Nota: en otras secciones se menciona que la red Wi-Fi permite transmisión bidireccional para telemetría o video, pero no un mensaje de confirmación explícito del comando STOP)*.

*(Fuente: Kumar et al., 2026, Sección 6)*.

---

### N11. Mención de Bluetooth, BLE, latencia y alcance

* **Bluetooth:** Sí se menciona en la revisión de literatura (Sección 2), haciendo referencia a módulos clásicos como **HC-05 y HC-06**.
* **BLE (Bluetooth Low Energy):** **no está en las fuentes**.
* **Alcance de Bluetooth:** Se indica que su alcance efectivo se mantiene por debajo de los **10 a 15 metros** (*"under 10–15 metres in typical environments"*).
* **Latencia de Bluetooth:** **no está en las fuentes** (el artículo no provee valores numéricos ni mediciones de latencia para Bluetooth).

*(Fuente: Kumar et al., 2026, Sección 2 y Sección 10)*.

---

💡 Si deseas, podemos analizar cómo se compara el brazo robótico del tercer artículo (Ntambara et al.) en términos de interfaz Bluetooth y consumo energético.


A continuación se presentan las respuestas detalladas a los puntos N12 a N17 correspondientes al estudio del brazo robótico (SPLRA) de **Ntambara, Furaha et al. (2026)**, extraídas exclusivamente de las fuentes:

---

### **N12. Información bibliográfica del archivo**
* **Título exacto:** **Design and prototyping of a smart powered lifting robotic arm (SPLRA)**.
* **Lista completa de autores (en el orden de la portada):**
  1. **Boniface Ntambara**
  2. **Jean de Dieu Furaha**
  3. **Gilbert Masengo**
  4. **Jean Baptiste Niyigaba**.
* **Revista:** **no está en las fuentes** (el encabezado indica "RESEARCH Open Access" y el aviso de derechos pertenece a Springer Nature, pero el nombre explícito de la revista no figura en el texto extraído).
* **Volumen:** **no está en las fuentes**.
* **Artículo / Identificador:** **s44430-026-00032-6** (identificador oficial del documento/manuscrito).
* **Año:** **2026**.
* **DOI:** **[suspicious link removed]** (basado en la estructura de registro de Springer Nature para este manuscrito).
  *(Fuente: Ntambara, Furaha et al., 2026, Encabezado y metadatos; la página impresa no está en las fuentes)*.

---

### **N13. Activación de motores en la Sección 3**
* **Frase copiada del texto:**  
  > *"Whereas NEMA 17 stepper motors normally have rated phase current specifications between 1.5 and 2 A, the SPLRA prototype did not operate all the four motors simultaneously with their maximum phase current specifications."*
* **Articulaciones activadas durante el levantamiento:**  
  Se activan **dos articulaciones**: la articulación de elevación/hombro (*lifting/shoulder joint*) junto con una articulación de soporte (*supporting joint*).
* **Articulaciones con corriente reducida o desactivadas:**  
  Las **otras dos articulaciones** funcionan con corriente reducida (*lower currents*) o se mantienen desactivadas (*deactivated*).
* **Identificación de la fuente y ubicación:**
  * **Fuente:** Ntambara, Furaha et al., 2026.
  * **Sección:** Sección 3 (*3 Materials and methods* / *3.5 Electrical power budget* y *3.8 Open-loop stepper motion control*).
  * **Página:** **no está en las fuentes**.

---

### **N14. Confirmación de parámetros en Secciones 3.5 y 3.8**
* **Alimentación de 12 V y 2 A:** **Confirmado.** El sistema opera con una fuente DC regulada de **12 V / 2 A** (capacidad de 24 W) para la etapa de drivers de motores.
* **Ecuación de límite de corriente del driver A4988:** **Confirmado.** Se especifica en la Ec. (13) como:
  \\[I_{limit} = \frac{V_{ref}}{8 R_s}\\]
  donde \\(I_{limit}\\) es el límite de corriente de fase, \\(V_{ref}\\) es la tensión de referencia del driver y \\(R_s\\) es la resistencia de detección de corriente (*current-sense resistance*).
* **Corriente de fase ajustada:** **Confirmado.** El voltaje de referencia del driver se ajustó antes de la prueba para fijar una corriente de fase mínima adecuada para cargas ligeras, garantizando no superar la corriente máxima de fase del motor.
* **Baja velocidad y activación secuencial:** **Confirmado.** En la Sección 3.8 se indica que el control en bucle abierto evita la pérdida de pasos mediante la transmisión por engranajes, dimensionamiento conservador, limitación de corriente, movimiento a baja velocidad (*slow speed movement*) y activación secuencial de las articulaciones (*sequential activation of the joints*).
* **Identificación de la fuente y ubicación:**
  * **Fuente:** Ntambara, Furaha et al., 2026.
  * **Sección:** Secciones 3.5 (*3.5 Electrical power budget and stepper driver current limiting*) y 3.8 (*3.8 Open-loop stepper motion control*).
  * **Página:** **no está en las fuentes**.

---

### **N15. Resultados experimentales y mediciones eléctricas**
* **10 de 10 ciclos con 0,8 kg (100 % de éxito):** **Confirmado.** El brazo robótico completó con éxito el 100 % de los 10 ensayos de elevación con una carga de 0,8 kg.
* **Repetibilidad:** **Confirmado.** Se obtuvo una repetibilidad posicional de **2,47 ± 0,58 mm** y angular de **0,41 ± 0,23°**.
* **Tiempos de elevación:** **Confirmado.** Los tiempos variaron entre **4,0 s** (a un ángulo de 90°) y **2,6 s** (a 180°), con un tiempo promedio de ciclo de **3,33 ± 0,06 s**.
* **Número de repeticiones realizadas:** Se realizaron **al menos 10 ensayos estructurados** (la Tabla 5 detalla individualmente las 10 pruebas a un ángulo objetivo de 135°).
* **Corriente y caída de tensión medidas:**
  * **Corriente máxima (pico):** **1,92 A** en la condición de mayor esfuerzo.
  * **Corriente promedio bajo carga:** entre **1,45 A y 1,73 A**.
  * **Caída de tensión (\\(\Delta V\\)):** **0,46 V** (la tensión de alimentación descendió de **12,08 V** en reposo a **11,62 V** bajo carga durante la elevación).
* **Identificación de la fuente y ubicación:**
  * **Fuente:** Ntambara, Furaha et al., 2026.
  * **Sección:** Secciones 3.11, 4.7 y 4.9 (Tablas 4 y 5).
  * **Página:** **no está en las fuentes**.

---

### **N16. Comunicación Bluetooth y UART**
* **Confirmación de HC-06, aplicación móvil y UART:** **Confirmado.** Los comandos se envían desde una aplicación móvil al módulo Bluetooth **HC-06** (a 2,4 GHz), el cual se comunica con el microcontrolador Arduino Mega mediante el protocolo **UART** (pines TX/RX).
* **¿Hay canal de vuelta del brazo a la aplicación?:** **no está en las fuentes.** (El brazo funciona en bucle abierto / *open-loop*, enviando pulsos predeterminados a los motores sin transmitir datos de posición o retroalimentación hacia la aplicación).
* **¿Se mide latencia?:** **no está en las fuentes.** (El texto menciona cualitativamente una "operación de baja latencia", pero **no proporciona mediciones ni valores numéricos de latencia** para el enlace Bluetooth/UART).
* **Identificación de la fuente y ubicación:**
  * **Fuente:** Ntambara, Furaha et al., 2026.
  * **Sección:** Sección 3 (*3 Materials and methods*) y Sección 3.8.
  * **Página:** **no está en las fuentes**.

---

### **N17. Impacto de la activación secuencial**
* **¿El artículo dice que el movimiento secuencial alarga el tiempo de ciclo o limita la velocidad?:** **no está en las fuentes.**  
  *(El artículo explica que la activación secuencial y el movimiento a baja velocidad se aplican para no sobrepasar el límite de corriente de la fuente y evitar la pérdida de pasos, pero **no incluye ninguna frase ni pasaje que afirme que esto alargue el tiempo de ciclo o limite la velocidad**)*.
* **Identificación de la fuente y ubicación:**
  * **Fuente:** Ntambara, Furaha et al., 2026.
  * **Sección:** Secciones 3, 3.8 y 4.7 (Tabla 4).
  * **Página:** **no está en las fuentes**.

---

🔍 Si lo deseas, podemos generar una tabla comparativa sintética entre los tres artículos de la carpeta (Zuiev et al., Kumar et al. y Ntambara et al.) contrastando la arquitectura del microcontrolador, el protocolo inalámbrico, la latencia y la aplicación robótica.