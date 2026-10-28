---
tipo: resumen
tema: alimentación del hub LEGO 51515 (reemplazo de batería)
fecha: 2026-10-24
actualizado: 2026-10-27
estado: plan A definido (SmallRig 5297) — pendiente de compra y pruebas
---

# Resumen: reemplazo de batería del hub 51515

## Objetivo
Alimentar el hub del LEGO Robot Inventor 51515 (brazo robótico, estático) con una fuente/batería alternativa a la original (7.3 V nominal, 2100 mAh).

## Estado actual (2026-10-26)
- **Plan A: SmallRig 5297 (NP-FZ100 USB-C, 850 Bs).** Se descartan las 18650 genéricas por desconfianza en baterías sin marca del mercado local; quedan como respaldo. Además se anota la **Opción B (6×AA NiMH en caja LEGO), solo a analizar con más detalle** (ver su sección).
- Criterio para avanzar con el proyecto: **si la batería alimenta el hub y los motores funcionan con ella, el brazo puede avanzar con la app de SPIKE**, independientemente de Pybricks.
- El hub **ya funciona con la app de SPIKE** (el firmware se actualizó desde la propia app, con USB). El problema abierto es Pybricks: su instalación reinicia el hub en modo DFU y falla por la batería/alimentación actual.
- Pruebas críticas pendientes, en este orden: (1) la batería alimenta el hub, (2) los motores funcionan con ella (uno a la vez, luego varios), (3) si el hub puede cargarla por + y − (prueba aparte, no bloquea el plan).

## Datos base
- Pack original: 2S Li-ion, **7.3-7.4 V nominal**, **8.4 V máximo (lleno)**, corte ~6 V.
- **Máximo absoluto para el hub: 8.4 V.** Fuente de pruebas a ~8.0 V en vacío, nunca más de 8.4 V.
- Original medida en reposo: **7.95 V** (antes de desarmarla).
- El hub trae su propio cargador de 2 celdas (MP2639A, tipo boost desde 5 V USB), con protección de sobrevoltaje y pin de temperatura (NTC).

## Pines de la batería (medidos)
| Cable  | Función                     | Evidencia                                     |
| ------ | --------------------------- | --------------------------------------------- |
| Negro  | + (potencia)                | N+ / B− = 7.95 V                              |
| Blanco | − (común)                   | idem                                          |
| Rojo   | NTC (sensor de temperatura) | R-B = 12.9 kΩ en la batería, baja al calentar |

- El hub **no enciende los LEDs sin una resistencia ~10 kΩ entre Rojo y Blanco** (probado con USB). Confirmado empíricamente.
- En pruebas con potenciómetro, el hub se apaga si el valor sube o baja demasiado (coherente con una ventana de temperatura del cargador; interpretación). **En el montaje final usar resistencia fija (~10 kΩ), no potenciómetro.**
- Pinout no verificado en documentación pública: se apoya solo en las mediciones.

## Pack original desarmado (2026-10-25)
**Identificación**
- Pack: modelo LGOYN57 (2ICP8/36/62), 7.3 V nominal, corte de carga 8.4 V, 2100 mAh / 15.33 Wh. Fabricante: Dongguan Amperex Technology.
- Celdas: 2 × ATL 743662 pouch, 3.65 V, 7.66 Wh cada una, en serie (2S). 2 × 7.66 Wh = 15.33 Wh.
- Es el mismo pack que el LEGO 45610 (SPIKE Prime Large Hub Battery); en BrickLink figura como 67704c01 para el 51515. La documentación de LEGO cita el mismo código de muestra LGOYN57 para ambos.

**Estado de las celdas: DESCARTADAS**
- Medidas: **0.62 V y 1.23 V**. Olor químico/metálico, envoltura abierta, sin hinchazón.
- Sobredescarga profunda (muy por debajo de 2.5 V): daño interno permanente, riesgo de cortocircuito interno al cargar.
- **No cargar ni intentar revivir.** Cubrir lengüetas con cinta aislante, guardar lejos de inflamables y llevar a reciclaje de baterías.
- Probable causa: pack guardado descargado durante mucho tiempo (LEGO recomienda no guardar el hub con batería drenada y separar la batería en almacenamiento largo).

