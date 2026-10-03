---
title: "update_claude_obsidian"
type: ideas
status: draft
created: 2026-10-02
scope: "Mejorar el flujo Claude (free) + MCP Filesystem + vault Obsidian"
---

# Ideas para mejorar el flujo Claude + Obsidian

> Contexto: plan free de Claude, MCP Filesystem y archivos `.md` como contexto ampliado.
> Cada punto tiene: **qué es**, **cómo se usa**, **para qué sirve**, **ventajas** y **desventajas**.
> Marcá con `[x]` lo que ya está implementado y con `[ ]` lo pendiente.

---

## 1. Memoria entre sesiones

### 1.1 Archivo de handoff (`_handoff.md`) `[ ]`
- **Qué es:** un resumen corto que Claude escribe al cerrar la sesión.
- **Cómo se usa:** al final se pide "resumí en `_handoff.md`" con: estado actual, decisiones tomadas, pendientes y próximo paso. La sesión nueva arranca leyendo solo ese archivo.
- **Para qué sirve:** continuar un trabajo sin recargar todo el historial.
- **Ventajas:** ahorra tokens, retoma rápido, es el patrón más útil en plan free.
- **Desventajas:** si el resumen es malo se pierde información; hay que mantenerlo corto y actualizado; depende de acordarse de cerrar la sesión a tiempo (antes del límite).

### 1.2 Log de decisiones (ADR corto) `[ ]`
- **Qué es:** un registro de una línea por decisión: `fecha | decisión | motivo | alternativa descartada`.
- **Cómo se usa:** se agrega una línea cada vez que se acuerda algo importante, en `_decisions.md` o dentro de cada proyecto.
- **Para qué sirve:** evitar rediscutir lo ya resuelto y recordar el porqué de cada elección.
- **Ventajas:** muy liviano, ideal para proyectos largos, Claude lo lee en segundos.
- **Desventajas:** crece con el tiempo (hay que archivar lo viejo); solo sirve si se registra con disciplina.

### 1.3 Changelog por proyecto `[ ]`
- **Qué es:** historial cronológico de qué se hizo en cada sesión.
- **Cómo se usa:** una entrada por sesión (`fecha | qué cambió | archivos tocados`).
- **Para qué sirve:** retomar proyectos después de semanas y auditar cambios.
- **Ventajas:** trazabilidad; complementa al handoff.
- **Desventajas:** duplica parte de la información del handoff si no se distinguen roles (handoff = estado actual, changelog = historia).

---

## 2. Contexto liviano (gastar menos tokens)

### 2.1 Índice o mapa del vault (`_index.md`) `[ ]`
- **Qué es:** un archivo con una línea por carpeta o nota importante (ruta + para qué sirve).
- **Cómo se usa:** Claude lee primero el índice y después abre solo lo que necesita.
- **Para qué sirve:** navegar el vault sin listar ni leer carpetas enteras.
- **Ventajas:** reduce lecturas innecesarias; da una visión global barata.
- **Desventajas:** se desactualiza si no se mantiene; Claude puede ayudar a regenerarlo periódicamente.

### 2.2 Frontmatter útil en cada nota `[ ]`
- **Qué es:** el bloque YAML al inicio de la nota con `status`, `tags`, `resumen`, `created`, etc.
- **Cómo se usa:** se define un contrato fijo (campos obligatorios) y se pide a Claude que lea solo las primeras líneas de cada nota.
- **Para qué sirve:** filtrar y decidir qué notas vale la pena abrir completas.
- **Ventajas:** compatible con Obsidian (Dataview, propiedades); permite consultas por estado o tema.
- **Desventajas:** exige consistencia; notas sin frontmatter quedan invisibles para el filtro.

### 2.3 Lectura por rangos `[x]` (ya aplicado en `_claude-plan`)
- **Qué es:** leer solo desde la línea 1 hasta una línea indicada, en vez del archivo completo.
- **Cómo se usa:** el usuario da ruta y línea final; Claude lee solo ese tramo.
- **Para qué sirve:** controlar cuánto contexto se consume.
- **Ventajas:** control total del gasto de tokens.
- **Desventajas:** el usuario debe saber dónde termina la parte relevante; puede cortar información importante.

