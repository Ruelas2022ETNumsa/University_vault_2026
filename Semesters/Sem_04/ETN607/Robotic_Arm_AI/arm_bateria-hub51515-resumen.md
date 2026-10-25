---
tipo: resumen
tema: alimentación del hub LEGO 51515 (reemplazo de batería)
fecha: 2026-10-24
estado: en pruebas
---

# Resumen: reemplazo de batería del hub 51515

## Objetivo
Alimentar el hub del LEGO Robot Inventor 51515 (brazo robótico, estático) con una fuente/batería alternativa a la original (7.3 V nominal, 2100 mAh).

## Datos base
- Pack original: 2S Li-ion, **7.3-7.4 V nominal**, **8.4 V máximo (lleno)**, corte ~6 V.
- **Máximo absoluto para el hub: 8.4 V.** Fuente de pruebas a ~8.0 V en vacío, nunca más de 8.4 V.
- Original medida en reposo: **7.95 V**.
- El hub trae su propio cargador de 2 celdas (MP2639A, tipo boost desde 5 V USB), con protección de sobrevoltaje y pin de temperatura (NTC).

## Pines de la batería (medidos)
| Cable  | Función                     | Evidencia                                     |
| ------ | --------------------------- | --------------------------------------------- |
| Negro  | + (potencia)                | N+ / B− = 7.95 V                              |
| Blanco | − (común)                   | idem                                          |
| Rojo   | NTC (sensor de temperatura) | R-B = 12.9 kΩ en la batería, baja al calentar |

- El hub **no enciende los LEDs sin una resistencia ~10 kΩ entre Rojo y Blanco** (probado con USB). Confirmado empíricamente.
- Pinout no verificado en documentación pública: se apoya solo en las mediciones.

## Decidido / confirmado
- Simulador de batería: **Negro (+) y Blanco (−) a la fuente, 10 kΩ entre Rojo y Blanco**.
- **No usar la protoboard** en la ruta de potencia (cables cortos y gruesos, o soldados).
- **Sin USB cuando se prueba con fuente**: el cargador del hub y la fuente compiten por el nodo.
- Condensador en paralelo cerca del hub: **470 µF, 25 V** (16 V mínimo), polaridad con franja al Blanco (−). 1000 µF en la salida del LM2596 podría dar inestabilidad (el módulo ya trae 220 µF).
- Un diodo en serie **no** sirve para proteger contra corriente de retorno si se quiere conservar la carga por USB.
- Para medir corriente: borne y rango de **10 A**; el rango de mA puede quemar el fusible y baja el voltaje al hub.

## Pruebas realizadas
- Fuente con LM2596 (12 V → ~7.1-8.2 V): la matriz intentó encender, a veces arrancó (hasta 4 pulsaciones), los motores no funcionaron. El hub se calentó un poco (USB desconectado en esa prueba).
- Con USB conectado: funciona todo menos los motores (5 V no alcanza para ellos).
- Medida N-B = 9.50 V con USB y sin batería: se interpreta como el cargador boost del hub sin batería que lo limite (no es un daño; hipótesis, no verificado).
- Mediciones de corriente poco confiables (0.4 A entrada vs 0.8 A salida): error de rango/unidades probable.

## Diagnóstico
El cuello de botella parece la **corriente sostenida y la respuesta a picos** del cargador de pared (adaptador sin regulación fina: etiqueta 8.4 V / 2 A, medía 12 V en vacío), no el voltaje. Pendiente confirmar midiendo el voltaje en la entrada del LM2596 mientras el hub arranca o mueve un motor.

## Opciones evaluadas
| Opción | Veredicto |
|---|---|
| **Pack 2×18650 en serie + BMS 2S** (celdas LELONG 2200 mAh que ya tengo) | **Elegida para la siguiente prueba.** Barata y protegida. Riesgo: celdas genéricas pueden no sostener picos |
| Batería LiPo 2S (Turnigy Shorty) | Buena en corriente, pero cara (≈600 Bs con cargador) y sin protección |
| Batería de juguete/dron/auto RC 2S con su cargador | Plan B si las 18650 no aguantan; añadir alarma de voltaje o BMS |
| Power bank Xiaomi Redmi 40000 mAh (9 V 2 A / 12 V 1.5 A) + trigger QC + LM2596 | Posible para uso fijo; riesgo de autoapagado y de que los 12 V no salgan |
| Power bank Ugreen 10000 mAh 20 W (12 V 1.67 A, PD) + trigger PD + LM2596 | Mejor que el Xiaomi (PD más fiable); verificar los 12 V |
| Cargador 2S 8.4 V 2 A como fuente | No concluyente; medía 12 V en vacío, no sirve directo |
| Diodo Schottky (SR560/SB560) para sumar fuente + USB | Idea en pruebas; comportamiento del cargador del hub desconocido |
| Programar por Bluetooth sin USB con fuente sola | Alternativa más segura |