**Placa BMS LGOYN57 REV.01 (inferido de fotos; no hay esquema público)**
- Cara de componentes: pads/contactos de celda B1+, B1−, B2+; un cuarto contacto sin rótulo (arriba a la izquierda).
- Topología 2S: tres puntos eléctricos distintos. **B2− comparte nodo con B1+** (nodo medio, usado para balanceo); por eso no tiene rótulo propio. Pendiente confirmarlo con continuidad.
- Camino negativo: B1− → shunt RS1 (R010 = 10 mΩ) → MOSFET Q1/Q2 → P−. Camino positivo: B2+ → fusible F1 → P+.
- Que P− no conduzca contra el negativo de las celdas es normal con la protección disparada (MOSFET abiertos).
- Conector J1: 4 pines, rótulos P+, RT, P−. Pads de prueba: P1+, P2−, NTC, GND1, GND2, más JP1.
- Medición de continuidad: solo 2 de los 4 pines de J1 conducen entre sí. **Mapa completo de J1 pendiente.**
- Estado de la placa: sin daño visible en fotos (las manchas negras sobre chips parecen resina de fábrica), pero **no verificada funcionalmente**. Solo se prueba con celdas sanas y fuente limitada.
- No se vende la placa sola; sí se vende el pack completo (45610 / 67704c01).

## Plan A: SmallRig 5297 (NP-FZ100 USB-C) — 850 Bs

**Especificaciones** (ficha técnica de SmallRig vía smallrigreseller.com / focusnordic.com, y caja)

| Parámetro | Valor |
|---|---|
| Tipo | Li-ion 2S, formato Sony NP-FZ100 |
| Voltaje nominal | 7.2 V |
| Límite de carga | 8.4 V |
| Capacidad celda / rated | 2600 mAh / 2520 mAh |
| Energía | 18.144 Wh (original: 15.33 Wh, +18 %) |
| **Descarga máxima** | **4 A** |
| **Corte de descarga** | **5.0 V** |
| Entrada USB-C | 5 V / 2 A máx. (límite de carga 5 V) |
| **Carga por contactos ("Li-ion port")** | **estándar 8.4 V / 520 mA; rápida 8.4 V / 1.5 A máx.** |
| Temperatura (según ficha) | carga 0-45 °C; descarga −20 a 60 °C |
| Indicador | 5 LED (20/40/60/80/100 %) |
| Certificaciones | CE (EMC), RoHS |

- La ficha no publica marca ni modelo de las celdas.
- Fecha de lanzamiento: no hay dato oficial; la reseña con fecha más antigua en B&H es del 2025-12-17 (probable lanzamiento a fines de 2025; inferencia).
- Referencia: la versión anterior SmallRig 4265 declara celdas "NCR18500A240A*2" (tipo Panasonic NCR18500A, 2 en serie, 2400 mAh). La celda Panasonic estándar tiene ~3.88 A de descarga continua máx. según datasheet de revendedor; el límite del pack depende de su protección.
- Descartadas por ahora: SmallRig kit 2 baterías + cargador doble (1300 Bs; cada batería 1940 mAh rated, menos capacidad que la original) y Caisi NP-FZ100-TYPE-C (450 Bs; sin datos de descarga máxima ni protección).

**Compatibilidad con cargadores NP-FZ100 por contactos**
- La ficha lista una línea de carga a 8.4 V distinta del USB-C (5 V), que solo puede ser la de los contactos.
- B&H lista como compatibles con el 5297 cargadores de contactos: Sony BC-QZ1, BC-ZD1, DC-C1; SmallRig NP-FZ100 Charger, 4-Channel y Power Bank Charger; y terceros (Dolgin, Jupio, Watson, Neewer, Nitecore, entre otros). La lista parece armada por tipo de batería (NP-FZ100), no por prueba de fábrica.
- Conclusión: es muy probable que cargue en cualquier cargador NP-FZ100 estándar, pero **ninguna fuente lo afirma textualmente para el 5297**.

**Cómo decide el hub que la batería está llena (MP2639A)**
- Tres fases: corriente de goteo, corriente constante (CC) y voltaje constante (CV). Termina cuando el voltaje llega a ~8.38 V (rango 8.35-8.41 V) y la corriente cae bajo el umbral de terminación. Tiene además temporizador de seguridad.
- Por eso la prueba con fuente hasta 8.2 V dejó el LED de carga en rojo: nunca llegó a CV. Además, una fuente fija no genera la caída gradual de corriente de una batería real.
- Con la batería ya al 100 %, el hub debería entrar casi directo a CV y terminar pronto (hipótesis; el LED depende del firmware del hub, no verificado).
- El voltaje de terminación del hub (~8.38 V) coincide con el límite de la batería (8.4 V).

