
---

## Resumen de sesión — Obsidian + Gemini como NotebookLM

### El objetivo

Replicar el comportamiento de NotebookLM **sin salir de Obsidian**: seleccionas texto (una pregunta, un concepto, un ejercicio de cálculo), ejecutas un comando, y la respuesta aparece en tu nota — basada **exclusivamente** en tus fuentes (PDFs de la materia).

---

### Lo que ya tienes

- Windows 10 (PC) y Windows 11 (laptop)
- Python 3.13 en `C:\Users\USUARIO\AppData\Local\Programs\Python\Python313\python.exe`
- Plugin Shell Commands instalado en Obsidian
- Google Cloud con proyecto existente (usado para rclone + Drive)
- PDFs de materias (ej. Cálculo) ya cargados en NotebookLM
- Plugin AI Image OCR (para OCR de capturas, misma API key de Gemini)(aun no configurado preguntar si esta listo al usuario)

---

### Las dos rutas en discusión

**Ruta A — Gemini Helper (plugin)** Plugin gratuito y open-source, ya tiene RAG sobre el vault, chat con Gemini, workflow builder y control de qué carpetas puede leer. Cero código. Pero la interacción es dentro del panel del plugin, no directamente en la nota con `{{selection}}`.

**Ruta B — Script Python + Shell Commands (custom)** Script propio que toma `{{selection}}`, consulta Gemini API con tus PDFs como contexto y pega la respuesta en la nota. Más control sobre el formato, el comportamiento y el flujo exacto. Requiere generar API key y escribir ~30 líneas de Python.

**Pendiente de discutir:** comparación detallada de ambas — cuál replica mejor el flujo de NotebookLM dentro de Obsidian para el caso de uso académico (PDFs de Cálculo, fórmulas, ejercicios).

---

### Pendiente para próxima sesión

- Verificar si Google Cloud ya tiene API key de Gemini generada o hay que crearla
- Comparación detallada Ruta A vs Ruta B
- Decisión de ruta y setup paso a paso

---

Copia este resumen al inicio de la próxima sesión y arrancamos directo donde lo dejamos.