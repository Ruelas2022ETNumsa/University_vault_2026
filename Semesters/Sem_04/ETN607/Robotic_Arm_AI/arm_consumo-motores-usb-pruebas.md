---
tipo: resultados
tema: consumo de motores y límite de alimentación por USB (hub 51515 sin batería, Pybricks)
fecha: 2026-10-29
estado: pruebas con 1 a 4 motores hechas; los 4 motores funcionaron a la vez con arranque suave (sin carga, ver Apéndice A); pendiente prueba con el brazo montado y con batería (SmallRig)
relacionado: "[[arm_bateria-hub51515-resumen]]"
---

# Consumo de motores y límite por USB (hub 51515 sin batería)

## Objetivo
Medir cuánto consume un motor y cuántos motores aguanta el hub alimentado solo por USB (sin batería), para documentar por qué hace falta la batería (plan A: SmallRig 5297).

## Condiciones
- Hub Robot Inventor 51515 con **firmware Pybricks** instalado. Programa corrido desde Pybricks Code por Bluetooth.
- **Sin batería**: alimentación solo por USB (PC o cargador de 5 V / 2250 mA). El hub funciona así, pero los motores quedan limitados.
- Motores libres, **sin el brazo montado**.
- Fuentes: 4 motores probados con USB de PC y con cargador (mismo resultado). Pruebas de 2 motores a 800 y 700 °/s: cargador + celular + Bluetooth. En las demás pruebas (1 motor, 2 motores a 200/500, 3 motores) no anoté la fuente.
- Medición con `hub.battery.voltage()` (mV), `hub.battery.current()` (mA) y `motor.load()` (mNm, estimado por Pybricks). Cargas en valor absoluto (el signo depende del sentido de giro).
- Corte de seguridad en los programas posteriores: si el voltaje baja de 6500 mV, se frenan los motores.

## Programas usados
| Archivo | Uso |
|---|---|
| `medir_motor_simple.py` | 1 motor, 200/500/800 °/s, 10 muestras cada 200 ms |
| `medir_4_motores.py` | A, B, C, D a la vez, 5 s por velocidad |
| `medir_motores_n.py` | N motores configurable, corte por voltaje bajo |
| `medir_800.py` | 2 motores a 800 °/s |
| `medir_700_3motores.py` | 3 motores a 700 °/s (se cambió la velocidad a mano para 600/500/400/300) |

## Resultados

### 1 motor (puerto A)
| Velocidad | mA prom | mA máx | mV prom | mV mín | Carga prom (mNm) | Carga máx |
|---|---|---|---|---|---|---|
| 200 °/s | 127.5 | 133 | 8400 | 8400 | 4.8 | 6 |
| 500 °/s | 152.1 | 158 | 8402 | 8401 | 9.0 | 11 |
| 800 °/s | 175.0 | 188 | 8401 | 8393 | 12.0 | 14 |

Estable en todas las velocidades. Consumo bajo, como se esperaba.

### 2 motores (A, B)
| Velocidad | mA prom | mA máx | mV prom | mV mín | Carga A / B prom (mNm) | Resultado |
|---|---|---|---|---|---|---|
| 200 °/s | 197 | 204 | 8408 | 8407 | 4.5 / 2.6 | estable |
| 500 °/s | 246 | 299 | 8358 | 8319 | 9.2 / 7.0 | pasó, voltaje oscilando |
| 700 °/s | 282 | 310 | 8260 | 8210 | 13.0 / 8.6 | pasó los 5 s |
| 800 °/s (PC) | 313 | 313 | 6326 | 6326 | 198 / 198 | corte en la 1ª muestra |
| 800 °/s (cargador) | 302 (3 muestras) | 336 | 6889 | 6073 | hasta 194 | corte en la 3ª muestra |

### 3 motores (A, B, C)
| Velocidad | mA | mV | Resultado |
|---|---|---|---|
| 300 °/s | 283 prom (máx 297) | 8346 prom (mín 8328) | pasó las 10 muestras |
| 400 °/s | 276-326 en las 5 primeras; 360 después | 8196-8243 en las 5 primeras; luego 6661 y 5770 | estable 5 muestras, degradó en la 6ª y cortó en la 7ª (≈3 s de medición) |
| 500 °/s | 417 | 6049 | corte en la 1ª muestra |
| 600 °/s | 427 | 5980 | corte en la 1ª muestra |
| 700 °/s | 422 | 5990 | corte en la 1ª muestra |

### 4 motores (A, B, C, D)
Con PC y con cargador, a **200 °/s** (la velocidad más baja probada): corriente de 356 a 434 mA, voltaje de 5641 a 4910 mV en 6 muestras, y el hub se apagó. No pasó de la primera velocidad.

