---
project: ""
date: 
status: libre
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

**Última sesión:** 
**Retomar desde:** [ruta + línea final sugerida]
**Completado esta sesión:** 
**Próximo paso:** 
**Preguntas de cierre:** 

---

## Resumen y objetivo
%%
Una o dos líneas que describan el proyecto y su meta principal.
Debe responder: ¿qué se quiere lograr y por qué?
Es lo primero que se lee al retomar el proyecto — mantenerlo breve y preciso.
%%

## Decisiones

%%
Tabla de decisiones tomadas durante el proyecto.
Cada vez que se tome una decisión importante, se registra aquí con fecha y motivo.
Las decisiones descartadas o abandonadas van en el callout colapsado debajo.
%%

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
|       |          |        |

> [!note]- Descartadas
> Registrar aquí enfoques o decisiones que fueron considerados pero abandonados, con su motivo. Ejemplo: "Opción X descartada — requería herramienta de pago".

---

## Planificación
%%
Descripción del enfoque elegido para abordar el proyecto.
Incluye: contexto, restricciones clave (ej. debe ser gratuito, debe funcionar offline),
y el razonamiento detrás del enfoque seleccionado.
Si el proyecto fue replanificado, el plan anterior va en un callout colapsado tipo:
> [!error]- Planificación abandonada (motivo)
%%

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

## Preguntas abiertas
%%
Dudas, decisiones pendientes o puntos sin resolver que bloquean o condicionan el avance.
Cuando se resuelven, mover la respuesta a Decisiones y borrar la pregunta.
%%

---

## Recursos
%%
Todo lo necesario para ejecutar el proyecto en un solo lugar:
- Herramientas, plugins, scripts usados
- Archivos del vault relacionados (con ruta relativa)
- Links externos de referencia
%%
