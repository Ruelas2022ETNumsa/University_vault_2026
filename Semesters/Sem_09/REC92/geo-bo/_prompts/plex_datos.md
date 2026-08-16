---
title: "geo-bo — prompts Perplexity datos puntuales y complemento"
scope: REC92
date_updated: 2026-08-16
---

# Prompts Perplexity — Complemento de Datos

> Estos prompts buscan datos puntuales y concretos que los prompts del informe no obtienen bien porque están mezclados con contenido narrativo.
> Ejecutalos en paralelo a la Fase 1 del informe.
> Guardá cada respuesta como dato de referencia para alimentar NotebookLM.
> Marcá con ✅ cuando esté ejecutado y anotá las fuentes obtenidas.

---

## BLOQUE A — Datos económicos y de inversión

### PC-A1 — Inversión total ejecutada en el proyecto
```
¿Cuánto dinero ha invertido Bolivia en el proyecto geotérmico de Laguna Colorada hasta 2024? Buscá datos desagregados: inversión en exploración, perforaciones, planta piloto de 5 MW y proyecto de 100 MW. Fuentes: ENDE Corporación, JICA, Ministerio de Hidrocarburos y Energías de Bolivia o informes oficiales.
Al final, listá todas las fuentes utilizadas con autor, año y URL.
```
- [ ] ejecutado — fuentes: ___

---

### PC-A2 — Costo comparativo geotermia vs gas en Bolivia
```
¿Cuál es el costo de generación eléctrica por kWh de energía geotérmica comparado con gas natural en Bolivia o en países similares de Sudamérica? ¿Es económicamente competitiva la geotermia para Bolivia considerando su matriz actual basada en gas y el subsidio energético vigente? Buscá datos de IRENA, OLADE o análisis económicos confiables.
Al final, listá todas las fuentes utilizadas con autor, año y URL.
```
- [ ] ejecutado — fuentes: ___

---

## BLOQUE B — Análisis argumental

### PC-B1 — Por qué Bolivia no desarrolló su potencial geotérmico
```
¿Cuáles son las principales razones por las que Bolivia no ha desarrollado su potencial geotérmico a pesar de tener estudios desde los años 80 y un potencial estimado de 250-370 MW en Sol de Mañana? Buscá análisis que consideren factores políticos (cambios de gobierno, prioridades), económicos (costo de inversión, precio del gas), técnicos (altitud de 4.850 msnm, perforación en altura) e institucionales (capacidad de ENDE). Preferí fuentes académicas o de organismos internacionales.
Al final, listá todas las fuentes utilizadas con autor, año y URL.
```
- [ ] ejecutado — fuentes: ___

---

## BLOQUE C — Papers y fuentes académicas

### PC-C1 — Papers recientes sobre Sol de Mañana y geotermia boliviana
```
Buscá artículos académicos o papers publicados entre 2015 y 2024 sobre el campo geotérmico Sol de Mañana o la geotermia en Bolivia. Para cada resultado incluí: autores completos, año de publicación, nombre de la revista, volumen, número de página y DOI. Preferí revistas como Geothermics, Renewable Energy o similares indexadas.
Al final, listá todas las fuentes con formato de cita académica completa.
```
- [ ] ejecutado — fuentes: ___

---

### PC-C2 — Normativa boliviana para energías renovables
```
¿Cuál es el marco legal y normativo vigente en Bolivia para el desarrollo de energías renovables, incluyendo geotermia? Listá leyes, decretos supremos y políticas públicas relevantes con sus números de norma y año de promulgación. Incluí si existe alguna ley específica para recursos geotérmicos o si están regulados bajo la ley eléctrica general.
Al final, listá todas las fuentes utilizadas con autor, año y URL.
```
- [ ] ejecutado — fuentes: ___

---

## BLOQUE D — Dato puntual de alto valor

### PC-D1 — Comparación técnica: geotermia a gran altitud
```
¿Existen otros proyectos geotérmicos en el mundo desarrollados a altitudes similares a Sol de Mañana (4.850–4.980 msnm)? ¿Qué desafíos técnicos específicos presenta la perforación y operación geotérmica a esa altura? ¿Cómo los resolvieron otros países? Este dato es útil para explicar por qué el proyecto boliviano es técnicamente complejo.
Al final, listá todas las fuentes utilizadas con autor, año y URL.
```
- [ ] ejecutado — fuentes: ___

---

## Notas de uso

- Estos prompts buscan datos que los prompts del informe no traen bien por estar mezclados con narrativa
- Los datos de inversión (PC-A1) y papers (PC-C1) son prioritarios — ejecutalos primero
- Si Perplexity no encuentra el dato exacto, anotá qué sí encontró y buscá manualmente en la fuente oficial
- PC-D1 es un dato de valor argumental para la sección de análisis — no es urgente pero suma mucho al informe
- Toda fuente con DOI verificable es candidata a cargar en NotebookLM como PDF
