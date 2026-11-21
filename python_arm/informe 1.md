# Brazo robótico LEGO con visión por cámara para recoger y depositar objetos

**Autores:** [pendiente]
**Asignatura / institución:** [pendiente]
**Fecha:** [pendiente]

> **Estado del borrador (21-nov-2026):** solo la Introducción. El brazo aún no está terminado, por lo que no hay resultados ni conclusiones. Las referencias [1] a [8] se tomaron de `referencia.md` y `resumen_16.md`, donde solo se leyeron extractos, no los trabajos completos. Antes de entregar hay que leerlas y confirmar cada afirmación que se apoya en ellas.

---

## 1. Introducción

### 1.1 Contexto

Los brazos robóticos que recogen un objeto y lo colocan en otro lugar (*pick and place*) son una de las aplicaciones más comunes de la robótica de manipulación. Para que el brazo sepa dónde está el objeto, un enfoque habitual es agregar una cámara y procesar la imagen. En proyectos de bajo costo, una solución frecuente es segmentar el color del objeto, obtener su centroide en la imagen y convertir esa posición en los ángulos de las articulaciones, ya sea con cinemática inversa o con calibraciones más simples [1][2].

Este enfoque también se ha llevado a plataformas educativas basadas en LEGO. Existen proyectos de brazos con el hub LEGO Inventor 51515 que siguen una pelota roja con una cámara web [3], y un proyecto oficial de Pybricks con un brazo LEGO SPIKE Prime y cámara que detecta objetos de colores para tomarlos [4]. Otros trabajos con LEGO delegan la visión a una computadora externa, porque la cámara del propio robot no tiene la potencia necesaria [5].

Pybricks, un firmware alternativo en MicroPython para los hubs LEGO, ofrece además una función en versión beta llamada *smart sensors*, que permite usar la cámara de un teléfono como sensor conectado al hub [6]. Este trabajo aprovecha esa función para dotar de visión a un brazo armado con piezas y motores LEGO.

### 1.2 Planteamiento del problema

El proyecto parte de un brazo construido con un hub LEGO Inventor 51515 con firmware Pybricks y cuatro motores: base giratoria, codo, muñeca y garra. Se busca que el brazo encuentre una pelota roja con la cámara de un celular, la agarre y la deje en un cubo café, usando la computadora solo para dar comandos por teclado.

Esto presenta varias dificultades propias de un montaje de bajo costo:

- **Alimentación limitada.** El brazo funciona solo con alimentación USB, sin batería. Por eso se mueve un motor a la vez y se vigila el voltaje del hub, con una pausa si baja de 5500 mV.
- **Precisión limitada.** Los motores no tienen la precisión de un brazo industrial y, según observaciones previas del proyecto, al soltarlos aparecen desvíos de pocos grados y holguras en los engranajes.
- **Relación entre la imagen y el movimiento.** La cámara entrega la posición del objeto en la imagen (`x`, `y`, ancho y alto), pero el brazo necesita ángulos de motor. Hace falta un procedimiento que conecte ambas cosas.
- **Cámara montada sobre el brazo.** Tras agregar un soporte trasero, la cámara gira junto con el brazo. Esto obliga a tomar las calibraciones siempre con el brazo en la misma posición de referencia.

### 1.3 Objetivos

**Objetivo general**

Desarrollar un brazo robótico LEGO controlado con Pybricks que localice una pelota roja con la cámara de un celular, la tome y la deposite en un cubo café.

**Objetivos específicos**

1. Definir y programar las cuatro articulaciones del brazo (base, codo, muñeca y garra) con sus multiplicadores y rangos de movimiento.
2. Integrar la cámara del celular como *smart sensor* del hub, de modo que el programa reciba la posición y el tamaño de la pelota y del cubo.
3. Diseñar un procedimiento de calibración manual que registre, para varias posiciones, la lectura de la cámara junto con los ángulos del brazo, y que genere las tablas de toma y de depósito.
4. Implementar una rutina automática que busque el cubo y la pelota, calcule la pose del brazo interpolando las tablas, tome la pelota, la deje en el cubo y regrese a la posición inicial.
5. Evaluar el desempeño del sistema. *(Pendiente: depende de terminar el montaje y de definir las pruebas.)*

