---
project: "Mapa de IAs del vault — roles y APIs"
date: 2026-07-19
status: creciente
---

## Handoff

**Última sesión:** 2026-07-19
**Retomar desde:** Snippet completo entregado — pendiente decidir si se integra a un beacon o queda en `tsk_emergn`
**Completado esta sesión:** Investigación de IAs, roles definidos, APIs gratuitas identificadas
**Próximo paso:** Decidir ubicación final del snippet dentro del vault
**Preguntas de cierre:** —

---

## Resumen y objetivo

Documentar qué tarea cumple cada IA dentro del Sistema Galaxy, qué APIs gratuitas están disponibles para scripts en Obsidian, y dejar un snippet de referencia rápida para sesiones futuras.

---

## Snippet — IAs del vault

### IAs activas en el sistema

| IA | Rol en el vault | Galaxy body donde aplica |
|---|---|---|
| **Claude** | Edición del vault, planificación de proyectos, configuración técnica, búsqueda de libros conocidos, sesiones de trabajo con Filesystem MCP | `beacon`, `tsk_`, cualquier nota |
| **NotebookLM** | Estudio activo por materia, generación de scripts de ejercicios, transcripción guiada de apuntes | `supernova`, `workshop`, `asteroid` |
| **Gemini** | OCR de imágenes y PDFs escaneados, transcripción de texto manuscrito, generación de imágenes puntuales | `photon`, `supernova` |
| **ChatGPT** | Nombramiento de archivos, significados de palabras, mejora y formateo de respuestas de NotebookLM, presentación visual de procedimientos paso a paso | `tsk_`, `comet`, `dwarf` |
| **Perplexity** | Búsqueda de libros y autores nuevos o desconocidos, investigación con fuentes verificables y citadas en tiempo real | `asteroid`, `_library-system` |
| **Napkin AI** | Generación de diagramas e infografías a partir de texto — sin prompts, pega el texto y genera el visual | `photon`, `observatory` |
| **DeepSeek** | Similar a ChatGPT — razonamiento y formateo, alternativa de bajo costo, uso ocasional | `comet`, `dwarf` |

---

### ¿Qué hace mejor cada una?

| IA | Especialidad real |
|---|---|
| **Claude** | Textos largos, razonamiento técnico, seguir instrucciones complejas, edición de archivos con contexto del vault |
| **NotebookLM** | Estudio basado en tus propias fuentes cargadas — no sale de ellas |
| **Gemini** | Multimodal: imagen, audio, video, PDF escaneado. Contexto de 1M tokens gratis |
| **ChatGPT** | Versatilidad general, escritura natural, formateo de contenido, ecosistema de plugins |
| **Perplexity** | Búsqueda web en tiempo real con citas verificables — no es un chatbot, es un motor de respuestas |
| **Napkin AI** | Texto → visual automático (diagramas, mapas, infografías) sin diseño manual ni prompts |
| **DeepSeek** | Razonamiento matemático y código a precio mínimo — open source, se puede hostear local |

---

### APIs gratuitas disponibles para scripts en Obsidian

Relevante para crear ayudantes internos dentro del vault via Shell Commands + Python.

| IA | API gratuita | Límite free | Requiere tarjeta | Mejor para scripts de |
|---|---|---|---|---|
| **Gemini** | ✅ Google AI Studio | Gemini 2.5 Flash: 10 RPM, ~600 req/hora | ❌ No | OCR, resumen de PDFs, multimodal |
| **DeepSeek** | ✅ deepseek.com | 5M tokens al registrarse (30 días) | ❌ No | Razonamiento, formateo, código |
| **Groq** | ✅ groq.com | Alta velocidad, límite diario | ❌ No | Respuestas rápidas (Llama, DeepSeek-R1) |
| **OpenRouter** | ✅ openrouter.ai | 50 req/día, 35+ modelos gratuitos | ❌ No | Variedad de modelos con una sola API key |
| **Claude** | ⚠️ Anthropic API | Sin tier gratuito permanente | ✅ Sí | — |
| **ChatGPT** | ⚠️ OpenAI API | Sin tier gratuito permanente desde 2024 | ✅ Sí | — |
| **NotebookLM** | ❌ | Sin API pública disponible | — | — |
| **Napkin AI** | ❌ | Sin API pública disponible | — | — |
| **Perplexity** | ⚠️ Sonar API | $1/1M tokens — sin tier gratuito real | ✅ Sí | — |

> **Para scripts en Obsidian sin costo:** Gemini (Google AI Studio) es la opción más sólida — sin tarjeta, límite generoso, multimodal. DeepSeek como segunda opción para razonamiento puro.

---

## Decisiones

| Fecha | Decisión | Motivo |
|---|---|---|
| 2026-07-19 | Napkin AI clasificado como generador de `photon`/`observatory` | Convierte texto en visual — encaja con ambos tipos según complejidad del output |
| 2026-07-19 | DeepSeek marcado como uso ocasional | Similitud con ChatGPT, privacidad de datos en China, sin integración activa al workflow |
| 2026-07-19 | Gemini identificado como mejor candidato para scripts gratuitos | API sin tarjeta, límite alto, soporte multimodal — alinea con el uso OCR ya activo |

> [!note]- Descartadas
> NotebookLM API — no existe API pública. No se puede integrar como script.

---

## Preguntas abiertas

- ¿Se crea un `beacon` dedicado a este mapa de IAs en `_config/` o queda documentado aquí?
- ¿Se prueba Gemini API como ayudante interno en Obsidian para alguna tarea específica (ej. OCR automático al pegar una imagen)?

---

## Recursos

- Google AI Studio (Gemini API gratis): https://aistudio.google.com
- DeepSeek API: https://platform.deepseek.com
- OpenRouter (multi-modelo gratis): https://openrouter.ai
- Napkin AI: https://www.napkin.ai
- Perplexity Sonar API: https://docs.perplexity.ai

%%
# galaxy-links
[[_app/_config/_galaxy-system.md]]
[[_app/_config/_library-system.md]]
[[_app/_appnotes/script_guide.md]]
%%
