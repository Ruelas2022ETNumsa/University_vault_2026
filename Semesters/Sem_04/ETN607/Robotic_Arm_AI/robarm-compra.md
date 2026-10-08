---
galaxy_body: dropship
carrier: "[[Semesters/Sem_04/ETN607/Robotic_Arm_AI/tsk_carrier.md]]"
scope: compra
status: activo
date: 2026-10-05
---

## Proposito

Comparativa de opciones de compra del hardware LEGO para el brazo robótico ETN607, ordenadas por conveniencia. Ubicación del comprador: La Paz, Bolivia. Presupuesto máximo: **3.500 Bs**.

---

## Decisión 2026-10-07 (contexto para retomar)

**Se opta por el Inventor 51515 nuevo (4.000 Bs, Santa Cruz, retira familia).** Se sube el tope de presupuesto de 3.500 a 4.000 Bs.

**Por qué el 51515**
- Nuevo y sellado: hub y motores completos, sin depender de la palabra de un vendedor.
- El brazo ya existe: 4-Motor Arm de OneKitProjects (Dave Parker), con PDFs gratis y código Python para Pybricks (proyecto Fast Block Flipper, motores en puertos A, B, D, F).
- 949 piezas y 4 motores medianos, 6 puertos. Más piezas que el 45544 (541).
- Pybricks soporta el Inventor Hub; no depende de la app oficial.

**Lo que se pierde frente al EV3 45544**
- Sin touch sensors: homing por topes mecánicos o detección de bloqueo del motor (run_until_stalled).
- Motores medianos, menos torque que los Large del EV3.
- Canal Bluetooth en vez de USB (más sensible a cortes).

**Arquitectura acordada**
IA / Python en laptop (Windows 11) → JSON → Bluetooth (Pybricks, pybricksdev o Brickpipe) → hub ejecuta acciones predefinidas. La IA decide a alto nivel; no hay control fino en tiempo real.

**Riesgo conocido:** la app Robot Inventor se discontinúa el 1 oct 2026. No se usa; Pybricks funciona desde el navegador y se puede volver al firmware oficial desde code.pybricks.com (menú de herramientas, Restore official LEGO firmware).

**Pasos de inicio (con el hub en mano)**
1. Chrome o Edge (Firefox, Safari y Brave no sirven; iPhone/iPad tampoco). Abrir code.pybricks.com una vez con internet.
2. Cable micro USB de datos. Hub cargado.
3. Instalar firmware Pybricks desde code.pybricks.com (Install Pybricks firmware). Modo DFU si hace falta: hub apagado, sin USB, mantener botón Bluetooth y conectar USB.
4. Emparejar por Bluetooth y probar un programa mínimo; luego un motor en puerto A.
5. Armar el brazo con los 5 PDFs de OneKitProjects y probar el código Fast Block Flipper.
6. Control desde laptop: Python para Windows, pybricksdev o Brickpipe.

**Repositorios y recursos**
- github.com/pybricks/pybricks-micropython (firmware)
- code.pybricks.com (editor web)
- onekitprojects.com/51515/4-motor-arm (PDFs y programas originales)
- pybricks.com, proyecto Fast Block Flipper (código Python del brazo)
- Paquete brickpipe en PyPI (enviar comandos desde laptop, tercero)
- github.com/gpdaniels/spike-prime y github.com/azzieg/mindstorms-inventor (plan B con firmware oficial por USB/serial)

**Opciones reales consideradas hoy**
- 51515 nuevo, 4.000 Bs: elegido.
- 45544 usado, 3.100 Bs (video del vendedor funcionando): plan B.
- 9797 usado, 2.000 Bs: descartado (condición desconocida, faltan cables, brick NXT sin verificar).
- 8527 caja abierta, 5.500 Bs y 31313 (usado ~4.200 Bs / nuevo 6.050 Bs): descartados.
- SPIKE Prime: no se encontró a la venta.

---

## Contenido

### Opciones ordenadas por conveniencia

| # | Opción | Lugar | Precio | Notas |
| - | ------ | ----- | ------ | ----- |
| 1 | EV3 45544 + 45560 por separado | La Paz (si el vendedor separa el lote) | ~3.200-3.500 Bs | Ideal, pero el vendedor pide el lote completo |
| 2 | Inventor 51515 nuevo | Santa Cruz | 4.000 Bs | Familia lo recoge, nuevo. Pasa el tope por 500 y tiene menos margen para el brazo |
| 3 | 45544 usado (sin expansión) | Sucre | ~3.200 Bs con envío | Entra en presupuesto, pero con riesgo de envío y falta la expansión |
| 4 | 31313 usado | La Paz | ~4.200 Bs | Presencial. Pasa el tope por 700 y no trae expansión |
| 5 | Lote completo (EV3 + NXT + neumática + HiTechnic) | La Paz | 6.800 Bs | Incluye el EV3 con expansión, pero no alcanza el presupuesto |
| 6 | 31313 nuevo | La Paz | 6.050 Bs | Caro para lo que es |
| 7 | NXT 8527 | Sucre | 5.500 Bs + envío | Descartado: plataforma vieja y envío riesgoso |

### Comparativa de piezas clave

| Componente | 45544 (EV3 Education) | 31313 (EV3 Home) | 8527 (NXT 1.0) | Inventor 51515 |
| ---------- | --------------------- | ---------------- | -------------- | -------------- |
| Ladrillo | EV3, ARM9 300 MHz, Linux | EV3, idéntico | NXT, ARM7 48 MHz | Hub 6 puertos, Bluetooth |
| ev3dev / Pybricks | Sí | Sí | No | Pybricks sí |
| Motores | 2 Large + 1 Medium | 2 Large + 1 Medium | 3 NXT | 4 Medium (corregido 2026-10-07) |
| Touch | 2 | 1 | 2 | No |
| Color | 1 | 1 | No | 1 |
| Gyro | 1 | No | No | Integrado en hub |
| Ultrasónico | 1 | No (infrarrojo) | 1 | Distancia |

### Veredicto

- **Actualizado 2026-10-07:** elegido Inventor 51515 nuevo (ver sección Decisión).
- **Anterior, ahora plan B:** EV3 45544 (+ 45560 si se consigue). Incluye el H25 oficial, turntable grande, 2 touch para homing y control por USB.
- **Plan B:** 45544 usado a 3.100 Bs con verificación previa. El 51515 pasó a ser la opción principal.
- **Tope de oferta EV3 (solo si se vuelve al plan B):** 3.500 Bs. No pasar de ahí.

### Negociación (lote La Paz)

- Vendedor pide el lote completo, bajó a 6.800 Bs.
- Estrategia: no mostrar urgencia ni presupuesto. Pedir el EV3 por separado ofreciendo 3.200 Bs en efectivo, retiro propio.
- Si no separa: pasar a la opción 2 o 3.

### Verificar antes de pagar (usado)

- El ladrillo EV3 enciende.
- Los 3 motores giran.
- La turntable y las piezas vienen completas.

### Pendiente

- Confirmar ubicación del EV3 + expansión de ~3.000-3.200 Bs (tienda de Facebook en la config original).
- Respuesta del vendedor del lote en La Paz (ya poco relevante si se compra el 51515).
- Confirmar con la familia la compra y recogida del 51515 en Santa Cruz.
- Primer día con el hub: verificar que cargue, instalar Pybricks y probar Bluetooth en Windows 11 antes de armar.
- Probar torque de los motores medianos con el peso real de la garra y objetos.
- Definir método de homing sin touch sensors.
- Definir formato de comandos JSON entre laptop y hub.
