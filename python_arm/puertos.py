from pybricks.iodevices import PUPDevice
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait

# puertos.py = detecta QUE hay conectado en cada puerto (A-F) y lo imprime en la consola.
# No mueve ningun motor: solo lee el ID que cada dispositivo reporta al hub.
# Esperado en este brazo: A hombro, C codo, B muneca, F garra (4 motores) + 1 sensor de color (D o E).

# Puertos del hub Inventor 51515
PUERTOS = [
    ("A", Port.A),
    ("B", Port.B),
    ("C", Port.C),
    ("D", Port.D),
    ("E", Port.E),
    ("F", Port.F),
]

# Rol esperado segun ha.py (None = sin rol fijo)
ROLES = {
    "A": "hombro",
    "B": "muneca",
    "C": "codo",
    "F": "garra",
}

# ID LEGO (Powered Up) -> (nombre, tipo)
DISPOSITIVOS = {
    1: ("Motor WeDo 2.0", "motor"),
    2: ("Motor de tren", "motor"),
    8: ("Luces", "otro"),
    34: ("Sensor inclinacion WeDo 2.0", "sensor"),
    35: ("Sensor distancia WeDo 2.0", "sensor"),
    37: ("Sensor color/distancia BOOST", "sensor"),
    38: ("Motor interactivo BOOST", "motor"),
    46: ("Motor Technic L", "motor"),
    47: ("Motor Technic XL", "motor"),
    48: ("Motor mediano Spike/Inventor", "motor"),
    49: ("Motor grande Spike/Inventor", "motor"),
    61: ("Sensor de color", "sensor"),
    62: ("Sensor de distancia", "sensor"),
    63: ("Sensor de fuerza", "sensor"),
    65: ("Motor pequeno Spike", "motor"),
    75: ("Motor mediano Technic", "motor"),
    76: ("Motor grande Technic", "motor"),
}


def leer_id(puerto):
    """Devuelve el ID del dispositivo, o None si no hay nada conectado."""
    try:
        return PUPDevice(puerto).info()["id"]
    except OSError:
        return None


def detalle(tipo, id_, puerto):
    """Dato extra para confirmar que el dispositivo responde."""
    try:
        if tipo == "motor":
            m = Motor(puerto)
            return "angulo actual: {} deg".format(m.angle())
        if tipo == "sensor" and id_ == 61:
            s = ColorSensor(puerto)
            return "color visto: {}".format(s.color())
    except OSError:
        return "(no respondio al leer)"
    return ""


print("== Deteccion de puertos ==")
wait(1000)  # tiempo para que los dispositivos se sincronicen con el hub

motores = 0
sensores = 0
problemas = 0

for letra, puerto in PUERTOS:
    id_ = leer_id(puerto)
    esperado = ROLES.get(letra)

    if id_ is None:
        print("Puerto {}: VACIO".format(letra))
        if esperado:
            print("   !! se esperaba un motor ({})".format(esperado))
            problemas += 1
        continue

    nombre, tipo = DISPOSITIVOS.get(id_, ("Desconocido (id {})".format(id_), "otro"))
    extra = detalle(tipo, id_, puerto)
    linea = "Puerto {}: {} [{}]".format(letra, nombre, tipo)
    if esperado:
        linea += " -> rol {}".format(esperado)
    print(linea)
    if extra:
        print("   " + extra)

    if tipo == "motor":
        motores += 1
        if not esperado:
            print("   ?? motor en puerto sin rol asignado en ha.py")
            problemas += 1
    elif tipo == "sensor":
        sensores += 1
        if esperado:
            print("   !! en ha.py este puerto es un motor ({})".format(esperado))
            problemas += 1
    elif esperado:
        print("   !! se esperaba un motor ({})".format(esperado))
        problemas += 1

print("== Resumen ==")
print("Motores: {} (esperados 4) | Sensores: {} (esperado 1 de color)".format(motores, sensores))
if problemas == 0 and motores == 4 and sensores >= 1:
    print("Todo OK: coincide con ha.py (A hombro, C codo, B muneca, F garra).")
else:
    print("Revisar conexiones: {} aviso(s).".format(problemas))