**Qué NO está confirmado (por eso es plan A, no garantizado)**
1. Que el pack acepte carga por + y − **sin el pin de datos** (el hub no lo tiene) y qué hace su protección con el cargador del hub.
2. Que los motores del brazo no hagan saltar la protección de 4 A (consumo real del brazo desconocido, sobre todo varios motores a la vez).
3. Que el USB-C del pack cargue mientras alimenta una carga: una respuesta del Q&A de B&H (sobre el modelo de 2400 mAh, no el 5297) indica que no carga por USB-C estando en una cámara. **Asumir que no.**
4. Que la instalación de Pybricks (modo DFU por USB) funcione con esta batería.

## Decidido / confirmado
- Simulador de batería: **Negro (+) y Blanco (−) a la fuente, 10 kΩ entre Rojo y Blanco**.
- **No usar la protoboard** en la ruta de potencia (cables cortos y gruesos, o soldados).
- **Sin USB cuando se prueba con fuente**: el cargador del hub y la fuente compiten por el nodo.
- Condensador en paralelo cerca del hub: **470 µF, 25 V** (16 V mínimo), polaridad con franja al Blanco (−). 1000 µF en la salida del LM2596 podría dar inestabilidad (el módulo ya trae 220 µF).
- Un diodo en serie **no** se usa: con el diodo bloqueando, el cargador del hub deja de ver la batería y el voltaje puede subir (~9.5 V medidos sin batería) hacia los puertos; además cae 0.3-0.5 V y a 4 A disipa calor.
- Para medir corriente: borne y rango de **10 A**; el rango de mA puede quemar el fusible y baja el voltaje al hub.
- **Las celdas del pack original no se reutilizan.** De la batería vieja solo se aprovecha el conector J1 y sus cables (opcional).
- Regla de conexión: **batería primero, USB después; al desconectar, primero el USB.** No usar a la vez el USB-C de la batería y el USB del hub.
- Uso normal esperado: la batería solo descarga hacia el hub y se carga fuera del hub por su USB-C (o cargador NP-FZ100). La carga por el hub es un extra a verificar, no un requisito.

## Pruebas realizadas
- Fuente con LM2596 (12 V → ~7.1-8.2 V): la matriz intentó encender, a veces arrancó (hasta 4 pulsaciones), los motores no funcionaron. El hub se calentó un poco (USB desconectado en esa prueba).
- Con USB conectado: funciona todo menos los motores (5 V no alcanza para ellos).
- Medida N-B = 9.50 V con USB y sin batería: se interpreta como el cargador boost del hub sin batería que lo limite (no es un daño; hipótesis, no verificado).
- Fuente de laboratorio subida hasta 8.2 V con el hub: el LED de carga siguió en rojo (explicado arriba: no se alcanzó CV).
- Mediciones de corriente poco confiables (0.4 A entrada vs 0.8 A salida): error de rango/unidades probable.
- Pack original desarmado: celdas a 0.62 V y 1.23 V (ver sección anterior).
- Hub con app de SPIKE: funciona; el firmware se actualizó desde la app.

## Diagnóstico
El cuello de botella parece la **corriente sostenida y la respuesta a picos** del cargador de pared (adaptador sin regulación fina: etiqueta 8.4 V / 2 A, medía 12 V en vacío), no el voltaje. Pendiente confirmar midiendo el voltaje en la entrada del LM2596 mientras el hub arranca o mueve un motor. Una batería con baja resistencia interna y 4 A declarados debería resolverlo.

