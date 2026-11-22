### **N18. Módulo externo y retransmisión a controlador educativo cerrado**

* **no está en las fuentes**
* **Aclaración:** Ninguna de las fuentes cargadas describe una arquitectura en la que un módulo externo (PC, Raspberry Pi o celular) envíe órdenes por Wi-Fi a un microcontrolador para que este las retransmita por otro canal hacia un **controlador educativo cerrado**.
  * *Lo que sí describen las fuentes:* **Kumar et al. (2026)** conectan un smartphone/PC vía Wi-Fi directamente a un ESP8266/ESP32 que maneja drivers de motor L298N/L293D; **Zuiev et al. (2024)** reciben señales de radiocontrol vía S.BUS en un ESP32 que controla etapas PWM *(mencionan la Raspberry Pi únicamente en su revisión bibliográfica para control directo por PWM de 4 servos)*; y **Ntambara, Furaha et al. (2026)** conectan un celular por Bluetooth al módulo HC-06 de un Arduino Mega que maneja drivers A4988.

---

### **N19. Latencia y alcance de BLE y Tabla 1 de Tzompantzi Netzahual et al. (2019)**

* **no está en las fuentes**
* **Detalle:** Ninguna fuente cargada mide la latencia o el alcance de **BLE (Bluetooth Low Energy)** en modo broadcast ni en modo con conexión.
* La **Tabla 1 de Tzompantzi Netzahual et al. (2019)** **no está en las fuentes** (dicho artículo no forma parte de la carpeta cargada ni aparece citado en las referencias de los estudios presentes).

---

### **N20. Confirmación de fin de movimiento y canal de retorno**

1. **Canal de retorno (telemetría / datos de vuelta):**
   * **Kumar et al. (2026):** Describen la presencia de un canal de comunicación inalámbrico bidireccional por Wi-Fi que permite retornar al operador datos de telemetría de sensores, estado de la batería y transmisión de video en tiempo real de forma concurrente con el envío de comandos.  
     *(Fuente: Kumar et al., 2026, Sección 1, Sección 3 y Sección 10; la página impresa no está en las fuentes)*.
   * **Zuiev et al. (2024):** Mencionan de forma teórica la existencia de protocolos de radio con canal de retorno y telemetría (como CRSF, FPort y MAVLink), además del protocolo de motores **DShot**, el cual transfiere al controlador la velocidad real de rotación de los motores (RPM) como señal de retroalimentación.  
     *(Fuente: Zuiev et al., 2024, Sección 3.1; la página impresa no está en las fuentes)*.
   * **Ntambara, Furaha et al. (2026):** Operan el brazo robótico bajo un esquema de bucle abierto (*open-loop*) sin canal de retorno ni telemetría hacia la aplicación móvil.

2. **Confirmación explícita de "fin de movimiento":**
   * **no está en las fuentes** *(ninguno de los artículos menciona un paquete o señal de ACK enviada por el robot para notificar específicamente la finalización de una maniobra)*.

---

### **N21. Restricción de alimentación, movimiento de motores y compensación**

* **Fuente que lo menciona:** **Ntambara, Furaha et al. (2026)**.

* **Descripción del problema y restricción de corriente:**
  * El prototipo del brazo robótico (SPLRA) se alimenta mediante una fuente de corriente continua regulada de **12 V y 2 A (capacidad de 24 W)**.
  * Debido a que los cuatro motores paso a paso NEMA 17 poseen especificaciones nominales de corriente de fase de entre 1,5 A y 2 A cada uno (lo que superaría el límite de 2 A si operaran todos simultáneamente a plena carga), el sistema **no activa los cuatro motores al mismo tiempo con su corriente nominal máxima**.
  * Para evitar sobrecargar la fuente o provocar reinicios en el microcontrolador, se limita la corriente en los drivers A4988 ajustando el voltaje de referencia (\\(V_{ref}\\)) y se ejecuta una **activación secuencial de las articulaciones**: durante el levantamiento se activan principalmente dos articulaciones (elevación/hombro y soporte), mientras las otras dos funcionan a menor corriente o permanecen desactivadas.  
    *(Fuente: Ntambara, Furaha et al., 2026, Sección 3, Sección 3.5 y Sección 4.7; la página impresa no me figura en las fuentes)*.

* **Qué hacen para compensarlo (Estrategias de compensación):**
  1. **Reducción mecánica por engranajes (Spur gear transmission):** Incorporan una etapa de engranajes rectos con una relación de transmisión de **4:1**, lo que multiplica el torque del motor (generando ~6,0 Nm en la articulación frente a los 2,04 Nm de torque de servicio necesarios), alcanzando un factor de seguridad del actuador de **2,94**. *(Sección 3.3 y 3.8)*.
  2. **Movimiento a baja velocidad (Slow speed movement):** Operan el brazo a velocidad reducida con secuencias de pasos predeterminadas, previniendo la pérdida de pasos (*step-loss*) sin exigir picos de corriente instantáneos. *(Sección 3.8)*.
  3. **Diseño liviano e impreso en 3D:** Diseñaron los eslabones en PLA/PETG con vaciados y geometrías optimizadas para reducir la masa y el momento de inercia. *(Sección 3.1 y 4.4)*.

---

💡 Si lo deseas, podemos redactar un cuadro sintético que resuma los factores de seguridad, límites de alimentación y tiempos de ciclo observados en las tres plataformas robóticas.