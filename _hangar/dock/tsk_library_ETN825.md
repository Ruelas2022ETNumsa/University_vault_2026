---
galaxy_body: ship
project: "Biblioteca ETN825"
date: 2026-07-30
status: in-orbit
fleet: ETN825
blocked_by:
---

## Handoff

**Última sesión:** 2026-08-26
**Retomar desde:** Revisar stack completo — 5 libros huérfanos sin rol en temario actual (Stallings DCC, Stallings Comunicaciones, Forouzan, Stevens TCP/IP, Tanenbaum Networks) + Schwartz & Ben David nunca registrado en descartados + definir si Stallings OS y Silberschatz aplican a T3 además de 2ª Parte E/S. Luego analizar diapositivas Stallings COA en PDF.
**Completado esta sesión:** Temario oficial 2026_1 recibido e incorporado; T8/T9/T10 reubicados como complementarios; Temario 2021 eliminado; 5 libros nuevos en stack; tabla “qué usar por tema” y flujo de uso reescritos contra temario oficial; limpieza general de library.
**Próximo paso:** (1) Decidir destino de 5 libros huérfanos (descartados o rol en temario). (2) Registrar Schwartz & Ben David en descartados. (3) Evaluar si Stallings OS / Silberschatz aplican a T3. (4) Analizar diapositivas Stallings COA en PDF.

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
- [ ] Subir fotocopias del docente (caps. 2,4,5,6 / 7 / 9,10,11,13) a NotebookLM y evaluar calidad de extracción
- [ ] Analizar diapositivas Stallings COA 10ª ed. en PDF — evaluar calidad de texto y definir uso en sesión
- [ ] Decidir destino de 5 libros huérfanos: Stallings DCC 10ª, Stallings Comunicaciones 6ª, Forouzan 5ª, Stevens TCP/IP 2ª, Tanenbaum Networks 5ª — descartados o rol real en temario
- [ ] Registrar Schwartz & Ben David — Understanding Machine Learning — en libros descartados
- [ ] Evaluar si Stallings OS 8ª y Silberschatz OS Concepts 10ª aplican también a T3 (interrupciones/DMA) y actualizar tabla si corresponde
- [x] Actualizar tabla “qué usar por tema” contra temario oficial (T1–T6 + Segunda Parte)
- [x] Actualizar flujo de uso contra temario oficial

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