## Plan de pruebas con la SmallRig (al recibirla)
1. Guardar caja y recibo (devolución si falla el paso 3).
2. Cargarla al 100 % por su USB-C, fuera del hub.
3. Tester en los contactos: debería dar ~8.0-8.4 V; identificar + y − por polaridad (pinout de contactos no verificado). Si da 0 V, probar el botón de LEDs. Si sigue en 0 V, no entrega sin cámara: devolver.
4. Montaje: contactos con presión o adaptador (no soldar a la celda), cables cortos y gruesos, fusible ~5 A en el +, resistencia fija 10 kΩ entre Rojo y Blanco, condensador 470 µF/25 V cerca del hub. Verificar polaridad dos veces.
5. Encender el hub sin motores y sin USB; medir voltaje en sus pines.
6. Motores: uno sin carga → uno con el peso del brazo → varios juntos. Medir la caída de voltaje al arrancar. Si el hub se apaga de golpe, sospechar la protección de 4 A.
7. Prueba de carga por el hub (aparte, vigilada): batería llena, tester en la batería, primero un puerto USB de PC (500 mA); voltaje ≤ 8.4 V, sin calentamiento (tocar cada ~15 min), observar el LED.
8. Pybricks (último hito, puede esperar): con el hub apagado y sin USB, entrar en DFU por USB. La guía de Pybricks indica que, si la luz no enciende tras unos 5 s, se desconecta el USB, se quita y se reinserta la batería y se repite. Probar con tester conectado; anotar si el hub se reinicia o la batería corta.

**Criterios:** si pasan los pasos 5 y 6, el proyecto del brazo avanza con la app de SPIKE. Si fallan los pasos 7 u 8, no bloquea: se carga la batería fuera del hub y Pybricks se resuelve después.

**Consulta al soporte de SmallRig** (redactada, a enviar a smallrig@smallrig.com): si el 5297 puede cargarse con un cargador NP-FZ100 estándar (Sony BC-QZ1 o SmallRig); y pedir el manual PDF del 5297. Preguntas adicionales útiles: si carga por contactos usando solo + y − sin pin de datos; si el USB-C carga mientras alimenta otro equipo; corriente máxima continua real.

Documentos útiles al llegar la caja: el manual del 5297 (sección de carga y notas de USB-C en uso). No son útiles los PDF de helpguide.sony.net (guías de cámara).

## Opción B (a analizar con más detalle): 6×AA NiMH en una caja de baterías LEGO como porta-pilas

**Estado:** idea en evaluación, **no decidida**. El plan A sigue siendo la SmallRig 5297. Todo lo marcado como (estimación/inferencia) no está verificado.

**Idea:** usar la caja de 6 AA de LEGO (tipo Power Functions; p. ej. la del set 42065 RC Tracked Racer u otra como la 8881) **solo como contenedor que pone las 6 pilas en serie**. Se puentea con cables desde los contactos internos de las pilas, solo + y −, hacia Negro (+) y Blanco (−) del hub, con 10 kΩ entre Rojo y Blanco (NTC). No se usan la electrónica ni los conectores de la caja ni los motores Power Functions.

**Datos reunidos**
- 6 × 1.2 V NiMH = **7.2 V nominal** (el pack original era 7.3 V).
- Recién salidas del cargador, una NiMH marca ~1.4-1.5 V por celda: seis pueden dar **8.4-9 V, por encima del límite de 8.4 V del hub**. Medir antes de conectar y dejar reposar o descargar un poco.
- Referencia (Eneloop Pro AA): 1.2 V, 2450-2550 mAh, ~25 mΩ de impedancia, curvas de descarga hasta 5 A; un test independiente la llevó hasta 10 A (+24 °C). Seis en serie ≈ 0.15 Ω (cálculo): a 4 A el voltaje cae ≥ 0.6 V (estimación).
- Energía estimada: ~14-18 Wh (similar a los 15.33 Wh originales).
- Motores LEGO a 7.2 V en vez de 9 V: giran más lento y con menos torque (en laboratorio, ≥ 1/4 menos de potencia mecánica); con NiMH en uso real rinde mejor que en laboratorio. Hay usuarios que usan Eneloop en cajas LEGO sin problema.
- Caja 8881: ~235 g, 4×8×11 studs. Las cajas viejas tienen un fusible rearmable que limita la corriente a ~750 mA; las nuevas no (se distinguen por el LED: verde amarillento apagado = vieja; verde oscuro brillante = nueva, según foros). Con el puenteo directo ese límite no interviene, pero **tampoco hay protección alguna**: poner fusible de ~5 A en el + lo más cerca posible de las pilas.
- **Nunca alcalinas:** nuevas dan 9 V (> 8.4 V) y tienen resistencia interna alta. 5 alcalinas (~7.5-8.0 V) solo para pruebas livianas; 5 NiMH (6.0 V) es demasiado bajo.
- **El hub no está pensado para cargar NiMH:** su cargador (MP2639A) es de Li-ion y termina por voltaje (~8.38 V) y corriente. Probablemente cargaría algo hasta ~1.4 V por celda, sin garantía de corte correcto ni balanceo (inferencia). **Recomendación: cargar las pilas fuera del hub** en un cargador NiMH decente (ojalá por celda).
- Lógica EV3/NXT (6 AA = 9 V): no aplica directo. Esos ladrillos se diseñaron para 9 V; el hub grande es de 7.3 V y LEGO solo admite su batería especial. **No hay dato publicado del voltaje máximo de entrada del hub**; no probar 9 V.
- Set 42042 Crawler Crane: trae **un solo motor L** con engranajes (no 4 motores) y caja de 6 AA; los motores Power Functions no enchufan al hub.

