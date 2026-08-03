---
galaxy_body: dropship
carrier: "[[ruta/tsk_carrier.md]]"
scope: config | opcion-A | opcion-B | prueba
status: activo
date: 
---

%%
# YAML — instrucciones de llenado

galaxy_body: dropship → siempre este valor, no cambiar

carrier:
  Apunta al tsk_ del carrier al que pertenece este dropship.
  Usar wikilink con ruta relativa desde la raíz del vault.
  Ejemplo: "[[_hangar/anki/tsk_anki.md]]"
  Si el carrier está en _hangar/ directo: "[[_hangar/tsk_nombre.md]]"

scope: elegir uno y borrar el resto
  - config     → configuración general del carrier (uno por carrier)
  - opcion-A/B/C → documentación de una opción o variante evaluada
  - prueba     → registro de pruebas y resultados puntuales

status: elegir uno
  - activo     → en evaluación o uso
  - evaluado   → prueba completada, veredicto registrado
  - descartado → opción descartada, motivo en el archivo

date: fecha de creación en formato YYYY-MM-DD

# Convención de nombre de archivo
  [alias-carrier]-opc_[X]-[distintivo].md
  Ejemplo: anki-opc_A-marginalia.md
  Para config: [alias-carrier]-config.md
  Ejemplo: anki-config.md

# Al crear este archivo
  1. Completar el YAML arriba
  2. Escribir el propósito en ## Proposito (1-2 líneas)
  3. Agregar el archivo a la tabla ## Archivos del carrier en tsk_carrier.md
  4. Desarrollar el contenido en ## Contenido
%%

---

## Proposito

%%
Una o dos líneas que describan qué documenta este dropship y a qué carrier pertenece.
Ejemplo: "Documenta la opción A de renderizado para el carrier anki — prueba con plugin X."
%%

---

## Contenido
