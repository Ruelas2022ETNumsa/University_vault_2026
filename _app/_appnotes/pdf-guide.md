# Guía de Plugins PDF — University Vault 2026

> **Sistema base:** [[_pdf_pp-system]]
> **Nivel:** Principiante — Tutorial paso a paso
> **Plugins cubiertos:** PDF++, Annotator, OmniSearch + Text Extractor
> **Última actualización:** 2026-05-27

---

## ¿Qué hace cada plugin y cuándo usarlo?

Antes de empezar a usar los plugins, es importante entender su rol dentro del sistema PDF del vault. No son intercambiables — cada uno tiene un dominio específico.

| Plugin | Rol principal | Cuándo usarlo |
|--------|--------------|---------------|
| **PDF++** | Lector y citador nativo | PDFs con texto seleccionable (slides, apuntes, libros digitales) |
| **Annotator** | Lector estilo Hypothesis | EPUBs y PDFs escaneados sin texto seleccionable |
| **OmniSearch** | Motor de búsqueda del vault | Encontrar cualquier contenido: notas, PDFs, ejercicios |

> **Regla de oro:** El 90% del tiempo usarás PDF++. Annotator es el plan B para archivos que PDF++ no puede leer. OmniSearch es la forma de encontrar todo.

---

## Parte 1 — PDF++

### ¿Qué es PDF++?

PDF++ reemplaza el lector de PDFs nativo de Obsidian. Cuando abres un `.pdf` dentro del vault, PDF++ lo muestra con su propio visor mejorado. Su superpoder es el sistema de citas: seleccionas texto en el PDF, presionas un atajo, y obtienes un bloque de cita ya formateado con el link exacto a esa página — listo para pegar en tu nota `asteroid`.

---

### Paso 1 — Abrir un PDF con PDF++

1. En el panel lateral izquierdo de Obsidian, navega hasta la carpeta `_PDF/`.
2. Haz clic en cualquier archivo `.pdf`.
3. El PDF se abre en el panel principal con el visor de PDF++.
4. Verás el PDF a la izquierda y un panel de miniaturas opcional a la derecha.

> **Tip:** También puedes abrir el PDF desde el link `pdf_file` en el YAML de tu nota `asteroid`. Haz clic sosteniendo `Ctrl` (Windows) sobre el link `[[ETN806-T01-apuntes-pdf-conjunta.pdf]]` y se abre directamente en PDF++.

---

### Paso 2 — Navegar dentro del PDF

| Acción | Cómo hacerlo |
|--------|--------------|
| Ir a una página específica | Escribe el número en el cuadro de página (parte superior) |
| Zoom | `Ctrl + Scroll` con el mouse |
| Buscar texto dentro del PDF | `Ctrl + F` — abre una barra de búsqueda interna |
| Ir a la siguiente página | `Flecha derecha` o `Page Down` |

---

### Paso 3 — Seleccionar texto y copiar una cita

Este es el flujo principal de PDF++. Cuando encuentras un fragmento importante:

1. **Selecciona el texto** con el mouse (clic y arrastra), igual que en cualquier documento.
2. Aparece un pequeño menú flotante sobre la selección.
3. Haz clic en el botón **"Copy as quote"** (o usa el atajo configurado).
4. PDF++ copia automáticamente al portapapeles un bloque con este formato:

```markdown
> [!PDF] [[ETN806-T01-apuntes-pdf-conjunta.pdf#page=12&selection=...|(ETN806-T01-apuntes-pdf-conjunta, p.12)]]
> El texto que seleccionaste aparece aquí tal como estaba en el PDF.
```

5. **Ve a tu nota `asteroid`** correspondiente y pega (`Ctrl + V`).

> **¿Qué es ese bloque?** Es un callout `[!PDF]` — un bloque de cita especial de Obsidian. El link dentro lleva exactamente a la página del PDF donde está el fragmento. Si alguien hace clic en ese link, el PDF se abre justo en esa página.

---

### Paso 4 — Crear un highlight (marcado permanente)

PDF++ puede guardar highlights directamente en el PDF:

1. Selecciona el texto que quieres marcar.
2. En el menú flotante, elige un color de highlight (amarillo, verde, azul, etc.).
3. El texto queda marcado en el PDF de forma permanente.
4. **Doble clic sobre el highlight** en el PDF → abre directamente la nota `asteroid` que contiene la cita de ese fragmento.

