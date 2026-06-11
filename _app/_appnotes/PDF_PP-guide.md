---
title: "PDF++ — Guía de Opciones y Menú Contextual"
galaxy_body: beacon
scope: vault
audience: [usuario, claude]
related_notes:
  - "[[_pdf-system]]"
  - "[[pdf-guide]]"
  - "[[_sync-system]]"
tags: [beacon, pdf, pdf-plus, infraestructura]
date_created: 2026-06-09
date_updated: 2026-06-09
status: activo
---

# PDF++ — Guía de Opciones y Menú Contextual

> Guía complementaria: [[pdf-guide]]
> Sistema PDF: [[_pdf-system]]
> Sincronización tablet: [[_sync-system]]

---

## Resumen rápido — flujo de uso veloz

Para trabajar rápido sin pasar por el menú contextual cada vez, combina dos toggles:

1. **Ribbon de Obsidian → Toggle auto-copy** — si está activado, simplemente seleccionar texto con el puntero ejecuta automáticamente "Copy link to selection" (genera `&selection=...`, copia al portapapeles).

2. **Barra del visor PDF → botón "Add highlight to file"** — si este botón está activo **junto con** el auto-copy del ribbon, cada selección además queda resaltada y guardada físicamente en el PDF (`&annotation=...`). Se recomienda mantenerlo activo para que el subrayado sea visible también en la tablet (TAB_nexus).

### Tabla resumen — qué genera cada combinación

|                                                 | Botón izquierda (Ribbon)                            | botón tope pdf                                                     |
| ----------------------------------------------- | --------------------------------------------------- | ------------------------------------------------------------------ |
|                                                 | `&selection=...` (Copy link to selection)           | `&annotation=...` (Add highlight to file)                          |
| **¿Se guarda en el PDF físico?**                | No                                                  | Sí — visible en cualquier lector y en la tablet                    |
| **Ctrl + hover sobre el link en el PDF**        | Abre vista previa mostrando dónde está lo subrayado | No abre vista previa                                               |
| **Al pasar el cursor sobre el link en la nota** | Muestra lo subrayado de forma simple                | Muestra lo subrayado de forma llamativa (en recuadro, se nota más) |
| **Copia al portapapeles**                       | Sí                                                  | Sí                                                                 |
| **Recomendado para**                            | Referencias rápidas dentro de Obsidian              | Apuntes de TAB_nexus que se anotan y vuelven a la tablet           |

> Configuración recomendada para sesiones de vaciado: activar **Toggle auto-copy** (ribbon) + **Add highlight to file** (visor PDF) juntos — cada selección queda resaltada en el PDF y lista para pegar en la nota.

---

## El menú contextual — visión general

Cuando seleccionas texto en un PDF con PDF++, aparece un menú con dos grupos de opciones:

```
Click derecho sobre texto seleccionado
        ↓
┌─────────────────────────────┐
│ Copy link to selection  →   │  ← copia link + highlight de color
│ Add highlight to file   →   │  ← solo agrega highlight, sin copiar
│ Copy selected text           │  ← copia el texto plano sin link
│ Copy link to search          │  ← copia link de búsqueda
│ Customize menu...             │  ← configura qué opciones aparecen
└─────────────────────────────┘
```

Al elegir **Copy link to selection** o **Add highlight to file**, se abre un segundo submenú con el formato de copia, y luego un tercer submenú con el formato del texto de display.

---

## Nivel 1 — Opciones principales

### Copy link to selection → [color]

>Resaltado directamente en obsidian no se guarda en el pdf (no se ve en la tablet)

Hace dos cosas a la vez:
1. Agrega un highlight del color elegido al PDF (obsidian)
2. Copia al portapapeles el link/cita en el formato configurado

**Cómo lo usaríamos nosotros:** esta es la opción que usarás constantemente al construir notas `comet` (ejercicios resueltos) y `planet` (teoría) a partir de un `asteroid` (PDF de referencia). Seleccionas la definición o el paso de un ejercicio en el PDF, eliges el color, y pegas el resultado directo en la nota que estés construyendo en `Semesters/Sem_NN/ETNXXX/Partial_N/Topic_NN_nombre/`.

**Colores disponibles:** Sin color, Amarillo, Verde, Azul, Rosa, Morado

