---
project: "pdf-marginalia-pp-system"
date: 2026-07-26
status: creciente
---
%%
status: nueva | creciente | llena
- nueva: disponible para uso temporal o sin proyecto asignado
- creciente: proyecto en curso
- llena: proyecto terminado, pendiente de documentar y archivar
%%

## Handoff
%%
Sobreescribir con edit_file al cerrar cada sesión.
Es lo primero que Claude lee al retomar — debe ser suficiente para arrancar sin re-explicar.
%%

**Última sesión:** 2026-07-26
**Retomar desde:** `_app/_config/_pdf_pp-system.md` — creación del beacon (no existe aún en disco)
**Completado esta sesión:** análisis de plugins, lectura de beacons, diseño del sistema, llenado del tsk_
**Próximo paso:** crear `_pdf_pp-system.md` en `_app/_config/` con el beacon completo del sistema
**Preguntas de cierre:** ¿se agrega `photon_type: pdf-crop` como subtipo oficial en `_galaxy-system.md`? ¿se crea una plantilla `tpl-photon-crop.md` separada de `tpl-photon.md`?

---

## Resumen y objetivo
%%
Una o dos líneas que describan el proyecto y su meta principal.
Debe responder: ¿qué se quiere lograr y por qué?
Es lo primero que se lee al retomar el proyecto — mantenerlo breve y preciso.
%%

Diseñar e implementar el sistema `PDF++ + Cornell Marginalia` para el vault. El sistema permite extraer texto e imágenes de PDFs con PDF++ hacia notas `.md` del Sistema Galaxy, y usar Cornell Marginalia para estudio activo (cues, blur, flashcards) directamente sobre esas notas. Cubre la brecha de NotebookLM con imágenes/gráficas que no pueden extraerse fácilmente. Entregable principal: beacon `_pdf_pp-system.md` que documenta el workflow completo y los tipos galaxy involucrados.

## Decisiones

%%
Tabla de decisiones tomadas durante el proyecto.
Cada vez que se tome una decisión importante, se registra aquí con fecha y motivo.
Las decisiones descartadas o abandonadas van en el callout colapsado debajo.
%%

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
| 2026-07-26 | Marginalia no superpone sobre el PDF — el workflow es siempre pantalla dividida PDF\|nota.md | Técnicamente el plugin vive en archivos .md; los modos “Direct PDF” y “Overlay” son nombres de workflow, no funciones de superposición real |
| 2026-07-26 | `photon_type: pdf-crop` como subtipo de `photon` para imágenes extraídas de PDF++ | Distingue origen de la imagen (recorte de PDF vs imagen arrastrada) sin crear un tipo galaxy nuevo |
| 2026-07-26 | Addon `Pdf Doodle & Harvest` de Marginalia activable para dibujo directo sobre PDF | Complementa PDF++ — permite anotaciones rápidas sobre el PDF sin salir del vault |
| 2026-07-26 | Addon `Anki Advanced Sync` incluido en el sistema — soporta crops de PDF++ como imágenes en tarjetas | Cierra el ciclo: extraçión de imagen → photon → marginalia → Anki con imagen |
| 2026-07-26 | El beacon se llama `_pdf_pp-system.md` (con guion bajo y pp) | Consistente con el nombre en galaxy-links del boot y galaxy-system; reemplaza al `_pdf-system.md` que no existe en disco |

> [!note]- Descartadas
> - Crear tipo galaxy nuevo para imágenes de PDF — descartado: `photon` con subtipo `pdf-crop` es suficiente, sin inflar el sistema galaxy.

---

## Planificación
%%
Descripción del enfoque elegido para abordar el proyecto.
Incluye: contexto, restricciones clave (ej. debe ser gratuito, debe funcionar offline),
y el razonamiento detrás del enfoque seleccionado.
Si el proyecto fue replanificado, el plan anterior va en un callout colapsado tipo:
> [!error]- Planificación abandonada (motivo)
%%

### Contexto

El vault ya usa NotebookLM como tutor conversacional y para transcripción de apuntes (tipo `supernova`). Limitación concreta: NotebookLM no extrae imágenes ni gráficas de PDFs de forma útil, y los plugins de gráficas (Desmos, TikZJax) cubren solo lo que se puede generar por código. Figuras, diagramas de circuitos, gráficas complejas de libros — esas solo se pueden capturar con PDF++.

### Enfoque — tres capas

1. **Capa de ingesta** — PDF++ lee el PDF, extrae backlinks de texto como highlights y exporta regiones como `.png` a `_assets/`.
2. **Capa de nota** — notas `.md` del Sistema Galaxy (`asteroid`, `planet`, `comet`, `photon`) reciben los backlinks y los embeds de imágenes. Puente entre el PDF y el grafo.
3. **Capa de estudio** — Cornell Marginalia opera sobre las notas `.md`: cues `%%> %%`, blur `;;`, flashcards, Explorer sidebar. Addon `Pdf Doodle & Harvest` para dibujar sobre el PDF cuando se necesite.

### Restricciones

