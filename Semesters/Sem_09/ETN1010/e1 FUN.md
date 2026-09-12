---
ejercicio: E1 — Fundamentos de IA
archivo: E1_FUNDAMENTOS_ETN1010.py
estado: probado ✓
---

# Notas de prueba — E1 Fundamentos

## Comportamiento observado

El chatbot responde correctamente solo si las preguntas se escriben **con tilde**, exactamente como están definidas en el diccionario.

Sin tilde → `No entiendo tu pregunta.`
Con tilde → respuesta correcta.

Esto se debe a que el código compara la entrada del usuario directamente con las claves del diccionario. Si la ortografía no coincide exactamente, no hay match.

## Preguntas válidas

- `qué es la ia` → responde la definición de IA
- `quién inventó la ia` → responde sobre John McCarthy
- `adiós` → cierra el programa

## Resultado

Funciona correctamente al escribir con acentos. Screenshot tomado mostrando las respuestas exitosas.