## Resumen por cantidad de motores
| Motores | Última velocidad que pasó 5 s | Primera que falló |
|---|---|---|
| 1 | 800 °/s (175 mA prom) | no falló |
| 2 | 700 °/s (282 mA prom) | 800 °/s |
| 3 | 300 °/s (283 mA prom) | 400 °/s |
| 4 | ninguna probada | 200 °/s (~380 mA) |

## Conclusiones
- Con motores libres el consumo es **bajo** y crece con la velocidad (1 motor: 128 → 175 mA entre 200 y 800 °/s).
- Por USB, sin batería, el hub se sostiene hasta **~300-330 mA medidos**. Por encima, el voltaje colapsa (de 8.4 V a ~6 V o menos), las cargas estimadas de los motores saltan a ~200 mNm (no aceleran) y el hub se apaga si no hay corte.
- Todas las pruebas que pasaron quedaron entre 265 y 326 mA; todas las que fallaron superaron ese rango o ya venían colapsando.
- Los valores de corriente tomados con el voltaje ya colapsado (~420 mA con 3 motores a 500-700 °/s) son lo que el hub pudo entregar, **no la demanda real** de los motores.
- Con la corriente de pico y la carga del brazo real, el consumo será mayor que el medido aquí. Por USB no se puede probar el brazo con 3 o 4 motores a velocidad normal: **hace falta la batería**.
- El `hub.battery.voltage()` marca ~8400 mV con 1 motor aunque no hay batería (probable valor regulado por el cargador interno del hub; no es una medida confiable del voltaje que llega a los motores).

## Hipótesis (sin verificar)
- El límite no depende de la fuente: PC y cargador de 2.25 A dieron el mismo comportamiento (a 800 °/s con 2 motores el cargador aguantó 3 muestras y la PC 1; un solo ensayo por fuente, diferencia no concluyente). Posible límite de corriente de entrada del cargador interno del hub (MP2639A) en el camino USB → batería/carga → sistema. Confirmar con el datasheet o midiendo con tester en serie.
- 8.4 V × ~0.3 A ≈ 2.5 W: consistente con un límite de ~500 mA a 5 V, pero es solo un cálculo orientativo.

## Pendiente
- ~~Prueba con 4 motores a velocidad baja~~ → hecha, ver Apéndice A (falla con arranque normal; pasa con arranque suave y escalonado).
- Medir con tester en serie la corriente real de entrada por USB.
- Repetir las pruebas con el brazo montado (carga real) y **con la batería SmallRig 5297** cuando esté disponible: ahí el límite relevante pasa a ser la protección de 4 A.
- ~~Base con motor parado~~ → medida en las pausas del Apéndice A: ~92-105 mA con el hub encendido y los motores parados.
- Registrar `motor.speed()` en la próxima prueba para comprobar que los motores alcanzan la velocidad ordenada (ver observación sobre la carga de -79 mNm en el Apéndice A).

---

## Apéndice A — 4 motores: de la falla al arranque suave (2026-10-29)

### Programas usados
| Archivo | Qué prueba |
|---|---|
| `medir_4motores_baja.py` | 4 motores a la vez a 100, 90, 80, 50 y 10 °/s, corte a 6500 mV |
| `medir_4motores_escalonado.py` | arranque escalonado A, B, C, D cada 1 s a 100 °/s, corte a 5000 mV |
| `medir_4motores_subida_bajada.py` | etapas A, AB, ABC, ABCD, BCD, CD, D con velocidad según motores activos |
| `medir_4motores_suave.py` | igual que el anterior + aceleración limitada (400 °/s²), torque limitado (80 mNm), rampa de velocidad y pausa de 1 s entre etapas, corte a 5500 mV |

### A) 4 motores a la vez, velocidad baja (corte 6500 mV)
En todas las velocidades el voltaje ya estaba colapsado en la primera muestra y se cortó. Los motores no llegaron a funcionar ni un segundo.

| Velocidad | mA | mV | Cargas A/B/C/D (mNm) |
|---|---|---|---|
| 100 °/s | 333 | 5750 | -7, -3, -4, -7 |
| 90 °/s | 335 | 5738 | -5, -3, -5, -7 |
| 80 °/s | 333 | 5740 | -8, -2, -3, -7 |
| 50 °/s | 336 | 5747 | -9, -3, -6, -6 |
| 10 °/s | 493 | 6355 | -37, -30, -39, -36 |

La corriente y el voltaje casi no cambian entre 100 y 50 °/s: con 4 motores energizados a la vez el límite no depende de la velocidad.

### B) Arranque escalonado cada 1 s, 100 °/s (corte 5000 mV)
| Motores activos | mV | mA | Resultado |
|---|---|---|---|
| 1 (A) | 8401-8405 | 147-208 | estable |
| 2 (AB) | 8402-8405 | 199-263 | estable |
| 3 (ABC) | 7969 → 5843 | 393, 274, 265, 265 | voltaje cae durante el segundo |
| 4 (ABCD) | 5452 → 5027 en 11 muestras (~2.75 s) | 331-434 | el hub se apagó solo, sin llegar al corte de 5000 mV |