## Lista de compra (siguiente prueba)
- 2 celdas 18650 Li-ion **sin protección**, 2000-2600 mAh, **≥10 A de descarga continua**, mismo lote (marca conocida mejor).
- **BMS 2S 7.4 V / 8.4 V para Li-ion 18650, con balanceo, ≥10 A**, 3 cables de celda (B−, B1, B+), salida P+/P−, carga y descarga por los mismos terminales.
- Portapilas 2×18650 en serie.
- Cable de silicona 20-22 AWG, termocontraíble, fusible opcional ~5 A.
- Reutilizar los pines de la batería vieja del hub (fotografiar o anotar colores antes de desarmar).

Preguntas para el vendedor de la BMS: ¿2S para Li-ion de 8.4 V?, ¿amperios continuos?, ¿balanceo?, ¿carga y descarga por P+/P−?

## Procedimiento de armado
1. Cargar cada celda en el cargador de 4 ranuras hasta luz verde (~4.2 V).
2. Medir: diferencia entre celdas < 0.1 V.
3. Portapilas 2S → BMS (B−, B1, B+) → P+/P− al hub (Negro +, Blanco −), 10 kΩ (o NTC) entre Rojo y Blanco.
4. Verificar polaridad con el tester antes de conectar.
5. Primera prueba sin motores; medir voltaje en los pines del hub al pulsar el botón.
6. Carga posterior: por el USB del hub (vigilar la primera vez: pack ≤ 8.4 V, sin calentamiento) o sacando las celdas al cargador.

## Correcciones y matices técnicos (verificados en internet)
- LM2596: la entrada debe superar la salida ≥ 1.5 V; uso continuo recomendado ≤ 1.5-2 A (disipador sobre 2.5 A); **sin protección contra polaridad invertida**.
- BMS: la sobredescarga corta a ~2.5 V por celda (≈5 V el pack); rendir ≤ 50 % de la corriente nominal de forma continua.
- Motores: pierden torque con voltaje bajo; recargar cerca de 8.0 V es lo recomendado por la comunidad. No ajustar la fuente a ~7.1 V.
- Un cargador de baterías no es una buena fuente para motores: su etiqueta de amperios es un tope, no una garantía de respuesta a picos.

## Pendiente / no verificado
- Por qué el hub encendía sin el cable Negro (probable alimentación por USB, sin confirmar).
- Si 18650 genéricas sostienen el arranque de los motores.
- Que el cargador interno del hub cargue bien un pack 2S + BMS casero (probar vigilando).
- Que los power banks entreguen realmente 12 V por QC/PD y no se apaguen en reposo.
- Que los 9.5 V con USB sin batería no lleguen a puertos y motores (no dejar motores conectados en ese estado).

## Seguridad
- Nunca más de 8.4 V al hub; ajustar el reductor sin el hub conectado.
- Polaridad del condensador y de la fuente: revisar dos veces.
- No cortocircuitar celdas, aislar empalmes, no cargar sin supervisión la primera vez.
- Descargar el condensador con una resistencia antes de manipularlo.

## Fuentes
- https://github.com/GO-Robot-FLL/Python-for-Spike-Prime
- https://github.com/jilinhuang/spike-prime
- https://protosupplies.com/product/lm2596s-adjustable-dc-dc-step-down-module/
- https://surplustronics.co.nz/products/6943-dc-dc-adjustable-step-down-module-lm2596
- https://www.electronicsforu.com/electronics-projects/industry-grade-projects/2s-cell-charger-with-an-integrated-boost-converter
- https://www.mouser.in/new/monolithicpowersystems/mps-mp2639a-chargers
- https://makerselectronics.com/product/lithium-battery-charger-protection-module-bms-2s-20a-8-4v-with-cell-balancing/
- https://sigmanortec.ro/en/bms-module-2s-5a-lithium-74v
- https://www.mi.com/my/20000mah-redmi-18w-fast-charge-power-bank/specs