**Actualización de firmware con USB (menos de 5 min)**
- Riesgo que estimo bajo: ~0.25-0.3 A × 5 min ≈ 20-25 mAh, menos del 1 % de unas pilas de 2500 mAh (cálculo).
- Condiciones: solo NiMH, voltaje medido antes de conectar, fusible, motores y sensores desconectados, tester puesto, desconectar el USB primero si algo sube de 8.4 V o calienta.
- Una posible ventaja frente a la SmallRig (razonamiento propio): un pack de pilas no tiene protección que se desconecte, así que el cargador del hub siempre ve una batería conectada (evita el caso de los ~9.5 V sin batería).
- Pybricks DFU con este pack: sin probar.

**Ventajas / desventajas frente a la SmallRig**
- A favor: más barata si ya se tiene la caja; pilas intercambiables; química más tolerante; sin electrónica desconocida.
- En contra: el hub no la carga; menos torque; indicador de batería del hub impreciso (curva plana); cableado manual sin protección propia; más peso; no hay pruebas publicadas con el hub 51515.

**Pendiente de analizar**
- Qué caja se usaría exactamente (modelo, tipo de LED, estado) y dónde están los contactos internos; medir + y − con tester.
- Disponibilidad y precio local de NiMH de marca (Eneloop Pro u otra conocida) y de un cargador NiMH.
- Consumo real del brazo (A) y caída de voltaje al arrancar los motores.
- Voltaje máximo de entrada del hub: revisar los PDF eléctricos del repositorio spike-prime (regulador y driver de motores).
- Comparar costo total contra los 850 Bs de la SmallRig.

## Ideas evaluadas y aparcadas
- **Relé (o 2 relés) para pasar de USB a batería durante la actualización:** funcionaría en teoría, pero la bobina de 5 V no aguanta 8-9.5 V, hay tiempo de corte/rebote del contacto (se desconoce cuánto aguanta el hub sin energía) y el peor caso es dejar batería y cargador conectados a la vez. Solo si Pybricks falla con la SmallRig; en ese caso, preferir un selector de fuente tipo "ideal diode" con MOSFET, mejor que un relé.
- **Dummy battery Neewer LP-E6 (DR-LPE6, 450 Bs):** no es una batería, es un adaptador de pared (8 V / 3 A, 24 W) con forma de batería Canon. Sin almacenamiento, 3 A < 4 A de la SmallRig, entrada de 110-120 V según la ficha oficial (Bolivia usa 230 V: revisar etiqueta antes de enchufar) y el USB del hub choca con una fuente fija. **Descartada.**

