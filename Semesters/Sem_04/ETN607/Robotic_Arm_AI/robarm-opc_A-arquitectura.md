---
galaxy_body: dropship
carrier: "[[Semesters/Sem_04/ETN607/Robotic_Arm_AI/tsk_carrier.md]]"
scope: arquitectura
status: activo
date: 2026-09-13
---

## Proposito

Documenta la arquitectura de software del sistema: servidor Python intermediario en PC, integración con IA (Claude + Gemini Flash), protocolo de comunicación USB Serial hacia el EV3 Brick, y estructura de skills.

---

## Contenido

### Flujo completo

```
1. Usuario escribe en chat o terminal:
   → "modo demo" / "tomar de las 3, poner en las 9"

2. Python carga skill_readme.md como system prompt (solo al inicio de sesión)

3. Gemini Flash interpreta el pedido → genera JSON:
   → {"skill":"saludo"}
   → {"skill":"trabajo","origen":3,"destino":9}

4. Python recibe JSON → lo envía por USB Serial al EV3 Brick (python-ev3dev)

5. EV3 Brick parsea JSON → ejecuta skill → mueve servomotores con encoder

6. EV3 confirma posición final → Python puede registrar o mostrar resultado
```

> Claude actúa como orquestador de alto nivel (razonamiento, visión en fase 2).
> Gemini Flash actúa como delegado rápido de traducción lenguaje natural → JSON.

---

### Estructura del skill README (system prompt)

```markdown
# BRAZO ROBÓTICO EV3 — SKILLS DISPONIBLES

Sos el controlador de un brazo robótico LEGO EV3. Respondé SOLO con JSON válido.

## skill_saludo
El brazo ejecuta secuencia de saludo (movimiento arriba/abajo repetido).
Parámetros: ninguno
Respuesta: {"skill":"saludo"}

## skill_trabajo
Toma objeto en posición origen y lo mueve a posición destino.
Posiciones en formato reloj (1-12).
Respuesta: {"skill":"trabajo","origen":X,"destino":Y}

## skill_home
El brazo vuelve a posición inicial calibrada.
Parámetros: ninguno
Respuesta: {"skill":"home"}

Respondé SOLO con el JSON. Sin texto adicional.
```

---

### Código EV3 — estructura (MicroPython / Pybricks)

```python
#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor
from pybricks.parameters import Port, Stop, Direction
from pybricks.tools import wait
import ujson

ev3 = EV3Brick()

# Motores del Robot Arm H25
gripper_motor = Motor(Port.A)
elbow_motor   = Motor(Port.B, Direction.COUNTERCLOCKWISE, [8, 40])
base_motor    = Motor(Port.C, Direction.COUNTERCLOCKWISE, [12, 36])

# Sensores para homing
touch_elbow = TouchSensor(Port.S2)
touch_base  = TouchSensor(Port.S1)

def home():
    # Calibrar posición inicial con Touch Sensors
    while not touch_base.pressed():
        base_motor.run(-200)
    base_motor.reset_angle(0)
    base_motor.hold()

    while not touch_elbow.pressed():
        elbow_motor.run(-200)
    elbow_motor.reset_angle(0)
    elbow_motor.hold()

    gripper_motor.run_until_stalled(200, then=Stop.HOLD)
    gripper_motor.reset_angle(0)

def skill_saludo():
    for _ in range(3):
        elbow_motor.run_angle(200, 30)
        elbow_motor.run_angle(200, -30)

def skill_trabajo(origen, destino):
    angulo_origen  = origen  * 30   # 360° / 12 posiciones = 30° por posición
    angulo_destino = destino * 30
    base_motor.run_target(200, angulo_origen)
    elbow_motor.run_angle(200, 45)           # bajar
    gripper_motor.run_angle(200, -90)         # cerrar garra
    elbow_motor.run_angle(200, -45)           # subir
    base_motor.run_target(200, angulo_destino)
    elbow_motor.run_angle(200, 45)            # bajar
    gripper_motor.run_angle(200, 90)          # abrir garra
    elbow_motor.run_angle(200, -45)           # subir

# Bucle principal — escucha JSON por USB stdin
home()
while True:
    line = input()
    cmd = ujson.loads(line)
    skill = cmd.get("skill")
    if skill == "saludo":
        skill_saludo()
    elif skill == "trabajo":
        skill_trabajo(cmd["origen"], cmd["destino"])
    elif skill == "home":
        home()
    print(ujson.dumps({"status": "ok", "skill": skill}))
```

---

### Código Python intermediario en PC

```python
import subprocess
import json
import google.generativeai as genai  # pip install google-generativeai

# Cargar system prompt
with open("skill_readme.md") as f:
    system_prompt = f.read()

# Configurar Gemini Flash (Google AI Studio — tier gratuito)
genai.configure(api_key="TU_API_KEY")
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    system_instruction=system_prompt
)

# Conectar al EV3 por USB (ev3dev expone stdin/stdout del programa)
# Alternativa: usar ev3dev-lang-python con RPyC o USB serial directo
import serial
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=5)  # Linux; en Windows: 'COM3'

def pedir_a_ia(mensaje_usuario):
    respuesta = model.generate_content(mensaje_usuario)
    return json.loads(respuesta.text.strip())

while True:
    cmd = input("→ ")
    try:
        json_skill = pedir_a_ia(cmd)
        ser.write((json.dumps(json_skill) + '\n').encode())
        confirmacion = ser.readline().decode().strip()
        print(f"EV3: {confirmacion}")
    except Exception as e:
        print(f"Error: {e}")
```

---

### APIs y librerías

| Componente | Tecnología | Tier gratuito |
| ---------- | ---------- | ------------- |
| Orquestador IA | Claude (claude.ai free) | Sí |
| Traducción → JSON | Gemini 2.0 Flash (Google AI Studio) | Sí, sin tarjeta |
| Firmware EV3 | MicroPython (Pybricks) o ev3dev Python | Gratis |
| Comunicación PC↔EV3 | pyserial + USB Mini-B | — |

---

### Estado de implementación

- [ ] Instalar ev3dev o Pybricks en EV3 Brick (microSD)
- [ ] Implementar código EV3 base (homing + skills)
- [ ] Implementar servidor Python en PC
- [ ] Crear skill_readme.md de producción
- [ ] Obtener API key Gemini Flash (Google AI Studio)
- [ ] Probar integración end-to-end
- [ ] Agregar skill home/reset
