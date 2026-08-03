---
galaxy_body: logbook
scope: 
status: on-track | at-risk | blocked
date_updated: 
---

%%
# YAML — instrucciones de llenado

galaxy_body: logbook → siempre este valor, no cambiar

scope: nombre corto del carrier al que pertenece este logbook
  Ejemplo: anki | cornell | galaxy

status: elegir uno y borrar el resto — salud general del proyecto
  - on-track → avanzando sin impedimentos
  - at-risk   → hay señales de alerta pero no está bloqueado
  - blocked   → detenido por dependencia externa o decisión pendiente

date_updated: actualizar cada vez que se modifica este archivo (YYYY-MM-DD)

# Rol de este archivo
  Este logbook es el README histórico del carrier — visión de alto nivel.
  NO es el archivo de trabajo sesión a sesión (eso es tsk_carrier.md).
  Claude lo lee cuando retoma el proyecto después de mucho tiempo
  o cuando necesita entender el proyecto completo sin leer todos los dropships.

# Al actualizar este archivo
  1. Actualizar date_updated y status en el YAML
  2. Revisar ## Estado actual si cambió la salud del proyecto
  3. Agregar entradas a ## Hitos cuando se completa algo significativo
  4. Agregar a ## Archivos del carrier cuando se crea un dropship nuevo
  5. Actualizar ## Riesgos y dependencias si aparece algo nuevo
%%

---

## Visión general

%%
2-4 líneas que describen qué es este proyecto y por qué existe como carrier (proyecto grande)
y no como ship simple. Responde: ¿qué se quiere lograr, cuál es el alcance, y cuál es
el criterio de éxito?
%%

---

## Estado actual

%%
Actualizar cuando haya un cambio significativo en el proyecto — no en cada sesión.
Formato sugerido:
  **Salud:** on-track | at-risk | blocked
  **Resumen:** una o dos líneas de dónde está parado el proyecto ahora mismo.
  **Último avance:** qué se completó recientemente.
  **Próximo hito:** qué viene después.
%%

**Salud:** 
**Resumen:** 
**Último avance:** 
**Próximo hito:** 

---

## Archivos del carrier

%%
Tabla de todos los archivos de la carpeta del carrier.
Actualizar cuando se crea o elimina un archivo — permite a Claude saber
qué existe sin listar el directorio.

Tipos posibles: tsk | logbook | chronicle | dropship | void
Estado para dropships: activo | evaluado | descartado
%%

| Archivo | Tipo | Estado | Descripción |
| ------- | :--: | :----: | ----------- |
| `logbook.md` | logbook | — | este archivo — README histórico del proyecto |
| `tsk_.md` | tsk | — | archivo de trabajo activo |
| `chronicle.md` | chronicle | — | registro cronológico de pruebas |

---

## Hitos

%%
Lista de logros significativos alcanzados durante el proyecto, con fecha.
No registrar tareas menores — solo avances que marcan un antes y un después.
Formato: - YYYY-MM-DD — descripción breve del hito alcanzado
%%

-

---

## Riesgos y dependencias

%%
Qué puede bloquear o está bloqueando el proyecto.
Incluir: dependencias de otros carriers, decisiones pendientes, limitaciones técnicas.
Al resolverse, no borrar — tachar o anotar la resolución con fecha.
%%

-

---

## Decisiones clave

%%
Las decisiones más importantes tomadas durante el ciclo de vida del proyecto.
No es el registro sesión a sesión (eso va en tsk_carrier.md) — solo las que
definen la dirección general del proyecto y que cualquiera debería conocer
para entenderlo.
%%

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
|       |          |        |
