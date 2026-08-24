---
title: "Document Comments — Integración Galaxy"
galaxy_body: beacon
scope: vault
audience: [usuario, claude]
related_notes:
  - "[[_galaxy-system]]"
  - "[[_marginalia_system]]"
  - "[[_claude-boot]]"
  - "[[_sidenotes-system]]"
tags: [beacon, obsidian, plugins, infraestructura, comments, galaxy]
date_created: 2026-08-24
date_updated: 2026-08-24
status: activo
---

# Document Comments — Integración Galaxy

> Plugin: **Document Comments** by kylemcd — [GitHub](https://github.com/kylemcd/obsidian-document-comments)
> Referencia de Marginalia: [[_marginalia_system]]
> Para el arranque de sesión con Claude: [[_claude-boot]]

Document Comments agrega comentarios estilo Notion/Linear al margen de las notas. Los comentarios se almacenan como HTML comments invisibles dentro del `.md` — no alteran el contenido, no aparecen en export, y Claude puede leerlos directamente desde Filesystem MCP sin configuración adicional.

**Diferencia clave con Marginalia:** Marginalia es para aprender (active recall, flashcards, semantic highlighting, threads). Document Comments es para gestionar — estados, revisiones, pendientes anclados al texto exacto. No se reemplazan, se complementan.

---

## Sintaxis

Cada comentario tiene dos partes que el plugin genera automáticamente:

**Parte 1 — ancla** (marca el texto en el cuerpo):
```
<!--c:ID-->texto resaltado<!--/c:ID-->
```

**Parte 2 — bloque de datos** (el comentario en sí, invisible en lectura):
```
<!--co:ID by:autor at:2026-08-24T03:10:00.000Z status:open quote:"texto"
autor (2026-08-24T03:10:00.000Z): mensaje del comentario
-->
```

| Campo | Valores | Descripción |
|---|---|---|
| `by:` | nombre del autor | Configurar en Settings → Document Comments → Author |
| `status:` | `open` / `resolved` | Estado del comentario |
| `quote:` | texto resaltado | Referencia del ancla |
| líneas de thread | `autor (fecha): texto` | Mensajes del hilo, uno por línea |

### Estados
| Estado | Qué significa | Cómo cambiarlo |
|---|---|---|
| `open` | Pendiente, visible en el margen | Hover sobre tarjeta → ✓ Resolve |
| `resolved` | Atendido, oculto por defecto | Hover sobre tarjeta → ↺ Reopen |

### Cómo agregar un comentario
1. Seleccionar texto en la nota
2. Click derecho → **Add comment** (o Command Palette → `Add comment on selection`)
3. Escribir en la tarjeta del margen → Enter para guardar

### Configuración de autor
Settings → Document Comments → Author → escribir el nombre (ej: `alex`). Por defecto es `me`.

---

## Uso por galaxy_body

### `comet` — errores en ejercicios resueltos

**Caso:** detectás un error en un paso durante la resolución. En lugar de borrar y reescribir, comentás el paso exacto.

**Ventaja sobre Marginalia:** el comentario puede marcarse `resolved` una vez corregido — Marginalia no tiene ese estado. El error queda visible como registro de proceso.

```
Ejemplo de uso:
→ Seleccionar el paso con error
→ Comentar: "X- signo incorrecto en el desarrollo — ver moon de propiedades"
→ Corregir el paso en el cuerpo
→ Marcar el comentario como resolved
```

| Tag sugerido | Uso |
|---|---|
| Sin tag | Error detectado y corregido en el mismo momento |
| Con reply de claude | Error que requiere verificación o explicación adicional |

---

### `supernova` — tareas del docente con estado

**Caso:** el docente asigna una tarea durante la clase. El tag `T-` de Marginalia marca la tarea pero no tiene estado — no hay forma de saber si ya la completaste sin leer el texto.

**Ventaja sobre Marginalia `T-`:** Document Comments agrega estado `open`/`resolved`. Cuando completás la tarea, la marcás resuelta. El comentario queda en el archivo como registro.

> ⚠️ `T-` de Marginalia sigue siendo el marcador visual durante la transcripción. Document Comments complementa con el estado de completitud.

```
Flujo sugerido:
→ Durante transcripción: anotar con %%> T- tarea asignada %%
→ Después de clase: seleccionar la línea de la tarea → Add comment → "pendiente de entrega"
→ Al completar: marcar resolved
```

---

### `asteroid` — observaciones sobre fuentes

**Caso:** estás leyendo un `asteroid` (extracto de libro o paper) y querés anotar algo que no es contenido sino una observación sobre el contenido — "esto contradice lo del planet X", "verificar con el docente", "dato no confirmado".

**Ventaja:** el comentario no forma parte del contenido del asteroid — es metadata de revisión. No ensucia el cuerpo ni aparece en export.

```
Ejemplos de comentarios en asteroid:
→ "contradice ETN806-T01-joint-pdf — verificar edición del libro"
→ "confirmar con docente si este teorema aplica al parcial actual"
→ "fuente citada incorrectamente — buscar edición original"
```

Marcar `resolved` cuando verificaste.

---

### `beacon` — discrepancias y pendientes de actualización

**Caso:** encontrás una discrepancia en un beacon (ej: lo documentado no coincide con lo que hay en disco) o un campo que quedó desactualizado.

**Ventaja sobre `_ToDo-system`:** el comentario vive pegado al texto problemático exacto. No necesitás ir a otra nota para encontrar qué hay que arreglar — al abrir el beacon, el margen ya lo muestra.

```
Flujo sugerido:
→ Detectar discrepancia → seleccionar la línea → Add comment → describir el problema
→ Marcar resolved cuando el beacon se actualice
→ Actualizar date_updated del beacon
```

> Esta es la forma recomendada de marcar TODOs dentro de beacons en lugar de comentarios Markdown inline (`<!-- TODO: ... -->`), que son invisibles en lectura y no tienen estado.

---

### `workshop` — bloqueos y dependencias por sección

**Caso:** una sección del workshop está bloqueada esperando información externa (enunciado oficial, respuesta del docente, resultado de otro paso).

```
Ejemplos:
→ "bloqueado — esperando enunciado oficial del docente"  → resolved al recibir
→ "depende de completar sección 2 primero"               → resolved al desbloquear
→ "revisar con compañero antes de entregar"              → resolved al verificar
```

---

## Canal de comunicación con Claude

Document Comments funciona como canal asíncrono entre el usuario y Claude. Claude puede leer los comentarios `open` de cualquier nota directamente desde Filesystem MCP y actuar sobre ellos en la siguiente sesión.

### Flujo de revisión

```
Usuario:
→ Agrega comentario open en una nota ("revisar esta derivación")
→ En la próxima sesión comparte la nota con Claude

Claude:
→ Lee los comentarios open en el archivo
→ Responde con un reply en el mismo thread
→ Marca resolved si el problema está resuelto
→ Deja open si requiere acción del usuario
```

### Convenciones de autor

| Autor | Cuándo |
|---|---|
| `alex` (o el nombre configurado) | Comentarios propios — observaciones, dudas, tareas |
| `claude` | Replies de Claude — respuestas, correcciones, confirmaciones |

### Colores de autor

| Autor | Color | RGB | Hex |
|---|---|---|---|
| `alex` | azul petróleo | 0, 162, 199 | `#00A2C7` |
| `claude` | naranja ladrillo | 220, 105, 55 | `#DC6937` |

> Configurar en Settings → Document Comments → Use author colors (ON) → asignar el hex a cada autor.

> Claude escribe en el archivo usando Filesystem MCP con la misma sintaxis que genera el plugin. Los comentarios de Claude son indistinguibles visualmente de los del usuario — aparecen en el mismo margen con la misma tarjeta.

### Qué puede hacer Claude directamente

| Acción | Cómo |
|---|---|
| Crear comentario nuevo | Escribe ancla + bloque `<!--co:...-->` en el archivo |
| Agregar reply a thread existente | Agrega línea `claude (fecha): texto` al bloque |
| Marcar resolved | Cambia `status:open` → `status:resolved` en el bloque |
| Reabrir comentario | Cambia `status:resolved` → `status:open` |

> Claude nunca modifica el contenido de la nota al gestionar comentarios — solo edita los bloques `<!--co:...-->`.

---

## Limitaciones conocidas

| Limitación | Detalle |
|---|---|
| Highlights en tablas | En Live Preview el highlight no se muestra sobre texto dentro de tablas. El comentario funciona, el highlight aparece en Reading View y Source Mode |
| Comentarios superpuestos | Evitar comentar texto que ya está dentro de otro comentario — se guardan bien pero son difíciles de gestionar |
| Sin formato en quotes | La `quote:` del bloque almacena texto plano — el formato Markdown del texto resaltado no se preserva |
| Fecha no personalizable | El plugin genera siempre formato ISO completo (`2026-08-24T03:10:00.000Z`). En el margen se muestra como `just now` / `2h` / `3d` — la fecha larga solo es visible en el raw del archivo |
| Mobile | En móvil no hay margen flotante — los highlights marcan el texto y los comentarios se gestionan desde el sidebar |

---

## Lo que Document Comments NO reemplaza

| Sistema | Sigue siendo para |
|---|---|
| **Cornell Marginalia** | Aprendizaje activo — semantic highlighting, active recall `;;`, flashcards, threads entre notas, blur mode |
| **Side-Notes** (`<span class="sidenote">`) | Notas narrativas al margen que forman parte del contenido de la nota — formato HTML oficial |
| **`_ToDo-system.md`** | Pendientes globales del vault sin ancla a texto específico |

---

%%
# galaxy-links
[[_app/_config/_galaxy-system.md]]
[[_app/_config/_marginalia_system.md]]
[[_app/_config/_claude-boot.md]]
[[_app/_config/_sidenotes-system.md]]
%%
