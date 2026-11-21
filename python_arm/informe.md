# Brazo robótico LEGO con visión por cámara para recoger y depositar objetos

**Autores:** [pendiente]
**Asignatura / institución:** [pendiente]
**Docente:** [pendiente]
**Fecha:** [pendiente]

> **Estado del borrador (21-nov-2026):** reorganizado según el esquema del docente (ver `resumen_21.md`). Tienen contenido las secciones 1 y 2. Las secciones 3, 4 y 5 son estructura con marcas `[pendiente]`. El brazo aún no está terminado, por lo que no hay resultados ni conclusiones.
>
> **Citas y referencias (APA 7):** las fuentes se leyeron solo por extractos (`referencia.md`, `resumen_16.md`), no completas. Donde falta el dato de autor o de año aparece `[pendiente]`. Hay que leer los trabajos completos, completar esos datos y confirmar cada afirmación antes de entregar. Copia anterior de este archivo: `informe 1.md`.

---

## 1. Introducción y antecedentes

### 1.1 Antecedentes

Los brazos robóticos que recogen un objeto y lo colocan en otro lugar (*pick and place*) son una de las aplicaciones más comunes de la robótica de manipulación. Para que el brazo sepa dónde está el objeto, un enfoque habitual es agregar una cámara y procesar la imagen. En proyectos de bajo costo, una solución frecuente es segmentar el color del objeto, obtener su centroide en la imagen y convertir esa posición en los ángulos de las articulaciones, ya sea con cinemática inversa o con calibraciones más simples (Autores [pendiente], 2026; Autores [pendiente], [año pendiente]).

Este enfoque también se ha llevado a plataformas educativas basadas en LEGO. Existen proyectos de brazos con el hub LEGO Inventor 51515 que siguen una pelota roja con una cámara web (LEGO Ideas, s. f.), y un proyecto oficial de Pybricks con un brazo LEGO SPIKE Prime y cámara que detecta objetos de colores para tomarlos (Pybricks, s. f.-a). Otros trabajos con LEGO delegan la visión a una computadora externa, porque la cámara del propio robot no tiene la potencia necesaria (Autor [pendiente], s. f.).

Pybricks, un firmware alternativo en MicroPython para los hubs LEGO, ofrece además una función en versión beta llamada *smart sensors*, que permite usar la cámara de un teléfono como sensor conectado al hub (Pybricks, s. f.-b).

La Tabla 1 resume los antecedentes más cercanos a este proyecto y qué aporta cada uno.

**Tabla 1**

*Antecedentes más cercanos al proyecto*

| Antecedente | Qué hace | Relación con este trabajo |
| ----------- | -------- | ------------------------- |
| Brazo de 3 GDL con una sola cámara cenital (Autores [pendiente], 2026) | Segmenta por color en HSV, obtiene el centroide y calcula los ángulos con cinemática inversa. Se validó con luz controlada, cámara fija y pocas pruebas. | Mismo principio de detectar por color; este proyecto usa tablas calibradas en lugar de cinemática inversa. |
| Kit educativo de visión con brazo de 3 GDL (Autores [pendiente], [año pendiente]) | Deriva la cinemática inversa con trigonometría proyectando sobre el plano. | Referencia para una posible mejora geométrica del cálculo de ángulos. |
| VISION (LEGO Ideas, s. f.) | Brazo con hub Inventor 51515 y cámara web en una PC para seguir una pelota roja. | Es el más parecido al hardware. Aquí la cámara es un celular conectado al hub. |
| Brazo con visión de Pybricks (Pybricks, s. f.-a) | Brazo SPIKE Prime con cámara de celular que detecta objetos de colores para tomarlos. | Base del proyecto: se adaptó el hub, los puertos, el color y el arranque. |
| LEGO con Raspberry Pi y OpenCV (Autor [pendiente], s. f.) | Procesa la visión en una Raspberry Pi y se comunica con el robot por Bluetooth. | Alternativa de arquitectura, descartada por ahora para no agregar equipos. |

*Nota.* Elaboración propia a partir de las fuentes citadas. Verificar contra los trabajos completos.