> **Importante:** Los highlights solo funcionan en PDFs con texto seleccionable. En PDFs escaneados (imágenes), PDF++ no puede marcar — para eso usarás Annotator.

---

### Paso 5 — Flujo completo de ejemplo con PDF++

**Situación:** Tienes el PDF `ETN806-T01-apuntes-pdf-conjunta.pdf` en `_PDF/ETN806/` y quieres extraer la definición de densidad conjunta.

```
1. Abres el PDF desde la carpeta _PDF/ETN806/
        ↓
2. Navegas a la página 8 donde está la definición
        ↓
3. Seleccionas el texto de la definición
        ↓
4. Clic en "Copy as quote" en el menú flotante
        ↓
5. Abres tu nota asteroid: ETN806-T01-apuntes-pdf-conjunta.md
        ↓
6. En la sección "## Notas del capítulo", pegas el bloque copiado:

> [!PDF] [[ETN806-T01-apuntes-pdf-conjunta.pdf#page=8&selection=...|(ETN806-T01, p.8)]]
> La densidad conjunta f(x,y) se define como la función tal que su integral
> doble sobre cualquier región R da la probabilidad de que (X,Y) caiga en R.

        ↓
7. Debajo del callout, escribes tu propia explicación:
   - Conectas con [[ETN806-T01-joint-pdf-definition]] (wikilink al planet)
   - Agregas tu interpretación en español
```

---

### Referencia rápida PDF++

```
Abrir PDF               → Clic en el archivo .pdf en el panel lateral
Seleccionar texto        → Clic y arrastra con el mouse
Copiar como cita         → Menú flotante → "Copy as quote"
Crear highlight          → Menú flotante → elige color
Buscar en el PDF         → Ctrl + F
Ir a página              → Cuadro de número de página (arriba)
Desde highlight → nota   → Doble clic en el highlight
```

---

### Configuración de PDF++ relevante para el sistema

#### Formato de copia activo — Quote

El sistema Galaxy usa un único formato de copia. Los demás existen pero no se usan en el flujo diario.

| Formato | Cuándo usarlo |
|---------|--------------|
| **Quote** ← activo | Extraer citas a la nota `asteroid` — uso principal |
| Link | Referenciar una página dentro de una oración |
| Embed | Ver el PDF renderizado dentro de la nota — no recomendado en `asteroid` |
| Callout / Quote in callout | Solo si usas colores de highlight con significado semántico |

El formato Quote produce exactamente esto al copiar:

```markdown
> [!PDF] [[ETN806-T01-apuntes-pdf-conjunta.pdf#page=8|(ETN806-T01-apuntes-pdf-conjunta, p.8)]]
> El texto seleccionado aparece aquí.
```

#### Display text — Title & page

Controla el texto que aparece después del `|` en el wikilink. La opción activa **Title & page** produce `ETN806-T01-apuntes-pdf-conjunta, p.8` — identifica archivo y página de un vistazo. No es necesario cambiarlo.

#### Toggles del ribbon (menú izquierdo)

Tres botones que se activan y desactivan según el momento de trabajo:

| Toggle | Qué hace | Cuándo activarlo |
|--------|----------|-----------------|
| **Auto-copy** | Copia el link automáticamente al seleccionar texto | Sesión de extracción rápida |
| **Auto-paste** | Pega automáticamente en la nota activa | En combinación con auto-copy |
| **Auto-focus** | Salta el cursor a la nota en cuanto copias | Cuando tienes PDF y nota en paneles lado a lado |

Para el flujo normal (PDF a la izquierda, nota `asteroid` a la derecha), activar **auto-focus** elimina el clic extra entre cada cita. Los tres están desactivados por defecto — úsalos en sesiones intensivas de extracción y desactívalos después.

#### PDF editing — mantener desactivado

La opción `Enable PDF editing` permite modificar el archivo `.pdf` en disco. **No activar** para el flujo Galaxy: las citas y highlights viven en las notas `asteroid`, no en el PDF físico. Activarla solo si en algún momento necesitas dividir un PDF y que los links del vault se actualicen automáticamente — y solo con backup previo de `_PDF/`.

