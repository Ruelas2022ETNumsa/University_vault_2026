---
title: "Shell Commands — notebooklm_fix"
galaxy_body: beacon
scope: vault
author: [usuario, claude]
audience: [usuario, claude]
related_notes:
  - "[[shellcmd_scripting_guide]]"
  - "[[shellcmd_config_script]]"
  - "[[shellcmd_config_gral]]"
tags: [beacon, obsidian, shell-commands, notebooklm, infraestructura, automatizacion]
date_created: 2026-08-13
date_updated: 2026-08-13
status: activo
---

# Shell Commands — notebooklm_fix

> Script de corrección automática sobre archivos `.md` generados desde NotebookLM.
> Normaliza bloques Cornell, etiquetas de bloques de código (desmos, tikz), notación matemática y arrays antes de usar el archivo en Obsidian.

---

## 1. Propósito

NotebookLM entrega el output con varios problemas de formato que impiden el renderizado correcto en Obsidian. Este script los corrige en un solo paso directamente sobre el archivo `.md` activo.

---

## 2. Archivo del script

```
.obsidian/scripts/python/notebooklm_fix/src/main.py
```

---

## 3. Correcciones que aplica

### 3.1 Bloques Cornell mal formados

NotebookLM a veces separa el identificador `cornell` del bloque de backticks con un salto de línea. Obsidian no lo reconoce así.

**Antes:**
`````
`````
cornell
::cue
...
`````

**Después:**
`````
`````cornell
::cue
...
`````

También corrige bloques con 3 o 4 backticks en lugar de 5, y cierres con menos de 5 backticks.

---

### 3.2 `\frac` → `\dfrac`

Reemplaza todas las ocurrencias de `\frac` por `\dfrac` para forzar el tamaño de fracción display, más legible en apuntes. No afecta `\dfrac` ni `\tfrac` ya existentes.

**Antes:**
```
\frac{1}{2}
```

**Después:**
```
\dfrac{1}{2}
```

---

### 3.3 Bloques desmos sin etiqueta

NotebookLM genera bloques de código desmos sin la etiqueta del lenguaje. El script la detecta por la firma `left=` en la primera línea del bloque.

**Antes:**
````
```
left=-0.5; right=5.5; bottom=-1; top=24;
```
````

**Después:**
````
```desmos-graph
left=-0.5; right=5.5; bottom=-1; top=24;
```
````

---

### 3.4 Bloques tikz sin etiqueta

NotebookLM genera bloques tikz/pgfplots sin etiqueta. El script detecta tres casos por la firma de la primera línea:

| Caso | Firma detectada | Resultado |
|------|----------------|-----------|
| A | ` ``` ` + `\usepackage{` | agrega `tikz` |
| B | ` ``` ` + `\begin{tikzpicture}` | agrega `tikz` |
| C | ` ``` ` + `\begin{axis}` | agrega `tikz` |

**Antes:**
````
```
\usepackage{pgfplots}
\begin{document}
...
```
````

**Después:**
````
```tikz
\usepackage{pgfplots}
\begin{document}
...
```
````

> Los entornos `tikzpicture` y `axis` son los dos más comunes generados por NotebookLM. Si aparece un entorno nuevo, agregar su caso en el paso 2b del script.

---

### 3.5 Arrays en una línea

Cuando un array `$$\begin{array}...\end{array}$$` llega todo en una línea con ` \ ` como separador de filas, el script lo expande con saltos de línea reales.

**Antes:**
```
$$\begin{array}{rcl} a & = & b \ c & = & d \end{array}$$
```

**Después:**
```
$$\begin{array}{rcl}
a & = & b \\
c & = & d
\end{array}$$
```

---

### 3.6 Bloques marginalia en Cornell

Inserta automáticamente los bloques `marginalia` dentro de cada bloque Cornell si aún no los tiene. Es idempotente — no duplica si ya están presentes.

**Antes:**
`````
`````cornell
::cue
palabras clave

::note
contenido
`````
`````

**Después:**
`````
`````cornell
::cue
````marginalia %%> %%
palabras clave

````
::note
````marginalia %%< %%
contenido
`````
`````

---

### 3.7 Normalización de notación LaTeX — INACTIVO

El script incluye un bloque comentado para normalizar la notación LaTeX de doble backslash que entrega la app de NotebookLM en Android (`\\(` → `\(`, `\\[` → `\[`) y convertirla directamente a `$...$` y `$$...$$`.

**Este bloque está inactivo** porque el plugin `Fix Math for Obsidian` (mod alx-rul) ya realiza esta conversión. Activar solo si el script corre sin ese plugin.

> Ver: `ship_fix-math-mod.md` en `_legacy` para el detalle de la modificación del plugin.

---

## 4. Qué no toca

- No modifica bloques de código inline ni triple backtick con contenido propio
- No toca el YAML frontmatter
- Es idempotente — si corre dos veces el resultado es el mismo

---

## 5. Configuración en Shell Commands

### Pestaña General

| Campo | Valor |
|---|---|
| Alias | `NBLM — fix formato` |
| Confirmación antes de ejecutar | OFF |
| stdin | vacío |

**Comando (Windows):**
```
python "{{vault_path}}\.obsidian\scripts\python\notebooklm_fix\src\main.py" "{{file_path:relative}}" "{{vault_path}}"
```

### Pestaña Environments

| Campo | Valor |
|---|---|
| Windows shell command | (mismo comando que arriba) |
| Terminal de Windows | `PowerShell 5` |

### Pestaña Output

| Canal | Valor |
|---|---|
| stdout | `Notification balloon` |
| stderr | `Notification balloon` |
| Output handling mode | `Wait until finished` |
| Show notification when executing | `Do not show` |

### Pestaña Preactions

Ninguna — el script no requiere input del usuario.

### Pestaña Events

| Campo | Valor |
|---|---|
| Availability in command palette | `Command palette & hotkeys` |
| Todos los eventos automáticos | OFF |

### Pestaña Variables

| Variable | Si no está disponible |
|---|---|
| `{{file_path}}` | `Cancel execution and show errors` |
| `{{vault_path}}` | `Cancel execution and show errors` |

---

## 6. Flujo de uso

1. Abrir el `.md` exportado desde NotebookLM en Obsidian
2. Ejecutar el comando desde la paleta (`NBLM — fix formato`)
3. El script notifica `Correcciones realizadas.` o `Sin cambios.`
4. Correr el plugin `Fix Math` para convertir la notación LaTeX a `$...$`
5. El archivo queda listo para usar en Obsidian

---

## 7. Plugins requeridos

| Plugin | Rol |
|---|---|
| Shell Commands (Obsidian) | Ejecuta el script Python desde Obsidian |
| Fix Math for Obsidian (mod alx-rul) | Convierte notación LaTeX a formato Obsidian, incluye soporte doble backslash Android |

---

%%
# galaxy-links
[[shellcmd_scripting_guide]]
[[shellcmd_config_script]]
[[shellcmd_config_gral]]
%%
