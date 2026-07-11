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
date_updated: 2026-06-25
status: activo
---

# Sistema TABnote — University Vault

> Sistema base: [[_galaxy-system]]
> Convención de notas: [[_note-system]]
> Sistema PDF (fuentes externas): [[_pdf-system]]
> Sistema NotebookLM (transcripción): [[_notebooklm-system]]
> Pendientes: [[_ToDo-system]]

> **Estado: activo** (cerrado 2026-06-24). Las decisiones de diseño están resueltas. Ver sección Registro de decisiones cerradas.

> **Nota de versión (2026-06-20):** este documento tuvo un cambio de arquitectura a mitad de la discusión. La primera versión proponía exportar los apuntes como PDF y guardarlos como pieza activa dentro del baúl (`_tabnotes/`). Tras validar empíricamente la edición multi-dispositivo (ver más abajo), se abandonó ese modelo: **los apuntes manuscritos ahora viven nativamente en Samsung Cloud**, y el baúl solo recibe la transcripción `.md`. El export a PDF se conserva, pero degradado a **respaldo de archivo al cerrar cada parcial**, no como flujo activo. Las secciones de este documento reflejan ya el modelo nuevo; donde aplica, se deja constancia de qué quedó descartado del modelo anterior.

---

## Objetivo

Los apuntes manuscritos se toman en la tablet con **Samsung Notes**, en formato nativo `.sdocx`, y ahora también se editan/completan desde la PC vía la app oficial de Windows. Este sistema define cómo ese material se relaciona con el baúl, manteniéndose **separado del Sistema PDF** ([[_pdf-system]]) a propósito:

> `_pdf/` almacena **fuentes externas** (libros, slides del profesor, prácticas oficiales) — material que el usuario no produjo. Se sincroniza con Mega.
> Los **apuntes manuscritos propios** ya no se almacenan como archivo activo dentro del baúl — viven en **Samsung Cloud**, sincronizados entre tablet y PC/laptop directamente por la app de Samsung. El baúl solo recibe su **transcripción en texto** vía NotebookLM, y opcionalmente un **snapshot PDF de archivo** al cerrar el parcial.

Mezclar el almacenamiento activo de apuntes propios con `_pdf/` (fuentes externas) seguiría siendo un error conceptual aunque ya no se vayan a guardar ahí de forma activa — la distinción de naturaleza (producción propia vs fuente externa) se mantiene como principio del sistema.

---

## Nomenclatura usada en este documento

Para evitar confusión entre dos herramientas con nombres parecidos:

| Término | Qué es |
|---|---|
| **PDF+(Samsung)** | PDF exportado desde Samsung Notes con la opción "edición habilitada" — permite anotar con S Pen y editar cuadros de texto *solo dentro de la app Samsung Notes*. La plantilla de fondo queda fija al exportar. En el modelo actual, se usa únicamente como snapshot de archivo, no como flujo activo. |
| **PDF++(Obs)** | Plugin [obsidian-pdf-plus](https://github.com/ryotaushio/obsidian-pdf-plus) usado en el baúl para leer/anotar/citar PDFs dentro de Obsidian. Documentado en [[_pdf-system]]; aplica a los snapshots archivados de este sistema, no a los apuntes vivos. |
| **.sdocx** | Formato nativo de Samsung Notes. Es la única forma 100% editable (plantilla, cuadros de texto, trazos como objetos). Vive en Samsung Cloud, sincronizado entre tablet y PC — **es la fuente de verdad activa** en el modelo actual. |

---

## Edición multi-dispositivo (PC + Tablet) — validado empíricamente, 2026-06-20

Se probó editar una misma nota nativa `.sdocx` desde tablet y desde PC (Samsung Notes para Windows + app Samsung Account, instaladas vía Microsoft Store), con sincronización por Samsung Cloud.

**Resultado de la prueba (tablet → PC → tablet):**

| Elemento | Resultado |
|---|---|
| Sincronización | Casi inmediata (~2 segundos) una vez configurada |
| Texto a mano (S Pen) | Se ve correctamente en PC |
| Texto ASCII (teclado) | Perfecto en ambas direcciones, incluyendo edición (agregar/borrar) |
| Imagen pegada | Llega correctamente, editable desde PC (ej. rotar) |
| Trazo hecho con mouse en PC | Llega a la tablet, pero se ve "feo"/anguloso — el mouse no transmite presión/velocidad como el S Pen. No es un error de sync, es una limitación estética del input. |
| Plantilla | Al crear una nota nueva **desde la PC**, no aparece la plantilla personalizada. Se soluciona fácilmente cambiándola desde la tablet — no se considera un problema bloqueante. |

**Conclusión práctica:** la edición de texto desde PC es completamente confiable y es ahora el método preferido para convertir trazos a texto ASCII (más rápido con teclado que el conversor nativo de escritura a texto, y no depende de que el reconocimiento de Samsung interprete bien la letra del usuario). El motivo de optar por edición manual en vez del conversor automático de Samsung: el conversor a veces no transcribe bien por legibilidad de la letra o por requerir conexión a internet — pasar el texto a ASCII manualmente desde el teclado de PC es más confiable para el caso de uso del usuario.

> Esto **resuelve y reemplaza** la antigua "Decisión pendiente: validar el modo PDF reader de edición en sitio" — no se está usando ese modo, sino edición directa del `.sdocx` nativo vía la app instalada. Ver Registro de decisiones cerradas.

**Idioma de reconocimiento de escritura a texto:** se eligió **Español (México)** entre las opciones disponibles (España, México, Colombia, Estados Unidos) por ser el perfil más usado como "español latinoamericano neutro" en motores de reconocimiento, sin las particularidades de conjugación de España (vosotros) y con vocabulario técnico más cercano al usado en Bolivia que el perfil de Estados Unidos. No hay opción específica para Bolivia. Colombia queda como alternativa a probar si México falla mucho en vocabulario técnico puntual.

**Pendiente de repetir:** la misma prueba en la laptop Windows 11 (ASUS) del usuario, para confirmar que el comportamiento es consistente entre equipos.

---

## Flujo de vida de un apunte (modelo actual)

```
1. CAPTURA Y EDICIÓN — Samsung Notes, formato nativo .sdocx
   Ocurre indistintamente en tablet o PC (Samsung Notes para Windows),
   sincronizado vía Samsung Cloud casi en tiempo real.
   Aquí se hace también la limpieza de trazos a texto ASCII desde PC,
   para facilitar la siguiente etapa.
        ↓
2. TRANSCRIPCIÓN — NotebookLM
   La nota (como PDF exportado puntualmente para este fin, o el método
   que defina [[_notebooklm-system]]) se sube a NotebookLM →
   transcripción a .md con LaTeX.
   Guía de formato para que NotebookLM transcriba bien: PENDIENTE,
   ver [[_notebooklm-system]].
        ↓
3. INTEGRACIÓN AL GRAFO
   La transcripción .md se reparte en notas Galaxy normales
   (planet, moon, comet, etc.) según su contenido — NO queda como
   un solo bloque.
        ↓
4. VISIBILIDAD PARA CLAUDE
   La transcripción .md llega a GitHub →
   Claude puede leerla vía conectores y ayudar con la materia.
        ↓
5. ARCHIVO (al cerrar el parcial) — opcional pero recomendado
   Se exporta un único PDF+(Samsung) de la nota ya cerrada y se
   guarda como snapshot histórico en el baúl — ver sección Archivo
   de cierre de parcial. No es parte del flujo activo, es solo
   un respaldo contra pérdida total del original en Samsung Cloud.
```

> **Descartado del modelo anterior:** ya no existe un paso de "export y guardar PDF en `_tabnotes/`" como pieza activa sincronizada en cada sesión de estudio. El PDF solo se genera una vez, al cerrar el tema/parcial, como archivo histórico.

---

## Archivo de cierre de parcial (snapshot, no flujo activo)

Cuando un tema/parcial se da por terminado y la nota `.sdocx` ya no se va a seguir editando, se recomienda generar **un único** PDF+(Samsung) de esa nota y guardarlo en el baúl, como red de seguridad ante los riesgos conocidos de Samsung Cloud (ver más abajo) — no porque se vaya a usar activamente desde ahí.

**Dónde se guarda:**

```
University_Vault_2026/
│
├── _pdf/                       ← fuentes externas (libros, slides, prácticas) — ver [[_pdf-system]]
│   └── ETNXXX/
│
└── _tabnotes_archivo/          ← ★ snapshots de cierre de parcial, NO flujo activo
    └── ETNXXX/
        └── ETNXXX-P2-T01-apuntes-cierre.pdf
```

Se mantiene como carpeta separada de `_pdf/` por la misma razón conceptual de siempre: producción propia vs fuente externa. Se renombra de `_tabnotes/` a `_tabnotes_archivo/` para dejar explícito en el propio nombre que ya no es almacenamiento activo, sino histórico.

**Convención de nombre:**

```
ETNXXX-PN-TNN-apuntes-cierre.pdf
```

Un solo archivo por tema, generado una sola vez al cerrar — no se reexporta ni se sobrescribe después, porque para entonces la nota ya no se edita más.

**Exclusión de Git/GitHub:** igual que `_pdf/`, esta carpeta no sube a GitHub (binarios pesados rompen la sincronización de Git). Se sincroniza con el resto del sistema vía Mega/Obsidian Sync igual que `_pdf/`.

```
.gitignore
_pdf/
_tabnotes_archivo/
```

---

## Nota `supernova` — el puente al grafo (modelo actual)

A diferencia del modelo anterior, la nota `tabnote` ya **no apunta a un PDF activo en el baúl** — apunta a la nota viva en Samsung Cloud (como referencia, no como archivo abrible desde Obsidian) y a la transcripción, que sí es el contenido realmente integrado al grafo. El snapshot de cierre de parcial es opcional y se enlaza solo si existe.

```yaml
---
title: "ETN806 — T01 — Apunte de tablet: Joint PDF"
galaxy_body: supernova
subject: ETN806
semester: 8
partial: 2
topic: 1
source: "Samsung Cloud — Samsung Notes (.sdocx), sincronizado tablet + PC"
transcribed: false
transcription_note: "[[ETN806-T01-transcripcion-notebooklm]]"
archive_snapshot: "[[ETN806-P2-T01-apuntes-cierre.pdf]]"   # solo si ya se cerró el parcial
related_planets:
  - "[[ETN806-T01-joint-pdf-definition]]"
tags: [ETN806, galaxy-supernova, P2, T01]
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
| `source` | Deja explícito que la fuente viva no está en el baúl, sino en Samsung Cloud — evita que alguien busque el archivo dentro del repo y no lo encuentre. |
| `transcribed` | `false` hasta que exista una transcripción NotebookLM vinculada. Permite filtrar con DataView qué apuntes faltan transcribir. |
| `transcription_note` | Wikilink a la nota que contiene la transcripción `.md`. Esa nota sí participa de Git/GitHub. |
| `archive_snapshot` | Wikilink al PDF de cierre de parcial, si ya existe. Vacío/omitido mientras el tema sigue activo. |
| `status` | `en-proceso` mientras el tema sigue en escritura activa, `cerrado` cuando el parcial termina (momento en que corresponde generar el `archive_snapshot`). |

---

## Acceso a Samsung Notes / Samsung Cloud desde PC

| Método | Qué permite | Confiabilidad |
|---|---|---|
| App "Samsung Notes" (Microsoft Store) + app "Samsung Account" + Sync con Samsung Cloud | Ver y **editar** notas `.sdocx` nativas directo en PC, mismas que en la tablet, sync casi inmediato | **Alta — validado empíricamente el 2026-06-20.** Instalar primero "Samsung Account" fue necesario para que el login funcionara. |
| Portal web `account.samsung.com` → Samsung Cloud → ícono "Samsung Notes" | Ver/editar notas desde cualquier navegador, sin instalar nada (PWA opcional, solo cambia la ventana, no agrega funcionalidad) | Media — hay reportes (2024-2025) de exportaciones de Samsung Cloud que llegan vacías. No se probó edición real por este medio, se usó la app instalada en su lugar. |
| Modo "Samsung Notes PDF reader" al abrir un PDF | Edición en sitio sobre un PDF ya exportado | **Descartado del flujo actual** — bug conocido de guardado que pierde contenido. Ya no es necesario evaluarlo porque la edición ahora ocurre directo sobre el `.sdocx`, no sobre un PDF intermedio. |

> Nota: Samsung restringe oficialmente la app de Windows a equipos Galaxy Book; en PCs no-Samsung puede no aparecer el botón de login hasta instalar la app "Samsung Account" por separado. Esto funcionó en la prueba del usuario (PC no-Samsung).

---

## Riesgos conocidos (no hipotéticos)

Samsung Notes ha tenido rupturas de compatibilidad documentadas en actualizaciones grandes:

| Cuándo | Qué pasó |
|---|---|
| 2020 | Migración de formato separó "notas viejas" de "nuevas"; algunos usuarios perdieron categorías y necesitaron un add-on para recuperar acceso a notas antiguas. |
| 2024–2025 | Actualización rompió la visualización de PDFs importados desde apps de escaneo de terceros (quedaban en blanco) — afectó a usuarios con miles de notas. |
| Recurrente | Reportes de guardado de PDF anotado que pierde el contenido original, dejando solo la capa de anotación. |

**Mitigación en el modelo actual:** al ya no exportar PDF de forma activa, el `.sdocx` en Samsung Cloud es la **única** copia del apunte mientras el tema está en proceso — no hay redundancia en el baúl hasta el cierre del parcial. Esto hace **más importante, no menos**, generar el snapshot de archivo al cerrar cada tema (ver sección correspondiente), como única red de seguridad ante estos riesgos documentados.

---

## Resumen Pros / Contras (actualizado 2026-06-20)

**Pros del modelo actual (apuntes nativos en Samsung Cloud, sin PDF activo en el baúl):**

1. Elimina el problema de divergencia entre dos copias (.sdocx vs PDF) — solo hay una fuente viva.
2. Elimina el problema de Git con binarios pesados sobrescritos seguido — el PDF ya no entra al flujo activo.
3. Edición con teclado desde PC, validada y confiable, más rápida que el conversor automático de escritura a texto.
4. Edita donde la herramienta es más capaz: trazos vectoriales reales, plantillas, sin las limitaciones del PDF+(Samsung) documentadas antes.
5. El baúl queda más limpio: solo contiene lo que aporta valor real (transcripción buscable + PDFs de libros), nada de copias "muertas".
6. Pipeline hacia NotebookLM para transcripción a `.md` con LaTeX se mantiene igual.
7. Como efecto secundario de la transcripción, Claude puede leer los apuntes vía GitHub para ayudar con la materia.

**Contras del modelo actual:**

1. El apunte en bruto (manuscrito, diagramas) ya **no tiene respaldo en el baúl** mientras el tema sigue activo — depende 100% de que Samsung Cloud funcione bien. Mitigado solo parcialmente con el snapshot de cierre de parcial.
2. Riesgo real (no hipotético) de ruptura de compatibilidad en actualizaciones de Samsung Notes — ver Riesgos conocidos.
3. El contenido manuscrito no es buscable directamente — la búsqueda real vive en la transcripción `.md`, no en Samsung Cloud.
4. Trazo hecho con mouse desde PC se ve estéticamente pobre (sin presión/velocidad) — aceptable porque el caso de uso es texto, no dibujo, pero limita si se quisiera anotar gráficos finos desde PC.
5. Plantilla personalizada no aparece al crear nota nueva desde PC — hay que crearla/cambiarla desde la tablet (menor, no bloqueante).
6. Tamaño en almacenamiento del PDF+(Samsung) vs `.sdocx`: sin dato confirmado, pendiente de prueba empírica del usuario — relevante ahora solo para el snapshot de cierre de parcial, no para el flujo diario.

---

## Decisiones pendientes (bloquean pasar este sistema a `status: activo`)

| Pregunta abierta | Notas |
|---|---|
| Repetir la prueba de edición multi-dispositivo en la laptop ASUS (Windows 11) | Confirmar que el comportamiento (sync casi inmediato, edición de texto confiable) se repite en un segundo equipo. |
| Guía de formato de apuntes para NotebookLM | Qué estructura (¿Cornell? ¿headers claros? ¿prompt de configuración en NotebookLM?) mejora la transcripción. Pendiente, documentar en [[_notebooklm-system]]. |
| Medir tamaño real del snapshot PDF+(Samsung) de cierre de parcial | Ya no es urgente (no es flujo activo), pero útil para estimar peso acumulado en `_tabnotes_archivo/` a lo largo del semestre. |
| Definir disparador/recordatorio para generar el snapshot al cerrar cada parcial | Sin esto, el paso de archivo (la única red de seguridad del modelo actual) depende de que el usuario se acuerde manualmente. Posible tarea recurrente en [[_ToDo-system]]. |

---

## Registro de decisiones de diseño (ya cerradas)

| Decisión | Razón |
|---|---|
| Los apuntes manuscritos viven en Samsung Cloud, no como PDF activo en el baúl | Validado empíricamente que la edición multi-dispositivo (tablet + PC) vía Samsung Cloud es rápida y confiable para texto, eliminando la necesidad de pasar por un PDF intermedio en el flujo diario. Reemplaza el modelo original de `_tabnotes/` como almacén activo. |
| Edición de texto desde PC (teclado) en vez de depender del conversor de escritura a texto | El conversor automático puede fallar por legibilidad de letra o necesitar internet; escribir directo en ASCII desde el teclado es más confiable para el caso de uso del usuario. |
| Modo "PDF reader" de edición en sitio: descartado | Ya no aplica — la edición ocurre directo sobre el `.sdocx` nativo vía la app instalada, no sobre un PDF intermedio. Reemplaza la antigua decisión pendiente de "validar este modo". |
| Idioma de reconocimiento de escritura: Español (México) | Perfil más cercano a "español latinoamericano neutro" entre las opciones disponibles (no existe Bolivia); evita particularidades de España (vosotros) y es más afín a vocabulario técnico que el perfil de Estados Unidos. |
| El PDF+(Samsung) se conserva solo como snapshot de archivo al cerrar cada parcial | Sirve como red de seguridad ante los riesgos documentados de Samsung Cloud, sin reintroducir el problema de divergencia/Git que tenía el modelo anterior de export activo. |
| Carpeta renombrada de `_tabnotes/` a `_tabnotes_archivo/`, excluida de GitHub | El nombre deja explícito que ya no es almacenamiento activo. Se mantiene fuera de Git por el mismo motivo que `_pdf/` — binarios pesados rompen la sincronización. |
| Transcripción `.md` (NotebookLM) como lo único que llega a GitHub | Es lo único realmente buscable e indexable, y es lo que necesita Claude para ayudar con la materia vía conectores. |
| Nomenclatura PDF+(Samsung) vs PDF++(Obs) | Evitar confusión entre dos herramientas con nombres casi idénticos pero de naturaleza totalmente distinta (export con anotación vs plugin lector de Obsidian). |
| `_pdf/` reservado exclusivamente para libros/fuentes externas | Se mantiene sin cambios respecto a [[_pdf-system]]; los apuntes propios (activos o archivados) nunca se mezclan ahí. |
| `galaxy_body: supernova` como tipo #14 (no extender `asteroid`) | La transcripción de NotebookLM es producción propia, no una fuente externa — forzarla en `asteroid` rompía el principio producción-propia vs fuente-externa que es eje del sistema. Se aprueba `supernova` (✨) como tipo propio. Nombre elegido por la metáfora: material en bruto de alta energía que aún no se ha condensado en notas galaxy. Registrado en [[_galaxy-system]] como tipo #14. Plantilla: `tpl-supernova.md`. |
| Convención de nombres para notas `supernova` | `class` individual: `ETNXXX-classNNN-PN-mesdía.md` (ej. `ETN901-class001-P1-jun15.md`). Fusionada: `ETNXXX-TN-slug_del_tema-PN.md` (ej. `ETN901-T1-densidad_probabilidad_conjunta-P1.md`). Slug en español con guion_bajo, sin tildes ni ñ. Contador `classNNN` corrido por semestre, no reinicia por parcial. |
| Ruta de las notas `supernova` | `Semesters/Sem_NN/ETNXXX/Partial_N/` — raíz del parcial, no dentro de `Topic_NN/`, porque una class puede cubrir subtítulos de varios temas. |
| Ciclo de vida `supernova` | `class` individuales con `status: en-proceso`. Al terminar el tema se fusionan en un solo archivo cuyo nombre cambia a la convención fusionada y `status: completo`. Las `class` originales se marcan `status: diseccionada` antes de eliminar. |

%%
galaxy-links
[[_galaxy-system]]
[[_note-system]]
[[_pdf-system]]
[[_template-system]]
[[_notebooklm-system]]
[[_ToDo-system]]
%%
