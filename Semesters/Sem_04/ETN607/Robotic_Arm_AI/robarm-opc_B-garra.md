---
galaxy_body: dropship
carrier: "[[Semesters/Sem_04/ETN607/Robotic_Arm_AI/tsk_carrier.md]]"
scope: opcion-B
status: activo
date: 2026-09-13
---

## Proposito

Documenta el diseño de la garra de 3 dedos para reemplazar la pala original del Mould King Digger, usando exclusivamente piezas Technic disponibles en el set principal y los 2 sets adicionales.

---

## Contenido

### Problema

El Mould King Digger trae pala de excavadora. Para un brazo robótico funcional se necesita una garra de 3 dedos capaz de tomar y soltar objetos.

### Solución planteada: garra paralela de 3 dedos

Mecanismo de bielas accionado por 1 motor M. Los 3 dedos se abren y cierran simultáneamente en movimiento paralelo.

```
        [Motor M]
            |
       [engranaje]
       /    |    \
  [biela][biela][biela]
    |      |      |
 [dedo1][dedo2][dedo3]
```

**Ventajas:**
- Solo consume 1 motor (quedan 5 para el brazo)
- Piezas Technic estándar: liftarms, pins, engranajes pequeños
- Movimiento simple y confiable para demo

### Piezas clave necesarias

| Pieza Technic | Uso | Disponible en Digger |
| ------------- | --- | -------------------- |
| Liftarms 1x5 o 1x7 | dedos de la garra | Sí |
| Pins 3L con bush | articulaciones | Sí |
| Engranaje 8t o 16t | transmisión desde motor | Sí |
| Beam 3x5 L-shape | base de la garra | Posiblemente en sets extra |
| Conector perpendicular | unión dedos-biela | Sí |

### Consideraciones de diseño

- Los 3 dedos no necesitan ser totalmente independientes para el MVP — movimiento paralelo sincronizado es suficiente
- La apertura máxima depende del largo de las bielas — ajustable con liftarms de diferente longitud
- El motor M tiene torque suficiente para tomar objetos ligeros (bloques, pelotas pequeñas)
- Punto de montaje: reemplaza directamente el bucket original en el extremo del boom

### Pendiente definir

- [ ] Boceto o referencia visual del mecanismo de bielas
- [ ] Largo óptimo de dedos (estimado: liftarms 1x7)
- [ ] Ángulo de apertura máximo necesario según objetos a tomar
- [ ] Prueba de torque del motor M con la garra montada

### Alternativa simple (si las piezas no alcanzan)

Garra de 2 dedos (pinza) accionada por 1 motor — más fácil de construir, funciona igual para la demo. Requiere menos piezas y el mecanismo es más directo.