---

## Parte 2 — Annotator

### ¿Qué es Annotator?

Annotator convierte una nota markdown en un lector de PDF o EPUB con sistema de anotaciones estilo Hypothesis (la plataforma de anotación web académica). En lugar de abrir el PDF directamente, abres la nota `asteroid` que lo referencia — y Annotator muestra el PDF con un panel lateral de comentarios.

**Úsalo cuando:**
- El PDF está escaneado (son imágenes, no texto) y PDF++ no puede seleccionar nada.
- Trabajas con archivos `.epub` (libros digitales) — Annotator es el único plugin que los lee.
- Prefieres escribir comentarios largos junto al fragmento en lugar de solo copiar texto.

---

### Paso 1 — Activar Annotator en una nota

Annotator se activa nota por nota con un campo especial en el YAML:

1. Abre (o crea) la nota `asteroid` del PDF que quieres anotar.
2. En el bloque YAML (entre los `---`), agrega el campo:

```yaml
---
title: "Apuntes ETN806 — PDF Conjunta"
galaxy_body: asteroid
subject: ETN806
annotation-target: _PDF/ETN806/ETN806-T01-apuntes-pdf-conjunta.pdf
---
```

3. **Guarda la nota** (`Ctrl + S`).
4. En la esquina superior derecha del panel de la nota, aparece un ícono de Annotator (una hoja con marcas).
5. Haz clic en ese ícono — la nota cambia a modo lector y muestra el PDF con el panel de anotaciones.

> **Para EPUBs:** Mismo proceso, solo cambia la extensión:
> `annotation-target: _PDF/ETN806/ETN806-T00-libro-papoulis.epub`

---

### Paso 2 — Crear una anotación

Con el PDF visible en modo Annotator:

1. **Selecciona texto** en el PDF (igual que en un documento normal).
2. Aparece un pequeño menú con opciones.
3. Elige **"Annotate"** para crear un comentario, o **"Highlight"** para solo marcar.
4. Se abre un cuadro con dos pestañas:

| Pestaña | Qué hace | Cuándo usarla |
|---------|----------|---------------|
| **Annotations** | El comentario queda anclado al fragmento de texto seleccionado | Cuando el comentario aplica a un párrafo o frase específica |
| **Page Notes** | El comentario queda anclado a la página completa, sin texto específico | Cuando quieres resumir toda una página o conectarla con un wikilink (`ver [[ETN806-T02-bayes]]`) |

5. Escribe tu comentario y haz clic en **"Save"** — aparece en el panel lateral.

---

### Paso 3 — Ver todas las anotaciones de un PDF

En el panel lateral derecho (cuando estás en modo Annotator) verás una lista de todas las anotaciones del documento, ordenadas por página. Puedes hacer clic en cualquiera para saltar directamente a esa parte del PDF.

---

### Paso 4 — Volver al modo nota normal

Para salir del modo Annotator y volver a editar el markdown:

- Haz clic en el mismo ícono de Annotator en la esquina superior derecha.
- La nota vuelve a mostrarse como markdown editable.
- Las anotaciones que hiciste en Annotator quedan guardadas y aparecen en el cuerpo de la nota como bloques especiales.

---

### Flujo de ejemplo con Annotator

**Situación:** Tienes un PDF escaneado de apuntes escritos a mano del profesor (`ETN302-T05-laplace-apuntes.pdf`). PDF++ no puede seleccionar texto porque son imágenes.

```
1. Creas la nota asteroid: ETN302-T05-laplace-apuntes.md

   YAML de la nota:
   ---
   title: "Apuntes Laplace — Manuscritos Profesor"
   galaxy_body: asteroid
   subject: ETN302
   annotation-target: _PDF/ETN302/ETN302-T05-laplace-apuntes.pdf
   ---

        ↓
2. Guardas la nota y haces clic en el ícono de Annotator
        ↓
3. El PDF se muestra en modo lector
        ↓
4. Seleccionas una región del PDF (aunque sea imagen)
        ↓
5. Escribes tu comentario en Annotations:
   "El profe usa convención de signo positivo en el
   denominador — diferente al libro Papoulis, ver [[ETN302-T05-laplace-def]]"
        ↓
   O usas Page Notes para resumir toda la página:
   "Páginas 3-4: desarrollo completo de la transformada unilateral,
   ver [[ETN302-T05-laplace-unilateral]]"
        ↓
6. Guardas la anotación
        ↓
7. Vuelves al modo nota para agregar wikilinks adicionales
```

