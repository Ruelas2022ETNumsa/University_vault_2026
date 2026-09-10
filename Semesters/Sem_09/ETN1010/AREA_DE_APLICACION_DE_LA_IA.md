# Áreas de Aplicación de la Inteligencia Artificial

Ing. Ruben Tarquino

<div style="page-break-after: always;"></div>

# Principales Áreas de Aplicación de la IA

La Inteligencia Artificial (IA) tiene impacto en diversas industrias, facilitando la automatización y mejorando la eficiencia. A continuación, exploramos algunas de sus aplicaciones más importantes:

## IA en la Salud

-Diagnóstico de enfermedades mediante redes neuronales.
-Predicción de epidemias a través del análisis de datos.
-Cirugías asistidas por robots.
-Procesamiento de imágenes médicas (radiografías, resonancias).

*Ejemplo:* IBM Watson en diagnóstico de cáncer.

<div style="page-break-after: always;"></div>

## IA en Finanzas

-Análisis de riesgos y predicción de fraudes.
-Algoritmos de trading automático.
-Chatbots bancarios y asistentes financieros.

*Ejemplo:* Robo-advisors como Betterment o Wealthfront.

## IA en la Industria Automotriz

-Vehículos autónomos (Tesla, Waymo).
-Sistemas de asistencia a la conducción (frenado automático, detección de peatones).
-Optimización de rutas y tráfico con IA.

<div style="page-break-after: always;"></div>

## IA en Seguridad y Vigilancia

- Reconocimiento facial para identificación en aeropuertos y sistemas de vigilancia.
- Análisis de video en tiempo real para detectar comportamientos sospechosos.

*Ejemplo:* Cámaras de seguridad con IA en aeropuertos.

## IA en el Entretenimiento

- Algoritmos de recomendación (Netflix, Spotify, YouTube).
- Creación de contenido con IA generativa (ChatGPT, Midjourney, DALL-E).

*Ejemplo:* IA de Google DeepMind para generación de música.

## IA en la Educación

- Sistemas de tutoría inteligente.
- Generación de materiales educativos personalizados.
- Evaluación automática de exámenes y tareas.

*Ejemplo:* Duolingo y su uso de IA para enseñanza de idiomas.

<div style="page-break-after: always;"></div>

# Herramientas Modernas para el Desarrollo de IA

## Lenguajes de Programación Más Utilizados

- **Python**: El más popular en IA por su facilidad de uso y librerías avanzadas.
- **Java**: Empleado en grandes sistemas de IA empresarial.
- **C++**: Utilizado en sistemas de IA en tiempo real (juegos, robótica).

## Principales Bibliotecas de IA

| Biblioteca | Uso |
|---|---|
| **TensorFlow** | Redes neuronales y aprendizaje profundo. |
| **PyTorch** | Modelos de Deep Learning flexibles. |
| **Scikit-learn** | Algoritmos de Machine Learning clásicos. |
| **OpenCV** | Visión por computadora y análisis de imágenes. |
| **NLTK / SpaCy** | Procesamiento de lenguaje natural (NLP). |
| **Keras** | Construcción rápida de redes neuronales. |
| **Pandas / NumPy** | Análisis de datos y preprocesamiento. |

<div style="page-break-after: always;"></div>

[ima001]

<div style="page-break-after: always;"></div>

# Algoritmo de K-Vecinos más Cercanos

El algoritmo de K-Vecinos más Cercanos (KNN) es uno de los algoritmos más sencillos y populares en el ámbito del aprendizaje supervisado, utilizado para clasificación y regresión. A continuación, te explico en detalle cómo funciona este algoritmo.

KNN es un algoritmo que clasifica un nuevo dato (por ejemplo, una flor con ciertas características) basándose en la mayoría de los vecinos más cercanos en el conjunto de entrenamiento.

