---
galaxy_body: dropship
carrier: "[[Semesters/Sem_04/ETN607/Robotic_Arm_AI/tsk_carrier.md]]"
scope: config
status: activo
date: 2026-09-13
---

## Proposito

Configuración general de hardware y stack técnico del brazo robótico ETN607. Documento de referencia para saber qué se usa y por qué.

---

## Contenido

### Hardware

| Componente | Modelo | Cantidad | Notas |
| ---------- | ------ | -------- | ----- |
| Set principal | LEGO Mindstorms EV3 Core Set (45544) | 1 | EV3 Brick + 3 servomotores + 5 sensores + 541 piezas |
| Set expansión | LEGO Mindstorms EV3 Expansion Set (45560) | 1 | 853 piezas estructurales — sin motores ni sensores |
| **Total** | | | **~Bs 3000 (encontrado en tienda Facebook)** |

### Componentes incluidos en el Core Set 45544

| Componente | Cantidad | Uso en el brazo |
| ---------- | -------- | --------------- |
| EV3 Intelligent Brick | 1 | Controlador principal — ARM9, Linux, USB nativo |
| Large Servo Motor (con encoder) | 2 | Base (rotación) + Codo (subir/bajar) |
| Medium Servo Motor (con encoder) | 1 | Garra (abrir/cerrar) |
| Touch Sensor | 2 | Homing / calibración de posición inicial |
| Color Sensor | 1 | Detección de objetos (fase 2 o MVP) |
| Gyro Sensor | 1 | Disponible para estabilización si se necesita |
| Ultrasonic Sensor | 1 | Detección de distancia / obstáculos |
| Cable USB | 1 | Conexión EV3 Brick ↔ PC (canal de control) |
| Piezas Technic | ~541 | Estructura del brazo |

### Componentes incluidos en la Expansion Set 45560

| Contenido | Notas |
| --------- | ----- |
| 853 piezas Technic | Beams, ejes, conectores, engranajes especiales |
| Plataforma giratoria grande (turntable) | Útil para la base de rotación del brazo |
| Engranajes especiales | Transmisión, reducción de velocidad |
| Elementos de personalización | Estructura adicional del brazo extendido |
| **Motores** | **Ninguno** |
| **Sensores** | **Ninguno** |

### Punto de partida: Robot Arm H25

El modelo oficial Robot Arm H25 (instrucciones incluidas en el Core Set) es la base de construcción. Usa exactamente 3 motores:

| Motor | Puerto EV3 | Articulación | Gear ratio |
| ----- | ---------- | ------------ | ---------- |
| Medium Servo | Port A | Garra (abrir/cerrar) | directo |
| Large Servo | Port B | Codo (subir/bajar) | 8t → 40t |
| Large Servo | Port C | Base (rotación) | 12t → 36t |

La **muñeca** es un mecanismo pasivo (biela/rack) accionado por el movimiento del codo — no requiere motor adicional. Esto es suficiente para el MVP.

### Stack de software

| Capa | Tecnología | Costo |
| ---- | ---------- | ----- |
| Firmware EV3 | ev3dev (Linux) + MicroPython (Pybricks) | Gratis |
| Orquestador IA | Claude (claude.ai free) | Gratis |
| Delegado traducción JSON | Gemini Flash (Google AI Studio) | Gratis |
| Servidor intermediario | Python 3 + python-ev3dev o pybricks-micropython | Gratis |
| Comunicación | USB cable (Mini-USB EV3 ↔ PC) | — |

### Comunicación

```
[Usuario — chat Claude]
        ↓ texto natural
[Python en PC]
        ↓ llama API Gemini Flash → obtiene JSON skill
        ↓ python-ev3dev por USB
[EV3 Brick]
        ↓ parsea JSON → ejecuta skill
[Servomotores con encoder]
        ↑ feedback de posición (grados reales)
[EV3 Brick]
        ↑ confirma posición a Python
```

### Skills definidas (MVP)

```json
{"skill": "saludo"}
{"skill": "trabajo", "origen": 3, "destino": 9}
```

Sistema de skills: archivo README cargado como system prompt. IA interpreta lenguaje natural y genera el JSON correspondiente. El EV3 ejecuta la skill y confirma posición final.

### Presupuesto de latencia estimado

| Etapa | Tiempo |
| ----- | ------ |
| Input usuario → API IA | ~0 ms |
| Gemini Flash (traducción a JSON) | ~500-1000 ms |
| Python → USB → EV3 | ~20 ms |
| EV3 ejecuta skill (movimiento real) | ~1000-3000 ms |
| **Total percibido** | **~2-4 segundos** |

### Fase 2 — Visión IA (postergado)

- Cámara web USB en PC → Python → Claude Vision o Gemini Vision
- Claude detecta objeto y calcula posición → genera JSON con coordenadas reales
- No requiere cambios de hardware en el brazo
- El encoder del EV3 hace que la calibración coordenada→ángulo sea directa y reproducible
