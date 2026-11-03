from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait, StopWatch

# uni.py = inicio.py + take.py + left.py en un solo flujo:
#   pide angulos de take -> pide angulos de left -> take -> left -> inicio

# Cambiar PrimeHub por tu hub: InventorHub, EssentialHub, CityHub, etc.
hub = PrimeHub()

hombro = Motor(Port.A, Direction.CLOCKWISE)
codo = Motor(Port.C, Direction.CLOCKWISE)
muneca = Motor(Port.B, Direction.CLOCKWISE)
garra = Motor(Port.F, Direction.CLOCKWISE)

VELOCIDAD = 200          # grados/segundo del MOTOR (todos los motores)
UMBRAL_MV = 5000         # si el voltaje baja de esto, se detienen todos los motores
PERIODO_MS = 50          # cada cuanto se mide durante el movimiento
TIMEOUT_ART_MS = 10000   # tiempo maximo por movimiento de articulacion
TIMEOUT_GARRA_MS = 3000  # tiempo maximo para la garra
ESPERA_INICIO_MS = 500   # espera antes de volver a inicio (tiempo para alejarse)

GARRA_ABIERTA = 90
GARRA_CERRADA = 0

# nombre: (motor, multiplicador, minimo, maximo)  -> rangos en grados de la ARTICULACION
# El motor gira (angulo x multiplicador) para que la articulacion se mueva el angulo ingresado.
ARTICULACIONES = {
    "A": (hombro, 3, 0, 270),
    "C": (codo, 1, -180, 45),
    "B": (muneca, 3, 0, 190),
}
ORDEN = ["A", "C", "B"]
NOMBRES = {"A": "hombro", "C": "codo", "B": "muneca"}

# Secuencia de inicio: (nombre, motor, multiplicador, timeout) en orden B -> C -> A -> garra
SECUENCIA_INICIO = [
    ("B muneca", muneca, 3, TIMEOUT_ART_MS),
    ("C codo", codo, 1, TIMEOUT_ART_MS),
    ("A hombro", hombro, 3, TIMEOUT_ART_MS),
    ("F garra", garra, 1, TIMEOUT_GARRA_MS),
]


# ---------------- Utilidades comunes ----------------

def detener_todo():
    for m in (hombro, codo, muneca, garra):
        m.stop()


def a_articulacion(motor, mult):
    """Convierte los grados medidos por el motor a grados de la articulacion."""
    return round(motor.angle() / mult, 1)