---

### Referencia rápida Annotator

```
Activar en una nota    → Agregar "annotation-target: ruta/archivo.pdf" en YAML
Entrar modo lector     → Ícono Annotator (esquina superior derecha de la nota)
Crear anotación        → Seleccionar texto → "Annotate" → pestaña Annotations → Save
Page Note              → Seleccionar texto → "Annotate" → pestaña Page Notes → Save
Solo highlight         → Seleccionar texto → "Highlight"
Ver todas anotaciones  → Panel lateral derecho en modo Annotator
Salir modo lector      → Mismo ícono Annotator
```

---

## Parte 3 — OmniSearch + Text Extractor

### ¿Qué es OmniSearch?

OmniSearch es el motor de búsqueda del vault. La búsqueda nativa de Obsidian (`Ctrl + Shift + F`) solo encuentra texto en notas markdown. OmniSearch va más lejos: busca dentro del contenido de PDFs, imágenes (con OCR), y cualquier archivo del vault.

**Text Extractor** es el plugin compañero que hace posible la búsqueda dentro de PDFs. Sin él, OmniSearch solo encontraría el nombre del archivo, no su contenido. Ambos deben estar instalados y activos.

---

### Paso 1 — Abrir OmniSearch

| Método | Atajo / Acción |
|--------|---------------|
| Atajo de teclado | `Ctrl + Shift + O` (configurable) |
| Paleta de comandos | `Ctrl + P` → escribir "OmniSearch" → Enter |
| Panel lateral | Si está anclado, clic en el ícono de lupa |

Se abre una barra de búsqueda flotante sobre el vault.

---

### Paso 2 — Hacer una búsqueda básica

1. Escribe el término que buscas — por ejemplo: `densidad conjunta`.
2. OmniSearch muestra resultados en tiempo real mientras escribes.
3. Los resultados incluyen:
   - Notas markdown que contienen ese texto.
   - PDFs cuyo contenido contiene ese texto (gracias a Text Extractor).
   - El fragmento de contexto donde aparece el término.
4. Haz clic en un resultado para abrir la nota o el PDF directamente.

> **Nota sobre velocidad:** La primera vez que indexa el vault puede tardar unos minutos. Una vez completado el índice, las búsquedas son instantáneas.

---

### Paso 3 — Búsquedas avanzadas

OmniSearch soporta algunos operadores útiles:

| Operador | Ejemplo | Resultado |
|----------|---------|-----------|
| Comillas (frase exacta) | `"transformada de Laplace"` | Solo resultados con esa frase exacta |
| Múltiples términos | `laplace ETN302` | Resultados que contienen ambos términos |
| Nombre de archivo | `ETN806-T01` | Encuentra archivos que empiecen con ese código |

---

### Paso 4 — Interpretar los resultados

Los resultados de OmniSearch muestran:
- **Nombre del archivo** — con su ruta en el vault.
- **Fragmento de contexto** — el párrafo donde aparece el término buscado.
- **Relevancia** — los resultados más relevantes aparecen primero.

Las carpetas `_app`, `_templates` y `_assets` están configuradas como "downranked" — aparecen al final de los resultados para no contaminar las búsquedas con infraestructura del vault.

---

### Flujo de ejemplo con OmniSearch

**Situación:** Estudiando para parcial de ETN806, quieres encontrar todo lo relacionado con "marginal" en el vault — notas, PDFs, ejercicios.

```
1. Presionas Ctrl + Shift + O para abrir OmniSearch
        ↓
2. Escribes: marginal ETN806
        ↓
3. Aparecen resultados:
   - ETN806-T01-marginal-density-formula.md (tu nota planet)
   - ETN806-T01-apuntes-pdf-conjunta.pdf (el PDF con la sección de marginales)
   - ETN806-T02-ejercicio-marginal-gaussiana.md (un comet con ejercicio)
        ↓
4. Haces clic en el PDF → se abre en PDF++ en la sección donde aparece "marginal"
        ↓
5. Encuentras el fragmento exacto y lo citas en tu nota de repaso
```

