---
alias: ""
date: 
---

## Objetivo
Crear scripts con shell command para extraer secciones de n archivos, y poder reintegrarlos si es necesario.
Sirve para 

Crear el script de multi-extract y multi-reintegrate, probrlos

**Detalle técnico:** `section_reintegrate` debería poder manejar múltiples entradas en `section.md` — requiere rediseño de cómo se parsea el archivo temporal.

# Comentarios

bien borre los prompts creados si es con el data.json y luego cree el prompt de "secction reintegrate" se debe hacer en la configuracion general de shell commands y ya probe el script, ojo que debia quitar el antiguo y colocar el nuevo en ribon con commander.
resumne si funciona los scripts el de extraccion y el de integracion.
se extrajeron 3 titulos de diferentes archivos y los 3 llegaron a section.md ahi se les agrego una linea de prueba para ver si esta llegaba en la reintegracion. luego al ver le json ti tenia los 3 titulos y sus rutas. al reintegrar pide la ruta se le entraga y procede a reintegrar el titulo en el archivo que corrsponde lo hace bien y no copiar la ruta eso tambien salio bien. al revisar el json se ve como se elimina el dato del titulo y la ruta de la seccion reintegraga, eso tambien esta bien

lo que falta ahora es la documentacion

---

## Pendientes

- [ ] Modo multi-extract (sesión posterior, baja prioridad)

> [!note]- Historial de pendientes
> **fecha** — 

---

## Completado

- [x] 

> [!note]- Historial de sesiones
> **fecha** — 

---

## Preguntas abiertas

**Qué hacer:** modificar `section_extract` para que si `section.md` ya tiene contenido, en lugar de abortar, acumule la nueva sección debajo con un cabezal de ruta (`--- ruta\archivo.md ---`). Permitiría extraer secciones de distintos archivos para armar contexto.

**Archivos a leer antes:**
- `E:\University_vault_2026\.obsidian\scripts\python\section_extract\src\main.py`
- `E:\University_vault_2026\.obsidian\scripts\python\section_reintegrate\src\main.py`

---

## Herramientas / plugins

**Herramientas:** Filesystem MCP, edit_file.

---

## Archivos relacionados


---

## Decisiones

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
|       |          |        |












---
