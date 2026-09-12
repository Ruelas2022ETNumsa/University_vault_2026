---
ejercicio: E2 — Fundamentos de IA
archivo: E2_FUNDAMENTOS_ETN1010.py
estado: probado ✓
entorno: Google Colab (obligatorio)
---

# Notas de prueba — E2 Fundamentos

## Comportamiento observado

A diferencia del E1, este chatbot usa `difflib` para tolerar errores de escritura, por lo que acepta preguntas sin tilde y con ortografía aproximada.

Ejemplo: `que es la ia` (sin tilde) → responde correctamente.

## Preguntas base del diccionario

- `qué es la ia`
- `quién inventó la ia`
- `qué es machine learning`
- `qué es deep learning`
- `qué diferencia hay entre machine learning y deep learning`

## Comportamiento con preguntas desconocidas

Si el bot no reconoce la pregunta, muestra un campo para enseñarle una respuesta nueva.

**Caso especial — entrada vacía (solo Enter):**
Queda atrapado pidiendo que se ingrese una respuesta. La única salida es escribir una pregunta válida y guardarla para cerrar el panel.

## Comando de salida

`adiós` (con tilde) → muestra "¡Hasta luego!" y detiene el procesamiento.

## Persistencia de respuestas aprendidas

Las respuestas nuevas se guardan en `respuestas.json` dentro del entorno de Colab, pero son volátiles: al cerrar la sesión el archivo se elimina y el chatbot vuelve al diccionario base.

Para ver el JSON durante la sesión:

```python
import json
with open("respuestas.json", "r", encoding="utf-8") as f:
    print(json.dumps(json.load(f), ensure_ascii=False, indent=4))
```

Para descargarlo:

```python
from google.colab import files
files.download("respuestas.json")
```

## JSON obtenido en la prueba

```json
{
    "qué es la ia": "La Inteligencia Artificial es la simulación de la inteligencia humana en computadoras.",
    "quién inventó la ia": "El término 'IA' fue acuñado por John McCarthy en 1956.",
    "qué es machine learning": "Machine Learning es un subconjunto de la IA que permite a las máquinas aprender a partir de datos sin ser programadas explícitamente.",
    "qué es deep learning": "Deep Learning es un tipo de Machine Learning basado en redes neuronales profundas.",
    "qué diferencia hay entre machine learning y deep learning": "Machine Learning abarca diferentes técnicas de aprendizaje automático, mientras que Deep Learning usa redes neuronales profundas para procesar datos complejos.",
    "adios": "chao, te cuidas",
    "nos vemos": "bye",
    "¡hasta luego!": "x"
}
```

## Resultado

Funciona correctamente en Colab. Screenshot tomado mostrando la interfaz con widgets y respuestas exitosas.