---

### Referencia rápida OmniSearch

```
Abrir búsqueda         → Ctrl + Shift + O
Frase exacta           → "escribe entre comillas"
Múltiples términos     → término1 término2
Abrir resultado        → Clic en el resultado
Buscar en PDF          → Funciona automáticamente (requiere Text Extractor activo)
```

---

## Parte 4 — Flujo de Trabajo Integrado

Este es el flujo completo que une los tres plugins. Úsalo como referencia cuando incorpores un nuevo PDF al vault.

---

### Flujo completo: de PDF nuevo a nodo del cerebro

```
┌─────────────────────────────────────────────────────────┐
│  INICIO: Consigues un PDF (apunte, libro, práctica)     │
└─────────────────────┬───────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────────────┐
│  PASO 1 — Renombrar con convención Galaxy               │
│  ETN806-T01-apuntes-pdf-conjunta.pdf                    │
│  (SIGLA-TNN-nombre-descriptivo.pdf)                     │
└─────────────────────┬───────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────────────┐
│  PASO 2 — Mover el PDF a _PDF/ETN806/                   │
│  OmniSearch lo indexará automáticamente                 │
└─────────────────────┬───────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────────────┐
│  PASO 3 — Crear la nota asteroid en Semesters/          │
│  Con el YAML completo incluyendo pdf_file               │
└─────────────────────┬───────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────────────┐
│  PASO 4 — ¿El PDF tiene texto seleccionable?            │
│                                                         │
│  SÍ (apuntes digitales, slides, libro digital)          │
│  → Usar PDF++ para extraer citas                        │
│                                                         │
│  NO (escaneado, manuscrito) o es EPUB                   │
│  → Usar Annotator (agregar annotation-target al YAML)   │
└─────────────────────┬───────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────────────┐
│  PASO 5 — Extraer el contenido importante               │
│                                                         │
│  Con PDF++:                                             │
│  Seleccionar → Copy as quote → Pegar en nota asteroid   │
│                                                         │
│  Con Annotator:                                         │
│  Activar modo lector → Seleccionar → Annotate → Save    │
│  (Annotations para fragmentos, Page Notes para páginas) │
└─────────────────────┬───────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────────────┐
│  PASO 6 — Conectar al grafo Galaxy                      │
│  Agregar wikilinks a planets y stars relacionados       │
│  en el bloque %% de la nota asteroid                    │
└─────────────────────┬───────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────────────┐
│  RESULTADO: El PDF es un nodo activo del cerebro        │
│  Buscable con OmniSearch, citado con PDF++,             │
│  conectado al grafo Galaxy                              │
└─────────────────────────────────────────────────────────┘
```

---

### Escenario de ejemplo — Parcial ETN806

**Situación:** Tienes 3 días para el parcial de ETN806. Quieres revisar todos los PDFs del tema de densidad conjunta y crear notas de repaso.

**Paso 1 — Encontrar todo el material disponible con OmniSearch**

```
Ctrl + Shift + O → escribir: densidad conjunta ETN806
```

Aparecen resultados: tus notas asteroid, los PDFs en `_PDF/ETN806/`, y cualquier ejercicio (comet) que mencione el tema. En 10 segundos tienes una vista completa de todo lo que hay en el vault sobre ese tema.

**Paso 2 — Revisar el PDF de slides con PDF++**

Haces clic en `ETN806-T01-apuntes-pdf-conjunta.pdf` desde los resultados de OmniSearch. Se abre en PDF++. Navegas por las páginas y seleccionas los conceptos clave que no tienes bien claros, copiando citas con "Copy as quote".

**Paso 3 — Revisar el apunte manuscrito con Annotator**

En la nota `asteroid` del apunte escaneado del profesor, activas Annotator. Anotas las partes que son diferentes al libro y agregas comentarios comparativos.

**Paso 4 — Crear nota de repaso del parcial**

Creas una nueva nota (o usas un `comet` de repaso) y pegas las citas de PDF++, con los wikilinks a los conceptos clave. OmniSearch encontrará también esta nota nueva inmediatamente.

---

## Parte 5 — Problemas Comunes

### OmniSearch no encuentra contenido dentro de PDFs

