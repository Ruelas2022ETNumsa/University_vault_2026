---
title: "Marginalia — Solves"
galaxy_body: beacon
scope: vault
audience: [claude, usuario]
related_notes:
  - "[[_sync-system]]"
tags: [beacon, marginalia, infraestructura, solve]
date_created: 2026-07-09
date_updated: 2026-08-20
status: activo
---

# Marginalia — Solves

## Ancho de línea por defecto rompe la visualización de notas Marginalia en móvil

**Error:** sin el snippet, las notas Marginalia en móvil y tablet se muestran con el ancho de línea por defecto de Obsidian — el plugin `cornell-marginalia` no ajusta este valor automáticamente, lo que hace que las notas al margen no se vean correctamente.

**Resultado esperado:**
- Tablet vertical: estética aceptable
- Tablet horizontal: equivalente a PC
- Celular horizontal: aceptable

**Causa:** Obsidian móvil no ajusta `--file-line-width` automáticamente para el plugin `cornell-marginalia`.

**Solución:** snippet `mobile-line-width.css` en `.obsidian/snippets/` con los siguientes valores:

```css
/* Línea legible para móvil y tablet — tema Default */
.is-mobile {
  --file-line-width: 50% !important;
}

.is-tablet {
  --file-line-width: 60% !important;
}
```

Activar en Obsidian → Settings → Appearance → CSS Snippets → activar `mobile-line-width`.

**Archivo legacy:** `mobile-line-width-minimal.css` en la misma carpeta — creado durante la etapa en que se evaluaron distintos temas. Quedó en desuso al decidir que todos los dispositivos usaran el tema Default. Se conserva como referencia.

**Estado:** resuelto.

---

## Marginalia no renderizan en Reading View

**Error:** las marginalia dejan de renderizarse en Reading View sin cambios aparentes en las notas.

**Causas posibles y verificación:**

### 1. `Enable in Reading View` desactivado

El processor del plugin tiene como primera instrucción:

```js
// main.js — línea ~14019
this.registerMarkdownCodeBlockProcessor("marginalia", async (source, el, ctx) => {
  if (!this.settings.enableReadingView) return;
```

Si `enableReadingView` es `false`, el processor sale inmediatamente y no renderiza nada.

**Verificar:** Settings → Cornell Marginalia → Appearance & Rendering → **Enable in Reading View** → debe estar ON.

---

### 2. Nombre del bloque de código incorrecto

El plugin (parcheado) registra el processor como `"marginalia"`. Los bloques en las notas deben estar escritos como:

````
```marginalia
texto  %%> nota %%
```
````

Si los bloques dicen ` ```cornell ` no renderizan — ese nombre quedó reservado para Cornell Notes tras el parche.

**Verificar:** que todos los bloques del vault usen ` ```marginalia `, no ` ```cornell `.

---

### 3. Parche en `main.js` perdido por actualización

El parche cambia `"cornell"` → `"marginalia"` en el `registerMarkdownCodeBlockProcessor`. Si el plugin se actualiza desde Community Plugins, el `main.js` se sobreescribe y el parche se pierde.

**Verificar:** buscar en `.obsidian/plugins/cornell-marginalia/main.js` la línea:

```
registerMarkdownCodeBlockProcessor("marginalia"
```

Si dice `"cornell"` — el parche se perdió, reaplicar.

**Estado actual (2026-08-20):** parche intacto, confirmado por grep.

---

**Estado:** documentado.

---

%%
# galaxy-links
[[_app/_config/_sync-system.md]]
[[_app/_appnotes/Marginalia_guide.md]]
[[_app/_config/_marginalia_system.md]]
%%
