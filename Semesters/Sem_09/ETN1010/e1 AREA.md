---
ejercicio: E1 — Área de Aplicación de la IA
archivo: E1_AREA_ETN1010.py
estado: probado ✓
entorno: terminal (CMD)
---

# Notas de prueba — E1 Área

## Qué hace

Carga el dataset Iris de `scikit-learn`, lo convierte a DataFrame de pandas y lo imprime completo — 150 filas × 5 columnas.

## Columnas del DataFrame

- `sepal length (cm)`
- `sepal width (cm)`
- `petal length (cm)`
- `petal width (cm)`
- `species` — valor numérico: 0 = setosa, 1 = versicolor, 2 = virginica

## Resultado

Imprime correctamente las 150 filas. El uso de `df.to_string()` evita que pandas trunque la salida con `...`.

## Screenshots

Se tomaron 2 capturas: inicio (filas 0–5) y final (filas 146–149). Es suficiente para evidenciar la ejecución completa.
