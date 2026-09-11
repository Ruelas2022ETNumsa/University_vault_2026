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

```ad-note
collapse: closed
title: Aclaraciones Ej. 1

- Corré en terminal o en Colab — no necesita ninguna librería externa.
- El `for/else` de Python es clave acá: el `else` del `for` solo se ejecuta si el bucle terminó **sin** hacer `break`. Es decir, si ninguna clave matcheó, imprime "No entiendo tu pregunta."
- El `.lower()` en el `input` hace que no importe si el usuario escribe en mayúsculas o minúsculas.
- El chatbot sale cuando el usuario escribe "adiós" — tiene que ser con tilde, exactamente así. Si querés probarlo sin tilde, cambiá la clave del diccionario a `"adios"`.
- Archivo: `E1_FUNDAMENTOS_ETN1010.py`
```


### Ejercicio 2
Chatbot mejorado con `difflib` y widgets de Google Colab.
- Diccionario ampliado (9+ preguntas)
- Usa `difflib.get_close_matches` para tolerar errores de escritura
- Interfaz con `ipywidgets` (Text + Button + Output)
- Puede aprender nuevas respuestas del usuario en tiempo real

**Entregable:** foto del código corriendo en Google Colab + foto de la salida.

```ad-note
collapse: closed
title: Aclaraciones Ej. 2

- **Corre SOLO en Google Colab.** Los `ipywidgets` no funcionan en terminal ni VS Code. Si intentas correrlo fuera de Colab, el código carga pero no aparece nada visual.
- El código de la diapo tiene un error sutil: la asignación de `pregunta_actual` y el `controles_aprendizaje.layout.display = 'flex'` quedaban dentro del bloque `with salida:` en lugar de fuera, lo que podía impedir que el widget de aprendizaje apareciera. En el archivo `.py` guardado esto ya está corregido.
- `difflib.get_close_matches` con `cutoff=0.6` significa que acepta preguntas con al menos 60% de similitud. Si el usuario escribe "ke es la ia" puede que no matchee — el cutoff es bastante estricto.
- Las respuestas aprendidas se guardan en `respuestas.json` en el mismo directorio. Si borramos ese archivo, el chatbot vuelve al diccionario base.
- La versión de la diapo tiene dos variantes: una sin JSON (más simple) y una con JSON (persistente). Se guardó la versión con JSON por ser la más completa.
- Archivo: `E2_FUNDAMENTOS_ETN1010.py`
```

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

```ad-note
collapse: closed
title: Aclaraciones Ej. 1

- Corre en terminal o Colab sin problema — solo requiere `sklearn` y `pandas`, ambas disponibles en Colab por defecto.
- La columna `species` guarda los valores **numéricos** (0, 1, 2), no los nombres. Si se quisiera ver los nombres habría que hacer un `.map()` adicional, pero la diapo no lo pide.
- `df.to_string()` fuerza que pandas muestre las 150 filas completas. Sin eso, pandas trunca la salida con `...` en el medio.
- El dataset Iris tiene 150 filas × 5 columnas (4 características + species).
- Archivo: `E1_AREA_ETN1010.py`
```


### Ejercicio 2
Clasificación KNN completa sobre el dataset Iris.
- Split 80/20 con `train_test_split`
- Modelo `KNeighborsClassifier(n_neighbors=3)`
- Muestra primeras 5 filas, cantidad de muestras por conjunto
- Predice sobre el set de prueba
- Compara etiquetas reales vs predichas
- Calcula accuracy con `accuracy_score`

**Entregable:** foto del código corriendo en Google Colab + foto de la salida.

```ad-note
collapse: closed
title: Aclaraciones Ej. 2

- Corre en terminal o Colab — no usa widgets, solo `print`. Sin dependencias raras.
- El emoji 🔹 del `print` original de la diapo fue eliminado para evitar problemas de encoding en terminales sin soporte UTF-8 completo.
- `random_state=42` en el split garantiza que siempre se obtenga la misma partición — los resultados son reproducibles. Sin eso, cada corrida daría un split diferente.
- Con `k=3` y este dataset el modelo típicamente alcanza **96.67% de accuracy** (29/30 correctos en el set de prueba).
- `result_df.head()` muestra solo las primeras 5 predicciones. Si se quiere ver todas, cambiar a `result_df.to_string()`.
- Los `print` de la diapo tenían espacios iniciales inconsistentes — limpiados en el archivo guardado.
- Archivo: `E2_AREA_ETN1010.py`
```


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
