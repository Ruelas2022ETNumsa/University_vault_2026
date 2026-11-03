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
TIMEOUT_GARRA_MS = 3000  # la garra puede quedar frenada por el objeto

GARRA_ABIERTA = 90
GARRA_CERRADA = 0

# nombre: (motor, multiplicador, minimo, maximo)  -> rangos en grados de la articulacion
ARTICULACIONES = {
    "A": (hombro, 3, 0, 270),
    "C": (codo, 1, -180, 45),
    "B": (muneca, 3, 0, 190),
}
ORDEN = ["A", "C", "B"]
NOMBRES = {"A": "hombro", "C": "codo", "B": "muneca"}


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


def mostrar_resumen(angulos):
    print("--- Resumen ---")
    print("Garra: abrir a", GARRA_ABIERTA, "al inicio, cerrar a", GARRA_CERRADA, "al final")
    for k in ORDEN:
        mult = ARTICULACIONES[k][1]
        print("{} ({}): {} deg x {} = {} deg motor".format(
            k, NOMBRES[k], angulos[k], mult, int(angulos[k] * mult)))


def ejecutar(angulos):
    """Garra abre -> A -> C -> B -> garra cierra. Devuelve True si termino sin corte por voltaje."""
    ok, minimo = mover(garra, GARRA_ABIERTA, TIMEOUT_GARRA_MS)
    print("Garra abierta | minimo:", minimo, "mV")
    if not ok:
        return False

    for k in ORDEN:
        motor, mult, vmin, vmax = ARTICULACIONES[k]
        objetivo = int(angulos[k] * mult)
        ok, minimo = mover(motor, objetivo, TIMEOUT_ART_MS)
        print("{} -> {} deg | minimo: {} mV".format(k, motor.angle(), minimo))
        if not ok:
            return False

    ok, minimo = mover(garra, GARRA_CERRADA, TIMEOUT_GARRA_MS)
    print("Garra cerrada | minimo:", minimo, "mV")
    return ok


# --- Programa principal ---
# Se asume que el brazo esta en su posicion de calibracion: este es el 0 de cada motor.
for m in (hombro, codo, muneca, garra):
    m.reset_angle(0)

print("Escribi 'x' para salir. Rangos: A 0-270, C -180 a 45, B 0-190.")

angulos = {}
salir = False
for k in ORDEN:
    valor = pedir_angulo(k)
    if valor is None:
        salir = True
        break
    angulos[k] = valor

while not salir:
    mostrar_resumen(angulos)
    cmd = input("Y=iniciar | X=salir | A/C/B=reingresar: ").strip().lower()

    if cmd == "x":
        break
    elif cmd in ("a", "b", "c"):
        valor = pedir_angulo(cmd.upper())
        if valor is None:
            break
        angulos[cmd.upper()] = valor
    elif cmd == "y":
        if ejecutar(angulos):
            print("Toma del objeto terminada.")
        else:
            print("Voltaje < {} mV -> motores detenidos.".format(UMBRAL_MV))
        break
    else:
        print("Comando no valido.")

detener_todo()
print("Programa terminado.")
