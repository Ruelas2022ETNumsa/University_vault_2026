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

## Prueba — sesión 2026-09-14

Comando usado:
```
cd /d E:\University_vault_2026\Semesters\Sem_09\ETN1010
python E1_AREA_ETN1010.py
```

Salida verificada — inicio:
```
   sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)  species
0                5.1               3.5                1.4               0.2        0
1                4.9               3.0                1.4               0.2        0
```

Salida verificada — final:
```
146                6.3               2.5                5.0               1.9        2
147                6.5               3.0                5.2               2.0        2
148                6.2               3.4                5.4               2.3        2
149                5.9               3.0                5.1               1.8        2
```

Funciona correctamente. La columna `species` muestra 0, 1, 2 en lugar de nombres — decisión de diseño del ejercicio, es suficiente y visualmente más limpio. No se requiere `.map()` adicional.
