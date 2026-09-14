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