### 1.4 Alcance y limitaciones

El alcance actual incluye el brazo de cuatro motores, un único hub conectado a la computadora (programa y comandos por teclado) y al celular (cámara). La pelota y el cubo permanecen quietos durante cada ejecución.

Quedan fuera del alcance de esta etapa:

- Control del brazo desde el celular. Existe la idea de conectar un ESP32 al brazo y a su vez a un celular para manejarlo de esa forma, pero **no está implementada** y se presenta solo como trabajo futuro.
- Alimentación con batería, que cambiaría la restricción de mover un motor a la vez.

Limitaciones conocidas:

- La función *smart sensors* de Pybricks está en beta y exige la versión beta de la aplicación y un firmware actualizado [6]. La guía oficial describe los pasos para SPIKE Prime; con el Inventor 51515 la prueba del proyecto indica que funciona igual, pero la documentación no lo nombra.
- El brazo todavía no está terminado. En una primera prueba real el programa funcionó en general, pero faltan ajustes de posición inicial, de salida en pantalla y de recalibración de la cámara con el nuevo montaje.

### 1.5 Trabajos relacionados

La tabla resume los antecedentes más cercanos a este proyecto y qué aporta cada uno.

| Referencia | Qué hace | Relación con este trabajo |
| ---------- | -------- | ------------------------- |
| Brazo de 3 GDL con una sola cámara cenital [1] | Segmenta por color en HSV, obtiene el centroide y calcula los ángulos con cinemática inversa. Se validó con luz controlada, cámara fija y pocas pruebas. | Mismo principio de detectar por color; este proyecto usa tablas calibradas en lugar de cinemática inversa. |
| Kit educativo de visión con brazo de 3 GDL [2] | Deriva la cinemática inversa con trigonometría proyectando sobre el plano. | Referencia para una posible mejora geométrica del cálculo de ángulos. |
| VISION, LEGO Ideas [3] | Brazo con hub Inventor 51515 y cámara web en una PC para seguir una pelota roja. | Es el más parecido al hardware. Aquí la cámara es un celular conectado al hub. |
| Brazo con visión de Pybricks [4] | Brazo SPIKE Prime con cámara de celular que detecta objetos de colores para tomarlos. | Base del proyecto: se adaptó el hub, los puertos, el color y el arranque. |
| LEGO con Raspberry Pi y OpenCV [5] | Procesa la visión en una Raspberry Pi y se comunica con el robot por Bluetooth. | Alternativa de arquitectura, descartada por ahora para no agregar equipos. |

### 1.6 Organización del informe

*(Propuesta, sujeta a cambios según avance el proyecto.)*

- **Sección 2. Marco teórico y herramientas:** Pybricks, *smart sensors*, visión por color y calibración.
- **Sección 3. Diseño del sistema:** montaje mecánico, articulaciones, alimentación y comunicación.
- **Sección 4. Implementación:** calibración manual, tablas de toma y depósito y rutina automática.
- **Sección 5. Pruebas y resultados:** pendiente hasta terminar el brazo.
- **Sección 6. Conclusiones y trabajo futuro:** incluye la idea del ESP32.

---

## Referencias

[1] Low Cost Single Camera Robotic Arm for Vision Guided Pick and Place. *Journal of Robotics and Control* (JRC), 2026. https://journal.umy.ac.id/index.php/jrc/article/view/28524

[2] Kit educativo de visión con brazo robótico de 3 GDL. ASEE. https://peer.asee.org/45199.pdf

[3] VISION. LEGO Ideas. https://ideas.lego.com/challenges/339f0029-37b3-4dad-9dd2-6bcec3b93349/application/1099c817-11f6-4d42-8224-381674d1c749

[4] Robotic arm with vision. Pybricks. https://pybricks.com/project/robot-arm-camera-tracker/

[5] LEGO con Raspberry Pi y OpenCV. Universidad de Tampere. https://joedavid-tuni.github.io/MR3/

[6] Use your phone as a smart sensor. Pybricks. https://pybricks.com/learn/smart-sensors/getting-started/

[7] Proyectos de Pybricks. https://pybricks.com/project/python/

[8] Documentación de `messaging` (AppData, BLERadio). Pybricks. https://docs.pybricks.com/en/stable/messaging/index.html
