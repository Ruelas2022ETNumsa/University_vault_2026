---
galaxy_body: carrier
project: ""
date: 
status: docking
fleet:           # opcional — materia o contexto al que pertenece
blocked_by:      # opcional — solo si status: delayed
---
%%
status:
- docking: activo dentro de su carpeta, en proceso
- in-orbit: fue trabajado, pausado sin dependencia externa
- delayed: bloqueado por dependencia externa — ver blocked_by
- delivered: terminado y documentado, listo para archivar
- aborted: proyecto no viable, descartado

Archivos del carrier:
- tsk_carrier.md  → este archivo — tareas activas, se lee en cada sesión
- logbook.md      → README histórico del proyecto, se lee cuando el proyecto lo necesita
- chronicle.md    → registro cronológico de pruebas por dropship
- dropships       → opciones, configuración y pruebas (ver ## Archivos del carrier)
- void_*          → archivos de prueba desechables, sin YAML
%%

## Handoff
%%
Sobreescribir con edit_file al cerrar cada sesión.
Es lo primero que Claude lee al retomar — debe ser suficiente para arrancar sin re-explicar.
%%

**Última sesión:** 
**Retomar desde:** [ruta + línea final sugerida]
**Completado esta sesión:** 
**Próximo paso:** 
**Preguntas de cierre:** 

---

## Tareas

%%
Lista unificada de tareas pendientes y completadas.
Usar - [ ] para pendiente y - [x] para completado.
No separar en dos listas — marcar directamente sobre la misma lista.
%%

- [ ] 
- [ ] 

---

## Archivos del carrier

%%
Lista de todos los archivos de la carpeta. Actualizar cuando se crea o elimina un archivo.
Permite a Claude saber qué existe sin listar el directorio.
%%

| Archivo | Tipo | Estado | Descripción |
| ------- | ---- | ------ | ----------- |
| `logbook.md` | logbook | — | README histórico del proyecto |
| `chronicle.md` | chronicle | — | Registro cronológico de pruebas |
| | dropship | | |
