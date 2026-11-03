from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.tools import wait, StopWatch

# Cambiar PrimeHub por tu hub: InventorHub, EssentialHub, CityHub, etc.
hub = PrimeHub()

hombro = Motor(Port.A, Direction.CLOCKWISE)
codo = Motor(Port.C, Direction.CLOCKWISE)
muneca = Motor(Port.B, Direction.CLOCKWISE)
garra = Motor(Port.F, Direction.CLOCKWISE)

VELOCIDAD = 200          # grados/segundo del MOTOR (todos los motores)
UMBRAL_MV = 5000         # si el voltaje baja de esto durante un movimiento, se detienen todos
PERIODO_MS = 50          # cada cuanto se mide durante el movimiento
TIMEOUT_ART_MS = 10000   # tiempo maximo por movimiento de articulacion
TIMEOUT_GARRA_MS = 3000  # la garra puede quedar frenada por el objeto
ESPERA_INICIO_MS = 500   # espera antes de empezar (tiempo para alejarse)
PAUSA_ETAPA_MS = 1000    # intervalo entre una etapa y la siguiente
PAUSA_MOTOR_MS = 4000    # intervalo despues de cada motor

UMBRAL_REINTENTO_MV = 6000  # en reposo, antes de mover un motor: si el voltaje es menor, espera y reintenta
PAUSA_REINTENTO_MS = 1000   # espera entre reintentos
MAX_REINTENTOS = 30         # tras estos reintentos seguidos (30 s) sin recuperar, se aborta

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

# Que motores se quedan SUJETOS (hold) al terminar su movimiento. Los demas se frenan (brake)
# sin seguir empujando, para no acumular consumo. Ajustar segun lo que el brazo aguante:
# si una articulacion se cae por gravedad al soltarla, ponerla en True.
MANTENER = {"A": True, "C": True, "B": False}

# Orden para volver a la posicion inicial (inverso al de take): B -> C -> A -> garra
# (nombre, motor, multiplicador, timeout, mantener)
SECUENCIA_INICIO = [
    ("B muneca", muneca, 3, TIMEOUT_ART_MS, MANTENER["B"]),
    ("C codo", codo, 1, TIMEOUT_ART_MS, MANTENER["C"]),
    ("A hombro", hombro, 3, TIMEOUT_ART_MS, MANTENER["A"]),
    ("F garra", garra, 1, TIMEOUT_GARRA_MS, False),
]


def detener_todo():
    for m in (hombro, codo, muneca, garra):
        m.stop()


def a_articulacion(motor, mult):
    """Convierte los grados medidos por el motor a grados de la articulacion."""
    return round(motor.angle() / mult, 1)


def esperar_voltaje():
    """En reposo, antes de mover un motor: mientras el voltaje sea < UMBRAL_REINTENTO_MV
    espera 1 s y vuelve a medir. Devuelve False si no se recupera tras MAX_REINTENTOS."""
    intentos = 0
    v = hub.battery.voltage()
    while v < UMBRAL_REINTENTO_MV:
        if intentos >= MAX_REINTENTOS:
            print("  Voltaje en reposo sigue bajo: {} mV < {} tras {} reintentos".format(
                v, UMBRAL_REINTENTO_MV, MAX_REINTENTOS))
            return False
        intentos += 1
        print("  Reposo {} mV < {} -> espero 1 s ({}/{})".format(
            v, UMBRAL_REINTENTO_MV, intentos, MAX_REINTENTOS))
        wait(PAUSA_REINTENTO_MS)
        v = hub.battery.voltage()
    return True


def mover(motor, objetivo, timeout_ms, mantener):
    """Mueve al angulo absoluto del MOTOR. Devuelve (ok, minimo_mV).
    mantener=True: al llegar queda sujeto (hold). mantener=False: queda frenado (brake).
    ok=False si el voltaje bajo del umbral (y se detuvieron todos los motores).
    Si se agota el tiempo, se frena el motor y se continua (ok=True)."""
    if not esperar_voltaje():
        detener_todo()
        return False, hub.battery.voltage()
    minimo = hub.battery.voltage()
    reloj = StopWatch()
    motor.run_target(VELOCIDAD, objetivo, then=(Stop.HOLD if mantener else Stop.BRAKE), wait=False)
    while not motor.done():
        v = hub.battery.voltage()
        if v < minimo:
            minimo = v
        if v < UMBRAL_MV:
            detener_todo()
            return False, minimo
        if reloj.time() > timeout_ms:
            if mantener:
                motor.hold()
            else:
                motor.brake()
            break
        wait(PERIODO_MS)
    v = hub.battery.voltage()
    if v < minimo:
        minimo = v
    if minimo < UMBRAL_MV:
        detener_todo()
        return False, minimo
    return True, minimo


def pausa_motor(nombre):
    """Pausa despues de un motor y muestra voltaje y corriente en reposo (para ubicar el consumo)."""
    wait(PAUSA_MOTOR_MS)
    print("  reposo tras {}: {} mV, {} mA".format(
        nombre, hub.battery.voltage(), hub.battery.current()))


def pedir_angulo(clave):
    """Pide el angulo de una articulacion hasta que este en rango. Devuelve None si escribe X."""
    motor, mult, vmin, vmax = ARTICULACIONES[clave]
    while True:
        texto = input("{} ({}) [{} a {}]: ".format(clave, NOMBRES[clave], vmin, vmax)).strip().lower()
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


