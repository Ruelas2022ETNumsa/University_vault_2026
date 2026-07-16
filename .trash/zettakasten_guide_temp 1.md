---
title: "Zettelkasten via Margin Threads — Guía temporal"
galaxy_body: beacon
scope: vault
audience: [usuario, claude]
tags: [beacon, marginalia, zettelkasten, stitch, infraestructura]
date_created: 2026-07-07
date_updated: 2026-07-07
status: borrador
---

# Zettelkasten via Margin Threads — Guía temporal

> Estado: en prueba. Flujo descubierto en sesión 2026-07-07.
> Depende de: [[Marginalia_guide]] · [[cornell_guide]] · [[plugin_guide]]

---

## ¿Qué es esto?

Margin Threads + ZK es un sistema para conectar marginalia de distintas notas y materializar esa conexión como una nota `bridge` enriquecida. El stitch agrega un comentario corto de conexión entre dos marginalia; la nota ZK permite explorar y expandir esa conexión.

**Usos identificados:**
- Puente entre materias — mismo concepto en MAT101 y ETN901
- Mismo concepto en distinto nivel — T01 superficial vs T03 profundo
- Generación asistida de galaxy-links entre notas relacionadas

---

## Flujo completo de creación

### 1. Agregar marginalia en las notas a conectar

En cada nota, agregar una marginalia que describa el concepto a conectar:

```
%%> ! concepto clave %%
```

Usar prefijos semánticos si aplica (`!` importante, `?` pregunta, etc.).

### 2. Crear el stitch en Marginalia Explorer

1. Abrir Explorer con `Alt+E`
2. Ir al tab **Vault** (`Alt+2`)
3. Hacer clic sobre reloj (recientes)  
4. Hacer clic en **Stitch** sobre la marginalia origen 
5. Seleccionar la marginalia destino
6. En el modal escribir una descripción corta de la conexión
7. Confirmar — el plugin escribe el Block ID en ambas notas

**Resultado en las notas:**
- Nota origen: `%%> concepto [[nota-destino#^blockid]] {stitch: descripción} %%`
- Nota destino: `%%> concepto ^blockid %%`

### 3. Materializar como nota ZK (opcional)

Solo cuando la conexión merece ser explorada con más profundidad:

1. En tab **Threads** — localizar el thread creado
2. Arrastrar el thread al recuadro de captura del sidebar
3. Agregar contexto adicional si se quiere
4. Presionar el botón **⚡** para crear la nota en `Zettelkasten/`
5. Templater se activa — responder los 4 prompts:
   - **Slug** — nombre descriptivo (ej: `MAT101-ETN901-derivacion-campo`)
   - **Materia(s)** — (ej: `MAT101, ETN901`)
   - **Tipo de conexión** — (ej: `mismo concepto`, `contraste`, `continuación`)
   - **Parcial** — número de parcial

### 4. Completar la nota ZK

Al abrirse la nota generada:
1. Llenar `connected_notes` en el YAML con los wikilinks de las notas conectadas
2. Agregar galaxy-links en el bloque `%%` al pie
3. Expandir la conexión con texto si aporta valor

---

## Template actual — `tpl-zk.md`

```
<%*
const slug = await tp.system.prompt("Nombre del stitch (slug corto)");
const subject = await tp.system.prompt("Materia(s) (ej: MAT101, ETN901)");
const connection_type = await tp.system.prompt("Tipo de conexión");
const partial = await tp.system.prompt("Parcial (1, 2 o 3)");
if (slug) await tp.file.rename(slug);
%>
```

YAML generado incluye: `galaxy_body: bridge` · `scope: stitch` · `subject` · `connection_type` · `partial` · `tags` · `date_created` · `date_updated`

---

## Carpeta y configuración

| Campo | Valor |
|---|---|
| Carpeta ZK | `Zettelkasten/` |
| Template path | `_templates/tpl-zk.md` |
| Carpeta ignorada por Marginalia | agregar a Ignored Folders |

---

## Pendientes

- [ ] Evaluar script Python para extraer automáticamente los links del stitch e insertarlos en `connected_notes` al crear la nota ZK
- [ ] Definir si `Zettelkasten/` se mueve dentro de `_app/` o se queda en raíz
- [ ] Documentar en `Marginalia_guide.md` sección Margin Threads cuando el flujo esté cerrado
- [ ] Definir tags adicionales por tipo de conexión (`bridge-materias`, `bridge-temas`, etc.)
- [ ] Evaluar si galaxy-links se pueden generar asistidos desde una marginalia apuntando a un título

---

%%
# galaxy-links
[[Marginalia_guide]]
[[cornell_guide]]
[[plugin_guide]]
%%
