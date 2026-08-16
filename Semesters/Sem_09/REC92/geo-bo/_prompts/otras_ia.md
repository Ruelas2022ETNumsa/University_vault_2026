---
title: "geo-bo — prompts ChatGPT y Gemini por sección"
scope: REC92
date_updated: 2026-08-16
---

# Prompts para otras IAs — REC92

> Cada IA tiene un rol distinto en el proyecto.
> Perplexity → datos y fuentes actuales
> ChatGPT → síntesis, redacción y análisis
> Gemini → comparativas, tablas y contenido visual

---

## ChatGPT

> Usarlo con el modo de respuesta larga activado.
> Ideal para redacción de secciones del informe y análisis argumentativo.

---

### C1 — Marco teórico completo (Persona 1)
```
Redactá el marco teórico de un informe universitario sobre energía geotérmica para estudiantes de Ingeniería Electrónica. Debe incluir: definición de energía geotérmica, tipos de sistemas (alta, media y baja entalpía), principio de funcionamiento de una planta geotérmica, tipos de ciclos de conversión (flash, binario, dry steam) y ventajas frente a otras energías renovables. Nivel universitario, redacción formal en español, sin bullets — solo prosa continua. Extensión aproximada: 600-800 palabras.
```
- [ ] usado

---

### C2 — Análisis: por qué Bolivia no desarrolló geotermia (Persona 3)
```
Escribí un análisis argumentativo de 400-500 palabras sobre las razones por las que Bolivia no ha desarrollado su potencial geotérmico a pesar de tener estudios desde los años 80 y un potencial estimado de 250-370 MW en el campo Sol de Mañana, Potosí. Considerá factores políticos, económicos, técnicos e institucionales. Mencioná el rol de ENDE Corporación y el financiamiento de JICA. Redacción formal universitaria en español.
```
- [ ] usado

---

### C3 — Conclusiones del informe (Persona 5)
```
Redactá las conclusiones de un informe universitario sobre energía geotérmica en Bolivia para la carrera de Ingeniería Electrónica, con enfoque en concientización sobre recursos naturales renovables. El informe abarca: fundamentos teóricos de la geotermia, el potencial de Bolivia (250-370 MW estimados en Sol de Mañana), el proyecto Laguna Colorada de ENDE (100 MW proyectados, sin operar desde el contrato de 2016), y la comparativa con Chile y Argentina. Bolivia tiene 0 MW geotérmicos operativos en 2022 sobre una matriz de 3.822 MW totales. Conclusiones en prosa, 300-400 palabras, tono académico.
```
- [ ] usado

---

### C4 — Introducción del informe (Persona 5)
```
Redactá la introducción de un informe universitario sobre energía geotérmica en Bolivia. El trabajo es para la materia de concientización sobre recursos naturales renovables, carrera Ingeniería Electrónica. La introducción debe contextualizar la problemática energética global, mencionar el potencial geotérmico de Bolivia y plantear el objetivo del informe. Prosa continua, tono académico, 250-350 palabras.
```
- [ ] usado

---

### C5 — Síntesis comparativa regional (Persona 4)
```
Escribí una síntesis comparativa de 400 palabras sobre el desarrollo de la energía geotérmica en Bolivia, Chile y Argentina. Para Bolivia: potencial de 250-370 MW en Sol de Mañana, proyecto de 100 MW de ENDE sin operar, contrato firmado 2016 con JICA. Para Chile: proyecto El Tatio. Para Argentina: proyecto Copahue. Analizá por qué la región tiene resultados modestos según la CEPAL y qué diferencia a los países que sí avanzaron. Redacción formal universitaria.
```
- [ ] usado

---

## Gemini

> Mejor para generar tablas comparativas, esquemas y contenido que luego se pueda trasladar a diapositivas.
> Pedirle siempre formato tabla o lista estructurada — responde bien a eso.

---

### G1 — Tabla comparativa de tipos de plantas geotérmicas (Persona 1)
```
Creá una tabla comparativa de los tres tipos principales de plantas geotérmicas: ciclo flash, ciclo binario y dry steam. La tabla debe incluir las columnas: tipo de planta, temperatura requerida del recurso, principio de funcionamiento, eficiencia aproximada, ejemplos de países que la usan y si aplica para Bolivia. Formato tabla markdown.
```
- [ ] usado

---

### G2 — Tabla comparativa geotermia vs otras renovables (Persona 1)
```
Creá una tabla en markdown que compare la energía geotérmica con solar, eólica e hidroeléctrica en los siguientes criterios: disponibilidad (continua/intermitente), factor de planta aproximado (%), impacto ambiental, costo de instalación estimado por MW, vida útil de la planta y presencia en Bolivia. Nivel universitario de ingeniería.
```
- [ ] usado

---

### G3 — Cronología visual del proyecto Laguna Colorada (Persona 3)
```
Creá una cronología en formato tabla markdown del Proyecto Geotérmico Laguna Colorada de Bolivia, desde 1970 hasta 2024. Columnas: año, hito, actor responsable. Incluí: primeros estudios (1970), perforaciones de los 80, estudio de factibilidad 1990, reevaluación 1996-97, estudio West JEC 2007-08, renovación con JICA 2010, convenio Costa Rica 2015, contrato 100 MW 2016, contrato planta piloto 5 MW 2019, estado 2023-2024.
```
- [ ] usado

---

### G4 — Tabla de capacidad geotérmica instalada en Sudamérica (Persona 4)
```
Creá una tabla en markdown con la capacidad geotérmica instalada en países de Sudamérica y América Latina al 2023-2024. Columnas: país, MW instalados operativos, principales proyectos, estado (operativo/en construcción/exploración). Incluí Bolivia, Chile, Argentina, Perú, México, Costa Rica y El Salvador como referencia regional.
```
- [ ] usado

---

### G5 — Esquema de funcionamiento de una planta geotérmica (Persona 1)
```
Describí paso a paso el funcionamiento de una planta geotérmica de ciclo flash en formato de lista numerada, pensado para ser trasladado a una diapositiva de exposición universitaria. Máximo 8 pasos, cada uno en una línea corta y clara. Sin tecnicismos excesivos — el público es ingeniería electrónica, no mecánica.
```
- [ ] usado

---

## Notas de uso

- **ChatGPT** → pedirle siempre que cite fuentes al final si las conoce; verificar con Perplexity antes de usar datos numéricos que traiga
- **Gemini** → las tablas que genere copiarlas directo al informe en markdown; son fáciles de convertir a tabla Word o PowerPoint
- Si algún prompt trae texto demasiado genérico, agregale al final: "enfocá la respuesta en el caso boliviano"
