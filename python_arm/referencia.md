# Referencia: control de brazo robótico con visión e IA

Fecha: 13-nov-2026. Búsqueda hecha con Claude. Solo se leyeron los extractos de los resultados, **no los papers completos**. Sirve como lista de lectura para decidir qué ideas tomar para el brazo LEGO (ver `resumen_13_nov.md`, `resumen_8_nov.md` y `propuesta.md`).

---

## 1. Visión con OpenCV y cinemática inversa en brazos baratos

Los más cercanos al plan de cámara fija y objetos de colores.

- [Low Cost Single Camera Robotic Arm for Vision Guided Pick and Place (JRC, 2026)](https://journal.umy.ac.id/index.php/jrc/article/view/28524)
  - Brazo de 3 grados de libertad con cámara cenital. Segmentación HSV, contornos y centroide para obtener coordenadas, y cinemática inversa para calcular los ángulos.
  - Limitación declarada: solo validado con luz controlada, cámara fija, objetos en plano y pocas pruebas.
- [Visión en Raspberry Pi 4 para brazo de 3 GDL (Ingeniería e Investigación, UNAL)](https://revistas.unal.edu.co/index.php/ingeinv/article/download/118562/99002/800485)
  - Clasifica y apila objetos por forma y color con OpenCV. Cinemática inversa geométrica y perfiles de velocidad trapezoidales.
- [RecycleBot (Cornell)](https://courses.ece.cornell.edu/ece5990/ECE5725_Fall2018_Projects/yf92_yw2226_M/index.html)
  - Convierte a HSV para aislar un color. Por falta de tiempo usó una conversión lineal de píxel a posición. Útil para ver el atajo y por qué una homografía es mejor.
- [eyalabraham/robotic-arm (GitHub)](https://github.com/eyalabraham/robotic-arm)
  - OpenCV identifica bloques rojos, azules y verdes sobre una hoja blanca, calcula posición y orientación y los apila ordenados. Trae código descargable.
- [Kit educativo de visión con brazo de 3 GDL (ASEE)](https://peer.asee.org/45199.pdf)
  - Deriva la cinemática inversa con trigonometría, proyectando sobre el plano x-y. Misma geometría que la base más dos eslabones del brazo.

## 2. Brazos LEGO con visión

- [VISION, LEGO Ideas](https://ideas.lego.com/challenges/339f0029-37b3-4dad-9dd2-6bcec3b93349/application/1099c817-11f6-4d42-8224-381674d1c749)
  - Brazo con hub Inventor 51515 al que se conecta una PC con webcam para seguir una pelota roja en tres dimensiones. **El más parecido al hardware actual.**
- [Proyectos de Pybricks](https://pybricks.com/project/python/)
  - Incluye un brazo LEGO SPIKE Prime con cámara que detecta objetos de colores para tomarlos.
- [LEGO con Raspberry Pi y OpenCV (Tampere)](https://joedavid-tuni.github.io/MR3/)
  - Conecta el robot por Bluetooth y corre OpenCV en una Raspberry Pi, porque la cámara del EV3 no tiene potencia para visión. Sirve para ver cómo resuelven la comunicación PC-hub.

## 3. Torre de Hanói con brazo

- [RoboGPT (arXiv 2304.11018)](https://arxiv.org/pdf/2304.11018)
  - Usó ChatGPT-4 para generar la secuencia de Hanói con un brazo Franka. Un módulo de visión reconoce discos y torres; las torres se marcaron con etiquetas cuadradas para simplificar. Referencia de "IA que decide, brazo que ejecuta".
- [Hanoi-iiwa](https://ningshan-gif.github.io/project/hanoi)
  - Usa la recursión de 2ⁿ-1 movimientos. En simulación con 3 discos resolvió 10 de 10 corridas.
- [UR5 resolviendo Hanói (portafolio)](https://www.freelancer.sg/u/YosefMirsky/portfolio/Industrial-robot-arm-solving-the-Towers-of-Hanoi-puzzle-3597378)
  - El robot primero mide tamaño y posición de cada disco y recién corre la recursión cuando los datos coinciden con lo esperado. Idea de verificar el estado antes de mover.
- [Proyecto de Iowa State sobre colocar discos en postes](https://home.engineering.iastate.edu/alexs/classes/2011_Spring_585X/final_projects/Campbell_project.pdf)
  - Se centra en el problema de meter el disco en el poste, no en resolver el puzle. Toca el punto débil de precisión.
- [OMiLAB XOMiArm4](https://austria.omilab.org/psm/content/xomiarm4/info?view=desc)
  - Permite jugar a Hanói con un brazo, o que el sistema calcule y ejecute los movimientos solo. Gran parte se validó sin el brazo, en un espacio virtual.

## 4. Tesis y calibración cámara-brazo

- [Tesis de Laratta (Padova)](https://thesis.unipd.it/retrieve/14757125-380d-4a79-9d01-bfaf5746bab9/Laratta_Luigi.pdf.pdf)
  - Calibración de cámara, validación, detección de marcadores ArUco y localización de objetos.
- [Tesis de Koznarová (CTU Praga)](https://dspace.cvut.cz/bitstream/handle/10467/83354/F3-DP-2019-Koznarova-Zuzana-Vision-guided_handling_operations_for_assistive_robots_in_un-structured_environments.pdf)
  - Compara detección con transformada de Hough, YOLO y características, y trata la calibración robot-cámara.
- [Dobot con homografía y OpenCV (PNJ)](https://repository.pnj.ac.id/21204/7/BAGIAN%201%20%281%29.pdf)
  - Usa una webcam Logitech C270 y homografía para calibrar coordenadas entre cámara y brazo. Es el método que propone `propuesta.md`.

## 5. Contexto de IA (más teórico)

- [Survey de aprendizaje por refuerzo profundo en manipulación (Sensors, 2023)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10098871/)
  - Recorre algoritmos basados en valor, en política y actor-crítico para manipulación.
- [Mini-review de DRL en control de manipulación (arXiv 2102.04148)](https://arxiv.org/pdf/2102.04148)
  - Concluye que aprender habilidades robustas con DRL sigue lejos de estar resuelto para aplicaciones reales.
- [Survey de modelos visión-lenguaje-acción (arXiv 2508.13073)](https://arxiv.org/pdf/2508.13073v2)
  - Revisa modelos que combinan un modelo visión-lenguaje grande con generación de acciones, monolíticos o jerárquicos.

---

## Qué tomar y qué evitar (opinión de Claude)

- **Aplica directo:** sección 1 (OpenCV + cinemática inversa), VISION de LEGO, y los de Hanói con verificación de estado.
- **RoboGPT** es la referencia para plantear "la IA decide, el brazo ejecuta". Para Hanói los movimientos salen de una recursión exacta, sin IA.
- **Calibración:** los de la sección 4 respaldan la homografía píxel → cm con marcas medidas.
- **Solo contexto:** aprendizaje por refuerzo y modelos VLA. Exigen simulación, entrenamiento y hardware con más precisión que el del brazo actual.
- **Riesgo común:** los desvíos al soltar los motores (unos pocos grados) y la muñeca rotacional pueden complicar meter un disco en un poste.

---

## Prompt para Perplexity

Copiar y pegar tal cual. Conviene usar modo **Pro/Deep Research** y la opción de fuentes **Académico** para la primera parte.

```
Actúa como investigador en robótica. Necesito referencias reales y verificables (con enlace) para un proyecto de brazo robótico de bajo costo controlado por visión por computadora e inteligencia artificial.

CONTEXTO DEL PROYECTO
- Brazo hecho con motores LEGO (hub LEGO Inventor 51515 con firmware Pybricks, MicroPython), alimentado por USB desde una PC.
- 4 motores: base giratoria (rotacional), hombro (levanta el brazo), muñeca (rotacional) y garra. Sin encoders de alta precisión; al soltar los motores hay desvíos de pocos grados.
- Objetivo: que una cámara fija con OpenCV vea el entorno (objetos de colores o distintos tamaños), la PC calcule qué mover y envíe al hub los ángulos de cada articulación. Primer objetivo concreto: resolver la Torre de Hanói; luego pick and place general.
- La PC debe comunicarse con el hub (Bluetooth o USB), por ejemplo con pybricksdev, bleak o stdin/stdout del hub.

BUSCA Y ENTRÉGAME, agrupado por tema, con título, año, enlace y 2 líneas de resumen de cada uno:
1. Papers, tesis y proyectos de brazos robóticos de bajo costo con visión (OpenCV, segmentación HSV, homografía o calibración píxel→coordenadas) y cinemática inversa para pick and place.
2. Proyectos de brazos LEGO (Mindstorms, SPIKE, Robot Inventor, Pybricks) controlados desde una PC con cámara o visión.
3. Robots que resuelven la Torre de Hanói (con brazo real), indicando cómo detectan el estado, cómo calculan los movimientos y qué precisión lograron al colocar los discos.
4. Trabajos que usan modelos de lenguaje o IA (por ejemplo LLM, VLM o modelos visión-lenguaje-acción) para planificar tareas de un brazo, y comparaciones entre OpenCV clásico y detección con redes neuronales (YOLO, etc.) en entornos controlados.
5. Métodos para compensar la imprecisión del brazo con retroalimentación visual (lazo cerrado, visual servoing) en robots de bajo costo.
6. Comunicación entre una PC y un hub Pybricks (Bluetooth o USB): ejemplos de código o repositorios en GitHub.

REGLAS
- Solo fuentes reales con enlace. Si no encuentras algo, dilo; no inventes referencias.
- Prefiere trabajos de 2018 en adelante, pero incluye clásicos si son muy relevantes.
- Al final, dame una tabla comparativa: referencia | qué hardware usa | cómo detecta objetos | cómo calibra | precisión reportada | qué puedo reutilizar en mi proyecto.
- Marca cuáles son más parecidos a mi caso (hardware LEGO, cámara fija, objetos de colores).
```

**Variante corta (para búsqueda rápida):**

```
Dame 10 proyectos, tesis o papers con enlace de brazos robóticos de bajo costo (idealmente LEGO o Pybricks) que usen OpenCV y cinemática inversa para pick and place, incluyendo al menos 3 que resuelvan la Torre de Hanói. Para cada uno: hardware, método de detección, método de calibración y precisión lograda. No inventes enlaces.
```
