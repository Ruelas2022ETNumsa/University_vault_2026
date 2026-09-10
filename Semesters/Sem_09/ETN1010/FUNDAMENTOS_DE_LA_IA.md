# Fundamentos de la Inteligencia Artificial

Ing. Ruben Tarquino

<div style="page-break-after: always;"></div>

# ¿Qué es la Inteligencia Artificial?

## Definición:

Inteligencia Artificial (IA) es el campo de la informática que busca desarrollar sistemas capaces de realizar tareas que normalmente requieren inteligencia humana, como el aprendizaje, la toma de decisiones y el reconocimiento de patrones.

## Ejemplos:

**Siri y Alexa:** Asistentes virtuales que responden preguntas.

**ChatGPT:** Procesamiento de lenguaje natural (NLP) avanzado.

**Tesla Autopilot:** Conducción autónoma mediante redes neuronales.

<div style="page-break-after: always;"></div>

# Características de un sistema inteligente

**Aprendizaje:** Capacidad de mejorar su rendimiento con datos.

Ejemplo: Un asistente virtual como Siri o Google Assistant mejora sus respuestas con el uso continuo y la retroalimentación de los usuarios.

**Razonamiento:** Capacidad de tomar decisiones basadas en reglas.

Ejemplo: Un chatbot de servicio al cliente que analiza preguntas y selecciona la mejor respuesta basada en un conjunto de reglas predefinidas.

**Percepción:** Análisis de imágenes, sonidos y textos.

Ejemplo: Los coches autónomos utilizan cámaras y sensores para detectar señales de tráfico, peatones y otros vehículos.

**Interacción:** Comunicación con humanos y otros sistemas.

Ejemplo: Amazon Alexa, que recibe comandos de voz y controla dispositivos inteligentes en un hogar.

<div style="page-break-after: always;"></div>

# Test de Turing

El Test de Turing es una prueba propuesta por el matemático y científico de la computación Alan Turing en 1950 para determinar si una máquina puede exhibir un comportamiento inteligente equivalente al de un ser humano.

El test se basa en un experimento en el que un juez humano mantiene una conversación escrita con dos participantes:
- Un humano
- Una máquina (inteligencia artificial)

Si el juez no puede distinguir con certeza cuál de los dos es la máquina basándose únicamente en sus respuestas, se considera que la máquina ha pasado el Test de Turing.

<div style="page-break-after: always;"></div>

## Objetivo del Test

- Evaluar la capacidad de una inteligencia artificial para imitar el lenguaje y el pensamiento humano lo suficientemente bien como para engañar a un evaluador.

## Limitaciones

- No evalúa la comprensión real de la máquina, solo su capacidad de imitación.
- No mide la inteligencia general ni la conciencia, sino solo la habilidad de responder como un humano.
- Existen sistemas avanzados como ChatGPT o Google Bard que pueden superar el test en algunas circunstancias, pero siguen sin poseer una verdadera comprensión o conciencia.

En 2014, un programa llamado Eugene Goostman, que simulaba ser un niño ucraniano de 13 años, logró engañar a algunos jueces en un experimento. Sin embargo, el resultado fue debatido debido a las limitaciones del contexto.

El test sigue siendo un referente en la inteligencia artificial, aunque hoy en día se han desarrollado pruebas más avanzadas para evaluar la comprensión y la creatividad de las máquinas.

<div style="page-break-after: always;"></div>

# Ramas de la Inteligencia Artificial

Dentro de la IA, existen tres enfoques principales:

## 1. IA Simbólica (Basada en Reglas)

La IA simbólica se basa en el uso de reglas lógicas y representaciones explícitas del conocimiento para tomar decisiones y resolver problemas. Este enfoque fue dominante en las primeras investigaciones sobre IA.

### Características:

- Usa reglas "si-entonces" para estructurar el conocimiento.
- Emplea lógica formal y sistemas expertos para razonar sobre los datos.
- No aprende por sí misma; depende de la información programada por humanos.