El principio fundamental de KNN es que objetos similares están cerca unos de otros en el espacio de características. Es decir, si tienes un conjunto de datos con flores de distintas especies, y se te presenta una nueva flor con ciertas características, KNN intentará identificar a qué especie pertenece la flor comparando sus características con las de las flores cercanas en el conjunto de entrenamiento.

<div style="page-break-after: always;"></div>

## Algoritmo KNN

### 1. Selección de k (el número de vecinos):

El primer paso es elegir el número k, que indica cuántos vecinos más cercanos se deben considerar para hacer la predicción. Por ejemplo, si k=3, se tomarán los 3 vecinos más cercanos al punto que se quiere clasificar.
La elección de k es crucial. Si k es muy pequeño, el modelo puede ser muy sensible al ruido (overfitting). Si k es demasiado grande, puede ser que el modelo no capture correctamente las relaciones locales (underfitting).

### 2. Cálculo de la distancia:

Para clasificar una nueva muestra, KNN calcula la distancia entre el punto a clasificar y todos los puntos del conjunto de entrenamiento. La distancia más comúnmente utilizada es la distancia euclidiana, aunque también se pueden usar otras métricas, como la distancia de Manhattan o la distancia de Minkowski.
La distancia euclidiana se calcula como la raíz cuadrada de la suma de las diferencias al cuadrado de las características:

$$d = \sqrt{(x_1 - y_1)^2 + (x_2 - y_2)^2 + (x_3 - y_3)^2 + ...(x_n - y_n)^2}$$

Donde x1,x2,…,xn son las características de un punto de entrada y y1,y2,…,yn son las características de otro punto.

<div style="page-break-after: always;"></div>

### 3. Selección de los k vecinos más cercanos

Una vez calculada la distancia entre el punto a clasificar y todos los puntos del conjunto de entrenamiento, el algoritmo selecciona los k puntos más cercanos (es decir, los que tienen la menor distancia).

### 4. Predicción

Para clasificación, el algoritmo asigna la etiqueta de clase que es más frecuente entre los k vecinos más cercanos. Por ejemplo, si de los 3 vecinos más cercanos, 2 son de la clase A (por ejemplo, "setosa") y 1 es de la clase B (por ejemplo, "versicolor"), el algoritmo predice que el punto pertenece a la clase A.

Para regresión, el valor predicho es el promedio de los valores de los k vecinos más cercanos.

<div style="page-break-after: always;"></div>

## Ejercicio 1.

```python
from sklearn import datasets
import pandas as pd

# Cargar el conjunto de datos Iris
iris = datasets.load_iris()

# Convertir a DataFrame de Pandas para mejor visualización
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Agregar la columna de la especie (0 = setosa, 1 = versicolor, 2 = virginica)
df["species"] = iris.target

# Imprimir todas las filas
print(df.to_string())  # to_string() evita la truncación y muestra todas las filas
```

<div style="page-break-after: always;"></div>

## Ejercicio 2. Clasificación de Flores con IA de la base de datos Iris.

```python
# Step 1: Import necessary libraries
from sklearn import datasets  # Load dataset
from sklearn.model_selection import train_test_split  # Split data
from sklearn.neighbors import KNeighborsClassifier  # KNN model
from sklearn.metrics import accuracy_score  # Evaluate performance
import pandas as pd  # For better visualization

# Step 2: Load the Iris dataset
iris = datasets.load_iris()

# Step 3: Convert dataset into a Pandas DataFrame for better visualization
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['target'] = iris.target
iris_df['species'] = iris_df['target'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

# Show first 5 rows of the dataset
print("🔹 First 5 rows of the dataset:")
print(iris_df.head(), "\n")

# Step 4: Define features (X) and labels (y)
X = iris.data  # Features: petal/sepal length & width
y = iris.target  # Labels: 0 = setosa, 1 = versicolor, 2 = virginica

# Step 5: Split data into training (80%) and test (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

<div style="page-break-after: always;"></div>

```python
# Show the number of samples in each set
print(f" Training samples: {len(X_train)}, Test samples: {len(X_test)}\n")

