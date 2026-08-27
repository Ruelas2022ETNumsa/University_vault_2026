---
galaxy_body: ship
project: Biblioteca ETN825
date: 2026-07-30
status: in-orbit
fleet: ETN825
blocked_by:
---

## Handoff

**Última sesión:** 2026-08-27
**Retomar desde:** Subir ambos prompts a NotebookLM. Proyecto al 90%.
**Completado esta sesión:** Guias ETN825_AHPL.md y ETN825_TikzJax.md creadas y revisadas (`E:\University_vault_2026\_app\notebooklm\guides\ETN825\`); prompt ETN825-comp_indice_BCv1.md creado y corregido (`E:\University_vault_2026\_app\notebooklm\prompts\ETN825\`) — referencias a caps/capítulos unificadas a temas, Langdon eliminado, ahpl_diseno_sistemas_digitales como segunda opción T1; prompt dividido en 2 archivos (`ETN825-comp_indice_BCv1i.md` T1–T3 y `ETN825-comp_indice_BCv1ii.md` T4–2ª Parte), ambos bajo el límite de 10000 caracteres; _library_ETN825.md corregida (Silberschatz registrado como descartado, Hamacher T4 agregado, typo status, fila duplicada stack, nota aclaratoria caps vs temas, Tanenbaum 2ª ed. especificada, Langdon marcado ❌ OCR falló 2 intentos — uso en sesión directa, ahpl_diseno_sistemas_digitales reemplaza Langdon en T1, Mano CSA como consulta puntual 2ª Parte E/S, Fernández confirmado como tercer autor VHDL, nombre 825-Hill-Peterson-Resumen-Docente-ESP corregido); stack cargado en NotebookLM completo excepto Langdon; 9 complementos subidos a NotebookLM; guías subidas a NotebookLM.
**Próximo paso:** Subir `ETN825-comp_indice_BCv1i.md` y `ETN825-comp_indice_BCv1ii.md` a NotebookLM.

---

## Resumen y objetivo

Construir y mantener la biblioteca de libros y complementos para ETN825 (Arquitectura de Computadores), optimizada para su uso en NotebookLM como sistema de estudio por temas y parciales.

---

## Decisiones

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
| 2026-07-30 | Usar NotebookLM como motor de consulta, no leer los libros completos | El volumen de libros es alto; NotebookLM permite consultas puntuales por tema |
| 2026-07-30 | Separar stack principal de complementos ChatGPT | ChatGPT no tiene contexto de ETN825 — sus veredictos requieren revisión antes de aceptarlos |
| 2026-07-30 | Congelar reajuste hasta tener temario 2026 completo | El temario 2026_1 es parcial (solo T8–T10 tienen subtemas); trabajar sobre él sería en vano |
| 2026-07-30 | Mantener temario 2021 como referencia histórica | Permite comparar qué cambió entre semestres y conservar el material de AHPL/SIC |
| 2026-07-30 | AHPL/SIC queda en el stack aunque no esté confirmado en 2026 | El docente mencionó AHPL explícitamente — se evalúa tras obtener temario completo |
| 2026-08-26 | Temario 2021 eliminado de la library | Contenido idéntico al 2026_1 — sin valor diferencial |
| 2026-08-26 | T8/T9/T10 reubicados como complementarios no evaluados | No forman parte del temario oficial 2026_1 — se mantienen como referencia opcional |
| 2026-08-26 | Hill & Peterson 3ª ed. sin conseguir — no prioritario | Fotocopias del docente (2ª ed.) cubren el contenido necesario; se busca solo si se requiere |
| 2026-08-27 | Langdon descartado de NotebookLM | OCR falló 2 intentos (PDF24) — PDF de escaneo antiguo no recuperable. ahpl_diseno_sistemas_digitales reemplaza su rol como segunda opinión RTL en T1 |
| 2026-08-27 | Silberschatz OS Concepts 10ª descartado | Stallings OS 8ª ya cubre el rol SO para 2ª Parte E/S — redundante |

> [!note]- Descartadas
> - Ediciones anteriores de libros repetidos (COD 3ª, 4ª; Quantitative 5ª) — redundantes con versiones más nuevas ya en el stack.
> - Hill & Peterson Switching Theory 2ª ed. — redundante con la 3ª.
> - Libros de Machine Learning, HPC y FPGAs que aparecieron en bibliografía 2021 — fuera del scope del temario.

---

## Planificación

El proyecto tiene dos fases:

**Fase 1 — Completada:** Armar el stack base con los libros disponibles, documentar complementos (PDFs, resúmenes, ejercicios), registrar libros por conseguir y establecer el flujo de uso por tema y parcial.

**Fase 2 — En pausa:** Reajustar todo el stack contra el temario oficial 2026 una vez el docente lo entregue completo. Incluye reevaluar relevancia de AHPL/SIC, agregar libros para T9 (protocolos de comunicación) y T10 (multiprocesadores), y actualizar las tablas de uso por tema.

Restricciones:
- Solo libros conseguibles en PDF (gratuito o ya obtenido)
- Archivos deben ser seleccionables en texto para funcionar bien en NotebookLM
- No subir libros redundantes — cada fuente debe aportar algo distinto

---

## Sugerencias

- Switching Theory 3ª ed. (Hill & Peterson) es PDF de fotos — puede fallar en NotebookLM. Si falla, usar 2ª ed. (`xoxo Hill Peterson - Switching Theory and Logical Design - 2ed.pdf`). Ambas en carpeta hasta probar.
- Digital Systems 1ª ed. (Hill & Peterson, 1973) — descartada, no tiene rol de respaldo. Eliminar de carpeta (`xoxo Hill Peterson - Digital Systems Hardware Organization and Design - 1ed`).

---

## Flujo de pasos

1. Obtener temario completo y oficial 2026 del docente
2. Comparar temario 2026 vs 2021 tema por tema
3. Reevaluar stack completo — marcar libros que pierden relevancia y los que ganan
4. Reevaluar complementos tabla principal contra temas 2026
5. Reevaluar complementos tabla ChatGPT contra temas 2026 (corregir veredictos si aplica)
6. Definir si AHPL/SIC queda en stack ETN825 o se mueve a ETN821
7. Buscar libros específicos para T9 (RS-232, USB, Ethernet, PCI, DMA, controladores)
8. Buscar libros específicos para T10 (multiprocesadores simétrico/asimétrico)
9. Actualizar tabla "qué usar por tema" con etiquetas T1–T10 del nuevo temario
10. Actualizar flujo de uso
11. Actualizar sección "Archivos divididos" si se consiguen nuevos PDFs de Hill & Peterson
12. Marcar pendientes 2026_2 como completados en `_library_ETN825.md`

---

## Tareas

- [x] Definir stack base de libros por bloque (A y B)
- [x] Evaluar bibliografía entregada por el docente
- [x] Documentar libros conseguidos con veredicto ✅/⚠️/❌
- [x] Documentar complementos PDF leídos en sesión
- [x] Documentar complementos evaluados por ChatGPT (borrador)
- [x] Registrar capítulos disponibles de Hill & Peterson 2ª ed.
- [x] Agregar temario 2026_1 (parcial) al archivo de biblioteca
- [x] Crear pendientes 2026_2 en archivo de biblioteca
- [x] Revisar complementos ChatGPT contra temario 2026 (OSTEP y tesis Swanson eliminados)
- [x] Confirmar edición Mano CSA (DK 2007, 539 pp.) y mapear capítulos por tema
- [x] Registrar fotocopias docente Hill & Peterson 2ª ed. caps. 2,4,5,6 / 7 / 9,10,11,13 como recibidas
- [x] Descargar y registrar diapositivas Stallings COA del GitHub (21 caps. convertidos a PDF)
- [x] Agregar ETN825-Hill-Peterson-Resumen-Docente-ESP a complementos
- [x] Autocompletar subtemas T1–T7 del temario 2026_1 con material del docente — library activado
- [x] ~~Conseguir Hill & Peterson Digital Systems 3ª ed. en buena calidad~~ → **No conseguida. Reemplazada por fotocopias del docente (caps. 2,4,5,6 / 7 / 9,10,11,13 de la 2ª ed.) — aceptable como material base.**
- [x] ~~Reevaluar `operating_systems_three_easy_pieces` contra temario 2026~~ → **Eliminado del stack — SO puro, fuera del scope.**
- [x] ~~Reevaluar `extensiones_ahpl_compilador_msi_lsi` contra temario 2026~~ → **Eliminado del stack — excede nivel del temario.**
- [x] Obtener temario completo 2026 del docente — recibido 2026-08-26
- [x] Ejecutar reajuste 2026_2 — iniciado y parcialmente completado (temario, stack, libros nuevos)
- [x] Conseguir libros pendientes — Pérez VHDL, Stallings OS, Silberschatz, Tanenbaum Distributed, Hauck Reconfigurable ✔️
- [x] Cargar stack completo a NotebookLM — completado salvo 2 PDFs en espera (ver abajo).
- [x] Subir fotocopias del docente (caps. 2,4,5,6 / 7 / 9,10,11,13) a NotebookLM y evaluar calidad de extracción → **Subidas correctamente.**
- [x] ~~`Langdon - Computer Design.pdf`~~ → **❌ OCR falló 2 intentos (PDF24) — no cargable en NotebookLM. Descartado como fuente NotebookLM. Uso en sesión directa únicamente. ahpl_diseno_sistemas_digitales reemplaza su rol como segunda opinión RTL en T1.**
- [x] ~~`Hill Peterson - Switching Theory and Logical Design - 3ed.pdf`~~ → **❌ falló carga a NotebookLM (PDF de fotos). Reemplazada por 2ª ed. — `Hill Peterson - Switching Theory and Logical Design - 2ed.pdf` cargada exitosamente a NotebookLM.**
- [x] ~~Analizar diapositivas Stallings COA 10ª ed. en PDF — evaluar calidad de texto y definir uso en sesión~~ → **No se suben a NotebookLM — son muchas diapositivas, se usan directamente en sesión como repaso rápido.**
- [x] ~~Decidir destino de 5 libros huérfanos: Stallings DCC 10ª, Stallings Comunicaciones 6ª, Forouzan 5ª, Stevens TCP/IP 2ª, Tanenbaum Networks 5ª~~ → **Descartados — redes/protocolos, fuera del scope del temario 2026.**
- [x] ~~Silberschatz OS Concepts 10ª~~ → **Descartado — Stallings OS ya cubre el rol SO para 2ª Parte E/S.**
- [x] Normalizar nombres de PDFs en carpeta y actualizar library con nombres exactos
- [x] ~~Registrar Schwartz & Ben David — Understanding Machine Learning — en libros descartados~~ → **Registrado — Machine Learning, fuera del scope del temario 2026.**
- [x] ~~Evaluar si Stallings OS 8ª aplica también a T3 (interrupciones/DMA) y actualizar tabla si corresponde~~ → **No aplica a T3 — T3 es orientado a AHPL/hardware. Stallings OS queda solo en 2ª Parte E/S.**
- [x] Actualizar tabla "qué usar por tema" contra temario oficial (T1–T6 + Segunda Parte)
- [x] Actualizar flujo de uso contra temario oficial
- [x] Integrar sección ChatGPT a tabla principal de Complementos — sección separada eliminada; `slide-introduccion_ahpl` y `ahpl_diseno_sistemas_digitales` integradas con veredictos y correcciones aplicadas.
- [x] Subir guías a NotebookLM — `ETN825_AHPL.md` (AHPL/LaTeX) y `ETN825_TikzJax.md` subidas correctamente.
- [ ] Subir prompt a NotebookLM — prompt dividido en 2 archivos:
  - `ETN825-comp_indice_BCv1i.md` (T1–T3) — bajo el límite ✅
  - `ETN825-comp_indice_BCv1ii.md` (T4–2ª Parte) — bajo el límite ✅
- [x] Subir complementos pendientes a NotebookLM — todos los 9 complementos subidos correctamente.

---

## Tareas — Creación de contenido NotebookLM

> Guias y prompt para el notebook de ETN825. Referencia de formato: `E:\University_vault_2026\_app\notebooklm\guides\ETN607\` y `E:\University_vault_2026\_app\notebooklm\prompts\ETN607\`.

### Guias

- [x] Crear `ETN825_AHPL.md` — guía de notación AHPL para NotebookLM. Cubre: operadores (`←`, `=`, `→`), estructura de módulos (MEMORY, INPUTS, OUTPUTS, BUSES, LABELS, ONE SHOTS), convención de operandos (escalares, vectores, matrices), sentencias (DEAD END, NO DELAY, SYN), bifurcaciones fijas y condicionales, pasos numerados, tabla de registros para ejercicios. Es la guía principal — equivalente a `ETN607_latex.md`.
- [x] Crear `ETN825_TikzJax.md` — guía TikZJax orientada a ETN825. Tipos de diagrama: flujo (principal), tiempo (señales CLK/SCN/transferencias), cajas negras (módulos con entradas/salidas), paquetes de bits (registros con campos etiquetados). Sin circuitos. Incluir biblioteca de ejemplos por tipo. Equivalente a `ETN607_TikzJax.md`.

### Prompt

- [x] Crear `ETN825-comp-indice-BCv1.md` — prompt principal de complemento por índice. Basado en `ETN607-comp_indice_BCv4ii.md` con adaptaciones: jerarquía de fuentes (resumen docente primero, libros como profundización), formato de ejercicios AHPL (pasos numerados, tabla de registros) en lugar de algebraico, tipos de visual ETN825 (flujo, tiempo, caja negra, paquetes de bits), referencia a `_library_ETN825.md`, mensajes adaptados al temario T1–T6 + Segunda Parte.

---

## Libros por conseguir

| Libro | Prioridad | Razón |
|---|---|---|
| Hill, F.J. & Peterson, G.R. — Digital Systems: Hardware Organization & Design — 3ª ed. (1978) | 🔴 Baja | Muy difícil de conseguir — fotocopias del docente (2ª ed.) cubren el contenido necesario. Buscar solo si se requiere explícitamente. |

---

## Preguntas abiertas

- ¿El docente maneja AHPL/SIC en ETN825 o solo en ETN821? (determina si el stack de AHPL se mantiene o se archiva)
- ¿El libro Pérez VHDL tiene uso real en el temario o es solo referencia bibliográfica del docente?

---

## Recursos

**Archivo principal:**
- `E:\University_vault_2026\_app\_config\_library_ETN825.md`

**Archivos relacionados:**
- `E:\University_vault_2026\_app\_config\_library-system.md` — protocolo general de biblioteca
- `E:\University_vault_2026\_app\_config\_library_MAT101.md` — referencia de formato

**Sitios de búsqueda de libros:**
- https://annas-archive.org
- https://libgen.is
- https://archive.org
- https://z-lib.id