### 1.2 Propósito general del trabajo

Construir y documentar un brazo robótico con motores y hub LEGO Inventor 51515 con firmware Pybricks que use la cámara de un celular para encontrar una pelota roja, tomarla y dejarla en un cubo café, con la computadora usada solo para dar comandos por teclado.

---

## 2. Objetivo

### 2.1 Objetivo general

Desarrollar un brazo robótico LEGO controlado con Pybricks que localice una pelota roja con la cámara de un celular, la tome y la deposite en un cubo café.

### 2.2 Objetivos específicos

1. Definir y programar las cuatro articulaciones del brazo (base, codo, muñeca y garra) con sus multiplicadores y rangos de movimiento.
2. Integrar la cámara del celular como *smart sensor* del hub, de modo que el programa reciba la posición y el tamaño de la pelota y del cubo.
3. Diseñar un procedimiento de calibración manual que registre, para varias posiciones, la lectura de la cámara junto con los ángulos del brazo, y que genere las tablas de toma y de depósito.
4. Implementar una rutina automática que busque el cubo y la pelota, calcule la pose del brazo interpolando las tablas, tome la pelota, la deje en el cubo y regrese a la posición inicial.
5. Evaluar el desempeño del sistema. *[Pendiente: depende de terminar el montaje y de definir las pruebas.]*

### 2.3 Alcance

El estudio incluye el brazo de cuatro motores, un único hub conectado a la computadora (programa y comandos por teclado) y al celular (cámara). La pelota y el cubo permanecen quietos durante cada ejecución.

Quedan fuera del alcance de esta etapa:

- El control del brazo desde el celular. Existe la idea de conectar un ESP32 al brazo y a su vez a un celular para manejarlo de esa forma, pero no está implementada y se menciona solo como trabajo futuro.
- La alimentación con batería, que cambiaría la restricción de mover un motor a la vez.

### 2.4 Limitaciones

- **Alimentación limitada.** El brazo funciona solo con alimentación USB, sin batería. Por eso se mueve un motor a la vez y se vigila el voltaje del hub, con una pausa si baja de 5500 mV.
- **Precisión limitada.** Los motores no tienen la precisión de un brazo industrial y, según observaciones previas del proyecto, al soltarlos aparecen desvíos de pocos grados y holguras en los engranajes.
- **Cámara montada sobre el brazo.** Tras agregar un soporte trasero, la cámara gira junto con el brazo, por lo que las calibraciones deben tomarse siempre con el brazo en la misma posición de referencia. *[Por confirmar con pruebas.]*
- **Función en beta.** La función *smart sensors* de Pybricks exige la versión beta de la aplicación y un firmware actualizado (Pybricks, s. f.-b). La guía oficial describe los pasos para SPIKE Prime; con el Inventor 51515 la prueba del proyecto indica que funciona igual, pero la documentación no lo nombra.
- **Montaje en desarrollo.** El brazo todavía no está terminado. En una primera prueba real el programa funcionó en general, pero faltan ajustes de posición inicial, de salida en pantalla y de recalibración de la cámara con el nuevo montaje.

---

## 3. Justificación del proyecto

> Esta sección responde: ¿por qué se quiere hacer el estudio y para qué servirá? Hay que definirla con el usuario; no se escribió contenido para no inventar datos de la institución.

### 3.1 Importancia para la institución

[pendiente: por qué el estudio es importante para la institución.]

### 3.2 Escenario del proyecto

[pendiente: dónde y en qué contexto se desarrolla el proyecto.]

### 3.3 Impacto esperado y utilidad

Indicar qué impacto se busca lograr al terminar el proyecto y para qué servirá.

| Tipo de impacto | Qué se busca lograr |
| --------------- | ------------------- |
| Científico | [pendiente] |
| Tecnológico | [pendiente] |
| Económico | [pendiente] |
| Social | [pendiente] |
| Ambiental | [pendiente] |
| Otro | [pendiente] |

---

## 4. Desarrollo del proyecto

### 4.1 Marco teórico

