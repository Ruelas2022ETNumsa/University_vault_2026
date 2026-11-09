from pybricks.iodevices import PUPDevice
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait, StopWatch
from pybricks.hubs import PrimeHub

# detect_motor.py = prueba los motores UNO POR UNO para identificar visualmente cual es cual.
#   1) detecta los puertos con motor (orden alfabetico A -> F)
#   2) por cada puerto pregunta; con 'y'/'Y' gira 270 deg a 200 deg/s y vuelve a 0
#   3) frena el motor y pasa al siguiente puerto
# Solo hay UN motor activo a la vez (limite de alimentacion por USB/PC).
# Base de movimiento y monitoreo de voltaje: ha.py

# Igual que ha.py (cambiar por tu hub si hace falta)
hub = PrimeHub()

PUERTOS = [
    ("A", Port.A),
    ("B", Port.B),
    ("C", Port.C),
    ("D", Port.D),
    ("E", Port.E),
    ("F", Port.F),
]

# IDs LEGO que corresponden a motores
IDS_MOTOR = (1, 2, 38, 46, 47, 48, 49, 65, 75, 76)

VELOCIDAD = 200          # grados/segundo del MOTOR
GRADOS = 270             # giro de prueba (ida) y luego regresa a 0
UMBRAL_MV = 5000         # si el voltaje baja de esto, se PAUSA el programa
MUESTRAS_CORTE = 3       # muestras SEGUIDAS bajo UMBRAL_MV para pausar
PERIODO_MS = 20          # cada cuanto se mide durante el movimiento
TIMEOUT_MS = 10000       # tiempo maximo por movimiento
HOLD_MUESTRA_MS = 300    # espera corta tras cada movimiento


def es_motor(puerto):
    """True si el puerto tiene un motor conectado."""
    try:
        return PUPDevice(puerto).info()["id"] in IDS_MOTOR
    except OSError:
        return False


def pausar(letra, motor, v, i):
    """Voltaje bajo sostenido: espera 'g' + Enter para continuar, 'x' para abortar.
    Devuelve True si se continua, False si se aborta."""
    motor.hold()
    print("  !! VOLTAJE BAJO en {}: {} mV con {} mA".format(letra, v, i))
    while True:
        texto = input("  PAUSA. 'g' + Enter = continuar | 'x' = abortar: ").strip().lower()
        if texto == "g":
            return True
        if texto == "x":
            motor.stop()
            return False
        print("  Escribi 'g' para continuar o 'x' para abortar.")


def mover(letra, motor, objetivo):
    """Mueve al angulo absoluto del motor vigilando el voltaje.
    Devuelve False solo si el usuario aborta ('x') durante una pausa."""
    bajos = 0
    vmin = hub.battery.voltage()
    imax = hub.battery.current()
    reloj = StopWatch()
    motor.run_target(VELOCIDAD, objetivo, wait=False)
    while not motor.done():
        v = hub.battery.voltage()
        i = hub.battery.current()
        if v < vmin:
            vmin = v
        if i > imax:
            imax = i
        if v < UMBRAL_MV:
            bajos += 1
            if bajos >= MUESTRAS_CORTE:
                bajos = 0
                if not pausar(letra, motor, v, i):
                    return False
                motor.run_target(VELOCIDAD, objetivo, wait=False)
                reloj = StopWatch()
                continue
        else:
            bajos = 0
        if reloj.time() > TIMEOUT_MS:
            motor.hold()
            print("  ! timeout en puerto", letra)
            break
        wait(PERIODO_MS)
    wait(HOLD_MUESTRA_MS)
    print("  mon {}: Vmin {} mV | Imax {} mA".format(letra, vmin, imax))
    return True


def probar(letra, puerto):
    """Prueba UN motor: 0 -> 270 -> 0 y lo frena. Devuelve False si el usuario aborta."""
    motor = Motor(puerto, Direction.CLOCKWISE)
    motor.reset_angle(0)  # el 0 es la posicion actual
    print("  Girando puerto {} (motor activo)...".format(letra))
    ok = mover(letra, motor, GRADOS)
    if ok:
        ok = mover(letra, motor, 0)
    if ok:
        print("  Puerto {} -> volvio a {} deg".format(letra, motor.angle()))
    motor.stop()  # suelta el motor antes de pasar al siguiente
    return ok


# --- Programa principal ---
print("== Prueba de motores, uno por uno ==")
print("Bateria en reposo: {} mV, {} mA".format(hub.battery.voltage(), hub.battery.current()))
wait(1000)  # tiempo para que los dispositivos se sincronicen

registrados = []
for letra, puerto in PUERTOS:
    if es_motor(puerto):
        registrados.append((letra, puerto))

if not registrados:
    print("No se detecto ningun motor.")
else:
    nombres = ""
    for letra, puerto in registrados:
        nombres += letra + " "
    print("Motores detectados (orden alfabetico): " + nombres)
    print("Por cada puerto: 'y' = girar {} deg a {} deg/s y volver a 0 | otra tecla = saltar | 'x' = salir".format(
        GRADOS, VELOCIDAD))

    for letra, puerto in registrados:
        cmd = input("Puerto {}: proceder? (y/Y): ".format(letra)).strip().lower()
        if cmd == "x":
            break
        if cmd != "y":
            print("  Puerto {} saltado.".format(letra))
            continue
        if not probar(letra, puerto):
            print("Prueba abortada por el usuario (x) tras voltaje bajo -> motor detenido.")
            break

print("Programa terminado. Bateria final: {} mV".format(hub.battery.voltage()))
