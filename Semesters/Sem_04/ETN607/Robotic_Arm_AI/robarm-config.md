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

| Componente | Modelo | Cantidad | Costo aprox. |
| ---------- | ------ | -------- | ------------ |
| Set principal | Mould King Mechanical Digger (13112) | 1 | ~1800 Bs |
| Sets adicionales | Sets simples Mould King sin motor | 2 | ~600 Bs |
| Controlador | ESP32 (cualquier dev board estándar) | 1 | ~80 Bs |
| Driver motores | L298N o DRV8833 | 2-3 | ~100 Bs |
| Cables y misc | Jumpers, protoboard, alimentación | — | ~70 Bs |
| **Total** | | | **~2650 Bs** |

### Motores disponibles (del Digger)

| Motor | Cantidad | Uso asignado |
| ----- | -------- | ------------ |
| XL motor | 1 | Base / rotación principal |
| M motor | 4 | Hombro, codo, muñeca, garra |
| L motor | 1 | Extensión de brazo |

### Stack de software

| Capa | Tecnología | Costo |
| ---- | ---------- | ----- |
| Firmware | Arduino IDE + C++ | Gratis |
| IA / LLM | Gemini (Google AI Studio) o Groq | Gratis (tier gratuito) |
| Servidor intermediario | Python 3 + pyserial | Gratis |
| Comunicación | Serial USB (no WiFi) | — |

### Comunicación

```
[Chat / Terminal]
      ↓ texto natural
[Python en PC]
      ↓ llama API Gemini/Groq → obtiene JSON
      ↓ pyserial
[ESP32 por USB]
      ↓ parsea JSON
[Drivers L298N]
      ↓
[Motores Technic]
```

### Skills definidas (MVP)

```json
{"skill": "saludo"}
{"skill": "trabajo", "origen": 3, "destino": 9}
```

El sistema de skills usa un archivo README cargado como system prompt al inicio de cada sesión de chat. La IA interpreta lenguaje natural y genera el JSON correspondiente.

### Presupuesto de latencia estimado

| Etapa | Tiempo |
| ----- | ------ |
| Input usuario → API IA | ~0 ms |
| Procesamiento IA (Gemini Flash / Groq) | ~1000-2000 ms |
| API → Python → Serial | ~20 ms |
| ESP32 ejecuta skill | ~500-3000 ms (según movimiento) |
| **Total percibido** | **~2-5 segundos** |

### Fase 2 (postergado)

- Cámara web USB + Gemini Vision para detección automática de objetos
- El brazo detecta posición del objeto sin intervención manual