[pendiente: se redactará con las fuentes de Perplexity y NotebookLM. Temas previstos:]

- Brazos robóticos y tareas de *pick and place*
- Plataforma LEGO Inventor 51515 y firmware Pybricks
- *Smart sensors* de Pybricks: celular como cámara del hub
- Segmentación de color (HSV) y detección de objetos
- Calibración entre la cámara y el brazo: tablas e interpolación
- Cinemática del brazo (como contraste con el método de tablas)
- Imprecisión de motores sin encoders de alta precisión

### 4.2 Diseño del sistema

[pendiente: montaje mecánico, articulaciones (puertos, multiplicadores y rangos), alimentación y comunicación. Material de partida en `resumen_16.md`.]

### 4.3 Implementación

[pendiente: calibración manual, tablas de toma y depósito y rutina automática (`ha7.py`).]

### 4.4 Pruebas y resultados

[pendiente: hasta terminar el brazo.]

---

## 5. Conclusiones y recomendaciones

### 5.1 Conclusiones

[pendiente: dependen de terminar el brazo y de las pruebas.]

### 5.2 Recomendaciones

[pendiente: incluye la idea futura del ESP32 conectado al brazo y a un celular.]

---

## 6. Referencias bibliográficas e internet

> Formato APA 7. Completar autores y años al leer los trabajos completos, y ordenar la lista alfabéticamente al terminar. Solo se listan las fuentes citadas en el texto.

[Autores pendientes]. (2026). Low cost single camera robotic arm for vision guided pick and place. *Journal of Robotics and Control (JRC)*. https://journal.umy.ac.id/index.php/jrc/article/view/28524

[Autores pendientes]. ([año pendiente]). *Kit educativo de visión con brazo robótico de 3 GDL* [Artículo de conferencia]. American Society for Engineering Education (ASEE). https://peer.asee.org/45199.pdf

[Autor pendiente]. (s. f.). *LEGO con Raspberry Pi y OpenCV* [Proyecto]. Tampere University. https://joedavid-tuni.github.io/MR3/

LEGO Ideas. (s. f.). *VISION* [Propuesta de proyecto]. https://ideas.lego.com/challenges/339f0029-37b3-4dad-9dd2-6bcec3b93349/application/1099c817-11f6-4d42-8224-381674d1c749

Pybricks. (s. f.-a). *Robotic arm with vision*. https://pybricks.com/project/robot-arm-camera-tracker/

Pybricks. (s. f.-b). *Use your phone as a smart sensor*. https://pybricks.com/learn/smart-sensors/getting-started/

---

## Guía resumen del manual de publicaciones con normas APA

> Resumen breve de las reglas APA 7 que se aplican en este informe. Preliminar: contrastar con el texto que envió el docente y confirmar con él cómo debe presentarse esta sección.

- **Cita en el texto:** autor y año entre paréntesis, por ejemplo (Pybricks, s. f.). Con dos autores se unen con "y"; con tres o más se usa "et al.".
- **Sin fecha:** se escribe "s. f.". Si hay varias obras del mismo autor sin fecha, se distinguen con letras: s. f.-a, s. f.-b.
- **Cita textual corta** (menos de 40 palabras): entre comillas, con autor, año y página.
- **Lista de referencias:** en orden alfabético, con sangría francesa. Cada fuente citada debe estar en la lista y viceversa.
- **Páginas web y documentos en línea:** autor, fecha, título en cursiva y enlace. Si hay DOI, se escribe como enlace (https://doi.org/...).
- **Tablas y figuras:** número en negrita, título en cursiva debajo del número, y una nota si hace falta ("*Nota.*").

---

## Anexo A. Lista de acrónimos

*(Actualizar a medida que se redacte el texto final.)*

| Acrónimo | Significado |
| -------- | ----------- |
| ASEE | American Society for Engineering Education |
| GDL | Grados de libertad |
| HSV | Tono, saturación y valor (*hue, saturation, value*) |
| JRC | Journal of Robotics and Control |
| OpenCV | Open Source Computer Vision Library |
| USB | Bus serie universal (*Universal Serial Bus*) |
