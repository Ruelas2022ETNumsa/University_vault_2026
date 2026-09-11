# Paso 1: Importar bibliotecas necesarias
from sklearn import datasets                          # Cargar conjunto de datos
from sklearn.model_selection import train_test_split  # Dividir los datos
from sklearn.neighbors import KNeighborsClassifier    # Modelo KNN
import pandas as pd                                   # Para mejor visualización

# Paso 2: Cargar el conjunto de datos Iris
iris = datasets.load_iris()

# Paso 3: Convertir los datos en un DataFrame de Pandas para mejor visualización
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['target'] = iris.target
iris_df['species'] = iris_df['target'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

# Mostrar las primeras 5 filas del conjunto de datos
print("Primeras 5 filas del conjunto de datos:")
print(iris_df.head(), "\n")

# Paso 4: Definir las características (X) y las etiquetas (y)
X = iris.data   # Características: largo y ancho de sépalo/pétalo
y = iris.target  # Etiquetas: 0 = setosa, 1 = versicolor, 2 = virginica

# Paso 5: Dividir los datos en conjuntos de entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Mostrar la cantidad de muestras en cada conjunto
print(f"Muestras de entrenamiento: {len(X_train)}, Muestras de prueba: {len(X_test)}\n")

# Paso 6: Crear y entrenar el modelo KNN
modelo = KNeighborsClassifier(n_neighbors=3)  # Usar k=3 vecinos
modelo.fit(X_train, y_train)                  # Entrenar el modelo

# Paso 7: Mostrar el rango de cada característica
print("Rango de cada característica:")
for feature, (min_val, max_val) in zip(iris.feature_names, zip(X.min(axis=0), X.max(axis=0))):
    print(f"  {feature.capitalize()} - Min: {min_val:.2f}, Max: {max_val:.2f}")

# Paso 8: Permitir al usuario ingresar las características
print("\nIngresa las características de la flor:")
sepal_length = float(input("  Largo del sépalo (cm): "))
sepal_width  = float(input("  Ancho del sépalo (cm): "))
petal_length = float(input("  Largo del pétalo (cm): "))
petal_width  = float(input("  Ancho del pétalo (cm): "))

# Paso 9: Hacer una predicción basada en la entrada del usuario
user_input = [[sepal_length, sepal_width, petal_length, petal_width]]
predicted_species_index = modelo.predict(user_input)[0]
predicted_species = iris.target_names[predicted_species_index]

# Paso 10: Mostrar la especie predicha de la flor
print(f"\nEspecie predicha de la flor: {predicted_species}")
