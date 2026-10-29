---
tipo: resultados
tema: consumo de motores y límite de alimentación por USB (hub 51515 sin batería, Pybricks)
fecha: 2026-10-29
estado: pruebas con 1, 2 y 3 motores hechas; pendiente 4 motores a baja velocidad y prueba con batería (SmallRig)
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
- Prueba con **4 motores a velocidad baja** (probar por debajo de 200 °/s).
- Medir con tester en serie la corriente real de entrada por USB.
- Repetir las pruebas con el brazo montado (carga real) y **con la batería SmallRig 5297** cuando esté disponible: ahí el límite relevante pasa a ser la protección de 4 A.
- Base con motor parado (hub encendido, sin motores) para restar el consumo propio del hub.
