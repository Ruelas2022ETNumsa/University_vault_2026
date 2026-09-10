---
title: "Tareas ETN1010"
tags: [ETN1010, tareas]
date_created: 2026-09-09
status: activo
---

# Tareas ETN1010

## Tarea 1 — Fundamentos de IA

> Adjuntar las fotos del código y de su ejecución de los ejercicios 1 y 2.

**Diapositiva de origen:** `FUNDAMENTOS_DE_LA_IA.md`

### Ejercicio 1
Chatbot básico con diccionario y reglas simples (`if/for`).
- Responde 3 preguntas fijas sobre IA
- Usa `input()` en bucle `while True`
- Sale cuando el usuario escribe "adiós"



### Ejercicio 2
Chatbot mejorado con `difflib` y widgets de Google Colab.
- Diccionario ampliado (9+ preguntas)
- Usa `difflib.get_close_matches` para tolerar errores de escritura
- Interfaz con `ipywidgets` (Text + Button + Output)
- Puede aprender nuevas respuestas del usuario en tiempo real

**Entregable:** foto del código corriendo en Google Colab + foto de la salida.

---

## Tarea 2 — Área de Aplicación de la IA

> Adjuntar las fotos del código y de su ejecución de los ejercicios 1 y 2.

**Diapositiva de origen:** `AREA_DE_APLICACION_DE_LA_IA.md`

### Ejercicio 1
Cargar el dataset Iris con sklearn y mostrarlo completo con pandas.
- Importa `datasets` y `pandas`
- Carga `datasets.load_iris()`
- Convierte a DataFrame con `pd.DataFrame`
- Agrega columna `species` con `iris.target`
- Imprime todo con `df.to_string()`

### Ejercicio 2
Clasificación KNN completa sobre el dataset Iris.
- Split 80/20 con `train_test_split`
- Modelo `KNeighborsClassifier(n_neighbors=3)`
- Muestra primeras 5 filas, cantidad de muestras por conjunto
- Predice sobre el set de prueba
- Compara etiquetas reales vs predichas
- Calcula accuracy con `accuracy_score`

**Entregable:** foto del código corriendo en Google Colab + foto de la salida.

---

## Tarea 3 — Resolución de Problemas

> Adjuntar las fotos del código y de su ejecución de los ejercicios 1 y 2.

**Diapositiva de origen:** presentación aún no recibida — nombre inferido por el docente.

> [!warning] Pendiente
> Esta presentación todavía no fue entregada por el docente. Los ejercicios debajo son una inferencia basada en el patrón de las diapositivas anteriores. Confirmar cuando aparezca la diapo.

### Ejercicio 1 (inferido)
KNN con Iris — mismo código que Tarea 2 Ej. 2, posiblemente como punto de partida o con alguna variación menor.

### Ejercicio 2 (inferido)
KNN interactivo con entrada del usuario.
- Muestra rango (mín/máx) de cada característica del dataset
- El usuario ingresa manualmente: largo sépalo, ancho sépalo, largo pétalo, ancho pétalo
- El modelo predice la especie y la imprime
- Corresponde al **Ejercicio 3** de las diapositivas de Área de Aplicación

**Entregable:** foto del código corriendo en Google Colab + foto de la salida.

---

## Resumen

| Tarea | Ejercicio | Qué es | Estado |
|---|---|---|---|
| Fundamentos | Ej. 1 | Chatbot básico con reglas | ⬜ pendiente |
| Fundamentos | Ej. 2 | Chatbot con difflib + widgets Colab | ⬜ pendiente |
| Área de Aplicación | Ej. 1 | Cargar y mostrar dataset Iris | ⬜ pendiente |
| Área de Aplicación | Ej. 2 | KNN completo con accuracy | ⬜ pendiente |
| Resolución de Problemas | Ej. 1 | KNN Iris (inferido) | ⬜ pendiente |
| Resolución de Problemas | Ej. 2 | KNN interactivo con input del usuario | ⬜ pendiente |