### 2.4 Notas atómicas y resúmenes por nota larga `[ ]`
- **Qué es:** una idea por archivo; para notas largas, un archivo hermano `_resumen` de 5-10 líneas.
- **Cómo se usa:** Claude lee el resumen y solo baja al detalle si hace falta.
- **Para qué sirve:** cargar contexto preciso, no masivo.
- **Ventajas:** mejor enlazado en Obsidian, lecturas más baratas.
- **Desventajas:** más archivos que mantener; hay que sincronizar resumen y original.

### 2.5 Costo de las herramientas MCP `[ ]`
- **Qué es:** el servidor Filesystem genérico expone muchas herramientas, y cada definición consume contexto al cargarse.
- **Cómo se usa:** cargar solo las herramientas necesarias por sesión (ya lo hacés con skills por modo) y evitar listados grandes.
- **Para qué sirve:** dejar más espacio para trabajo real dentro del límite.
- **Ventajas:** más margen por sesión.
- **Desventajas:** menos flexibilidad si se necesita una herramienta no cargada a mitad de sesión.

---

## 3. Flujo de trabajo

### 3.1 Skills como "modos" `[x]` (ya implementado: work / plan / setup / boot)
- **Qué es:** archivos `.md` con instrucciones por tipo de tarea, cargados solo cuando se necesitan.
- **Cómo se usa:** `_start.md` carga el menú; el usuario elige un modo y Claude lee solo ese skill.
- **Para qué sirve:** que cada sesión tenga reglas claras sin gastar contexto en lo que no se usa.
- **Ventajas:** sesiones enfocadas, comportamiento predecible, menos tokens.
- **Desventajas:** mantener varios skills; riesgo de reglas contradictorias entre ellos.
- **Idea extra:** sumar un modo de **revisión semanal** (ver 3.4).

### 3.2 Inbox → procesar (`_inbox.md`) `[ ]`
- **Qué es:** un archivo donde se vuelca todo en crudo (ideas, apuntes, links).
- **Cómo se usa:** periódicamente Claude clasifica cada ítem, lo mueve a su carpeta y le agrega frontmatter.
- **Para qué sirve:** capturar rápido sin pensar en la organización.
- **Ventajas:** baja la fricción al anotar; Claude hace el trabajo tedioso.
- **Desventajas:** si se acumula demasiado, procesarlo consume una sesión entera; requiere revisar lo que Claude movió.

### 3.3 Plantillas con campos que Claude completa `[x]` (parcial: `tpl_worker`, `tpl_ship`, `tpl_carrier`)
- **Qué es:** estructuras fijas para tipos de nota repetidos (clase, paper, reunión, proyecto).
- **Cómo se usa:** el usuario aporta el contenido crudo y Claude lo vuelca en la plantilla.
- **Para qué sirve:** consistencia entre notas.
- **Ventajas:** uniformidad, más fácil de indexar y consultar.
- **Desventajas:** rigidez; las plantillas hay que actualizarlas cuando cambia el flujo.

### 3.4 Revisión periódica del vault `[ ]`
- **Qué es:** una pasada para detectar notas huérfanas, duplicadas, sin tags, con links rotos o con `status` vencido.
- **Cómo se usa:** modo "review" que lee índice y frontmatter (no el contenido completo) y devuelve una lista de problemas.
- **Para qué sirve:** que el segundo cerebro no se degrade con el tiempo.
- **Ventajas:** mantenimiento barato si se apoya en el frontmatter.
- **Desventajas:** en un vault grande no entra en una sola sesión; hay que revisar por carpetas.

### 3.5 Confirmar antes de escribir + backup `[x]` (ya aplicado)
- **Qué es:** la regla "avisar `cambios masivos, bk necesario` y esperar confirmación".
- **Para qué sirve:** evitar sobrescrituras accidentales.
- **Ventajas:** seguridad real sobre los archivos.
- **Desventajas:** agrega un paso manual (crear el bk).
- **Idea extra:** crear una carpeta `_bk/` y numerar versiones automáticamente.

---

## 4. Estudio (si el vault es universitario)

