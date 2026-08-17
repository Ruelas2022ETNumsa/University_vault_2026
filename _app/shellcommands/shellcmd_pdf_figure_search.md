---
title: "Shell Commands — pdf_figure_search"
galaxy_body: beacon
scope: vault
author: [usuario, claude]
audience: [usuario, claude]
related_notes:
  - "[[shellcmd_config_script]]"
  - "[[shellcmd_config_gral]]"
  - "[[DOC-ETN607-transcription]]"
tags: [beacon, obsidian, shell-commands, ETN607, notebooklm, pdf, infraestructura, automatizacion]
date_created: 2026-08-17
date_updated: 2026-08-17
status: activo
version: v2
---

# Shell Commands — pdf_figure_search

> Script que busca una etiqueta de figura en los PDFs de una materia y devuelve una lista de links PDF++ ordenados por proximidad al número de página entregado por NotebookLM. El resultado se copia al portapapeles listo para pegar en Obsidian.
> v2: el bloque NLM completo es obligatorio — la etiqueta se extrae del bloque automáticamente.

---

## 1. Propósito

Al transcribir apuntes con NotebookLM, el prompt de complemento (BCv4) entrega referencias a figuras de los libros fuente en formato:
```
[[nombre.pdf#page=N]]
*Fig. 2-1*
```
El `page=N` es el número de página **impreso** en el libro — puede tener desfase respecto al número del visor PDF++ (por portada, índice, etc.). Este script recibe esa referencia, extrae el PDF y la etiqueta del bloque, busca la etiqueta en el PDF real, y devuelve los 3 candidatos más cercanos al número indicado ordenados por error mínimo.

---

## 2. Archivo del script

```
.obsidian/scripts/python/pdf_figure_search/main.py
```

---

## 3. Output esperado al pegar

```
> Figura 2-1 en Dare A. Wells-SCHAUM'S Lagrangian Dynamics-McGraw-Hill.pdf — top 3 por proximidad a page=11 (NLM)

[[Dare A. Wells-SCHAUM'S Lagrangian Dynamics-McGraw-Hill.pdf#page=11]]  ← error 0
[[Dare A. Wells-SCHAUM'S Lagrangian Dynamics-McGraw-Hill.pdf#page=12]]  ← error 1
[[Dare A. Wells-SCHAUM'S Lagrangian Dynamics-McGraw-Hill.pdf#page=9]]   ← error 2
```

El candidato con `error 0` es coincidencia exacta. Los siguientes son respaldo por desfase de numeración.

---

## 4. Lógica del script

1. Recibe `sigla` y `nblm_ref` (obligatorios) y `etiqueta` (fallback opcional) como argumentos.
2. Parsea `nblm_ref` para extraer: nombre del PDF, etiqueta (`Fig. X` — ignorando asteriscos de italics) y `hint_page`.
3. La etiqueta del bloque NLM tiene prioridad sobre el campo fallback.
4. Localiza la carpeta del PDF en `_PDF/` según la sigla (tolera `ETN607` y `ETN-607`).
5. Agrupa PDFs partidos (`-1to9`, `-10to16`) bajo su nombre base — busca en todas las partes.
6. Genera 6 variantes de búsqueda: `Fig. X`, `Fig X`, `fig. X`, `fig X`, `Figure X`, `Figura X`.
7. Busca las variantes en cada página del PDF con PyMuPDF.
8. Calcula `error = |página_visor - hint_page|` para cada página encontrada.
9. Ordena por error ascendente y toma los 3 más cercanos.
10. Copia el resultado al portapapeles vía PowerShell Here-String.

**Modo de operación (v2):** siempre selectivo — busca solo en el PDF indicado por el bloque NLM con ranking por proximidad.

**PDFs sin capa de texto:** si no se encuentra la etiqueta, el script reporta el PDF como posiblemente sin OCR e incluye el comando `ocrmypdf` listo para correr en shell.

---

## 5. Cálculo de error

```
error = |página_visor - hint_page|
```

| Página visor | hint_page (NLM) | Error |
|:---:|:---:|:---:|
| 11 | 11 | 0 |
| 12 | 11 | 1 |
| 9  | 11 | 2 |
| 47 | 11 | 36 |

El script devuelve los 3 con menor error. En la práctica, el desfase suele ser pequeño (1-3 páginas por portada/índice), por lo que uno de los 3 candidatos siempre es el correcto.

---

## 6. Dependencias

| Dependencia | Instalación | Estado |
|---|---|---|
| PyMuPDF | `py -m pip install pymupdf` | instalado |
| OCRmyPDF | `py -m pip install ocrmypdf` | instalado |
| Tesseract | winget + tessdata `spa` | instalado |

---

## 7. Configuración en Shell Commands

