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

---

## edit_file duplica contenido cuando oldText no hace match exacto

**Error:** al usar `Filesystem:edit_file` con un `oldText` que no coincide
exactamente con el contenido del archivo (por caracteres corruptos, encoding
roto, texto truncado o espaciado diferente), la herramienta no lanza error
claro — en su lugar puede insertar el `newText` sin eliminar el `oldText`,
duplicando bloques enteros o incluso secciones completas del archivo.

**Causa:** el match de `edit_file` es exacto carácter a carácter. Si el
`oldText` fue copiado de un contexto con encoding dañado o texto cortado
(como un checklist que terminaba en `$...---` en lugar del texto completo),
el match falla silenciosamente y el contenido se inserta de todas formas.

**Solución conocida:** antes de cualquier `edit_file`, verificar el fragmento
exacto con `read_text_file` usando `view_range` apuntando a las líneas
específicas que se van a reemplazar. Copiar el `oldText` literalmente desde
esa lectura, no desde memoria ni desde contexto previo de la conversación.

**Solución preventiva:** para ediciones al final del archivo, usar siempre
el bloque `%%` o algún marcador único y estable como ancla del `oldText` —
no fragmentos de contenido que puedan estar corruptos o truncados.

**Estado:** sin solución automática en la herramienta — requiere disciplina
de verificación previa. Tenerlo en cuenta en cada edición.

%%
galaxy-links
[[_claude-boot]]
%%
