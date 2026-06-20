---
title: "Sistema TABnote — University Vault"
galaxy_body: beacon
scope: vault
audience: [usuario, claude]
related_notes:
  - "[[_galaxy-system]]"
  - "[[_note-system]]"
  - "[[_pdf-system]]"
  - "[[_template-system]]"
  - "[[_notebooklm-system]]"
  - "[[_ToDo-system]]"
tags: [beacon, tabnote, samsung-notes, infraestructura]
date_created: 2026-06-20
date_updated: 2026-06-20
status: en-discusion
---

# Sistema TABnote — University Vault

> Sistema base: [[_galaxy-system]]
> Convención de notas: [[_note-system]]
> Sistema PDF (fuentes externas): [[_pdf-system]]
> Sistema NotebookLM (transcripción): [[_notebooklm-system]]
> Pendientes: [[_ToDo-system]]

> **Estado: en discusión.** Este sistema documenta decisiones ya tomadas y deja explícitos los puntos aún abiertos. No se considera "activo" hasta cerrar la sección de Decisiones pendientes.

---

## Objetivo

Los apuntes manuscritos se toman en la tablet con **Samsung Notes**, en formato nativo `.sdocx`. Este sistema define cómo ese material entra al baúl sin romper la arquitectura Galaxy, y se mantiene **separado del Sistema PDF** ([[_pdf-system]]) a propósito:

> `_pdf/` almacena **fuentes externas** (libros, slides del profesor, prácticas oficiales) — material que el usuario no produjo.
> `_tabnotes/` almacena **producción propia** — apuntes manuscritos del usuario, capturados en tablet.

Mezclarlos sería un error conceptual: un capítulo de Papoulis y un apunte de clase escrito a mano no tienen la misma naturaleza, aunque ambos terminen como PDF.

---

## Nomenclatura usada en este documento

Para evitar confusión entre dos herramientas con nombres parecidos:

