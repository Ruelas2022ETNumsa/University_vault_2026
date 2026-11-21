# Resumen 21 de noviembre de 2026: esquema del informe y plan de fuentes

**Objetivo del día:** dejar claro cómo se debe armar el informe del brazo LEGO y cómo se van a reunir las fuentes. El brazo aún no está terminado, así que el informe se avanza por partes.

---

## 1. Decisiones de hoy

| Tema | Decisión |
| ---- | -------- |
| Torre de Hanói | **Fuera por ahora.** Primero se arma bien el brazo; hacia el final se decide si se agrega. |
| Hardware | LEGO Inventor **51515** con Pybricks. |
| Estilo de citas | **APA 7** en todo lo que se escriba. El texto del docente lo indica de forma implícita (la "Guía resumen del manual de publicaciones con normas APA"). Aún no es definitivo. |
| Formato del informe | El esquema de la sección 2 (lo entregó el usuario). |
| ESP32 + celular | Idea futura, no implementada. No entra como parte del sistema actual. |

## 2. Esquema del informe

Respetar este orden y estos títulos.

### 1. Introducción y antecedentes
Indicar brevemente los antecedentes y el propósito general del trabajo.

### 2. Objetivo
Indicar el alcance o la profundidad del estudio y sus limitaciones.

### 3. Justificación del proyecto
- Por qué el estudio es importante para la institución y cuál es el escenario del proyecto.
- La justificación dice **por qué** se quiere hacer la investigación y **qué impacto** se busca lograr cuando termine (científico, tecnológico, económico, social, ambiental u otro).
- Responde a la pregunta: **¿para qué servirá?**

### 4. Desarrollo del proyecto
Incluye los conceptos teóricos en los que se fundamenta (**marco teórico**).

### 5. Conclusiones y recomendaciones

### 6. Referencias bibliográficas e internet

### Al final
- Nota o sección titulada **"Guía resumen del manual de publicaciones con normas APA"**.
- **Anexo:** lista de acrónimos.

## 3. Qué hay ya y qué falta frente a este esquema

El borrador `informe.md` se **reorganizó el 21-nov** según este esquema (copia de la versión anterior en `informe 1.md`). Las secciones 1 y 2 tienen contenido; la 3, 4 y 5 están como estructura con marcas `[pendiente]`. Al final tiene una guía breve de APA y el anexo de acrónimos.

| Sección del esquema | Material disponible | Falta |
| ------------------- | ------------------- | ----- |
| 1. Introducción y antecedentes | Contexto y trabajos relacionados de `informe.md` | Ya reubicado; completar con las fuentes de Perplexity y NotebookLM |
| 2. Objetivo | Objetivo general, específicos, alcance y limitaciones de `informe.md` | Ya reubicado |
| 3. Justificación | Nada escrito | Definir institución, escenario e impacto esperado |
| 4. Desarrollo | `resumen_16.md` (montaje, calibración, ha7.py) y `propuesta.md` | Marco teórico; pruebas cuando el brazo esté terminado |
| 5. Conclusiones | Nada | Depende de terminar el brazo |
| 6. Referencias | Lista de `referencia.md` | Pasar a formato APA tras leer los trabajos completos |
| Anexo | Nada | Lista de acrónimos |

**Acrónimos candidatos** (a confirmar según lo que quede en el texto final): GDL, HSV, IMU, USB, BLE, ESP32, API.

## 4. Plan de fuentes

1. **Perplexity** (modo Pro / Deep Research, fuentes Académico): buscar tesis y papers. El prompt se entregó en el chat el 21-nov.
2. **Descargar o guardar** las fuentes relevantes.
3. **NotebookLM:** cargar las fuentes y pedir que extraiga de forma exhaustiva los puntos importantes por tema.
4. **Verificar** cada dato contra la fuente original antes de citarlo. Hasta hoy, las referencias de `referencia.md` solo se leyeron por extractos.
5. Pasar las referencias a **APA**.

## 5. Pendientes

1. Completar autores y años de las referencias en `informe.md` (APA) tras leer los trabajos completos.
2. Definir la **justificación** (institución, escenario, impacto).
3. Confirmar con el docente cómo debe aparecer la "Guía resumen del manual de publicaciones con normas APA". Por ahora quedó una guía breve al final de `informe.md`.
4. Terminar el brazo (ver pendientes de `resumen_16.md`, sección 4).
