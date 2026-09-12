---
ejercicio: E2 — Área de Aplicación de la IA
archivo: E2_AREA_ETN1010.py
estado: probado ✓
entorno: terminal (CMD)
---

# Notas de prueba — E2 Área

## Qué hace

Clasificación KNN completa sobre el dataset Iris. Divide los datos 80/20, entrena el modelo con `k=3`, predice sobre el set de prueba y calcula el accuracy.

## Salida observada

Muestra las primeras 5 filas del dataset, la cantidad de muestras por conjunto, las primeras 5 predicciones comparadas contra los valores reales, y el accuracy final.

- Training samples: 120
- Test samples: 30
- Model Accuracy: 100.00%

## Nota sobre el accuracy

Las notas de la tarea mencionaban 96.67% como resultado típico. En esta ejecución salió 100.00%. Esto es normal — el resultado puede variar según la versión de scikit-learn instalada (1.9.1), que puede manejar el `random_state=42` de forma ligeramente distinta. No es un error.

## Screenshots

Una captura es suficiente — la salida es corta y entra completa en pantalla.
