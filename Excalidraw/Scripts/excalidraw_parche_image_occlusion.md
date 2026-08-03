---
type: parche
script: Image Occlusion.md
script_path: Excalidraw/Scripts/Downloaded/Image Occlusion.md
bk_path: Excalidraw/Scripts/Downloaded/Image Occlusion.md.bk
date_created: 2026-08-02
date_updated: 2026-08-02
status: activo
galaxy_links:
  - "[[_excalidraw-system]]"
  - "[[_anki-system]]"
---

> Registro de modificaciones manuales aplicadas al script descargado `Image Occlusion.md`. Sirve como guía de re-aplicación si el script es actualizado o reemplazado por una nueva versión del plugin.

---

## Contexto

El script `Image Occlusion.md` es un script de Excalidraw descargado (plugin externo). No debe editarse su lógica principal, pero se le aplicaron parches puntuales para ajustar comportamiento de UI. Ante una actualización del script, estos cambios deben re-aplicarse manualmente usando este documento como referencia.

---

## Parches aplicados

### Parche 1 — Reordenar menú de modos: Hide All como opción por defecto

**Fecha:** 2026-08-02
**Motivo:** El flujo de trabajo habitual usa `Hide All, Guess One`. Al estar segundo en el menú, requería una selección extra innecesaria. Se movió a la primera posición para que sea la opción por defecto al presionar Enter.

**Ubicación en el script:** bloque `// Present user with operation mode choices`

**Antes:**
```js
const mode = await utils.suggester(
  [
    "⭐⠀      Add Cards:    Hide One, Guess One",
    "⭐⭐     Add Cards:    Hide All, Guess One",
    "🗑️⠀      Delete Cards: Delete old cards (add DELETE marker)",
    "🗑️💥     Delete Cards: Delete old cards files and related images (Be Cautious!!)"
  ],
  ["hideOne", "hideAll", "delete", "deleteFiles"],
  "Select operation mode"
);
```

**Después:**
```js
const mode = await utils.suggester(
  [
    "⭐⭐     Add Cards:    Hide All, Guess One",
    "⭐⠀      Add Cards:    Hide One, Guess One",
    "🗑️⠀      Delete Cards: Delete old cards (add DELETE marker)",
    "🗑️💥     Delete Cards: Delete old cards files and related images (Be Cautious!!)"
  ],
  ["hideAll", "hideOne", "delete", "deleteFiles"],
  "Select operation mode"
);
```

**Regla crítica:** los dos arrays deben mantenerse sincronizados por posición. El primero es lo que ve el usuario; el segundo son los valores internos que maneja el script. Si se cambia el orden en uno, se debe cambiar en el otro o el modo seleccionado será incorrecto.

---

## Procedimiento de re-aplicación ante actualización

1. Hacer backup del script nuevo antes de editar → `Image Occlusion.md.bk`
2. Buscar el bloque `// Present user with operation mode choices`
3. Verificar que las entradas `hideOne` y `hideAll` existen en ambos arrays
4. Aplicar el Parche 1: mover `hideAll` a posición 0 en ambos arrays simultáneamente
5. Verificar que `delete` y `deleteFiles` no cambiaron de posición

---

## Notas

- El backup del script original está en `Image Occlusion.md.bk` (fecha: 2026-08-01)
- No modificar la lógica de generación de imágenes ni de templates
- Ante dudas sobre el comportamiento original, comparar con el `.bk`