**Causa probable:** Text Extractor no está instalado o no está activo.

**Solución:**
1. Ve a `Configuración → Community Plugins`.
2. Busca "Text Extractor" en la lista de plugins instalados.
3. Activa el toggle si está desactivado.
4. Espera unos minutos para que reindexe el vault.

---

### PDF++ no puede seleccionar texto

**Causa probable:** El PDF está escaneado — las páginas son imágenes, no texto.

**Solución:** Usa Annotator en su lugar. Agrega `annotation-target` al YAML de la nota asteroid y trabaja desde el modo lector de Annotator.

---

### Annotator no aparece el ícono en la nota

**Causa probable:** Falta el campo `annotation-target` en el YAML, o el path es incorrecto.

**Verificación:**
```yaml
# Asegúrate de que el path sea relativo a la raíz del vault:
annotation-target: _PDF/ETN806/ETN806-T01-apuntes-pdf-conjunta.pdf

# NO uses rutas absolutas como:
annotation-target: E:/University_vault_2026/_PDF/ETN806/...
```

---

### Los highlights de PDF++ desaparecieron

**Causa probable:** El PDF original fue reemplazado por una versión nueva descargada.

**Prevención:** Una vez que agregas un PDF al vault, no lo reemplaces. Si hay una versión actualizada, nómbrala diferente (agrega `-v2` al nombre) y crea una nueva nota asteroid para ella.

---

## Resumen — Tabla de decisión rápida

| Tienes este archivo... | Haz esto primero | Luego usa... |
|------------------------|-----------------|--------------|
| PDF con texto (slides, apuntes digitales) | OmniSearch para encontrarlo | PDF++ para citar |
| PDF escaneado (manuscrito, fotos) | Crear nota asteroid con annotation-target | Annotator para anotar |
| EPUB (libro digital) | Crear nota asteroid con annotation-target | Annotator para anotar |
| No recuerdas dónde guardaste algo | OmniSearch directamente | — |
| Quieres ver todos los PDFs de una materia | OmniSearch → escribir el código: `ETN806` | — |

---

## Convención de nombres — Recordatorio rápido

```
SIGLA  - TNN - nombre-descriptivo          .pdf
ETN806 - T01 - apuntes-pdf-conjunta        .pdf
ETN806 - T00 - libro-papoulis-cap6         .pdf
ETN302 - T05 - laplace-apuntes             .pdf

T00 = material general de la materia (libros, formularios)
T01, T02... = temas específicos
```

---

*Guía generada para University Vault 2026 — Sistema PDF Galaxy*
*Ver también: [[_pdf_pp-system]] · [[_galaxy-system]] · [[_note-system]]*

---

## Embeds de página y recortes rectangulares

> [!attention] Consideración activa
> Esta sección es base para el ship `pdfpp_embed_nblm.md` en `_hangar/dock/`.
> Ver secciones: **Planificación**, **Flujo de pasos**, y **Preguntas abiertas**.

### Embed de página completa

Muestra la página entera del PDF renderizada inline en la nota:

```
![[archivo.pdf#page=N]]
```

No requiere selección previa. Útil cuando la figura ocupa gran parte de la página o cuando no se conoce el rect exacto.

### Embed con recorte rectangular

Muestra solo una región de la página:

```
![[archivo.pdf#page=N&rect=x1,y1,x2,y2]]
```

El `rect` se obtiene seleccionando una región rectangular en PDF++ (Rectangular selection embed). Es preciso pero requiere selección manual en PDF++.

### Trim selection embed

Muestra la selección de texto y su contexto inmediato, no la página completa. Se activa en Settings → PDF++. Útil para citas largas que ocupan varias líneas.

### Workaround — embed no renderiza

Si el embed no renderiza correctamente, agregar `[` al inicio del bloque:

```
[![[archivo.pdf#page=N]]
```

### Cuándo usar cada uno

| Caso | Formato recomendado |
| --- | --- |
| Figura ocupa casi toda la página | `![[archivo.pdf#page=N]]` |
| Figura pequeña en página densa | `![[archivo.pdf#page=N&rect=...]]` |
| Cita de texto con contexto visual | Trim selection embed |
| Solo referencia sin render | Link: `[[archivo.pdf#page=N]]` |

---

%%
# galaxy-links

%%
