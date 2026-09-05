---
galaxy_body: dropship
carrier: "[[_app/Tars/work/tars_conversion/tsk_carrier.md]]"
scope: opcion-C
status: activo
date: 2026-09-04
---

## Proposito

Documentar y probar la Opción C del carrier `tars-hpprgm-conversion` — usar un `.hpprgm` real generado por CASE (vía drag and drop) como plantilla, extrayendo su header exacto y reemplazando solo el contenido con el fuente nuevo.

---

## Contenido

### Concepto

En lugar de reconstruir el header desde cero, se toma un `.hpprgm` existente y válido (generado por CASE), se extrae el header binario real, y se reemplaza únicamente el contenido (la sección UTF-16 LE del código fuente). Garantiza que el header es 100% compatible porque viene de CASE mismo.

### Requisito previo

Tener al menos un `.hpprgm` válido generado por CASE vía drag and drop en `HP Prime\Calculators\Prime`. Este archivo actúa como plantilla base.

### Lógica de implementación

1. Leer el `.hpprgm` plantilla en binario
2. Localizar el offset donde termina el header y empieza el contenido (usando el separador `0x00 0x00` después del nombre)
3. Actualizar el nombre en el header con el nombre del nuevo programa (en UTF-16 LE)
4. Reemplazar el contenido con el fuente nuevo codificado en UTF-16 LE
5. Escribir el archivo resultante

### Ventaja clave

No requiere conocer la estructura exacta del header moderno — se usa el header real. Si HP actualiza el formato, el header plantilla sigue siendo válido siempre que venga de un `.hpprgm` generado por la versión actual de CASE.

### Preguntas abiertas

- ¿El header contiene algún campo con el tamaño del contenido que también haya que actualizar?
- ¿El nombre en el header está en una posición fija o hay que buscarlo dinámicamente?

### Resultados de prueba

- [ ] Prueba 1 — reemplazar contenido de `KMH_CONV.hpprgm` con fuente modificado: pendiente
- [ ] Prueba 2 — generar archivo con nombre distinto al de la plantilla: pendiente

### Veredicto

Pendiente.