> **Sugerencia de sistema de colores para tus apuntes:**
> - Amarillo → definición importante (candidata a nota `planet`)
> - Verde → fórmula clave (candidata a nota `moon`)
> - Azul → ejemplo o ejercicio resuelto (candidata a nota `comet`)
> - Rosa → duda o revisar después (queda pendiente en `_ToDo-system`)

---

### Add highlight to file → [color]

>Resaltado directamente en el pdf se guarda en el (se ve en la tablet y obsidian) 

Agrega el highlight al PDF. Marca visualmente el fragmento y lo guarda en el pdf. Además también se lleva al portapapeles.

**Cómo lo usaríamos nosotros:** en una primera pasada de lectura del PDF (antes de empezar a crear notas galaxy), usas esto para marcar todo lo importante con el sistema de colores de arriba. Después, en una segunda pasada, usas "Copy link to selection" sobre lo ya marcado para ir creando las notas `planet`, `moon` y `comet` correspondientes.

---

### Copy selected text

Copia el texto plano sin ningún link ni formato de Obsidian. Equivale a `Ctrl+C` normal.

**Cómo lo usaríamos nosotros:** poco frecuente dentro del Sistema Galaxy — casi todo lo que extraigas de un PDF debería llevar su link de vuelta a la página (trazabilidad). Útil solo si vas a pegar el texto fuera del vault, por ejemplo para pedirle a Claude que te explique un fragmento sin necesidad de abrir el PDF.

---

### Copy link to search

Copia un link que al hacer clic abre OmniSearch buscando el texto seleccionado dentro del vault.

**Cómo lo usaríamos nosotros:** cuando estás leyendo un PDF y un término te suena familiar de otra materia o tema, usas esto para verificar si ya existe una nota `planet` sobre ese concepto antes de crear una duplicada. Encaja con la Fase 3 del `_ToDo-system` (conexiones entre galaxias / bridges).

---

### Customize menu...

Abre la configuración de PDF++ para elegir qué opciones aparecen en el menú y en qué orden.

**Cómo lo usaríamos nosotros:** una vez que definas tu sistema de colores y formato preferido (Quote + Title & page), puedes ocultar las opciones que no uses (Embed, Callout) para que el menú sea más corto y rápido de navegar durante sesiones largas de estudio.

---

## Nivel 2 — Formato de copia

Al elegir **Copy link to selection** o **Add highlight to file**, aparece el submenú de formato:

| Opción | Qué produce | Cuándo usarlo |
|--------|-------------|---------------|
| **Quote** | Bloque callout con el texto + link a la página | Extraer citas a tu nota — **uso principal** |
| **Link** | Solo el wikilink a la página, sin texto | Referenciar una página dentro de una oración |
| **Embed** | Renderiza el fragmento del PDF dentro de la nota | Ver el PDF inline — uso ocasional |
| **Callout** | Callout sin texto de cita | Cuando usas colores con significado semántico |
| **Quote in callout** | Cita dentro de un callout con color | Combinar cita + color semántico |

### Quote — el más usado

Produce esto al pegar en tu nota:

```markdown
> [!PDF] [[archivo.pdf#page=8&selection=...|(archivo, p.8)]]
> El texto que seleccionaste aparece aquí tal como estaba en el PDF.
```

**Cómo lo usaríamos nosotros:** este es el formato estándar para construir el cuerpo de notas `comet` y `planet`. La cita queda como evidencia/origen, y debajo de cada bloque Quote escribes tu propia explicación o desarrollo. Esto también alimenta la conexión `orbiting` hacia el `asteroid` (el PDF) en el YAML de la nota.

nota.- similar a callout , diferencia es mas simple respeta el color seleccionado

---

### Link — para referencias inline

Produce esto:

```markdown
[[archivo.pdf#page=8|(archivo, p.8)]]
```

**Cómo lo usaríamos nosotros:** dentro de una nota `planet` o `comet`, cuando mencionas "ver la demostración completa en..." sin necesidad de copiar el texto. También útil en notas `star` (MOC) para enlazar directo a la sección del PDF correspondiente a cada tema.

Ejemplo de uso en una oración:
```markdown
La densidad conjunta se define formalmente en [[ETN806-T01.pdf#page=8|(ETN806-T01, p.8)]].
```

---

### Embed — renderiza el PDF inline

Produce esto:

```markdown
![[archivo.pdf#page=8&selection=...]]
```

> ojo ... pdf no genera bien el embed basta con agregar un **"["** al inicio