## Opciones evaluadas
| Opción | Veredicto |
|---|---|
| **SmallRig 5297 NP-FZ100 USB-C (850 Bs)** | **Plan A.** 4 A de descarga declarados, 18 Wh, protección propia, carga independiente por USB-C. Pendiente comprobar motores y carga por el hub |
| SmallRig kit 2 baterías + cargador doble (1300 Bs) | Descartada: baterías de 1940 mAh rated (menos que la original) |
| Caisi NP-FZ100-TYPE-C (450 Bs) | Descartada: no declara corriente de descarga ni protecciones |
| Dummy battery Neewer LP-E6 (450 Bs) | Descartada (ver arriba) |
| **6×AA NiMH en caja de baterías LEGO (puenteada, solo + y −)** | **Opción B, a analizar con más detalle** (ver sección). Posible y barata si ya se tiene la caja; el hub no la carga y da menos torque (7.2 V) |
| **Pack 2×18650 en serie + BMS 2S** (celdas LELONG 2200 mAh que ya tengo) | **Respaldo (antes plan B).** Barata y protegida. Riesgo: celdas genéricas pueden no sostener picos; poca confianza en celdas sin marca |
| Pack original (2 celdas ATL pouch + placa LGOYN57) | **Descartado**: celdas en 0.62 V / 1.23 V, dañadas |
| Batería LEGO 45610 / 67704c01 (pack nuevo completo) | Alternativa fiable pero cara (≈66 € en una tienda europea; descontinuada en LEGO Education). No se vende la placa sola |
| Batería LiPo 2S (Turnigy Shorty) | Buena en corriente, pero cara (≈600 Bs con cargador) y sin protección |
| Batería de juguete/dron/auto RC 2S con su cargador | Alternativa si las 18650 no aguantan; añadir alarma de voltaje o BMS |
| Power bank Xiaomi Redmi 40000 mAh (9 V 2 A / 12 V 1.5 A) + trigger QC + LM2596 | Posible para uso fijo; riesgo de autoapagado y de que los 12 V no salgan |
| Power bank Ugreen 10000 mAh 20 W (12 V 1.67 A, PD) + trigger PD + LM2596 | Mejor que el Xiaomi (PD más fiable); verificar los 12 V |
| Cargador 2S 8.4 V 2 A como fuente | No concluyente; medía 12 V en vacío, no sirve directo |
| Diodo Schottky (SR560/SB560) para sumar fuente + USB | Descartado por riesgo de voltaje hacia los puertos (ver "Decidido") |
| Programar por Bluetooth sin USB con fuente sola | Alternativa más segura |

## Respaldo: lista de compra (2×18650 + BMS)
- 2 celdas 18650 Li-ion **sin protección**, 2000-2600 mAh, **≥10 A de descarga continua**, mismo lote (marca conocida mejor).
- **BMS 2S 7.4 V / 8.4 V para Li-ion 18650, con balanceo, ≥10 A**, 3 cables de celda (B−, B1, B+), salida P+/P−, carga y descarga por los mismos terminales.
- Portapilas 2×18650 en serie.
- Cable de silicona 20-22 AWG, termocontraíble, fusible opcional ~5 A.
- Reutilizar el conector J1 y los cables de la batería vieja del hub (ya desarmada; mapear los 4 pines de J1 antes de soldar).

Preguntas para el vendedor de la BMS: ¿2S para Li-ion de 8.4 V?, ¿amperios continuos?, ¿balanceo?, ¿carga y descarga por P+/P−?

**Procedimiento de armado (respaldo 18650)**
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
- Almacenamiento: no dejar el pack descargado por meses; si el brazo estará apagado mucho tiempo, guardarlo a carga media y separar la batería del hub.

## Pendiente / no verificado
- **SmallRig 5297:** carga por contactos sin pin de datos; carga por el hub; USB-C mientras alimenta (asumido que no); corriente real del brazo frente a los 4 A; Pybricks DFU con esta batería.
- **Opción B (6×AA NiMH):** voltaje máximo de entrada del hub; consumo real del brazo; tipo de caja y contactos; si Pybricks DFU funciona con ese pack; no probar 9 V ni alcalinas.
- Por qué el hub encendía sin el cable Negro (probable alimentación por USB, sin confirmar).
- Si 18650 genéricas sostienen el arranque de los motores (solo si se usa el respaldo 18650).
- Que los power banks entreguen realmente 12 V por QC/PD y no se apaguen en reposo.
- Que los 9.5 V con USB sin batería no lleguen a puertos y motores (no dejar motores conectados en ese estado, ni durante la actualización de firmware).
- **Mapa de J1:** numerar pines 1-4 y medir continuidad de cada pin contra P1+, P2−, NTC, GND1, GND2 y entre sí; confirmar qué hace el cuarto pin.
- **Confirmar que el contacto sin rótulo de la placa (arriba a la izquierda) es B2− y que conduce con B1+.**
- Si se quiere reutilizar la placa LGOYN57: probarla con celdas sanas y fuente limitada en corriente (~100 mA, 4.2 V por celda), vigilando calor. Hasta entonces, no confiar en ella.