- Marginalia **no inyecta contenido sobre el PDF** — siempre trabaja en `.md`.
- PDF++ requiere que el PDF esté abierto en Obsidian para generar backlinks.
- El parche del bloque `marginalia` debe mantenerse tras cada actualización del plugin.
- Imágenes exportadas van a `_assets/` con naming `ETNXXX-TNN-descripcion.png`.
- `Anki Advanced Sync` es el canal de salida a Anki — soporta imágenes nativas y crops de PDF++.

### Entregables

| Entregable | Tipo | Estado |
|---|---|---|
| `_app/_config/_pdf_pp-system.md` | beacon nuevo | pendiente |
| `_templates/tpl-photon.md` — agregar `photon_type: pdf-crop` | edición de plantilla | pendiente |
| `_app/_config/_galaxy-system.md` — agregar subtipo `pdf-crop` en tabla `photon` | edición de beacon | pendiente |
| Sección PDF en `Marginalia_guide.md` o en el beacon nuevo | a decidir | pendiente |

---

## Sugerencias
%%
Antecedentes o referencias encontradas en la web sobre proyectos similares.
Se puebla cuando el usuario dispara la búsqueda con la palabra "web".
Incluir: fuente, resumen breve, y qué se puede aprovechar de ese antecedente.
%%

---

## Flujo de pasos
%%
Lista ordenada de pasos concretos para ejecutar el proyecto.
Debe ser accionable: cada paso es algo que se puede hacer y verificar.
Se deriva de la Planificación y las Sugerencias.
Puede actualizarse a medida que avanza el proyecto.
%%

1. Resolver preguntas abiertas (ver sección) antes de tocar archivos.
2. Crear `_app/_config/_pdf_pp-system.md` — beacon principal del sistema.
3. Editar `_templates/tpl-photon.md` — agregar `photon_type` con opciones `image` y `pdf-crop`.
4. Editar `_app/_config/_galaxy-system.md` — agregar descripción de `pdf-crop` en la tabla del tipo `photon`.
5. Decidir si la guía de uso con PDF va en `Marginalia_guide.md` (sección nueva) o en el beacon nuevo — y ejecutar.
6. Verificar que `_claude-boot.md` tenga galaxy-link a `_pdf_pp-system.md` (ya lo tiene como `[[_pdf_pp-system]]`).

---

## Tareas

%%
Lista unificada de tareas pendientes y completadas.
Usar - [ ] para pendiente y - [x] para completado.
No separar en dos listas — marcar directamente sobre la misma lista.
%%

- [x] Analizar cómo funciona Marginalia con PDFs (modos: Direct PDF, Active Recall, Overlay)
- [x] Analizar cómo funciona PDF++ (backlinks, highlight, exportación de imágenes)
- [x] Leer `cornell_guide.md` y `Marginalia_guide.md` del vault
- [x] Leer `_claude-boot.md` y `_galaxy-system.md`
- [x] Diseñar el sistema de tres capas (ingesta / nota / estudio)
- [x] Llenar este `tsk_pdf_marginalia_pp.md`
- [ ] Resolver preguntas abiertas con el usuario
- [ ] Crear `_app/_config/_pdf_pp-system.md`
- [ ] Editar `_templates/tpl-photon.md` con `photon_type: pdf-crop`
- [ ] Editar `_app/_config/_galaxy-system.md` — subtipo `pdf-crop` en tabla `photon`
- [ ] Decidir y ejecutar dónde va la sección de uso con PDF en las guías existentes

---

## Preguntas abiertas
%%
Dudas, decisiones pendientes o puntos sin resolver que bloquean o condicionan el avance.
Cuando se resuelven, mover la respuesta a Decisiones y borrar la pregunta.
%%

1. ¿Se agrega `photon_type: pdf-crop` como campo oficial en `tpl-photon.md` y en `_galaxy-system.md`, o se deja solo documentado en el beacon del sistema?
2. ¿La guía de uso de Marginalia con PDF va dentro de `Marginalia_guide.md` (sección nueva al final) o directamente en el beacon `_pdf_pp-system.md`?
3. ¿Se activan los addons `Pdf Doodle & Harvest` y `Anki Advanced Sync` ahora, o se documentan como opcionales para activar cuando se necesiten?

---

## Recursos
%%
Todo lo necesario para ejecutar el proyecto en un solo lugar:
- Herramientas, plugins, scripts usados
- Archivos del vault relacionados (con ruta relativa)
- Links externos de referencia
%%

**Plugins:**
- Cornell Marginalia v4.9.0 — `latazadehomero/cornell-marginalia`
- PDF++ — `ryotaushio/obsidian-pdf-plus`

**Archivos del vault:**
- `_app/_config/_claude-boot.md`
- `_app/_config/_galaxy-system.md`
- `_app/_appnotes/cornell_guide.md`
- `_app/_appnotes/Marginalia_guide.md`
- `_templates/tpl-photon.md` (a editar)
- `_app/_config/_pdf_pp-system.md` (a crear)

**Links externos:**
- https://github.com/latazadehomero/cornell-marginalia
- https://github.com/ryotaushio/obsidian-pdf-plus
