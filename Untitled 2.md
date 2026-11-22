
---
n1

A continuación se detalla la información del archivo de **Zuiev et al.** extraída directamente de las fuentes:

* **Título exacto:** **RESEARCH OF MICROPROCESSOR DEVICE AND SOFTWARE FOR REMOTE CONTROL OF A ROBOTIC SYSTEM**.  
  *(Fuente: Zuiev et al., 2024, Encabezado principal)*.

* **Lista completa de autores (en el orden de la portada):**
  1. **Andrii Zuiev**
  2. **Viktoriia Krylova**
  3. **Anatolii Hapon**
  4. **Stanislav Honcharov**  
  *(Fuente: Zuiev et al., 2024, Encabezado y sección de autores)*.

* **Revista:** **no está en las fuentes** (en la sección correspondiente al artículo de Zuiev et al. no se menciona explícitamente el nombre de la revista).

* **Volumen:** **no está en las fuentes**.

* **Número:** **no está en las fuentes**.

* **Páginas:** **no está en las fuentes**.

* **Año:** **2024** (indicado en la estructura del DOI `10.15587/2706-5448.2024.297339`).  
  *(Fuente: Zuiev et al., 2024, Encabezado / DOI)*.

* **DOI:** **10.15587/2706-5448.2024.297339**.  
  *(Fuente: Zuiev et al., 2024, Encabezado)*.

---

N2

**Confirmación:** Sí, en la Sección 3.1 se confirma que las señales CPPM y PWM tienen un retardo de aproximadamente 60 a 80 ms, mientras que S.BUS presenta un retardo de solo 10 a 20 ms.

* **Frase exacta del texto:**  
  > *"It should also be noted that the CPPM and PWM signals have a delay of about 60–80 ms, while the S.BUS is only 10–20 ms."*

* **Eventos entre los que se mide el retardo:**  
  El retardo de la señal se define como el tiempo que tarda el receptor en convertir la señal del transmisor en la señal que se enviará al controlador del sistema robótico (RTS). Se mide específicamente entre:
  1. **La recepción de la señal del transmisor por parte del receptor.**
  2. **La emisión de la señal convertida desde el receptor hacia el controlador del RTS.**  
  *(Definición en la fuente: "the time it takes for the receiver to convert the signal from the transmitter into the signal it is going to send to the RTS controller")*.

* **Identificación de la fuente y ubicación:**
  * **Fuente (Autor, Año):** Zuiev et al., 2024.
  * **Sección:** Sección 3.1 (*3.1. RTS remote control protocols*).
  * **Página:** El número de página impreso **no está en las fuentes** extraídas (únicamente se especifica la Sección 3.1).

---

N3

### 1. Latencia de Wi-Fi y Bluetooth en las fuentes

**En el artículo de Zuiev et al. (2024):**
* **Mención de latencia en Wi-Fi:** Sí menciona que en las redes Wi-Fi existe un retardo variable que puede alcanzar los 120 ms.
  * **Pasaje exacto:**  
    > *"Also, there are no solutions to the problem associated with the variable delay of the arrival time of packets in wireless Wi-Fi networks, only it is noted that it can reach 120 ms."*  
    *(Fuente: Zuiev et al., 2024, Sección 2; el número de página impreso no está en las fuentes)*.
* **Comparación con Wi-Fi y Bluetooth:** Sí compara de manera general el retardo obtenido en su investigación frente a las redes Wi-Fi o Bluetooth, indicando que el retardo de su sistema es significativamente menor, aunque no proporciona un valor numérico específico de latencia para Bluetooth.
  * **Pasaje exacto:**  
    > *"Also, the total delay time obtained is significantly less than the delays that are present when exchanging wireless communication channels via Wi-Fi or Bluetooth networks."*  
    *(Fuente: Zuiev et al., 2024, Sección 4 / Conclusions; el número de página impreso no está en las fuentes)*.

