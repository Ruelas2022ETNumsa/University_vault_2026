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

VELOCIDAD = 200          # grados/segundo del MOTOR
UMBRAL_MV = 5000         # si el voltaje baja de esto, se detienen todos los motores
T_ART = 10000            # tiempo maximo por articulacion (ms)
T_GARRA = 3000           # tiempo maximo para la garra (ms)
ESPERA_INICIO_MS = 500   # espera antes de empezar
PAUSA_ETAPA_MS = 1000    # intervalo entre etapas (inicio / take / left / inicio)
PAUSA_MOTOR_MS = 4000    # intervalo despues de cada motor (bajar a 0 para probar sin pausas)

GARRA_ABIERTA = 90
GARRA_CERRADA = 0

# nombre: (motor, multiplicador, minimo, maximo)  -> rangos en grados de la ARTICULACION
ART = {
    "A": (hombro, 3, 0, 270),
    "C": (codo, 1, -180, 45),
    "B": (muneca, 3, 0, 190),
}
ORDEN = "ACB"
NOMBRES = {"A": "hombro", "C": "codo", "B": "muneca"}

# Orden para volver al inicio: B -> C -> A -> garra   (nombre, motor, multiplicador, tiempo)
VUELTA = [
    ("B", muneca, 3, T_ART),
    ("C", codo, 1, T_ART),
    ("A", hombro, 3, T_ART),
    ("Garra", garra, 1, T_GARRA),
]


def detener_todo():
    for m in (hombro, codo, muneca, garra):
        m.stop()


def mover(motor, objetivo, tiempo):
    """Mueve un motor al angulo absoluto del MOTOR. Devuelve (ok, minimo_mV)."""
    minimo = hub.battery.voltage()
    reloj = StopWatch()
    motor.run_target(VELOCIDAD, objetivo, wait=False)
    while not motor.done():
        v = hub.battery.voltage()
        minimo = min(minimo, v)
        if v < UMBRAL_MV:
            detener_todo()
            return False, minimo
        if reloj.time() > tiempo:
            motor.hold()
            break
        wait(50)
    minimo = min(minimo, hub.battery.voltage())
    if minimo < UMBRAL_MV:
        detener_todo()
        return False, minimo
    return True, minimo


def paso(nombre, motor, objetivo, tiempo, mult=1):
    """Un movimiento + pausa. Muestra los grados de la articulacion y el minimo de voltaje."""
    ok, minimo = mover(motor, objetivo, tiempo)
    print("{} -> {} deg | minimo: {} mV".format(nombre, round(motor.angle() / mult, 1), minimo))
    if ok:
        wait(PAUSA_MOTOR_MS)
    return ok


def leer(clave):
    """Pide el angulo de una articulacion dentro de su rango. None si escribe X."""
    vmin, vmax = ART[clave][2], ART[clave][3]
    while True:
        texto = input("{} ({}) [{} a {}]: ".format(clave, NOMBRES[clave], vmin, vmax)).strip().lower()
        if texto == "x":
            return None
        try:
            valor = float(texto)
        except ValueError:
            print("Escribi un numero (o 'x' para salir).")
            continue
        if vmin <= valor <= vmax:
            return valor
        print("Fuera de rango [{} a {}].".format(vmin, vmax))


def pedir(titulo):
    """Pide A, C, B y el menu Y/X/A/C/B. Devuelve {A, C, B} o None si escribe X."""
    print("=== {} ===".format(titulo))
    ang = {}
    for k in ORDEN:
        ang[k] = leer(k)
        if ang[k] is None:
            return None
    while True:
        for k in ORDEN:
            print("{} ({}): {} deg -> motor {} deg".format(
                k, NOMBRES[k], ang[k], int(ang[k] * ART[k][1])))
        cmd = input("Y=iniciar | X=salir | A/C/B=reingresar: ").strip().upper()
        if cmd == "Y":
            return ang
        if cmd == "X":
            return None
        if cmd in ART:
            valor = leer(cmd)
            if valor is None:
                return None
            ang[cmd] = valor
        else:
            print("Comando no valido.")


def articulaciones(ang):
    """A -> C -> B."""
    for k in ORDEN:
        motor, mult = ART[k][0], ART[k][1]
        if not paso(k, motor, int(ang[k] * mult), T_ART, mult):
            return False
    return True


def inicio():
    """Lee la posicion actual de cada motor y lo lleva a 0 (sin reset_angle)."""
    print("=== INICIO ===")
    for nombre, motor, mult, tiempo in VUELTA:
        print("  {}: {} deg".format(nombre, round(motor.angle() / mult, 1)))
    for nombre, motor, mult, tiempo in VUELTA:
        if not paso(nombre, motor, 0, tiempo, mult):
            return False
    return True


def take(ang):
    """Garra abre -> A -> C -> B -> garra cierra."""
    if not paso("Garra abre", garra, GARRA_ABIERTA, T_GARRA):
        return False
    if not articulaciones(ang):
        return False
    return paso("Garra cierra", garra, GARRA_CERRADA, T_GARRA)


def left(ang):
    """A -> C -> B -> garra abre."""
    if not articulaciones(ang):
        return False
    return paso("Garra abre", garra, GARRA_ABIERTA, T_GARRA)


def esperar_p(siguiente):
    """Fin de un programa: suelta TODOS los motores (no se sostiene nada, como si el programa
    anterior hubiera terminado) y espera P para iniciar el siguiente. False si escribe X."""
    detener_todo()
    while True:
        cmd = input("P=iniciar {} | X=salir: ".format(siguiente)).strip().upper()
        if cmd == "P":
            wait(PAUSA_ETAPA_MS)
            return True
        if cmd == "X":
            return False
        print("Escribi P o X.")


def programa():
    """Inicio -P-> take -P-> left -P-> inicio. Devuelve 'ok', 'salida' (X) o 'corte' (voltaje)."""
    wait(ESPERA_INICIO_MS)
    if not inicio():
        return "corte"

    if not esperar_p("TAKE"):
        return "salida"
    a = pedir("TAKE")
    if a is None:
        return "salida"
    if not take(a):
        return "corte"

    if not esperar_p("LEFT"):
        return "salida"
    b = pedir("LEFT")
    if b is None:
        return "salida"
    if not left(b):
        return "corte"

    if not esperar_p("INICIO"):
        return "salida"
    return "ok" if inicio() else "corte"


# --- Programa principal ---
# Sin reset_angle: el cero es el de la ultima calibracion (hub encendido).
print("Rangos: A 0-270, C -180 a 45, B 0-190. 'x' para salir.")
resultado = programa()
if resultado == "corte":
    print("Voltaje < {} mV -> motores detenidos.".format(UMBRAL_MV))
else:
    print("Secuencia completa." if resultado == "ok" else "Salida solicitada.")
detener_todo()
print("Programa terminado.")
