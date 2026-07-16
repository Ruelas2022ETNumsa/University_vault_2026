---
title: "Marginalia — Ancho de línea en móvil y tablet"
galaxy_body: beacon
scope: vault
audience: [claude, usuario]
related_notes:
  - "[[_sync-system]]"
tags: [beacon, marginalia, infraestructura, solve]
date_created: 2026-07-09
status: activo
---

# Marginalia — Ancho de línea en móvil y tablet

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

%%
# galaxy-links
[[_sync-system]]
%%