---

**Información complementaria de latencia Wi-Fi en otras fuentes de la carpeta:**
* **Kumar et al. (2026):** Mide experimentalmente la latencia de ida y vuelta en Wi-Fi según la intensidad de la señal (38 ms en señal fuerte, 62 ms en señal moderada y ~120 ms en señal débil).  
  * **Pasaje exacto:**  
    > *"Under strong signal conditions, mean round-trip latency averaged 38 ms, and command execution success reached 99.6%. At moderate signal strength, latency rose to approximately 62 ms... Under weak signal conditions, occasional packet retransmissions pushed latency beyond 120 ms..."*  
    *(Fuente: Kumar et al., 2026, Sección 8; el número de página impreso no está en las fuentes)*.

---

### 2. Mención de BLE (broadcast o con conexión)

* **no está en las fuentes**  
*(Las fuentes únicamente mencionan la tecnología Bluetooth de forma genérica o mediante módulos clásicos como HC-05 y HC-06 en Kumar et al., 2026, Sección 2 y Ntambara et al., 2026, Sección 3, pero **no mencionan BLE** ni diferencian entre modos de broadcast o con conexión).*

---


N4

Basado en lo especificado en la Sección 3.4 del artículo de **Zuiev et al. (2024)**, se detallan los aspectos solicitados:

### 1. Qué hace el sistema (mecanismo de parada forzada)
* **Memorización del tiempo:** El sistema registra y memoriza el momento exacto en el que llega con éxito un paquete de control.
* **Emisión de la orden de parada:** Si no se recibe ningún paquete nuevo tras transcurrir cierto tiempo, el sistema emite automáticamente una **orden forzada de detención de los motores**.
* **Reinicio del movimiento:** El movimiento del sistema robótico (RTS) permanece completamente detenido **hasta que se restablezcan las señales de control**.

---

### 2. Intervalo de tiempo
* **no está en las fuentes**  
  *(El texto indica únicamente que el mecanismo se activa si no se reciben paquetes durante un tiempo —"if no packets are received for some time"—, pero **no especifica una cifra o valor numérico explícito** en milisegundos o segundos para dicho intervalo)*.

---

### 3. Identificación de la fuente y ubicación
* **Fuente (Autor, Año):** Zuiev et al., 2024.
* **Sección:** Sección 3.4 (*3.4. Practical implementation and research of the RTS control system on the ESP32 platform*).
* **Página:** **no está en las fuentes** (el número de página impreso del artículo no se incluye en el texto extraído de las fuentes).

---

N5


A continuación se presentan de manera exacta las **Tablas 2 y 3** del estudio de **Zuiev et al. (2024)**, junto con la confirmación de cada una de las cifras solicitadas:

---

### 1. Transcripción completa de las Tablas 2 y 3

#### **Tabla 2:** Calculation time for the algorithm for decomposing control commands on PWM channels (ESP32, 1 core, 160 MHz)

| No. | State | Calculation time min, μs | Calculation time max, μs |
| :--- | :--- | :---: | :---: |
| 1 | No control (Disable) | 3 | 3 |
| 2 | Rotation | 20 | 40 |
| 3 | Side shift | 25 | 45 |
| 4 | Change of speed or direction of movement | 10 | 15 |

---

#### **Tabla 3:** Comparison of the delay time for parallel and serial implementations of the algorithm for sending signals through PWM channels depending on the frequency of the processor

| No. | State | Delay time (160 MHz), μs (min) | Delay time (160 MHz), μs (max) | Delay time (240 MHz), μs (min) | Delay time (240 MHz), μs (max) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| 1 | Processing and recording | 3 | 3 | 2 | 2 |
| **Parallel sending of a PWM signal (queue)** | | | | | |
| 2 | Change of speed or direction of movement, or lateral shift (4 channels) | 40 | 46 | 29 | 32 |
| 3 | Rotation (2 channels) | 24 | 30 | 19 | 23 |
| **Sequential sending of a PWM signal (no queuing)** | | | | | |
| 4 | Change of speed or direction of movement, or lateral shift (4 channels) | 66 | 130 | 49 | 73 |
| 5 | Rotation (2 channels) | 91 | 104 | 48 | 60 |