<div style="page-break-after: always;"></div>

### Ejemplos:

- Sistemas expertos: Programas que imitan la toma de decisiones de un especialista en un área determinada (ej., diagnóstico médico).
- Planificación automática: Algoritmos que organizan tareas y optimizan recursos (ej., planificación de rutas en logística).

### Desventajas:

- Dificultad para manejar incertidumbre: No funciona bien cuando los datos son ambiguos o incompletos.
- Falta de escalabilidad: Es difícil programar manualmente todas las reglas necesarias para problemas complejos.

<div style="page-break-after: always;"></div>

## 2. IA Conexionista (Aprendizaje Automático)

La IA conexionista está inspirada en el funcionamiento del cerebro humano. Utiliza modelos matemáticos llamados redes neuronales **artificiales** para aprender patrones y realizar tareas sin necesidad de reglas predefinidas.

### Características:

Aprende a partir de grandes volúmenes **de** datos en lugar de reglas programadas.
Usa algoritmos de aprendizaje supervisado, no supervisado y por refuerzo.
Se adapta a situaciones nuevas sin intervención humana directa.

<div style="page-break-after: always;"></div>

### Ejemplos:

- Redes Neuronales Artificiales (ANNs): Modelos que procesan información en capas de "neuronas" interconectadas.
- Machine Learning: Algoritmos que identifican patrones en los datos y hacen predicciones (ej., reconocimiento de voz, visión por computadora).
- Deep Learning: Subcampo del Machine Learning que usa redes neuronales profundas para tareas más complejas (ej., ChatGPT, asistentes virtuales).

### Desventajas:

- Necesita grandes volúmenes de datos para entrenarse correctamente.
- Computacionalmente costosa: Requiere hardware potente (como GPUs y TPUs).
- Difícil de interpretar: Los modelos de redes neuronales son frecuentemente considerados "cajas negras" debido a la falta de explicabilidad de sus decisiones.

<div style="page-break-after: always;"></div>

## 3. IA Basada en Comportamiento

Esta rama se centra en la creación de agentes autónomos que interactúan con su entorno y aprenden a comportarse de manera eficiente sin necesidad de una programación rígida.

### Características:

- No sigue reglas explícitas ni depende de datos masivos; aprende a partir de la interacción con su entorno.
- Se basa en principios de autoorganización, evolución y adaptabilidad.
- Es utilizada en robots y sistemas de simulación.

<div style="page-break-after: always;"></div>

### Ejemplos:

- Robótica autónoma: Robots que aprenden a moverse y tomar decisiones sin intervención humana directa (ej., robots exploradores en Marte).
- Sistemas multiagente: Simulaciones de entornos donde múltiples agentes interactúan y cooperan (ej., modelos de tráfico urbano, enjambres de drones).
- Simulaciones evolutivas: Algoritmos inspirados en la evolución biológica para mejorar soluciones a problemas (ej., algoritmos genéticos).

### Desventajas:

- Difícil de controlar: Al ser autónoma, puede generar comportamientos inesperados.
- Mayor complejidad en el diseño: Requiere simulaciones avanzadas para evaluar su efectividad.

<div style="page-break-after: always;"></div>

# Aplicaciones Actuales de la IA

**1. Salud:** Diagnóstico de enfermedades con IA.

**2. Finanzas:** Algoritmos de trading automático.

**3. Automóviles Autónomos:** Tesla y Waymo usan IA para conducción.

**4. Reconocimiento Facial:** IA en seguridad y redes sociales.

**5. Entretenimiento:** Netflix y Spotify usan IA para recomendaciones.

**6. IA Generativa:** ChatGPT, Midjourney, Stable Diffusion.

<div style="page-break-after: always;"></div>

## Ejercicio 1.

Implementar un pequeño chatbot que responda preguntas básicas sobre IA usando reglas simples.

