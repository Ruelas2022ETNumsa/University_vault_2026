# Guía de Plugins PDF — University Vault 2026

> Sistema base: [[_galaxy-system]]
> Configuración del sistema: [[_pdf-system]]
> Última actualización: 2026-05-27

Esta guía es el manual de uso de los tres plugins que forman el sistema PDF del vault. Está escrita para alguien que nunca los ha usado. Sigue el orden: primero entiende qué hace cada plugin, luego el flujo integrado al final.

---

## Índice

1. [[#Plugin 1 — PDF++]]
2. [[#Plugin 2 — Annotator]]
3. [[#Plugin 3 — OmniSearch + Text Extractor]]
4. [[#Flujo de trabajo integrado]]
5. [[#Referencia rápida de atajos]]
6. [[#Errores comunes]]

---

## Plugin 1 — PDF++

### ¿Qué hace?

PDF++ reemplaza el lector de PDF nativo de Obsidian. Su función principal no es solo leer, sino **copiar citas con link a la página exacta** para pegarlas en tus notas `asteroid`. Es el plugin más importante del sistema PDF.

Cuando seleccionas texto en un PDF y copias con PDF++, obtienes esto en tu nota:

```markdown
> [!PDF] [[ETN806-T00-libro-papoulis-cap6.pdf#page=142&selection=...|(Papoulis, p.142)]]
> La densidad conjunta f(x,y) queda definida sobre la región de soporte donde la integral doble normaliza a 1.
```

Ese bloque es un callout `[!PDF]` con un link que apunta a la página 142 del PDF. Si haces doble click sobre el subrayado en el PDF, Obsidian te lleva a la nota donde pegaste la cita.

---

### Paso a paso: abrir un PDF con PDF++

1. En el panel izquierdo de Obsidian, navega a `_pdf/ETNXXX/`
2. Haz click sobre el archivo `.pdf` — PDF++ lo abre automáticamente
3. El PDF se muestra en el panel derecho o central según tu layout
4. Para dividir la pantalla: arrastra el tab del PDF hacia la derecha para tener nota + PDF lado a lado

> **Consejo:** El layout ideal es nota `asteroid` a la izquierda y el PDF a la derecha. Así copias y pegas sin cambiar de ventana.

---

### Paso a paso: copiar una cita

1. Abre el PDF con PDF++ (ver arriba)
2. Selecciona el texto que quieres citar con el cursor
3. Aparece un menú flotante — haz click en el ícono de copia o presiona el atajo configurado
4. Ve a tu nota `asteroid` y pega con `Ctrl + V`
5. El callout `[!PDF]` aparece con el link a la página exacta

**¿No aparece el menú flotante?** Verifica que estés usando PDF++ y no el lector nativo. El tab del PDF debe mostrar el ícono de PDF++ en la esquina.

---

### Paso a paso: resaltar texto en el PDF

1. Selecciona el texto
2. En el menú flotante elige el color del resaltado (amarillo, verde, azul, rojo)
3. El resaltado queda guardado en el PDF
4. Para ver todos los resaltados: panel lateral derecho → ícono de anotaciones

**Colores sugeridos para ingeniería:**
- 🟡 Amarillo → definiciones y conceptos clave
- 🟢 Verde → fórmulas y ecuaciones
- 🔵 Azul → ejemplos resueltos
- 🔴 Rojo → advertencias o errores comunes

---

### Paso a paso: navegar el PDF

| Acción | Cómo hacerlo |
|--------|--------------|
| Ir a una página específica | Click en el número de página en la barra superior → escribe el número |
| Zoom | `Ctrl + Scroll` o los botones `+` / `-` en la barra |
| Buscar texto dentro del PDF | `Ctrl + F` con el PDF enfocado |
| Ver índice/bookmarks | Panel lateral → ícono de lista (si el PDF tiene bookmarks) |
| Ir a la página desde un link | Click sobre cualquier callout `[!PDF]` en tus notas |

---

### Cuándo usar PDF++ (y cuándo NO)

**Usar PDF++:**
- PDFs con texto seleccionable: slides del profesor, apuntes digitales, libros en PDF, prácticas
- Cualquier PDF que puedas subrayar con el cursor — si puedes seleccionar el texto, PDF++ funciona

**NO usar PDF++ — usar Annotator en su lugar:**
- PDFs escaneados (imágenes de hojas escritas a mano)
- Archivos `.epub` (libros en formato EPUB)

---

## Plugin 2 — Annotator

### ¿Qué hace?

Annotator convierte una nota Obsidian en un lector de PDF o EPUB estilo Hypothesis. A diferencia de PDF++, **Annotator se activa por nota** — no es un lector global. Cada vez que quieras usar Annotator con un PDF, debes agregar un campo especial en el YAML de la nota.

Su ventaja principal: funciona con EPUBs y con PDFs escaneados donde PDF++ no puede seleccionar texto.

---

### Paso a paso: activar Annotator en una nota

1. Abre (o crea) la nota `asteroid` correspondiente al PDF
2. En el YAML de la nota, agrega el campo `annotation-target`:

```yaml
---
title: "Papoulis — Cap. 6"
galaxy_body: asteroid
subject: ETN806
annotation-target: _pdf/ETN806/ETN806-T00-libro-papoulis-cap6.pdf
---
```

3. Guarda la nota con `Ctrl + S`
4. En la esquina superior derecha del panel de la nota aparece un botón **"Annotate"** — haz click
5. La nota se transforma en el lector Annotator con el PDF cargado

> **Importante:** La ruta en `annotation-target` es relativa a la raíz del vault. Siempre empieza con `_pdf/ETNXXX/nombre-del-archivo.pdf` sin barras iniciales.

---

### Paso a paso: anotar en Annotator

1. Con Annotator activo, selecciona texto en el PDF
2. Aparece un menú con tres opciones:
   - **Highlight** → resaltado sin comentario
   - **Annotate** → resaltado con comentario de texto
   - **Comment** → comentario sin selección de texto
3. Escribe tu comentario y confirma
4. La anotación queda guardada **dentro de la nota** como bloques de markdown al final

**Ejemplo de anotación guardada automáticamente:**

```markdown
*[Annotation](https://via.hypothesis.is/...)*
**Highlight** — página 142
> La densidad conjunta f(x,y)...

Tu comentario: Esto es lo que usa el ejercicio 3 de la práctica 2.
```

---

### Paso a paso: alternar entre vista Annotator y vista normal

- Para volver a la nota markdown normal: botón **"More options" (···)** → **"Open as markdown"**
- Para volver a la vista Annotator: botón **"Annotate"** en la esquina superior derecha
- Obsidian recuerda la última vista usada por nota

---

### Cuándo usar Annotator

| Situación | ¿Usar Annotator? |
|-----------|-----------------|
| PDF con texto seleccionable | ❌ Usa PDF++ — más integrado con el grafo |
| PDF escaneado (imagen) | ✅ Sí — Annotator puede anotar sobre imágenes |
| Archivo EPUB | ✅ Sí — es la única opción del vault |
| Quiero comentarios largos tipo nota | ✅ Sí — Annotator tiene mejor UX para comentarios extensos |

---

## Plugin 3 — OmniSearch + Text Extractor

### ¿Qué hace?

OmniSearch es el motor de búsqueda del vault. Busca en **todo**: notas markdown, PDFs, y con Text Extractor activo, también en el contenido textual de los PDFs. Sin OmniSearch solo puedes buscar en los nombres de archivos. Con OmniSearch buscas dentro de un libro de 400 páginas.

Text Extractor es el plugin compañero que extrae el texto de los PDFs para que OmniSearch lo pueda indexar. Ambos deben estar activos.

---

### Paso a paso: hacer una búsqueda básica

1. Presiona `Ctrl + U` — se abre el panel de OmniSearch
2. Escribe tu consulta: puede ser una palabra, frase, o concepto
3. Los resultados aparecen ordenados por relevancia
4. Click sobre un resultado → Obsidian abre la nota o PDF en la página correspondiente

**Ejemplos de búsquedas útiles para ingeniería:**

```
densidad conjunta          → encuentra todas las notas y PDFs donde aparece ese término
transformada de Laplace     → busca en apuntes Y en los libros en _pdf/
ETN302 T05                 → filtra por materia y tema
fórmula de Bayes           → encuentra la definición y todos los ejercicios donde aparece
```

---

### Paso a paso: búsqueda avanzada con filtros

OmniSearch soporta algunos operadores de búsqueda:

| Operador | Ejemplo | Resultado |
|----------|---------|-----------|
| Comillas para frase exacta | `"función de densidad"` | Solo resultados con esa frase exacta |
| Nombre de archivo | `file:ETN806` | Solo archivos cuyo nombre contiene ETN806 |
| Excluir término | `-ejercicio` | Resultados que NO contienen "ejercicio" |

> **Nota:** Las carpetas `_app`, `_templates` y `_assets` están configuradas como "downranked" — aparecen al fondo de los resultados para no contaminar las búsquedas académicas.

---

### Paso a paso: forzar re-indexación de PDFs

Cuando agregas un nuevo PDF a `_pdf/`, OmniSearch lo indexa automáticamente en segundo plano. Si un PDF nuevo no aparece en búsquedas:

1. Abre la paleta de comandos: `Ctrl + P`
2. Escribe `OmniSearch` → selecciona **"OmniSearch: Clear cache and re-index"**
3. Espera unos segundos (el tiempo depende del tamaño del vault)
4. Busca de nuevo

---

### Cuándo OmniSearch no encuentra el contenido de un PDF

Si buscas texto que sabes que está en un PDF pero OmniSearch no lo encuentra, verifica:

1. **¿Está Text Extractor activo?** → `Configuración → Community plugins → Text Extractor` debe estar en ON
2. **¿El PDF tiene texto seleccionable?** → Abre el PDF con PDF++ e intenta seleccionar texto. Si no puedes, el PDF es una imagen escaneada y OmniSearch no puede indexar su contenido (solo indexa el nombre del archivo)
3. **¿Necesitas re-indexar?** → Usa el comando de clear cache descrito arriba

---

## Flujo de trabajo integrado

Este es el flujo completo para pasar de tener un PDF a tenerlo activo en el grafo del vault. Usa los tres plugins en secuencia.

---

### Escenario: recibes los apuntes del profesor en PDF

**Situación:** Tienes `apuntes-transformada-laplace.pdf` en tu carpeta de Descargas y quieres integrarlo al vault de ETN302, Tema 5.

---

#### Fase 1 — Ingreso al vault

**Paso 1: Renombrar el PDF con la convención Galaxy**

Antes de mover el archivo, renómbralo:
```
ETN302-T05-apuntes-laplace.pdf
```

**Paso 2: Mover a la carpeta correcta**

Copia el archivo a:
```
E:\University_vault_2026\_pdf\ETN302\ETN302-T05-apuntes-laplace.pdf
```

**Paso 3: Crear la nota `asteroid`**

En Obsidian, navega a la carpeta del tema:
```
Semesters/Sem_XX/ETN302/Partial_X/Topic_05_.../
```

Crea una nueva nota con el mismo nombre base:
```
ETN302-T05-apuntes-laplace.md
```

**Paso 4: Completar el YAML de la nota**

```yaml
---
title: "Apuntes Transformada de Laplace — ETN302"
galaxy_body: asteroid
subject: ETN302
semester: X
partial: X
topic: 5
source_type: pdf-apuntes
source_title: "Apuntes de clase — Transformada de Laplace"
source_author: "Profesor ETN302"
pdf_file: "[[ETN302-T05-apuntes-laplace.pdf]]"
related_planets: []
tags: [ETN302, galaxy-asteroid, pdf, T05]
date_created: 2026-05-27
status: en-proceso
---
```

---

#### Fase 2 — Lectura y extracción con PDF++

**Paso 5: Abrir el PDF en layout dividido**

1. En el panel de archivos, navega a `_pdf/ETN302/`
2. Click sobre `ETN302-T05-apuntes-laplace.pdf` — se abre en un tab
3. Arrastra el tab del PDF a la mitad derecha de la pantalla
4. La nota `asteroid` queda a la izquierda, el PDF a la derecha

**Paso 6: Leer y subrayar**

1. Lee el PDF con PDF++
2. Selecciona las definiciones clave → resalta en amarillo
3. Selecciona las fórmulas → resalta en verde
4. Selecciona ejemplos → resalta en azul

**Paso 7: Copiar citas a la nota**

1. Selecciona el texto de una definición importante
2. Click en el botón de copia del menú flotante de PDF++
3. En la nota `asteroid`, bajo el YAML, pega con `Ctrl + V`
4. Repite para cada cita relevante

La nota empieza a tomar esta forma:

```markdown
## Definiciones clave

> [!PDF] [[ETN302-T05-apuntes-laplace.pdf#page=3&selection=...|(Apuntes ETN302, p.3)]]
> La Transformada de Laplace de f(t) se define como la integral de f(t)·e^(-st) desde 0 hasta infinito.

## Fórmulas

> [!PDF] [[ETN302-T05-apuntes-laplace.pdf#page=7&selection=...|(Apuntes ETN302, p.7)]]
> Propiedad de desplazamiento en frecuencia: L{e^(at)·f(t)} = F(s-a)
```

**Paso 8: Agregar wikilinks al grafo**

Debajo de las citas, agrega conexiones con los planets y stars relevantes:

```markdown
## Conexiones al grafo

- Concepto central → [[ETN302-T05-definicion-laplace]]
- Propiedad usada en ejercicio → [[ETN302-T05-desplazamiento-frecuencia]]
- Ver también → [[ETN302-T03-serie-fourier]] (antecedente)
```

---

#### Fase 3 — Búsqueda posterior con OmniSearch

Una vez indexado el PDF, OmniSearch lo convierte en parte del cerebro.

**Paso 9: Usar OmniSearch para recuperar conocimiento**

Días después, cuando estés resolviendo un ejercicio y no recuerdes dónde está algo:

1. `Ctrl + U` → escribe `"transformada inversa"`
2. OmniSearch muestra la nota `asteroid` Y el PDF con el fragmento exacto
3. Click → vas directo a la página donde está el concepto

**Paso 10: Conectar búsqueda con nueva nota**

Si OmniSearch te lleva a un PDF y encuentras algo útil para una nueva nota:

1. Selecciona el texto en PDF++ (el PDF ya está abierto desde OmniSearch)
2. Copia la cita con PDF++
3. Pégala en la nueva nota

---

### Diagrama del flujo completo

```
PDF físico en Descargas
        ↓
Renombrar: ETN302-T05-apuntes-laplace.pdf
        ↓
Mover a: _pdf/ETN302/
        ↓
Crear nota asteroid con YAML + pdf_file
        ↓
        ├── PDF con texto seleccionable
        │       ↓
        │   Abrir con PDF++ en layout dividido
        │   Subrayar → Copiar citas → Pegar en asteroid
        │
        └── PDF escaneado o EPUB
                ↓
            Agregar annotation-target al YAML
            Abrir con Annotator → Anotar con comentarios
        ↓
Agregar wikilinks al grafo en la nota asteroid
        ↓
OmniSearch indexa el PDF automáticamente
        ↓
PDF activo en el cerebro — buscable y conectado al grafo
```

---

## Referencia rápida de atajos

| Acción | Atajo |
|--------|-------|
| Abrir OmniSearch | `Ctrl + U` |
| Copiar cita PDF++ | Seleccionar texto → menú flotante → botón copia |
| Buscar texto dentro de un PDF | `Ctrl + F` (con el PDF enfocado) |
| Paleta de comandos (para re-indexar) | `Ctrl + P` |
| Ir a una página desde un callout `[!PDF]` | Click sobre el link del callout |
| Alternar Annotator ↔ Markdown | Botón "Annotate" / "Open as markdown" en la esquina |
| Dividir panel (nota + PDF) | Arrastrar tab del PDF a la mitad derecha |

---

## Errores comunes

### "No puedo seleccionar texto en el PDF"

El PDF está escaneado — es una imagen, no texto. Usa Annotator en lugar de PDF++. Agrega `annotation-target` al YAML de la nota `asteroid`.

### "OmniSearch no encuentra el contenido del PDF"

Verifica que Text Extractor esté activo. Si lo está, fuerza re-indexación: `Ctrl + P` → "OmniSearch: Clear cache and re-index". Si el PDF es escaneado, OmniSearch no puede leer su contenido — solo indexa el nombre del archivo.

### "Annotator no aparece, solo veo el YAML"

El campo `annotation-target` debe estar en el YAML (entre los `---`), no en el cuerpo de la nota. La ruta debe ser relativa al vault sin barra inicial: `_pdf/ETN302/archivo.pdf`, no `/_pdf/ETN302/archivo.pdf`.

### "El callout [!PDF] no tiene link clickeable"

Verifica que PDF++ esté activo (no el lector nativo de Obsidian). El formato del callout debe ser exactamente `[!PDF]` con mayúsculas.

### "Abrí el PDF desde OmniSearch pero no veo PDF++"

OmniSearch abre el archivo — PDF++ se encarga de mostrarlo. Si ves el lector nativo, puede que PDF++ esté desactivado. Verifica en `Configuración → Community plugins`.

---

> **Siguiente paso:** Lee [[_pdf-system]] para entender la estructura completa del sistema y la convención de nombres antes de agregar tu primer PDF al vault.
