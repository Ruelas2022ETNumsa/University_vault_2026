---
galaxy_body: blueprint
status: idea
priority: alta | media | baja
date: 
---

%%
# YAML — instrucciones de llenado

galaxy_body: blueprint → siempre este valor, no cambiar

status: elegir uno y borrar el resto
  - idea       → anotado, sin evaluar
  - evaluando  → en análisis activo
  - aprobado   → aprobado para convertirse en ship o carrier

priority: elegir uno y borrar el resto
  - alta   → se quiere ejecutar pronto
  - media  → interesante pero no urgente
  - baja   → idea especulativa o lejana

date: fecha de creación en formato YYYY-MM-DD

# Convención de nombre de archivo
  _ideas_[N]_[tema].md
  Ejemplo: _ideas_1_anki.md
  El número es secuencial dentro de _hangar/blueprint/

# Al crear este archivo
  1. Completar el YAML
  2. Escribir el tema en el H1 y la relación en el bloque > de introducción
  3. Crear secciones temáticas con ideas agrupadas por categoría
  4. Usar - [ ] para cada idea individual
%%

# Ideas [tema]

> **Relación:** [una línea que define qué tienen en común todas las ideas de esta lista]

%%
Ejemplo de relación:
"Uso del plugin Shell Commands para crear scripts útiles en Obsidian"
"Integración de Anki con el sistema galaxy para flashcards desde el vault"
%%

---

## [Categoría 1]

- [ ] 
- [ ] 

---

## [Categoría 2]

- [ ] 
- [ ] 

---

## A depurar

%%
Ideas que pueden estar ya cubiertas por alguna herramienta o script existente.
Revisar antes de convertir en ship.
%%

- 