def mover(motor, objetivo, timeout_ms):
    """Mueve al angulo absoluto del MOTOR. Devuelve (ok, minimo_mV).
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


def pedir_angulo(titulo, clave):
    """Pide el angulo de una articulacion hasta que este en rango. Devuelve None si escribe X."""
    motor, mult, vmin, vmax = ARTICULACIONES[clave]
    while True:
        texto = input("[{}] {} ({}) [{} a {}]: ".format(
            titulo, clave, NOMBRES[clave], vmin, vmax)).strip().lower()
        if texto == "x":
            return None
        try:
            valor = float(texto)
        except ValueError:
            print("Valor no valido, escribi un numero (o 'x' para salir).")
            continue
        if valor < vmin or valor > vmax:
            print("Fuera de rango [{} a {}].".format(vmin, vmax))
            continue
        return valor


def mover_articulaciones(angulos):
    """Mueve A -> C -> B a los angulos indicados. Devuelve False si hubo corte por voltaje."""
    for k in ORDEN:
        motor, mult, vmin, vmax = ARTICULACIONES[k]
        objetivo = int(angulos[k] * mult)
        ok, minimo = mover(motor, objetivo, TIMEOUT_ART_MS)
        print("{} -> {} deg articulacion (motor {} deg) | minimo: {} mV".format(
            k, a_articulacion(motor, mult), motor.angle(), minimo))
        if not ok:
            return False
    return True


# ---------------- Fases ----------------

def ejecutar_take(angulos):
    """Garra abre -> A -> C -> B -> garra cierra."""
    ok, minimo = mover(garra, GARRA_ABIERTA, TIMEOUT_GARRA_MS)
    print("Garra abierta | minimo:", minimo, "mV")
    if not ok:
        return False

    if not mover_articulaciones(angulos):
        return False

    ok, minimo = mover(garra, GARRA_CERRADA, TIMEOUT_GARRA_MS)
    print("Garra cerrada | minimo:", minimo, "mV")
    return ok


def ejecutar_left(angulos):
    """A -> C -> B -> garra abre (suelta el objeto)."""
    if not mover_articulaciones(angulos):
        return False

    ok, minimo = mover(garra, GARRA_ABIERTA, TIMEOUT_GARRA_MS)
    print("Garra abierta | minimo:", minimo, "mV")
    return ok


def ejecutar_inicio():
    """B -> C -> A -> garra, todos a 0 (posicion de calibracion)."""
    wait(ESPERA_INICIO_MS)
    for nombre, motor, mult, timeout in SECUENCIA_INICIO:
        ok, minimo = mover(motor, 0, timeout)
        print("{} -> {} deg | minimo: {} mV".format(nombre, motor.angle(), minimo))
        if not ok:
            return False
    return True


# ---------------- Interfaz ----------------

def mostrar_resumen(ang_take, ang_left):
    print("--- Resumen ---")
    print("TAKE: garra abre a", GARRA_ABIERTA, "al inicio, cierra a", GARRA_CERRADA, "al final")
    for k in ORDEN:
        mult = ARTICULACIONES[k][1]
        print("  T{} ({}): {} deg articulacion -> motor {} deg (x{})".format(
            k, NOMBRES[k], ang_take[k], int(ang_take[k] * mult), mult))
    print("LEFT: garra cerrada durante el traslado, abre a", GARRA_ABIERTA, "al llegar")
    for k in ORDEN:
        mult = ARTICULACIONES[k][1]
        print("  L{} ({}): {} deg articulacion -> motor {} deg (x{})".format(
            k, NOMBRES[k], ang_left[k], int(ang_left[k] * mult), mult))
    print("INICIO: vuelve a 0 (B -> C -> A -> garra)")


def pedir_set(titulo):
    """Pide A, C, B para una fase. Devuelve el dict o None si el usuario sale."""
    angulos = {}
    for k in ORDEN:
        valor = pedir_angulo(titulo, k)
        if valor is None:
            return None
        angulos[k] = valor
    return angulos


# --- Programa principal ---
# Se asume que el brazo esta en su posicion de calibracion: este es el 0 de cada motor.
# Un solo reset al principio: take, left e inicio comparten las mismas coordenadas.
for m in (hombro, codo, muneca, garra):
    m.reset_angle(0)

print("Escribi 'x' para salir. Rangos: A 0-270, C -180 a 45, B 0-190.")

print("== Angulos para TAKE ==")
ang_take = pedir_set("TAKE")
ang_left = None
if ang_take is not None:
    print("== Angulos para LEFT ==")
    ang_left = pedir_set("LEFT")

salir = ang_take is None or ang_left is None

while not salir:
    mostrar_resumen(ang_take, ang_left)
    cmd = input("Y=iniciar | X=salir | TA/TC/TB o LA/LC/LB=reingresar: ").strip().lower()

    if cmd == "x":
        break
    elif cmd in ("ta", "tc", "tb"):
        valor = pedir_angulo("TAKE", cmd[1].upper())
        if valor is None:
            break
        ang_take[cmd[1].upper()] = valor
    elif cmd in ("la", "lc", "lb"):
        valor = pedir_angulo("LEFT", cmd[1].upper())
        if valor is None:
            break
        ang_left[cmd[1].upper()] = valor
    elif cmd == "y":
        ok = ejecutar_take(ang_take)
        if ok:
            print("Toma del objeto terminada.")
            ok = ejecutar_left(ang_left)
        if ok:
            print("Objeto soltado.")
            ok = ejecutar_inicio()
        if ok:
            print("Brazo en posicion inicial. Secuencia completa.")
        else:
            print("Voltaje < {} mV -> motores detenidos.".format(UMBRAL_MV))
        break
    else:
        print("Comando no valido.")

detener_todo()
print("Programa terminado.")
