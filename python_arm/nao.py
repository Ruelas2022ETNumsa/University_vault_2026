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

VELOCIDAD = 200          # grados/segundo del MOTOR (todos los motores)
UMBRAL_MV = 5000         # si el voltaje baja de esto, se detienen todos los motores
T_ART = 10000            # tiempo maximo por articulacion (ms)
T_GARRA = 3000           # tiempo maximo para la garra (ms)
ESPERA_INICIO_MS = 500   # espera antes de empezar (tiempo para alejarse)
PAUSA_ETAPA_MS = 1000    # intervalo entre programas (inicio / take / left / inicio)
PAUSA_MOTOR_MS = 0       # intervalo despues de cada motor (0 = como inicio/take/left por separado)

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
    """Un movimiento (+ pausa si PAUSA_MOTOR_MS > 0). Muestra grados de la articulacion y minimo."""
    ok, minimo = mover(motor, objetivo, tiempo)
    print("{} -> {} deg | minimo: {} mV".format(nombre, round(motor.angle() / mult, 1), minimo))
    if ok and PAUSA_MOTOR_MS > 0:
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


def pedir_angulos(titulo):
    """Pide A, C y B. Devuelve {A, C, B} o None si escribe X."""
    print("=== {} ===".format(titulo))
    ang = {}
    for k in ORDEN:
        ang[k] = leer(k)
        if ang[k] is None:
            return None
    return ang


def resumen(titulo, ang):
    print("--- {} ---".format(titulo))
    for k in ORDEN:
        print("{} ({}): {} deg -> motor {} deg".format(
            k, NOMBRES[k], ang[k], int(ang[k] * ART[k][1])))


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


def etapa_take(ang):
    """Garra abre -> A -> C -> B -> garra cierra."""
    print("=== TAKE ===")
    if not paso("Garra abre", garra, GARRA_ABIERTA, T_GARRA):
        return False
    if not articulaciones(ang):
        return False
    return paso("Garra cierra", garra, GARRA_CERRADA, T_GARRA)


def etapa_left(ang):
    """A -> C -> B -> garra abre (la garra sigue cerrada con el objeto durante el traslado)."""
    print("=== LEFT ===")
    if not articulaciones(ang):
        return False
    return paso("Garra abre", garra, GARRA_ABIERTA, T_GARRA)


def programa():
    """Inicio -> pide take y left -> take -> left -> inicio. Devuelve 'ok', 'salida' o 'corte'."""
    wait(ESPERA_INICIO_MS)
    if not inicio():
        return "corte"
    detener_todo()  # termina el inicio: no se sostiene nada mientras se escriben los angulos

    take = pedir_angulos("TAKE")
    if take is None:
        return "salida"
    left = pedir_angulos("LEFT")
    if left is None:
        return "salida"

    while True:
        resumen("TAKE", take)
        resumen("LEFT", left)
        cmd = input("Y=iniciar | X=salir | T=reingresar take | L=reingresar left: ").strip().upper()
        if cmd == "Y":
            break
        if cmd == "X":
            return "salida"
        if cmd == "T":
            take = pedir_angulos("TAKE")
            if take is None:
                return "salida"
        elif cmd == "L":
            left = pedir_angulos("LEFT")
            if left is None:
                return "salida"
        else:
            print("Comando no valido.")

    wait(PAUSA_ETAPA_MS)
    if not etapa_take(take):
        return "corte"
    wait(PAUSA_ETAPA_MS)
    if not etapa_left(left):
        return "corte"
    wait(PAUSA_ETAPA_MS)
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