def mostrar_resumen(titulo, angulos, texto_garra):
    print("--- Resumen {} ---".format(titulo))
    print("Garra:", texto_garra)
    for k in ORDEN:
        mult = ARTICULACIONES[k][1]
        print("{} ({}): {} deg articulacion -> motor gira {} deg (x{})".format(
            k, NOMBRES[k], angulos[k], int(angulos[k] * mult), mult))


def pedir_coordenadas(titulo, texto_garra):
    """Pide A, C, B y luego el menu Y/X/A/C/B. Devuelve el dict de angulos o None si escribe X."""
    print("=== {} ===".format(titulo))
    angulos = {}
    for k in ORDEN:
        valor = pedir_angulo(k)
        if valor is None:
            return None
        angulos[k] = valor

    while True:
        mostrar_resumen(titulo, angulos, texto_garra)
        cmd = input("Y=iniciar | X=salir | A/C/B=reingresar: ").strip().lower()
        if cmd == "x":
            return None
        elif cmd in ("a", "b", "c"):
            valor = pedir_angulo(cmd.upper())
            if valor is None:
                return None
            angulos[cmd.upper()] = valor
        elif cmd == "y":
            return angulos
        else:
            print("Comando no valido.")


def mover_articulaciones(angulos):
    """A -> C -> B. Devuelve True si no hubo corte por voltaje."""
    for k in ORDEN:
        motor, mult, vmin, vmax = ARTICULACIONES[k]
        objetivo = int(angulos[k] * mult)
        ok, minimo = mover(motor, objetivo, TIMEOUT_ART_MS, MANTENER[k])
        print("{} -> {} deg articulacion (motor {} deg) | minimo: {} mV".format(
            k, a_articulacion(motor, mult), motor.angle(), minimo))
        if not ok:
            return False
        pausa_motor(k)
    return True


def etapa_inicio():
    """Lee la posicion actual de cada motor y lo lleva a 0 (sin reset_angle)."""
    print("=== INICIO ===")
    print("Posiciones actuales (grados del motor):")
    for nombre, motor, mult, timeout, mantener in SECUENCIA_INICIO:
        print("  {}: {} deg motor ({} deg articulacion)".format(
            nombre, motor.angle(), round(motor.angle() / mult, 1)))

    for nombre, motor, mult, timeout, mantener in SECUENCIA_INICIO:
        ok, minimo = mover(motor, 0, timeout, mantener)
        print("{} -> {} deg | minimo: {} mV".format(nombre, motor.angle(), minimo))
        if not ok:
            return False
        pausa_motor(nombre)
    print("Brazo en posicion inicial.")
    return True


def etapa_take(angulos):
    """Garra abre -> A -> C -> B -> garra cierra (queda sujeta al objeto)."""
    ok, minimo = mover(garra, GARRA_ABIERTA, TIMEOUT_GARRA_MS, False)
    print("Garra abierta | minimo:", minimo, "mV")
    if not ok:
        return False
    pausa_motor("garra abre")
    if not mover_articulaciones(angulos):
        return False
    ok, minimo = mover(garra, GARRA_CERRADA, TIMEOUT_GARRA_MS, True)
    print("Garra cerrada | minimo:", minimo, "mV")
    if ok:
        pausa_motor("garra cierra")
        print("Toma del objeto terminada.")
    return ok


def etapa_left(angulos):
    """Con la garra cerrada: A -> C -> B -> garra abre."""
    if not mover_articulaciones(angulos):
        return False
    ok, minimo = mover(garra, GARRA_ABIERTA, TIMEOUT_GARRA_MS, False)
    print("Garra abierta | minimo:", minimo, "mV")
    if ok:
        pausa_motor("garra abre")
        print("Objeto soltado.")
    return ok


def programa():
    """Inicio -> take -> left -> inicio. Devuelve 'ok', 'salida' (X) o 'corte' (voltaje)."""
    wait(ESPERA_INICIO_MS)

    if not etapa_inicio():
        return "corte"
    wait(PAUSA_ETAPA_MS)

    take = pedir_coordenadas("TAKE", "abrir a {} al inicio, cerrar a {} al final".format(
        GARRA_ABIERTA, GARRA_CERRADA))
    if take is None:
        return "salida"
    if not etapa_take(take):
        return "corte"
    wait(PAUSA_ETAPA_MS)

    left = pedir_coordenadas("LEFT", "cerrada durante el traslado, abrir a {} al llegar".format(
        GARRA_ABIERTA))
    if left is None:
        return "salida"
    if not etapa_left(left):
        return "corte"
    wait(PAUSA_ETAPA_MS)

    if not etapa_inicio():
        return "corte"
    return "ok"


# --- Programa principal ---
# NO se hace reset_angle: el cero es el de la ultima calibracion (hub encendido).
print("Escribi 'x' para salir. Rangos: A 0-270, C -180 a 45, B 0-190.")
print("Voltaje inicial:", hub.battery.voltage(), "mV |", hub.battery.current(), "mA")

resultado = programa()
if resultado == "ok":
    print("Secuencia completa.")
elif resultado == "corte":
    print("Voltaje bajo -> motores detenidos.")
else:
    print("Salida solicitada.")

detener_todo()
print("Programa terminado.")
