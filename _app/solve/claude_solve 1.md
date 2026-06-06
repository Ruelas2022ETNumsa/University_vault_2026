---
title: "Claude — Errores conocidos y soluciones"
galaxy_body: beacon
scope: vault
audience: [claude, usuario]
related_notes:
  - "[[_claude-boot]]"
tags: [beacon, claude, infraestructura, solve]
date_created: 2026-06-03
status: activo
---

# Claude — Errores conocidos y soluciones

> Configuración de Claude: [[_claude-boot]]

---

## write_file destruye archivos existentes

**Error:** usar `Filesystem:write_file` en un archivo existente lo sobreescribe
completo si no se pasa el contenido íntegro. El archivo queda con solo el
fragmento que se pasó como contenido.

**Causa:** `write_file` no es una operación de edición — es una operación de
creación/reemplazo total. No hace merge ni append.

**Solución:** para modificar archivos existentes usar siempre
`Filesystem:edit_file` — modifica solo las líneas indicadas sin tocar el resto.

**Regla:** `write_file` solo para archivos nuevos. Ediciones siempre con `edit_file`.

%%
galaxy-links
[[_claude-boot]]
%%
