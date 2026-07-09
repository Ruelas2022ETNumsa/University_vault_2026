/----
title: Cornell Notes + Cornell Marginalia — Guía de uso
galaxy_body: beacon
scope: vault
audience:
  - usuario
  - claude
related_notes:
  - "[[_note-system]]"
  - "[[plugin_guide]]"
  - "[[Marginalia_guide]]"
tags:
  - beacon
  - cornell
  - marginalia
  - infraestructura
date_created: 2026-07-07
date_updated: 2026-07-07
status: activo
---

# Cornell Notes + Cornell Marginalia — Guía de uso

> Plugins: Cornell Notes (bytetiles) · Cornell Marginalia (ethantwardy v4.9.0)
> Convención de uso por tipo: [[_note-system]]

---

## Plugins involucrados

**Cornell Notes** — genera el layout de dos columnas (claves | desarrollo) dentro de un bloque ` `````cornell `.
- Columna izquierda: configurada como **Claves** (preguntas, palabras clave, mnemónicos)
- Columna derecha: configurada como **Desarrollo** (transcripción, definiciones, fórmulas)

**Cornell Marginalia** — agrega anotaciones al margen mediante bloques ` ````marginalia ` y sintaxis `%%> %%` / `%%< %%`.
- `%%> %%` → margen izquierdo
- `%%< %%` → margen derecho
- Opción `;;texto;;` → blur para active recall

> Conflicto resuelto: el plugin usa `marginalia` como alias (no `cornell`) para evitar conflicto con Cornell Notes. Ver [[plugin_guide]] sección Marginalia.

---

## Estructura de nota Cornell con Marginalia

### Dentro de un bloque `cornell` — obligatorio anidar `marginalia`

La sintaxis `%%> %%` no renderiza directamente dentro de un bloque `cornell`. Es obligatorio anidar un bloque `marginalia` para que Marginalia funcione.

~~~markdown
`````cornell
::cue
````marginalia %%> %%
Contenido de claves — palabras clave, preguntas, mnemónicos.
````

::note
````marginalia %%< %%
Contenido de desarrollo — transcripción, definiciones, fórmulas.
````
`````
~~~


`````cornell
::cue
````marginalia %%> %%
Contenido de claves — palabras clave, preguntas, mnemónicos.%%> marginalia izquierda prueba larga 1 prueba larga 2 prueba larga 3 prueba larga 4 prueba larga 5%%
````

::note
````marginalia %%< %%
Contenido de desarrollo — transcripción, definiciones, fórmulas.%%< marginalia derecha prueba larga 1 prueba larga 2 prueba larga 3 prueba larga 4 prueba larga 5%%
````
`````


**Notas:**
- El bloque `marginalia` va inmediatamente después de `::cue` y `::note`
- `%%> %%` en `::cue` (margen izquierdo) · `%%< %%` en `::note` (margen derecho)
- Los placeholders `%%> %%` y `%%< %%` son invisibles en modo lectura si están vacíos — no generan ruido visual
- El script `notebooklm_fix` inserta estos bloques automáticamente. Ver [[plugin_guide]] sección Script.

### Fuera de un bloque `cornell` — sintaxis directa

Para ejercicios, demostraciones y contenido fuera del layout Cornell, Marginalia se usa directamente sin bloque `marginalia`:

~~~markdown
##### Ej. enunciado

Desarrollo del ejercicio... %%< aclaración al margen%%
Paso siguiente... %%> nota de clave%%
~~~

El uso es **opcional** — aplicar según si la anotación agrega valor real.

---

## Uso por tipo de nota Galaxy

| `galaxy_body` | Cornell Notes | Cornell Marginalia | Observación |
|---|---|---|---|
| `supernova` | ✅ uso principal | ✅ uso principal | Se agregan al copiar desde NotebookLM |
| `planet` | ✅ heredado | ✅ heredado | Copia pura desde supernova, sin modificación |
| `comet` | ✅ heredado | ✅ heredado | Copia pura desde supernova, sin modificación |
| `dwarf` | ✅ | ✅ se puede enriquecer | Agregar preguntas `;;texto;;` para active recall |
| `star` | ❌ | ❌ | MOC de navegación, no de estudio |
| `beacon` | ❌ | ❌ | Todo texto .md, no aplica |
| `asteroid` | ❌ | ❌ | Referencia externa |
| `photon` | ❌ | ❌ | Imagen estática |
| `constellation` | ❌ | ❌ | Excalidraw |
| `observatory` | ❌ | ❌ | Excalidraw |

---

## Uso de blur `;;` en `dwarf`

En notas `dwarf` las marginalia pueden enriquecerse con preguntas ocultas para active recall:

```marginalia
%%> ;;¿Cuál es la condición de normalización?;;%%
```

El texto entre `;;` aparece difuminado en modo lectura — al hacer hover se revela.

%%
galaxy-links
[[_note-system]]
[[plugin_guide]]
[[Marginalia_guide]]
%%
