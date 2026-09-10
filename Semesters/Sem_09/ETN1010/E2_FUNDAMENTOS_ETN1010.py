import ipywidgets as widgets
from IPython.display import display
import difflib
import json

# Archivo donde se almacenarán las respuestas aprendidas
ARCHIVO_RESPUESTAS = "respuestas.json"

# Cargar respuestas desde el archivo JSON
try:
    with open(ARCHIVO_RESPUESTAS, "r", encoding="utf-8") as f:
        respuestas = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    respuestas = {
        "qué es la ia": "La Inteligencia Artificial es la simulación de la inteligencia humana en computadoras.",
        "quién inventó la ia": "El término 'IA' fue acuñado por John McCarthy en 1956.",
        "qué es machine learning": "Machine Learning es un subconjunto de la IA que permite a las máquinas aprender a partir de datos sin ser programadas explícitamente.",
        "qué es deep learning": "Deep Learning es un tipo de Machine Learning basado en redes neuronales profundas.",
        "qué diferencia hay entre machine learning y deep learning": "Machine Learning abarca diferentes técnicas de aprendizaje automático, mientras que Deep Learning usa redes neuronales profundas para procesar datos complejos.",
    }

def guardar_respuestas():
    """ Guarda las respuestas en un archivo JSON para que persistan. """
    with open(ARCHIVO_RESPUESTAS, "w", encoding="utf-8") as f:
        json.dump(respuestas, f, ensure_ascii=False, indent=4)

# Widgets en Google Colab
entrada = widgets.Text(placeholder="Escribe tu pregunta aquí...")
boton = widgets.Button(description="Enviar")
salida = widgets.Output()

# Widget para aprender nuevas respuestas
entrada_nueva_respuesta = widgets.Text(placeholder="Escribe la respuesta aquí...")
boton_aprender = widgets.Button(description="Guardar Respuesta")
controles_aprendizaje = widgets.VBox([entrada_nueva_respuesta, boton_aprender])
controles_aprendizaje.layout.display = 'none'  # Ocultar inicialmente
pregunta_actual = ""

def mejor_coincidencia(pregunta):
    """ Encuentra la mejor coincidencia basada en similitud de cadenas """
    coincidencias = difflib.get_close_matches(pregunta, respuestas.keys(), n=1, cutoff=0.6)
    return respuestas[coincidencias[0]] if coincidencias else None

def chatbot_interactivo(_):
    """ Maneja la lógica del chatbot interactivo """
    global pregunta_actual
    salida.clear_output()
    pregunta = entrada.value.strip().lower()

    if pregunta == "adiós":
        with salida:
            print("Chatbot: ¡Hasta luego!")
        return

    # Buscar respuesta exacta o la mejor coincidencia
    respuesta = respuestas.get(pregunta) or mejor_coincidencia(pregunta)

    with salida:
        if respuesta:
            print(f"Chatbot: {respuesta}")
        else:
            print("Chatbot: No conozco la respuesta. Escribe una respuesta y presiona 'Guardar Respuesta'.")
            pregunta_actual = pregunta  # Guardar la pregunta para aprendizaje
            controles_aprendizaje.layout.display = 'flex'  # Mostrar controles de aprendizaje

def aprender_nueva_respuesta(_):
    """ Permite al usuario agregar una nueva respuesta si no se encuentra """
    global pregunta_actual
    nueva_respuesta = entrada_nueva_respuesta.value.strip()
    if pregunta_actual and nueva_respuesta:
        respuestas[pregunta_actual] = nueva_respuesta
        guardar_respuestas()
        with salida:
            print("Chatbot: ¡Gracias! He aprendido una nueva respuesta.")
    entrada_nueva_respuesta.value = ""
    controles_aprendizaje.layout.display = 'none'  # Ocultar controles de aprendizaje

boton.on_click(chatbot_interactivo)
boton_aprender.on_click(aprender_nueva_respuesta)

# Mostrar interfaz en Google Colab
display(entrada, boton, salida, controles_aprendizaje)