**Cómo lo usaríamos nosotros:** uso ocasional — por ejemplo si una figura o diagrama del PDF es difícil de transcribir como texto y prefieres mostrarlo directo. Para uso frecuente, mejor recortar la imagen y guardarla como nota `photon` en `_assets/`, así la nota `planet` no queda pesada.

---

### Callout y Quote in callout

Versiones con color semántico, vinculadas al sistema de colores que definas.

**Cómo lo usaríamos nosotros:** si decides que el color del callout debe ser visible también en la nota (no solo en el PDF), por ejemplo para distinguir visualmente "definiciones" (amarillo) de "ejemplos" (azul) dentro de una misma nota `planet` larga.

nota.- Callout sirve mejor si no se especifica el color ya que se agrega un apartedo (`note`, `tip`, `warning`, `important`, etc. — los tipos nativos de Obsidian) y se copia el color de estos callouts.

---

## Nivel 3 — Formato del display text

Después de elegir el formato de copia, aparece el tercer submenú que controla el texto que aparece después del `|` en el wikilink:

| Opción | Ejemplo de resultado | Cuándo usarlo |
|--------|---------------------|---------------|
| **Title & page** | `ETN806-T01-apuntes, p.8` | **Recomendado siempre** |
| **Page** | `p.8` | Cuando el contexto ya deja claro de qué archivo es |
| **Text** | El texto seleccionado (truncado) | Cuando quieres que el link muestre el contenido |
| **Emoji** | 📄 p.8 | Visual, poco práctico para uso académico |
| **None** | Sin texto visible | No recomendado — rompe trazabilidad |

> **Recomendación fija para el Sistema Galaxy:** usa siempre **Title & page**. Con muchas notas `asteroid` (un PDF por tema/materia), saber de qué archivo y página viene cada cita es esencial para mantener la trazabilidad que pide el sistema.

---

## Auto-copy y Auto-focus — ribbon icons

Estos dos toggles viven en el ribbon (barra lateral izquierda de Obsidian) y cambian el comportamiento de PDF++ durante una sesión de trabajo.

### PDF++: Toggle auto-copy (se guarda en el pdf)

**Desactivado (normal):** Seleccionas texto → aparece el menú → eliges la opción → copia al portapapeles.

**Activado:** Seleccionas texto → se copia automáticamente al portapapeles en el formato configurado por defecto, **sin mostrar el menú**.

**Cómo lo usaríamos nosotros:** ideal para sesiones de "vaciado" — cuando ya leíste el PDF, marcaste todo con highlights, y ahora vas a transcribir rápido todo a una nota `comet` o `planet`. Configuras el formato por defecto a Quote + Title & page, activas auto-copy, y cada selección se copia lista para pegar.

> **Importante:** Cuando auto-copy está activo, el menú contextual no aparece — no puedes elegir color de highlight ni cambiar formato en ese momento. Desactívalo si necesitas variar.

---

### PDF++: Toggle auto-focus

**Desactivado (normal):** Copias la cita → tienes que hacer clic manualmente en la nota para posicionar el cursor y pegar.

**Activado:** Copias la cita → el cursor salta automáticamente a la nota que tengas abierta en el panel activo, lista para pegar con `Ctrl+V`.

**Cómo lo usaríamos nosotros:** trabajando en split view — PDF a la izquierda, nota `comet`/`planet` a la derecha. El flujo queda:

```
Seleccionas texto en PDF
        ↓
Auto-copy copia la cita (Quote + Title & page)
        ↓
Auto-focus salta el cursor a la nota
        ↓
Ctrl+V pega la cita
        ↓
Escribes tu explicación debajo del bloque Quote
        ↓
Clic de vuelta en el PDF para seguir leyendo
```

---

### Combinación recomendada para sesiones de estudio

| Escenario | Auto-copy | Auto-focus |
|-----------|-----------|------------|
| Sesión de vaciado/transcripción (muchas citas seguidas) | ✅ ON | ✅ ON |
| Primera lectura — solo marcar con colores | ❌ OFF | ❌ OFF |
| Solo armando referencias inline (Link) | ❌ OFF | ✅ ON opcional |
| Uso normal / mixto | ❌ OFF | ❌ OFF |

> Recuerda desactivar ambos al terminar la sesión de vaciado — si quedan activos durante lectura normal, pueden generar citas no deseadas con cada selección accidental.

---

## Habilitar edición en PDF++

La opción **Enable PDF editing** (en el ribbon o en Settings → PDF++) permite modificar el archivo `.pdf` físico en disco.

