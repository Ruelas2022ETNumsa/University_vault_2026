---
galaxy_body: dropship
carrier: "[[_hangar/IMA_NBLM/tsk_IMA_NBLM.md]]"
scope: opcion-A
status: activo
date: 2026-08-13
---

## Proposito

Documenta el caso especial de diapositivas para el carrier IMA_NBLM — fuentes sin número de página impreso ni etiqueta de figura. Pendiente de normalización antes de integrarse al flujo principal.

---

## Contenido

### Problema

Las diapositivas presentan condiciones distintas a los PDF de libros o apuntes:
- Frecuentemente no tienen número de página visible
- Raramente tienen etiqueta de figura (Figura X)
- El pie de figura puede estar ausente o ser muy genérico
- La única referencia posible suele ser el número de diapositiva (si el PDF lo conserva) o la posición visual del elemento

En la prueba realizada (2026-08-13), NBLM entregó un número de página incorrecto al no tener ni número impreso ni etiqueta como ancla. El bloque IMA-SRC resultante no era confiable para localizar la imagen.

### Preguntas abiertas

- ¿El número de diapositiva del PDF es accesible para NBLM?
- ¿Es suficiente con fuente + número de diapositiva + descripción del visual como identificador?
- ¿Vale la pena un campo `diapositiva:` separado de `página:` en el bloque IMA-SRC?
- ¿Cómo manejar diapositivas sin número visible — usar posición en el PDF como aproximación?

### Criterio de éxito tentativo

Un bloque IMA-SRC para diapositivas debería permitir localizar la imagen con:
- Nombre del archivo fuente
- Número de diapositiva (si disponible) o posición en el PDF
- Descripción mínima del visual que permita identificarlo visualmente

### Estado

Pendiente — no es el foco actual. Retomar cuando el flujo para PDF con etiqueta esté integrado en producción.