## Seguridad
- Nunca más de 8.4 V al hub; ajustar el reductor sin el hub conectado.
- Polaridad del condensador y de la fuente: revisar dos veces.
- No cortocircuitar celdas, aislar empalmes, no cargar sin supervisión la primera vez.
- Descargar el condensador con una resistencia antes de manipularlo.
- Celdas pouch dañadas (las del pack original): no perforar, doblar ni apretar; tenerlas en lugar ventilado sobre superficie no inflamable, con lengüetas cubiertas, hasta llevarlas a reciclaje.
- Durante la actualización de firmware: motores y sensores desconectados del hub.
- Temperatura de carga de la SmallRig: 0-45 °C (según ficha); no cargarla fuera de ese rango.

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
- https://www.eurobricks.com/forum/forums/topic/177641-2020-mindstorms-set/page/2 (batería del 51515 = SPIKE Prime, muestra LGOYN57)
- https://education.lego.com/en-au/support/spike-prime/faqs (batería 45610 por separado; almacenamiento)
- https://www.bricklink.com/catalogItemInv.asp?S=51515-1 (67704c01)
- https://rato-education.odoo.com/en/shop/leg-45610-lego-r-education-technic-large-hub-battery-610 (precio de referencia 45610)
- https://www.smallrigreseller.com/smallrig-usb-c-camera-battery-with-power-display-for-sony-np-fz100-5297.html (ficha SmallRig 5297: descarga 4 A, carga por puerto Li-ion)
- https://www.focusnordic.com/products/batteries-power-supply/batteries/camera-batteries/smallrig-5297-usb-c-camera-battery-with-power-display-for-sony-np-fz100 (misma ficha)
- https://www.bhphotovideo.com/c/product/1953622-REG/smallrig_5297_usb_c_battery_with_power.html (reseñas con fecha, Q&A, lista de cargadores compatibles)
- https://www.sony.co.jp/en/Products/diacc/systemchart/en-gb/details/BC-QZ1.html (cargador Sony BC-QZ1)
- https://nkon.nl/en/panasonic-ncr18500a.html (celda de referencia del 4265)
- https://cdn.eicom.ru/media/PDF24/333297.pdf (datasheet MP2639A: fases de carga y terminación)
- https://github.com/orgs/pybricks/discussions/688 (modo DFU de Pybricks en hubs SPIKE/Inventor)
- https://uk.neewer.com/products/neewer-dummy-battery-replacement-for-lp-e6-lp-e6n-lp-e6nh-66601977 (dummy Neewer DR-LPE6: 8 V / 3 A)
- Opción B (NiMH en caja LEGO):
  - https://www.eurobricks.com/forum/forums/topic/80194-best-batteries/ (NiMH en caja 8881: 7.2 V, Eneloop)
  - https://www.eurobricks.com/forum/forums/topic/122224-why-are-eneloop-pro-batteries-good (motores más lentos y con menos torque a 7.2 V)
  - https://www.eurobricks.com/forum/forums/topic/101400-technic-pub/page/22/ (cajas viejas con fusible rearmable vs nuevas sin limitador)
  - https://www.eurobricks.com/forum/forums/topic/149338-about-8878/ (límite ~750 mA de cajas con protección)
  - https://sariel.pl/2009/06/8878-rechargeable-battery-box-8887-transformer (8881: peso y tamaño; 7.2 V con recargables)
  - https://static.rapidonline.com/pdf/12-5745_v1.pdf (datasheet Eneloop Pro AA)
  - https://lygte-info.dk/review/batteries2012/Eneloop%20AA%20HR-3UWXB%202450mAh%20(Black)%20UK.html (test de corriente)
  - https://eneloop101.com/batteries/eneloop-test-results/ (NiMH vs alcalina a 1-3 A)
  - https://www.eblofficial.com/blogs/battery-101/nimh-battery-voltage (NiMH ~1.4-1.5 V recién cargada)
  - https://en.hothbricks.com/vite-teste-lego-technic-42065-rc-tracked-racer/ (set 42065: 6 AA + 3 AAA)
  - https://thelegocarblog.com/2016/07/23/the-big-blue-42042-crawler-crane-set-review/ (42042: un solo motor L)
  - https://brickarchitect.com/powered-up/ (hubs de 7.3 V vs 9 V)
  - https://education.lego.com/en-au/product-resources/spike-prime/troubleshooting/faqs/ (solo se admite la batería recargable especial)