### C) Etapas con velocidad según motores activos (3 corridas)
| Corrida | Etapa AB | Etapa ABC |
|---|---|---|
| 1 | 700 °/s: normal 2 muestras, colapso en la 3ª (7594 → 5018 mV, cargas -199); el hub se apagó | no llegó |
| 2 | 600 °/s: pasó los 5 s (8201-8390 mV, máx 327 mA) | 200 °/s: corte en la 6ª muestra (5381 mV) |
| 3 | 600 °/s: aguantó 18 muestras y colapsó al final (8009 y 7032 mV, cargas -160/-104) | 100 °/s: corte en la 3ª muestra (5476 mV) |

En las corridas 2 y 3 el corte estaba entre ~5500 y ~5600 mV (deducido de los valores donde cortó y los de la muestra anterior). La etapa A (1 motor, 800 °/s) fue estable en las tres. Con arranque normal, la etapa AB a 600 °/s quedó en el borde: pasó una vez y falló otra.

### D) Arranque suave: `medir_4motores_suave.py` (ACEL 400 °/s², TORQUE 80 mNm, corte 5500 mV, pausa 1 s)
**Resultado: se completaron todas las etapas, el hub no se apagó y no se activó el corte. Los 4 motores funcionaron a la vez (observación visual del usuario).**

| Etapa | Motores | Velocidad ordenada (°/s) | mV (mín-máx) | mA (rango) | Cargas (mNm) |
|---|---|---|---|---|---|
| A | 1 | 800 → 648 (5 s) | 8401-8410 | 149-176 | 0 a -17 al inicio; -79 fijo desde ~1.5 s |
| AB | 2 | 600 → 447 (5 s) | 8389-8404 | 156-260 | 0 a -11 al inicio; -79 fijo desde ~1.5 s |
| ABC | 3 | 200 → 123 (5 s) | 8347-8401 | 256-331 (máx en la 2ª muestra) | -19 a -1 |
| ABCD | 4 | 100 (1 s) | 6236-8400 | 345-443 | -12 a -36 |
| BCD | 3 | 120 → 180 (1 s) | 7944-8247 | 261-265 | -12 a 0 |
| CD | 2 | 440 → 560 (1 s) | 8384-8393 | 208-235 | -16 a -3 |
| D | 1 | 640 → 760 (1 s) | 8402-8407 | 162-171 | -15 a -4 |

**Pausas de 1 s (motores parados):**
- Corriente del hub encendido, sin motores: **~92-105 mA** (la primera lectura de cada pausa trae corriente residual de los motores que aún giran por inercia).
- Tras ABCD (4 motores) el voltaje bajó a 5845 mV y se recuperó en 1 s: 5845 → 6658 → 7225 → 7608 mV. Tras las demás etapas el voltaje se mantuvo entre 8384 y 8409 mV.
- Estimación por resta (corriente medida menos ~95 mA de base, no verificada): ~75 mA por motor en 1 y 2 motores, y ~55-60 mA por motor con 3 motores a baja velocidad.

### Qué se logró y qué no
- **Con arranque normal**, 3 motores a 200 °/s y 4 motores a cualquier velocidad fallaban. **Con arranque suave** pasaron ABC a 200 → 120 °/s durante 5 s y ABCD a 100 °/s durante 1 s, con el hub encendido hasta el final.
- Se cambiaron cuatro cosas a la vez (aceleración limitada, torque limitado, rampa de velocidad y pausa entre etapas). No se puede decir cuál fue la que resolvió el problema.
- La etapa de 4 motores solo duró 1 s y el voltaje bajó hasta 6236 mV (5845 mV en la primera lectura de la pausa). El margen frente al corte de 5500 mV es corto. **No hay datos de 4 motores sostenidos por más de ~1 s.**
- Pruebas hechas con los motores **sin carga** (sin el brazo montado). La carga real aumentará el consumo.

### Observaciones
- **LED del botón del hub:** se pone **naranja** cuando el hub está por apagarse o detenerse por el voltaje de corte (observación del usuario, sin otra fuente).
- **Carga de -79 mNm sostenida (a verificar):** en las etapas A y AB la carga estimada quedó clavada en -79 mNm a partir de ~1.5 s, casi igual al tope de torque de 80 mNm, mientras la corriente se mantuvo estable (171 mA y ~250 mA). Antes, con los mismos motores a 800 °/s, la carga era de -12 a -15 mNm. Posibles causas: el control está saturado en el tope o `motor.load()` informa el valor limitado. No lo sé. En el programa no se registró `motor.speed()`, así que no hay forma de confirmar que los motores alcanzaron la velocidad ordenada.
- El hub sigue siendo el límite: por USB, con motores sin carga, se sostienen 3 motores a baja velocidad y 4 motores solo por ~1 s con arranque suave. El brazo completo sigue necesitando la batería.