```python
def chatbot():
    respuestas = {
        "qué es la ia": "La IA es la simulación de la inteligencia humana en computadoras.",
        "quién inventó la ia": "El término 'IA' fue acuñado por John McCarthy en 1956.",
        "adiós": "¡Hasta luego!"
    }
    print("¡Hola! Soy un chatbot de IA. Pregúntame algo.")
    while True:
        pregunta = input("Tú: ").lower()
        for clave in respuestas:
            if clave in pregunta:
                print(f"Chatbot: {respuestas[clave]}")
                if clave == "adiós":
                    return
                break
        else:
            print("Chatbot: No entiendo tu pregunta.")
chatbot()
```

<div style="page-break-after: always;"></div>

## Ejercicio 2.

Modificar el chatbot para responder más preguntas sobre IA.

<div style="page-break-after: always;"></div>

```python
import ipywidgets as widgets
from IPython.display import display
import difflib

# Diccionario de respuestas
respuestas = {
    "qué es la ia": "La Inteligencia Artificial es la simulación de la inteligencia humana en computadoras.",
    "quién inventó la ia": "El término 'IA' fue acuñado por John McCarthy en 1956.",
    "qué es machine learning": "Machine Learning es un subconjunto de la IA que permite a las máquinas aprender a partir de datos sin ser programadas explícitamente.",
    "qué es deep learning": "Deep Learning es un tipo de Machine Learning basado en redes neuronales profundas.",
    "qué diferencia hay entre machine learning y deep learning": "Machine Learning abarca diferentes técnicas de aprendizaje automático, mientras que Deep Learning usa redes neuronales profundas para procesar datos complejos.",
    "qué es una red neuronal artificial": "Es un modelo inspirado en el cerebro humano, compuesto por neuronas artificiales organizadas en capas.",
    "qué es un chatbot": "Un chatbot es un programa que usa IA para interactuar con los usuarios mediante texto o voz.",
    "cómo funciona el reconocimiento facial": "Utiliza redes neuronales y técnicas de visión por computadora para identificar rostros en imágenes o videos.",
    "dónde se usa la ia": "La IA se usa en salud, finanzas, automóviles autónomos, entretenimiento, seguridad y muchos más sectores.",
}

# Widgets en Google Colab
entrada = widgets.Text(placeholder="Escribe tu pregunta aquí...")
boton = widgets.Button(description="Enviar")
salida = widgets.Output()

def mejor_coincidencia(pregunta):
    """ Encuentra la mejor coincidencia basada en similitud de cadenas """
    coincidencias = difflib.get_close_matches(pregunta, respuestas.keys(), n=1, cutoff=0.6)
    return respuestas[coincidencias[0]] if coincidencias else None
```

<div style="page-break-after: always;"></div>

```python
def chatbot_interactivo(b):
    """ Maneja la lógica del chatbot interactivo """
    with salida:
        salida.clear_output()
        pregunta = entrada.value.strip().lower()
        if pregunta == "adiós":
            print("Chatbot: ¡Hasta luego!")
            return
        # Buscar respuesta exacta o la mejor coincidencia
        respuesta = respuestas.get(pregunta) or mejor_coincidencia(pregunta)

        if respuesta:
            print(f"Chatbot: {respuesta}")
        else:
            print("Chatbot: No conozco la respuesta. ¿Quieres enseñarme una respuesta para esta pregunta? (sí/no)")
            if input().strip().lower() == "sí":
                aprender_nueva_respuesta(pregunta)

def aprender_nueva_respuesta(pregunta):
    """ Permite al usuario agregar una nueva respuesta si no se encuentra """
    respuesta_usuario = input("Escribe la respuesta para esta pregunta: ")
    respuestas[pregunta] = respuesta_usuario
    print("Chatbot: ¡Gracias! He aprendido una nueva respuesta.")

boton.on_click(chatbot_interactivo)

# Mostrar interfaz en Google Colab
display(entrada, boton, salida)
```
