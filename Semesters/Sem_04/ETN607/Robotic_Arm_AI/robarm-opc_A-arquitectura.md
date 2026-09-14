---
galaxy_body: dropship
carrier: "[[Semesters/Sem_04/ETN607/Robotic_Arm_AI/tsk_carrier.md]]"
scope: opcion-A
status: activo
date: 2026-09-13
---

## Proposito

Documenta la arquitectura de software del sistema: servidor Python intermediario, integración con API de IA gratuita, protocolo de comunicación Serial, y estructura de skills para el carrier Robotic Arm AI.

---

## Contenido

### Flujo completo

```
1. Usuario escribe en chat/terminal:
   → "modo demo" / "tomar de las 3, poner en las 9"

2. Python carga skill_readme.md como system prompt (solo al inicio)

3. API Gemini/Groq interpreta el pedido → genera JSON:
   → {"skill":"saludo"}
   → {"skill":"trabajo","origen":3,"destino":9}

4. Python recibe JSON → lo envía por pyserial al ESP32

5. ESP32 parsea JSON → ejecuta skill hardcodeada → mueve motores
```

### Estructura del skill README (system prompt)

```markdown
# BRAZO ROBÓTICO - SKILLS DISPONIBLES

Sos el controlador de un brazo robótico. Respondé SOLO con JSON válido.

## skill_saludo
El brazo ejecuta secuencia de saludo (ondas arriba/abajo).
Parámetros: ninguno
Respuesta: {"skill":"saludo"}

## skill_trabajo
Toma objeto en posición origen y lo mueve a destino.
Posiciones en formato reloj (1-12).
Respuesta: {"skill":"trabajo","origen":X,"destino":Y}

Respondé SOLO con el JSON. Sin texto adicional.
```

### Código ESP32 (estructura)

```cpp
// ESP32 escucha Serial, parsea JSON, ejecuta skill
#include <ArduinoJson.h>

void loop() {
  if (Serial.available()) {
    String input = Serial.readStringUntil('\n');
    StaticJsonDocument<200> doc;
    deserializeJson(doc, input);
    
    String skill = doc["skill"];
    
    if (skill == "saludo") ejecutarSaludo();
    if (skill == "trabajo") {
      int origen = doc["origen"];
      int destino = doc["destino"];
      ejecutarTrabajo(origen, destino);
    }
  }
}
```

### Código Python intermediario (estructura)

```python
import serial
import json
import requests  # o google.generativeai para Gemini

# Cargar system prompt
with open("skill_readme.md") as f:
    system_prompt = f.read()

ser = serial.Serial('COM3', 9600)  # ajustar puerto

def pedir_a_ia(mensaje_usuario):
    # llamada a Groq o Gemini con system_prompt + mensaje
    respuesta = llamar_api(system_prompt, mensaje_usuario)
    return json.loads(respuesta)

while True:
    cmd = input("→ ")
    json_skill = pedir_a_ia(cmd)
    ser.write((json.dumps(json_skill) + '\n').encode())
```

### APIs gratuitas compatibles

| API | Modelo recomendado | Tier gratuito |
| --- | ------------------ | ------------- |
| Google AI Studio | Gemini 2.0 Flash | Sí, sin tarjeta |
| Groq | Llama 3.1 8B | Sí, sin tarjeta |
| DeepSeek | DeepSeek V3 | Sí, con registro |

### Estado

- [ ] Implementar código ESP32 base
- [ ] Implementar servidor Python
- [ ] Crear skill_readme.md de producción
- [ ] Probar integración end-to-end