# Step 6: Create and train the KNN model
modelo = KNeighborsClassifier(n_neighbors=3)  # Use k=3 neighbors
modelo.fit(X_train, y_train)  # Train the model

# Step 7: Make predictions on test data
y_pred = modelo.predict(X_test)

# Step 8: Show actual vs. predicted labels
result_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
result_df['Actual_Species'] = result_df['Actual'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
result_df['Predicted_Species'] = result_df['Predicted'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

print(" Actual vs. Predicted Labels:\n", result_df.head(), "\n")

# Step 9: Evaluate model accuracy
precision = accuracy_score(y_test, y_pred)
print(f" Model Accuracy: {precision * 100:.2f}%")
```

<div style="page-break-after: always;"></div>

## Ejercicio3.

Utilizar el algoritmo de K-Vecinos más Cercanos (KNN) para clasificar flores en el conjunto de datos Iris, que contiene características de tres especies: setosa, versicolor y virginica. El objetivo es entrenar un modelo con el 80% de los datos y utilizar el 20% restante para probarlo. El programa debe mostrar el rango de valores (mínimos y máximos) de las características largo del sépalo (cm), ancho del sépalo (cm), largo del pétalo (cm) y ancho del pétalo (cm), para que el usuario pueda ingresar las características de una flor. Con esos valores ingresados, el modelo debe predecir la especie de la flor y mostrar el resultado. El usuario debe ingresar los valores de las características, y el programa debe predecir la especie de la flor en base a esos datos, utilizando el modelo KNN entrenado.

```python
# Paso 1: Importar bibliotecas necesarias
from sklearn import datasets  # Cargar conjunto de datos
from sklearn.model_selection import train_test_split  # Dividir los datos
from sklearn.neighbors import KNeighborsClassifier  # Modelo KNN
import pandas as pd  # Para mejor visualización

# Paso 2: Cargar el conjunto de datos Iris
iris = datasets.load_iris()

# Paso 3: Convertir los datos en un DataFrame de Pandas para mejor visualización
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['target'] = iris.target
iris_df['species'] = iris_df['target'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

# Mostrar las primeras 5 filas del conjunto de datos
print(" Primeras 5 filas del conjunto de datos:")
print(iris_df.head(), "\n")

# Paso 4: Definir las características (X) y las etiquetas (y)
X = iris.data  # Características: largo y ancho de sépalo/pétalo
y = iris.target  # Etiquetas: 0 = setosa, 1 = versicolor, 2 = virginica

# Paso 5: Dividir los datos en conjuntos de entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Mostrar la cantidad de muestras en cada conjunto
print(f" Muestras de entrenamiento: {len(X_train)}, Muestras de prueba: {len(X_test)}\n")

# Paso 6: Crear y entrenar el modelo KNN
modelo = KNeighborsClassifier(n_neighbors=3)  # Usar k=3 vecinos
modelo.fit(X_train, y_train)  # Entrenar el modelo

# Paso 7: Mostrar el rango de cada característica
print("\n Rango de cada característica:")
for feature, (min_val, max_val) in zip(iris.feature_names, zip(X.min(axis=0), X.max(axis=0))):
    print(f"{feature.capitalize()} - Min: {min_val:.2f}, Max: {max_val:.2f}")

# Paso 8: Permitir al usuario ingresar las características
print("\n Ingresa las características de la flor:")
sepal_length = float(input("Largo del sépalo (cm): "))
sepal_width = float(input("Ancho del sépalo (cm): "))
petal_length = float(input("Largo del pétalo (cm): "))
petal_width = float(input("Ancho del pétalo (cm): "))

# Paso 9: Hacer una predicción basada en la entrada del usuario
user_input = [[sepal_length, sepal_width, petal_length, petal_width]]
predicted_species_index = modelo.predict(user_input)[0]
predicted_species = iris.target_names[predicted_species_index]

# Paso 10: Mostrar la especie predicha de la flor
print(f"\n Especie predicha de la flor: {predicted_species}")
```
