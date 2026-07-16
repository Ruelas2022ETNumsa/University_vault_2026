---
title: "Script Guide — Scripts de automatización del vault"
galaxy_body: beacon
scope: vault
audience: [usuario, claude]
related_notes:
  - "[[plugin_guide]]"
  - "[[_galaxy-system]]"
tags: [beacon, obsidian, scripts, infraestructura, automatizacion]
date_created: 2026-07-11
date_updated: 2026-07-11
status: activo
---

# Script Guide — Scripts de automatización del vault

> Scripts Python ejecutados desde Obsidian via Shell Commands.
> Configuración del plugin: [[shellcommands_guide(scripts)]].
> Intérprete: `C:\Users\USUARIO\AppData\Local\Programs\Python\Python313\python.exe`
> Raíz de scripts: `{{vault_path}}\.obsidian\scripts\python\`

---

## Índice

- [[#1. notebooklm_fix]]
- [[#2. section_script]]
	- [[#2.1 section_extract]]
	- [[#2.2 section_reintegrate]]
- [[#3. Sync NotebookLM]]
---

## 1. notebooklm_fix

**Propósito:** Corrige errores frecuentes que NotebookLM comete al generar notas `.md`. Opera sobre el archivo activo.

**Ruta:** `.obsidian\scripts\python\notebooklm_fix\src\main.py`
**Alias en Shell Commands:** `NotebookLM Fix — nota activa`
**Icono:** (Commander)
**Argumentos:** `{{file_path:relative}}` `{{vault_path}}`

### Correcciones que aplica

| # | Error | Corrección |
|---|---|---|
| 0 | Bloques cornell mal formados (backticks separados de etiqueta) | Unifica en `` `````cornell `` |
| 1 | `\frac` sin prefijo `d` | `\dfrac` |
| 2 | Bloque desmos sin etiqueta | Agrega `desmos-graph` |
| 3 | Arrays LaTeX en una sola línea | `\\` + salto de línea |
| 4 | Bloques cornell sin `marginalia` anidado | Inserta bloques con placeholders |

---

## 2. section_script


### 2.1 section_extract

**Propósito:** Extrae una sección de cualquier nota del vault y la copia en `Rubbish\section.md` para edición puntual. Guarda metadata en `section.json` para que `section_reintegrate` pueda devolver el contenido al original.

**Ruta:** `.obsidian\scripts\python\section_extract\src\main.py`
**Alias en Shell Commands:** `Section Extract`
**Icono:** scissors
**Argumentos:** `{{file_path:relative}}` `{{vault_path}}` `{{_section_heading}}` `{{_section_source}}`

#### Custom variables (Shell Commands)

| Variable | Descripción |
|---|---|
| `{{_section_heading}}` | Heading exacto a extraer, ej: `## Título` |
| `{{_section_source}}` | Ruta absoluta del archivo fuente |

#### Archivos involucrados

| Archivo | Rol |
|---|---|
| `Rubbish\section.md` | Archivo temporal con la sección extraída |
| `.obsidian\scripts\python\section_tool\section.json` | Metadata: heading + ruta fuente |

#### Comportamiento

- Busca el heading exacto (respeta nivel: `##`, `###`, etc.)
- Extrae hasta el siguiente heading de mismo nivel o superior
- Si `section.md` ya tiene contenido, aborta con mensaje — correr `section_reintegrate` primero
- Requiere archivo activo abierto en Obsidian

#### Flujo de uso
```markdown

1. Abrir cualquier nota (para que {{file_path}} no falle)
2. Presionar boton Section Extract
3. Prompt campo 1: heading exacto (ej: ## Metodologia)
4. Prompt campo 2: ruta absoluta del archivo fuente
5. Obsidian confirma: "Seccion extraida: ## Titulo"
6. Editar Rubbish\section.md
7. Correr section_reintegrate
  
```

---

### 2.2 section_reintegrate

**Propósito:** Toma el contenido editado de `Rubbish\section.md`, crea un backup del original y reemplaza la sección correspondiente en el archivo fuente. Limpia los archivos temporales al terminar.

**Ruta:** `.obsidian\scripts\python\section_reintegrate\src\main.py`
**Alias en Shell Commands:** `Section Reintegrate`
**Icono:** file-input
**Argumentos:** `{{file_path:relative}}` `{{vault_path}}`

#### Comportamiento

- Lee heading y ruta fuente desde `section.json` — no pide inputs
- Crea backup automático: `nombre 1.md`, `nombre 2.md`, etc. en la misma carpeta del original
- Reemplaza la sección en el original con el contenido de `section.md`
- Limpia `section.md` (vacio) y elimina `section.json`
- Si `section.md` esta vacio, aborta con mensaje

---

## 3. Sync NotebookLM

(para otra sesion)

---

%%
# galaxy-links

%%