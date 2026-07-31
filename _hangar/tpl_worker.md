---
galaxy_body: operator
project: ""
date: 
status: free
---
%%
status: free | busy
- free: worker disponible, sin proyecto asignado
- busy: worker cargado con un ship activo

alias: wN → reemplazar N con el número del worker (w1...w7)
project: nombre corto del ship que está cargado — dejar vacío si status: free
%%

## Handoff
%%
Sobreescribir con edit_file al cerrar cada sesión.
Es lo primero que Claude lee al retomar — debe ser suficiente para arrancar sin re-explicar.
Si el worker queda free al cerrar, limpiar todo este bloque.
%%

**Última sesión:** 
**Retomar desde:** [ruta del ship en dock/ si se pausó, o línea final del flujo de pasos]
**Completado esta sesión:** 
**Próximo paso:** 
**Preguntas de cierre:** 

---

## Ship activo
%%
Descripción de una o dos líneas del ship que está cargado en este worker.
Responde: ¿qué se quiere lograr y por qué?
Si el worker está free, este bloque queda vacío.
%%

**Ship:** 
**Origen:** [dock/ | blueprint aprobado]
**Bloqueado por:** — 

---

## Decisiones

%%
Decisiones tomadas durante la ejecución de este ship.
Al terminar o pausar el ship, estas decisiones se copian al archivo correspondiente en dock/ antes de limpiar el worker.
%%

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
|       |          |        |

> [!note]- Descartadas
> Enfoques o decisiones considerados pero abandonados durante la ejecución.

---

## Flujo de pasos
%%
Pasos concretos para completar el ship cargado.
Se deriva del archivo ship en dock/ o del blueprint de origen.
Cada paso es algo que se puede hacer y verificar.
Al pausar o terminar el ship, el estado de los pasos se copia al archivo en dock/.
%%

---

## Tareas

%%
Lista unificada de tareas del ship activo.
- [ ] pendiente
- [x] completado
Al pausar → copiar al archivo ship en dock/ antes de limpiar.
Al terminar → documentar lo necesario y limpiar el worker.
%%

- [ ] 
- [ ] 

---

## Preguntas abiertas
%%
Dudas o puntos sin resolver que bloquean el avance del ship.
Al resolverse → mover la respuesta a Decisiones.
Si el ship se pausa por dependencia externa → registrar aquí qué se necesita para desbloquearlo.
%%

---

## Recursos
%%
Todo lo necesario para ejecutar el ship en un solo lugar:
- Ruta del archivo ship en dock/ (si aplica)
- Archivos del vault relacionados
- Links externos de referencia
- Herramientas o plugins usados
%%