**Con edición desactivada:** los highlights y anotaciones se guardan en un archivo `.json` separado al lado del PDF. No son visibles en otros lectores (Adobe, navegador, tablet).

**Con edición activada:** los highlights se graban directamente dentro del PDF. Son visibles en cualquier lector.

**Cómo lo usaríamos nosotros:** activa la edición específicamente para los PDFs que vienen de `_pdf/TAB_nexus/` (apuntes manuscritos de la tablet). Así, cuando subrayas o anotas en PDF++, esas marcas viajan de vuelta a la tablet vía el flujo bidireccional. Para PDFs de referencia/libros (`asteroid` permanentes), puede no importar tanto ya que esas citas terminan transcritas en notas `.md`.

---

## Flatten — quemar anotaciones al PDF

Si las anotaciones están guardadas en `.json` (edición desactivada) y quieres exportar el PDF con las marcas visibles permanentemente, necesitas "quemar" o aplanar las anotaciones.

En PDF++ busca **Flatten annotations** o **Export with annotations** en el menú del PDF.

**Cómo lo usaríamos nosotros:** poco frecuente si trabajas con edición habilitada desde el inicio (las marcas ya están en el PDF). Útil solo para PDFs antiguos donde las anotaciones quedaron en `.json` y ahora quieres consolidarlas en el archivo antes de archivar el PDF.

> **Nota:** El flatten es irreversible — guarda una copia del PDF original antes si lo necesitas.

---

## Flujo TAB_nexus + PDF++

```
Tablet exporta apunte manuscrito como PDF
        ↓
Autosync sube a Drive → llega a _pdf/TAB_nexus/ en vault (symlink)
        ↓
Abres el PDF en PDF++ con edición habilitada
        ↓
Subrayas y anotas (se graba en el PDF físico)
        ↓
File Stream detecta cambio → sube versión anotada a Drive
        ↓
Autosync bidireccional → PDF anotado baja a la tablet
        ↓
En la tablet ves el PDF con los subrayados de PDF++
```

> Configuración completa del flujo de sincronización en [[_sync-system]]

---

## Selection vs Annotation — comportamiento verificado

Aclaración práctica probada por el usuario sobre la diferencia real entre **Copy link to selection** y **Add highlight to file**:

**Copy link to selection** → genera `&selection=...`
- En el PDF: con `Ctrl` + hover sobre el link, se abre una vista previa mostrando dónde está lo subrayado
- En la nota: al pasar el cursor sobre el link, muestra lo subrayado de forma simple
- Ambos copian al portapapeles, pero el resaltado es principalmente visible/útil **dentro de Obsidian**

**Add highlight to file** → genera `&annotation=...`
- En el PDF: `Ctrl` + hover **no** abre vista previa
- En la nota: al pasar el cursor sobre el link, muestra lo subrayado de forma más llamativa (lo encierra en un recuadro, se nota más)
- Ambos copian al portapapeles, pero la diferencia clave es que **Add highlight to file subraya físicamente el PDF** — y por eso es lo que se ve también en la tablet vía TAB_nexus

> En resumen: si quieres que el subrayado viaje al PDF (y por tanto a la tablet), usa **Add highlight to file**. Si solo quieres una referencia visual dentro de Obsidian, **Copy link to selection** es suficiente.

---

## Annotation author

En **Settings → PDF++ → Annotation author** se configura el nombre que aparece como autor de las anotaciones. Es solo texto plano — no acepta variables como `{{date}}` o `{{time}}` (esas son propias del formato de Annotator, no de PDF++).

**Configuración actual:** `Ruelas`

---

## Referencia rápida — menú completo

```
Seleccionar texto → click derecho
│
├── Copy link to selection → [color] → [formato] → [display]
│       Agrega highlight + copia al portapapeles
│
├── Add highlight to file → [color]
│       Solo agrega highlight, no copia nada
│
├── Copy selected text
│       Texto plano sin link
│
├── Copy link to search
│       Link para buscar en OmniSearch
│
└── Customize menu...
        Configura qué opciones aparecen

Formatos: Quote · Link · Embed · Callout · Quote in callout
Display:  Title & page · Page · Text · Emoji · None

Ribbon:
├── Toggle auto-copy  → copia automático sin menú
└── Toggle auto-focus → cursor salta a la nota activa
```

---

%%
galaxy-links
[[_pdf-system]]
[[pdf-guide]]
[[_sync-system]]
[[_galaxy-system]]
%%