### 4.1 Quizzes y flashcards desde tus notas `[ ]`
- **Cómo se usa:** se le da una nota (o su resumen) y se pide preguntas con respuesta. Si ya usás Anki (`_hangar/anki`), se pueden generar en el formato de importación.
- **Ventajas:** estudio activo en vez de releer.
- **Desventajas:** hay que verificar que las respuestas sean correctas; depende de la calidad de la nota fuente.

### 4.2 Mapa de conexiones y huecos de conocimiento `[ ]`
- **Cómo se usa:** "¿qué notas se relacionan con X y qué falta cubrir?", apoyado en tags y enlaces.
- **Ventajas:** descubre vacíos antes de un examen.
- **Desventajas:** limitado a lo que Claude alcanza a leer en la sesión.

### 4.3 Resumen semanal `[ ]`
- **Cómo se usa:** Claude lee el changelog y las notas modificadas de la semana y arma un repaso.
- **Ventajas:** refuerza lo aprendido; sirve de handoff académico.
- **Desventajas:** requiere que changelog y frontmatter estén al día.

---

## 5. Trucos para el plan free

- Sesiones cortas con **un solo objetivo**.
- Cerrar con handoff **antes** de llegar al límite.
- Respuestas concisas en el chat; el detalle va al archivo.
- Evitar listar carpetas enormes; apoyarse en `_index.md`.
- Pedir siempre rutas exactas en vez de búsquedas amplias.

---

## 6. Repositorios para revisar a detalle

Todos giran en torno a "Obsidian como segundo cerebro de Claude". Ninguno se probó; son material de inspiración (probar siempre sobre una copia del vault).

| Repo | Qué aporta | Link |
|---|---|---|
| second-brain-starter | Vault mínimo pensado para Claude: mapa de carpetas con prefijos numéricos, contrato de frontmatter, `CLAUDE.md`, config MCP Filesystem y tres skills. Es el más parecido a tu enfoque. | https://github.com/SecondBrainProd/second-brain-starter |
| second-brain-os | Guía completa, vault plantilla, skills, comandos y scripts para un vault que se organiza solo. Pensado para Claude Code. | https://github.com/undefined-ui/second-brain-os |
| mcp-obsidian-second-brain | Servidor MCP con memoria en capas (entrada, memoria, wiki, salida) y método PARA. | https://github.com/neverprepared/mcp-obsidian-second-brain |
| CoMfUcIoS/second-brain-mcp | Servidor MCP de **solo lectura** con búsqueda semántica y filtro por metadatos; funciona con cualquier carpeta de `.md`. | https://github.com/CoMfUcIoS/second-brain-mcp |
| Mergoth/second-brain-mcp | Las reglas de archivado viven en el código (frontmatter correcto, carpeta correcta) en vez de depender del prompt. | https://github.com/Mergoth/second-brain-mcp |
| noesskeetit/second-brain-mcp | Índice semántico local sin plugins; lee `_index.md` completo como panorama del vault. | https://github.com/noesskeetit/second-brain-mcp |
| brainstem-mcp | Conector autoalojado que da acceso al vault desde claude.ai, móvil y Desktop (enlaces, backlinks, notas diarias). | https://github.com/vaneavasco/brainstem-mcp |
| secondbrain-mcp (ftdube) | Acceso al vault desde la app móvil de Claude; explica por qué el MCP Filesystem genérico es costoso en tokens. | https://github.com/ftdube/secondbrain-mcp |
| open-second-brain | Capa de memoria local en el vault, con adaptadores para varios agentes. | https://github.com/itechmeat/open-second-brain |

**Nota sobre limitaciones:** varios de estos repos requieren Claude Code, Docker o instalar servidores propios. Con plan free y solo MCP Filesystem, lo más aprovechable son las **ideas de estructura** (índice, frontmatter, handoff, skills), no necesariamente la instalación.

---

## 7. Próximos pasos sugeridos

- [ ] Marcar arriba qué ideas ya están implementadas.
- [ ] Elegir 2-3 de mayor impacto (sugerencia: handoff, `_index.md`, frontmatter).
- [ ] Revisar `second-brain-starter` para comparar estructura de carpetas y skills.
- [ ] Definir el contrato de frontmatter del vault.
