from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait, StopWatch

# Cambiar PrimeHub por tu hub: InventorHub, EssentialHub, CityHub, etc.
hub = PrimeHub()

hombro = Motor(Port.A, Direction.CLOCKWISE)
codo = Motor(Port.C, Direction.CLOCKWISE)
muneca = Motor(Port.B, Direction.CLOCKWISE)
garra = Motor(Port.F, Direction.CLOCKWISE)

VELOCIDAD = 200        # grados/segundo (todos los motores)
UMBRAL_MV = 5000       # si el voltaje baja de esto, se detienen todos los motores
PERIODO_MS = 50        # cada cuanto se mide durante el movimiento
TIMEOUT_ART_MS = 10000 # tiempo maximo por movimiento de articulacion
TIMEOUT_GARRA_MS = 3000  # tiempo maximo para la garra
ESPERA_INICIO_MS = 500   # espera antes de empezar a mover (tiempo para alejarse)

# (nombre, motor, multiplicador, timeout) en este orden: B -> C -> A -> garra
# (inverso al de agarrar.py; un solo motor a la vez)
SECUENCIA = [
    ("B muneca", muneca, 3, TIMEOUT_ART_MS),
    ("C codo", codo, 1, TIMEOUT_ART_MS),
    ("A hombro", hombro, 3, TIMEOUT_ART_MS),
    ("F garra", garra, 1, TIMEOUT_GARRA_MS),
]


def detener_todo():
    for m in (hombro, codo, muneca, garra):
        m.stop()


def mover(motor, objetivo, timeout_ms):
    """Mueve al angulo absoluto del motor. Devuelve (ok, minimo_mV).
    ok=False si el voltaje bajo del umbral (y se detuvieron todos los motores).
    Si se agota el tiempo, se frena el motor y se continua (ok=True)."""
    minimo = hub.battery.voltage()
    reloj = StopWatch()
    motor.run_target(VELOCIDAD, objetivo, wait=False)
    while not motor.done():
        v = hub.battery.voltage()
        if v < minimo:
            minimo = v
        if v < UMBRAL_MV:
            detener_todo()
            return False, minimo
        if reloj.time() > timeout_ms:
            motor.hold()
            break
        wait(PERIODO_MS)
    v = hub.battery.voltage()
    if v < minimo:
        minimo = v
    if minimo < UMBRAL_MV:
        detener_todo()
        return False, minimo
    return True, minimo


# --- Programa principal ---
# NO se hace reset_angle: se lee la posicion actual que mide cada motor
# y se lleva a 0 (el cero es el de la ultima calibracion, mientras el hub siga encendido).
wait(ESPERA_INICIO_MS)
print("Posiciones actuales (grados del motor):")
for nombre, motor, mult, timeout in SECUENCIA:
    print("  {}: {} deg motor ({} deg articulacion)".format(
        nombre, motor.angle(), round(motor.angle() / mult, 1)))

ok_total = True
for nombre, motor, mult, timeout in SECUENCIA:
    ok, minimo = mover(motor, 0, timeout)
    print("{} -> {} deg | minimo: {} mV".format(nombre, motor.angle(), minimo))
    if not ok:
        ok_total = False
        break

if ok_total:
    print("Brazo en posicion inicial.")
else:
    print("Voltaje < {} mV -> motores detenidos.".format(UMBRAL_MV))

detener_todo()
print("Programa terminado.")
