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

VELOCIDAD = 250          # grados/segundo
UMBRAL_MV = 5000         # si el voltaje baja de esto, se detienen todos los motores
PERIODO_MS = 50          # cada cuanto se mide durante el movimiento
PRINT_CADA_MS = 100      # cada cuanto se muestra el voltaje en pantalla
TIMEOUT_MS = 15000       # tiempo maximo por movimiento

# nombre: (motor, multiplicador)  -> sin limites de rango en este programa
ARTICULACIONES = {
    "A": (hombro, 3),
    "C": (codo, 1),
    "B": (muneca, 3),
}
NOMBRES = {"A": "hombro", "C": "codo", "B": "muneca"}


def detener_todo():
    for m in (hombro, codo, muneca, garra):
        m.stop()


def pedir_motor():
    """Pide A, C o B. Devuelve la clave en mayuscula, o None si escribe X."""
    while True:
        texto = input("Motor a ajustar (A/C/B) o X para salir: ").strip().upper()
        if texto == "X":
            return None
        if texto in ARTICULACIONES:
            return texto
        print("Escribi A, C o B (o X para salir).")


def pedir_angulo(clave):
    """Pide un angulo de la articulacion, sin limites. Devuelve None si escribe X."""
    while True:
        texto = input("Angulo de {} ({}) en grados (X para cancelar): ".format(clave, NOMBRES[clave])).strip().lower()
        if texto == "x":
            return None
        try:
            return float(texto)
        except ValueError:
            print("Valor no valido, escribi un numero.")


def mover(nombre, motor, objetivo):
    """Mueve UN solo motor al angulo absoluto del motor. Devuelve True si no hubo corte por voltaje."""
    v = hub.battery.voltage()
    minimo = v
    print("  [{}] inicio: {} mV".format(nombre, v))
    reloj = StopWatch()
    ultimo_print = 0
    motor.run_target(VELOCIDAD, objetivo, wait=False)
    while not motor.done():
        v = hub.battery.voltage()
        if v < minimo:
            minimo = v
        t = reloj.time()
        if t - ultimo_print >= PRINT_CADA_MS:
            print("  [{}] t={} ms  V={} mV".format(nombre, t, v))
            ultimo_print = t
        if v < UMBRAL_MV:
            detener_todo()
            print("  [{}] CORTE: {} mV < {}".format(nombre, v, UMBRAL_MV))
            return False
        if t > TIMEOUT_MS:
            motor.hold()
            print("  [{}] tiempo agotado, hold()".format(nombre))
            break
        wait(PERIODO_MS)
    print("  [{}] fin | minimo: {} mV".format(nombre, minimo))
    return True


# --- Programa principal ---
# NO se hace reset_angle: el 0 es el de la ultima calibracion mientras el hub siga encendido.
print("Ajuste de posicion. Multiplicadores: A x3, C x1, B x3. Sin limites de angulo.")
print("Voltaje inicial:", hub.battery.voltage(), "mV")

while True:
    for k, (m, mult) in ARTICULACIONES.items():
        print("{} ({}): {} deg articulacion ({} deg motor)".format(
            k, NOMBRES[k], round(m.angle() / mult, 1), m.angle()))

    clave = pedir_motor()
    if clave is None:
        break

    angulo = pedir_angulo(clave)
    if angulo is None:
        continue

    motor, mult = ARTICULACIONES[clave]
    objetivo = int(angulo * mult)
    print("{}: {} deg x {} = {} deg motor".format(clave, angulo, mult, objetivo))

    if not mover(clave, motor, objetivo):
        print("Voltaje < {} mV -> motores detenidos.".format(UMBRAL_MV))
        break

detener_todo()
print("Programa terminado.")