### Pestaña General

| Campo | Valor |
|---|---|
| Alias | `PDF — buscar figura` |
| Confirmación antes de ejecutar | OFF |
| stdin | vacío |

**Comando (Windows):**
```
py "{{vault_path}}\.obsidian\scripts\python\pdf_figure_search\main.py" "{{_sigla}}" "{{_nblm_ref}}" "{{_etiqueta}}"
```

### Pestaña Environments

| Campo | Valor |
|---|---|
| Terminal de Windows | `PowerShell 5` |

### Pestaña Output

| Canal | Valor |
|---|---|
| stdout | `Notification balloon` |
| stderr | `Notification balloon` |
| Output handling mode | `Wait until finished` |
| Show notification when executing | `Do not show` |

### Pestaña Preactions — Prompt: PDF — buscar figura

| Campo | Valor |
|---|---|
| Título | `PDF — buscar figura` |
| Descripción | `Busca una etiqueta de figura en los PDFs de la materia` |
| Preview shell command | OFF |
| Execute button text | `Buscar` |

**Campo 1 — Sigla:**

| | |
|---|---|
| Field label | `Sigla (ej: ETN607)` |
| Default value | `ETN607` |
| Target variable | `{{_sigla}}` |
| Is required | ON |

**Campo 2 — Referencia NotebookLM:**

| | |
|---|---|
| Field label | `Ref NotebookLM` |
| Description | `Bloque pegado desde NotebookLM. Formato esperado (dos lineas): [[Nombre del libro.pdf#page=11]] *Fig. 2-1* Pegar tal cual, sin modificar.` |
| Default value | vacío |
| Target variable | `{{_nblm_ref}}` |
| Field type | multiline text |
| Is required | ON |

**Campo 3 — Etiqueta (fallback):**

| | |
|---|---|
| Field label | `Etiqueta (fallback)` |
| Description | `Fallback opcional. Solo completar si el bloque NLM no trae etiqueta. Ej: Fig. 2-4` |
| Default value | vacío |
| Target variable | `{{_etiqueta}}` |
| Field type | text |
| Is required | OFF |

### Pestaña Variables

| Variable | Si no está disponible |
|---|---|
| `{{_sigla}}` | `Cancel execution and show errors` |
| `{{_nblm_ref}}` | `Cancel execution and show errors` |
| `{{_etiqueta}}` | `Cancel execution silently` |

---

## 8. Flujo de uso

1. `Ctrl+P` → `PDF — buscar figura`.
2. Completar sigla (`ETN607`).
3. En campo **Ref NotebookLM** pegar el bloque del prompt BCv4:
   ```
   [[Dare A. Wells-SCHAUM'S Lagrangian Dynamics-McGraw-Hill.pdf#page=11]]
   *Fig. 2-1*
   ```
4. Click **Buscar**.
5. Pegar resultado (`Ctrl+V`) en la nota — reemplaza el link placeholder de NotebookLM.
6. Abrir el candidato con `error 0` en PDF++ y verificar con `Ctrl+F`.

---

## 9. Notas de versión

### v1 — 2026-08-17
- Búsqueda por etiqueta con 6 variantes (`Fig.`, `fig.`, `Figure`, `Figura`, con y sin punto)
- Parseo de `nblm_ref`: extrae PDF, etiqueta y `hint_page` desde el bloque de NotebookLM
- Ranking por error mínimo — top 3 candidatos
- Agrupación de PDFs partidos (`-1to9`, `-10to16`)
- Detección de PDFs sin OCR + comando `ocrmypdf` de respaldo
- Campo `etiqueta` como fallback para búsqueda manual sin contexto NLM

### v2 — 2026-08-17 (actual)
- Bloque NLM obligatorio — `nblm_ref` pasa a argumento 2, `etiqueta` a argumento 3 (fallback opcional)
- Etiqueta se extrae siempre del bloque NLM — regex actualizado para ignorar asteriscos de italics Markdown (`*Fig. 2-1*`)
- Formato de entrada confirmado: `[[nombre.pdf#page=N]]` + `*Fig. X-X*` en línea siguiente
- Eliminado el modo búsqueda general — v2 es siempre selectivo (solo el PDF del bloque NLM)
- Validaciones explícitas: falla si no hay PDF o etiqueta extraíble del bloque
- Backup de v1 guardado como `mainv1.py.bk` en la misma carpeta

---

## 10. Plugins requeridos

| Plugin | Rol |
|---|---|
| Shell Commands (Obsidian) | Ejecuta el script Python desde Obsidian |

---

%%
# galaxy-links
[[shellcmd_config_script]]
[[DOC-ETN607-transcription]]
[[_hangar/pdfpp_embed_nblm/pdfpp_embed_nblm.md]]
%%
