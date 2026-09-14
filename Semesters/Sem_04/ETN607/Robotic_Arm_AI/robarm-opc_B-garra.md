---
galaxy_body: dropship
carrier: "[[Semesters/Sem_04/ETN607/Robotic_Arm_AI/tsk_carrier.md]]"
scope: garra
status: activo
date: 2026-09-13
---

## Proposito

Documenta el diseño de la garra para el Robot Arm H25 modificado, usando exclusivamente piezas Technic del Core Set 45544 y la Expansion Set 45560.

---

## Contenido

### Contexto

El Robot Arm H25 original incluye una garra de 2 lados (pinza simple) accionada por el Medium Motor en Port A. Esta garra ya es funcional para el MVP — puede tomar y soltar objetos de tamaño estándar (bloques LEGO, cubos pequeños).

La expansión 45560 incluye piezas adicionales que permiten escalar la garra si se necesita mayor apertura o agarre de 3 puntos.

---

### Opción A — Pinza H25 original (recomendada para MVP)

La garra original del H25 usa el Medium Motor con un mecanismo de clutch: cuando la garra cierra completamente o topa con el objeto, el motor desliza sin dañar el mecanismo. Esto elimina la necesidad de detectar límites por software.

```
[Medium Motor — Port A]
        |
   [engranaje]
   /         \
[dedo izq]  [dedo der]
```

**Ventajas:**
- Ya está diseñada y probada en el H25
- Clutch integrado → no necesita sensor de límite
- 2 lados es suficiente para tomar objetos estándar en la demo
- Libera tiempo de construcción para el resto del brazo

**Pendiente:**
- [ ] Verificar apertura máxima de la pinza H25 vs tamaño del objeto de demo
- [ ] Definir objeto estándar para la demo (recomendado: bloque LEGO 2x4 o cubo ~3cm)

---

### Opción B — Garra de 3 dedos con piezas del 45560 (fase 2 o si la pinza no alcanza)

Mecanismo de bielas accionado por el mismo Medium Motor (Port A). Los 3 dedos se abren y cierran simultáneamente en movimiento paralelo.

```
[Medium Motor — Port A]
        |
   [engranaje 16t]
   /      |      \
[biela] [biela] [biela]
  |       |       |
[dedo1] [dedo2] [dedo3]
```

**Piezas clave del 45560 útiles para esta garra:**

| Pieza Technic | Uso |
| ------------- | --- |
| Liftarms 1x7 | dedos de la garra |
| Pins 3L con bush | articulaciones de los dedos |
| Engranaje 16t | transmisión desde motor |
| Beam 3x5 L-shape | base de montaje |
| Conectores perpendiculares | unión dedos-biela |

**Consideraciones:**
- El clutch del motor M sigue funcionando como límite natural
- Apertura máxima ajustable cambiando largo de bielas
- Requiere más tiempo de construcción y prueba que la opción A

**Pendiente:**
- [ ] Boceto del mecanismo de bielas para 3 dedos
- [ ] Verificar torque del Medium Motor con 3 dedos cargados
- [ ] Largo óptimo de dedos (estimado: liftarms 1x7)

---

### Decisión recomendada

Empezar con la **Opción A (pinza H25 original)** para el MVP. Si el objeto de demo requiere agarre de 3 puntos o la pinza no tiene suficiente apertura, escalar a Opción B con piezas del 45560. No construir ambas en paralelo.