| Término | Qué es |
|---|---|
| **PDF+(Samsung)** | PDF exportado desde Samsung Notes con la opción "edición habilitada" — permite anotar con S Pen y editar cuadros de texto *solo dentro de la app Samsung Notes*. La plantilla de fondo queda fija al exportar. |
| **PDF++(Obs)** | Plugin [obsidian-pdf-plus](https://github.com/ryotaushio/obsidian-pdf-plus) usado en el baúl para leer/anotar/citar PDFs dentro de Obsidian. Ya documentado en [[_pdf-system]]. |
| **.sdocx** | Formato nativo de Samsung Notes. Es la única forma 100% editable (plantilla, cuadros de texto, trazos como objetos). Vive en la app / Samsung Cloud, no en el baúl. |

---

## Flujo de vida de un apunte

```
1. CAPTURA — Samsung Notes, formato nativo .sdocx
   Toda la escritura y edición real ocurre aquí, siempre.
        ↓
2. EXPORT — PDF+(Samsung)
   Se exporta cuando el apunte está en un punto estable
   (no necesariamente "terminado" — ver Convención de versionado).
        ↓
3. ALMACENAMIENTO — _tabnotes/ETNXXX/
   El PDF+(Samsung) entra al baúl, se sincroniza con todo el sistema
   (PC, laptop) EXCEPTO GitHub — ver Exclusión de Git.
        ↓
4. ENRIQUECIMIENTO (opcional, dentro de Obsidian)
   PDF++(Obs) permite seleccionar partes del PDF como imagen
   y llevarlas a notas (recortes → photon, pdf-crop).
        ↓
5. TRANSCRIPCIÓN — NotebookLM
   El PDF+(Samsung) se sube a NotebookLM → transcripción a .md con LaTeX.
   Guía de formato para que NotebookLM transcriba bien: PENDIENTE,
   ver [[_notebooklm-system]].
        ↓
6. INTEGRACIÓN AL GRAFO
   La transcripción .md se reparte en notas Galaxy normales
   (planet, moon, comet, etc.) según su contenido — NO queda como
   un solo bloque. El tabnote original queda como fuente de respaldo.
        ↓
7. VISIBILIDAD PARA CLAUDE
   La transcripción .md sí llega a GitHub (a diferencia del PDF) →
   Claude puede leerla vía conectores y ayudar con la materia.
```

---

## Dónde viven los archivos

```
University_Vault_2026/
│
├── _pdf/                       ← fuentes externas (libros, slides, prácticas) — ver [[_pdf-system]]
│   └── ETNXXX/
│
└── _tabnotes/                  ← ★ apuntes manuscritos propios, exportados de Samsung Notes
    ├── ETN806/
    ├── ETN302/
    └── ETNXXX/                 ← una carpeta por materia, sin sub-carpetas de parcial/tema
                                    (misma lógica que _pdf/ — la organización semántica
                                    la llevan el nombre del archivo y la nota tabnote)
```

`_tabnotes/` es estructuralmente igual a `_pdf/` (un almacén de archivos fuente, no de notas), pero semánticamente distinto: aquí no hay autor externo, el autor es el usuario.

---

## Convención de nombres

Mismo patrón Galaxy, sin sub-numeración de versión en el nombre — el control de versión real lo lleva el historial de Git sobre un único archivo (ver más abajo):

```
ETNXXX-TNN-nombre-descriptivo.pdf
```

```
_tabnotes/ETN806/ETN806-T01-apuntes-tablet-joint-pdf.pdf
_tabnotes/ETN806/ETN806-T00-apuntes-tablet-formulario-p2.pdf
```

> Un solo archivo por tema, en escritura continua durante el semestre. No se crean `-v1`, `-v2` — el archivo se sobrescribe a medida que el tema crece (subtítulo 2, subtítulo 3...) hasta archivarse al cerrar el parcial. Ver **Convención de versionado** abajo.

---

## Convención de versionado (un solo archivo, escritura continua)

El flujo real del usuario: un tema empieza con los primeros subtítulos, se exporta; semanas después se agregan subtítulos nuevos a la **misma nota .sdocx**, se reexporta y se **sobrescribe el mismo PDF** en `_tabnotes/`. Esto se mantiene así hasta que el parcial cierra.

Reglas:
- **Nunca editar el PDF directamente.** Toda edición ocurre en el `.sdocx` original en Samsung Notes. El PDF en el baúl siempre es un export, nunca la fuente de edición — esto reduce (no elimina) el riesgo del bug de guardado in situ, ver Riesgos conocidos.
- **Sobrescribir, no duplicar.** Mismo nombre de archivo en cada export. Git lleva el historial real de cambios — no hace falta numerarlo a mano.
- **Archivar al cerrar el parcial.** Cuando el tema/parcial se da por terminado, el archivo deja de tocarse. No requiere moverse de carpeta — su estado pasa a "cerrado" implícitamente (se podría marcar con un campo `status` en la nota `tabnote`, ver YAML abajo).

> **Pendiente de validar con uso real:** cómo se comporta el repositorio de Git con un PDF que se sobrescribe seguido durante el semestre (cada export es un blob binario nuevo, sin diff legible). Ver Decisiones pendientes.

---

## Nota `tabnote` — el puente al grafo

Igual que el `asteroid` conecta un PDF externo al grafo, el `tabnote` conecta un PDF+(Samsung) propio. Vive en `Semesters/` junto al resto de notas Galaxy del tema.

```yaml
---
title: "ETN806 — T01 — Apunte de tablet: PDF conjunta"
galaxy_body: tabnote
subject: ETN806
semester: 8
partial: 2
topic: 1
source_device: "Galaxy Tab — Samsung Notes"
export_format: "pdf-plus-samsung"
pdf_file: "[[ETN806-T01-apuntes-tablet-joint-pdf.pdf]]"
transcribed: false
transcription_note: "[[ETN806-T01-transcripcion-notebooklm]]"
related_planets:
  - "[[ETN806-T01-joint-pdf-definition]]"
tags: [ETN806, galaxy-tabnote, P2, T01]
date_created: YYYY-MM-DD
date_updated: YYYY-MM-DD
status: en-proceso
---
```

```markdown
%%
galaxy-links
[[ETN806-T01-joint-pdf-definition]]
%%
```

| Campo | Propósito |
|---|---|
| `export_format` | Siempre `pdf-plus-samsung` por ahora. Reservado por si en el futuro se prueba otro modo de export. |
| `transcribed` | `false` hasta que exista una transcripción NotebookLM vinculada. Permite filtrar con DataView qué apuntes faltan transcribir. |
| `transcription_note` | Wikilink a la nota que contiene la transcripción `.md`. Esa nota sí participa de Git/GitHub. |
| `status` | `en-proceso` mientras el tema sigue en escritura activa, `cerrado` cuando el parcial termina. |

> `tabnote` se diferencia de `asteroid` (ver [[_pdf-system]]) en que `asteroid` apunta a una fuente externa y `tabnote` apunta a producción propia. Ambos comparten la lógica de "el archivo es mudo, la nota lo activa".

---

## Exclusión de Git/GitHub

Los PDF+(Samsung) en `_tabnotes/` se sincronizan con todo el sistema (Obsidian Sync / la herramienta de sync de archivos que use el baúl entre PC y laptop) **pero no se suben a GitHub**, por el mismo motivo que ya se abandonó con los PDF de libros en `_pdf/`: archivos binarios pesados rompen la sincronización de Git.

```
.gitignore
_pdf/
_tabnotes/      ← se agrega esta línea
```

Lo que sí llega a GitHub (y por lo tanto a Claude vía conectores) es la **transcripción `.md`** generada con NotebookLM, no el PDF.

---

## Acceso a Samsung Notes / Samsung Cloud desde PC

Para mover trabajo de la tablet al baúl sin depender solo de exportar a mano:

| Método | Qué permite | Confiabilidad |
|---|---|---|
| App "Samsung Notes" (Microsoft Store, solo Windows) + Sync con Samsung Cloud | Ver y editar notas `.sdocx` nativas directo en PC, mismas que en la tablet | Alta — es el método recomendado |
| Portal web `account.samsung.com` → Samsung Cloud → ícono "Samsung Notes" | Ver/editar notas desde cualquier navegador | Media — hay reportes (2024-2025) de exportaciones de Samsung Cloud que llegan vacías |
| Modo "Samsung Notes PDF reader" al abrir un PDF | Edición en sitio: guarda cambios directo en la ubicación original del archivo, sin reexportar manualmente | Baja-media — bug conocido donde el guardado conserva solo la anotación y pierde el contenido original (queda en blanco). **Probar empíricamente con un archivo de bajo riesgo antes de confiar el flujo en esto.** |

---

## Riesgos conocidos (no hipotéticos)

Samsung Notes ha tenido rupturas de compatibilidad documentadas en actualizaciones grandes:

| Cuándo | Qué pasó |
|---|---|
| 2020 | Migración de formato separó "notas viejas" de "nuevas"; algunos usuarios perdieron categorías y necesitaron un add-on para recuperar acceso a notas antiguas. |
| 2024–2025 | Actualización rompió la visualización de PDFs importados desde apps de escaneo de terceros (quedaban en blanco) — afectó a usuarios con miles de notas. |
| Recurrente | Reportes de guardado de PDF anotado que pierde el contenido original, dejando solo la capa de anotación. |

**Mitigación:** el `.sdocx` original en Samsung Cloud sigue siendo la fuente de verdad mientras no se decida lo contrario (ver Decisiones pendientes). El PDF+(Samsung) en el baúl es una copia de trabajo/consulta, no el único respaldo.

---

## Resumen Pros / Contras (de la discusión 2026-06-20)

**Pros:**

1. Sincronización del apunte con todo el sistema del baúl (PC, laptop) salvo GitHub.
2. Pipeline hacia NotebookLM para transcripción a `.md` con LaTeX.
3. Como efecto secundario de la transcripción, Claude puede leer los apuntes vía GitHub para ayudar con la materia.
4. Posible enriquecimiento futuro con PDF++(Obs) — recortes de imagen hacia notas `photon`.
5. El PDF es formato universal — se puede abrir sin Samsung Notes instalado, aunque se pierda la edición.
6. Existe un modo de edición en sitio (PDF reader) que evitaría reexportar manualmente — pendiente de validar su fiabilidad.
7. No cambia el hábito de captura del usuario (años usando la tablet para apuntes).

**Contras:**

1. La plantilla queda fija al exportar — solo páginas nuevas agregadas después permiten elegir plantilla.
2. El modo de edición en sitio tiene un bug de guardado documentado — no confiar en él sin probarlo primero.
3. Riesgo real (no hipotético) de ruptura de compatibilidad en actualizaciones de Samsung Notes — mitigado manteniendo el `.sdocx` como fuente de verdad.
4. El contenido manuscrito no es buscable en el PDF — la búsqueda real vive en la transcripción `.md`, no en el PDF.
5. Tamaño en almacenamiento del PDF+(Samsung) vs `.sdocx`: sin dato confirmado, pendiente de prueba empírica del usuario.
6. Comportamiento de Git ante un archivo binario en escritura/sobrescritura continua durante el semestre: sin resolver aún.

---

## Decisiones pendientes (bloquean pasar este sistema a `status: activo`)

| Pregunta abierta | Notas |
|---|---|
| ¿Se conserva el `.sdocx` en Samsung Cloud como respaldo permanente, o se borra tras exportar? | El borrado simplifica "una sola fuente de verdad" pero pierde la edición nativa real. Conservarlo es más seguro pero crea dos copias que pueden divergir si no se respeta la regla de "nunca editar el PDF directo". |
| ¿`tabnote` como `galaxy_body` nuevo, o extender `asteroid` con `source_type: pdf-apunte-propio`? | Este documento usa `tabnote` como propuesta — falta decidir si se integra al registro de tipos en [[_galaxy-system]]. |
| Validar empíricamente el modo "PDF reader" de edición en sitio | Probar con un apunte de bajo riesgo: editar, guardar, reabrir en otro visor, confirmar que el contenido no se pierde. |
| Medir diferencia de tamaño real `.sdocx` vs PDF+(Samsung) | Exportar un apunte real con plantilla propia y comparar tamaños. |
| Guía de formato de apuntes para NotebookLM | Qué estructura (¿Cornell? ¿headers claros? ¿prompt de configuración en NotebookLM?) mejora la transcripción. Pendiente, documentar en [[_notebooklm-system]]. |
| Comportamiento de Git con el archivo en sobrescritura continua | Decidir si conviene algún tipo de Git LFS, o si el repo simplemente acepta el peso del historial binario mientras `_tabnotes/` esté en `.gitignore` (no debería pesar si nunca se sube — confirmar que `.gitignore` cubre esto desde el inicio del repo). |

---

## Registro de decisiones de diseño (ya cerradas)

| Decisión | Razón |
|---|---|
| `_tabnotes/` separado de `_pdf/` | `_pdf/` es para fuentes externas (libros, slides del profesor); `_tabnotes/` es producción propia. Mezclarlos rompe la distinción semántica que ya usa el resto del sistema (asteroid = fuente externa). |
| Edición siempre en el `.sdocx`, nunca en el PDF exportado | El PDF+(Samsung) editable solo funciona dentro del ecosistema Samsung y tiene bugs de guardado conocidos. Mantener la fuente de edición en la app reduce el riesgo de pérdida de contenido. |
| Un solo archivo por tema, sobrescrito, sin numeración de versión en el nombre | Refleja el flujo real del usuario (tema en escritura continua hasta cerrar parcial) y delega el versionado real al historial de Git. |
| `_tabnotes/` excluido de GitHub vía `.gitignore` | Mismo problema ya vivido con PDFs de libros en `_pdf/` — binarios pesados rompen la sincronización de Git. |
| Transcripción `.md` (NotebookLM) como lo único que llega a GitHub | Es lo único realmente buscable e indexable, y es lo que necesita Claude para ayudar con la materia vía conectores. |
| Nomenclatura PDF+(Samsung) vs PDF++(Obs) | Evitar confusión entre dos herramientas con nombres casi idénticos pero de naturaleza totalmente distinta (export con anotación vs plugin lector de Obsidian). |

%%
galaxy-links
[[_galaxy-system]]
[[_note-system]]
[[_pdf-system]]
[[_template-system]]
[[_notebooklm-system]]
[[_ToDo-system]]
%%