---

### 2. Confirmación de las cifras solicitadas

* **3–45 µs:** **Confirmado.** Representa el rango completo del tiempo de cálculo (*Calculation time*) registrado en la **Tabla 2** para el microcontrolador a 160 MHz, abarcando desde 3 µs (mínimo en estado sin control/desactivado) hasta 45 µs (máximo en desplazamiento lateral).
* **24–46 µs:** **Confirmado.** Corresponde al rango de retardo en el **envío paralelo con cola (queue)** operando a **160 MHz** en la **Tabla 3**, donde el valor mínimo es de 24 µs (rotación) y el máximo es de 46 µs (cambio de velocidad, dirección o desplazamiento lateral).
* **66–130 µs:** **Confirmado.** Figura en la **Tabla 3** en la fila 4 (*Sequential sending of a PWM signal / no queuing*) para la frecuencia de **160 MHz**, donde el valor mínimo de retardo es 66 µs y el máximo es 130 µs.
* **Frecuencia de 160 MHz:** **Confirmado.** Es la frecuencia base del procesador ESP32-WROOM v3.1 bajo la cual se midieron los tiempos de cálculo de la Tabla 2 y la primera columna comparativa de retardo de la Tabla 3.

---

### 3. Identificación de la fuente y ubicación

* **Fuente (Autor, Año):** Zuiev et al., 2024.
* **Sección:** Sección 3.5 (*3.5. System efficiency analysis and conclusions*).
* **Página:** **no está en las fuentes** (el número de página impreso del documento no se encuentra disponible en las fuentes extraídas).

---

N6

### 1. ¿El robot es un vehículo o un brazo?

* **En Zuiev et al. (2024):** Es un **vehículo terrestre autónomo** montado sobre un chasis con tracción en las cuatro ruedas (4WD).  
  *(Fuente: Zuiev et al., 2024, Sección 3.5; la página impresa no está en las fuentes)*.

* **En las demás fuentes de la carpeta:**
  * **Kumar et al. (2026):** Es un **vehículo móvil** de 4 ruedas. *(Fuente: Kumar et al., 2026, Sección 2 y Sección 5.1)*.
  * **Ntambara et al. (2026):** Es un **brazo robótico** de elevación (*Smart Powered Lifting Robotic Arm - SPLRA*). *(Fuente: Ntambara et al., 2026, Sección 1)*.

---

### 2. ¿Hay algún canal de vuelta (telemetría o confirmación) del robot al operador?

* **En el sistema práctico implementado por Zuiev et al. (2024):** **no está en las fuentes**. La implementación física descrita en la investigación se enfoca exclusivamente en la recepción y procesamiento de mandos de control desde la emisora hacia el receptor FrSky y los controladores del motor.
  * *Mención teórica de protocolos:* En el análisis teórico del artículo se indica que el protocolo empleado (**S.BUS**) es un canal digital de una sola vía hacia el controlador, aunque mencionan que otros protocolos de radio (como **CRSF, IBUS, FPort o MAVLink**) o de motores (como **DShot**) sí cuentan con capacidad bidireccional y telemetría. *(Fuente: Zuiev et al., 2024, Sección 3.1; la página impresa no está en las fuentes)*.

* **En otras fuentes (Kumar et al., 2026):** Su plataforma Wi-Fi sí soporta comunicación bidireccional, permitiendo enviar datos de telemetría, estado de la batería o video en vivo de vuelta al operador de forma concurrente con las órdenes de control. *(Fuente: Kumar et al., 2026, Sección 1 y Sección 10)*.

---
