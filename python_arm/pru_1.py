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

VELOCIDAD = 200          # grados/segundo (todos los motores)
UMBRAL_MV = 5000         # si el voltaje baja de esto, se detienen todos los motores
PERIODO_MS = 50          # cada cuanto se mide durante el movimiento
PRINT_CADA_MS = 100      # cada cuanto se muestra el voltaje en pantalla
PAUSA_MS = 1000          # pausa entre cada movimiento
TIMEOUT_ART_MS = 10000   # tiempo maximo por movimiento de articulacion
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


def mover(nombre, motor, objetivo, timeout_ms):
    """Mueve UN solo motor al angulo absoluto y espera a que termine.
    Muestra el voltaje en pantalla mientras se mueve. Devuelve (ok, minimo_mV).
    ok=False si el voltaje bajo del umbral (y se detuvieron todos los motores).
    Si se agota el tiempo, se frena el motor con hold() y se continua (ok=True)."""
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
            return False, minimo
        if t > timeout_ms:
            motor.hold()
            print("  [{}] tiempo agotado, hold()".format(nombre))
            break
        wait(PERIODO_MS)
    v = hub.battery.voltage()
    if v < minimo:
        minimo = v
    print("  [{}] fin: {} mV".format(nombre, v))
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


def mostrar_resumen(titulo, angulos, texto_garra):
    print("--- {} ---".format(titulo))
    print("Garra:", texto_garra)
    for k in ORDEN:
        mult = ARTICULACIONES[k][1]
        print("{} ({}): {} deg x {} = {} deg motor".format(
            k, NOMBRES[k], angulos[k], mult, int(angulos[k] * mult)))


def pedir_coordenadas(titulo, texto_garra):
    """Pide A, C, B y luego el menu Y/X/A/C/B. Devuelve el dict de angulos o None si se sale."""
    print("=== {} ===".format(titulo))
    angulos = {}
    for k in ORDEN:
        valor = pedir_angulo(k)
        if valor is None:
            return None
        angulos[k] = valor

    while True:
        mostrar_resumen(titulo, angulos, texto_garra)
        print("Voltaje actual:", hub.battery.voltage(), "mV")
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


def paso(nombre, motor, objetivo, timeout_ms):
    """Un movimiento (un solo motor) + pausa de 1 s. Devuelve False si hubo corte por voltaje."""
    ok, minimo = mover(nombre, motor, objetivo, timeout_ms)
    print("{} -> {} deg | minimo: {} mV".format(nombre, motor.angle(), minimo))
    if not ok:
        return False
    wait(PAUSA_MS)
    print("  reposo tras {}: {} mV".format(nombre, hub.battery.voltage()))
    return True


def mover_articulaciones(angulos):
    for k in ORDEN:
        motor, mult, vmin, vmax = ARTICULACIONES[k]
        if not paso(k, motor, int(angulos[k] * mult), TIMEOUT_ART_MS):
            return False
    return True


def tomar(angulos):
    """Garra abre -> A -> C -> B -> garra cierra."""
    if not paso("Garra abre", garra, GARRA_ABIERTA, TIMEOUT_GARRA_MS):
        return False
    if not mover_articulaciones(angulos):
        return False
    return paso("Garra cierra", garra, GARRA_CERRADA, TIMEOUT_GARRA_MS)


def dejar(angulos):
    """Con la garra cerrada: A -> C -> B -> garra abre."""
    if not mover_articulaciones(angulos):
        return False
    return paso("Garra abre", garra, GARRA_ABIERTA, TIMEOUT_GARRA_MS)


def corte():
    print("Voltaje < {} mV -> motores detenidos.".format(UMBRAL_MV))


# --- Programa principal ---
# Se asume que el brazo esta en su posicion de calibracion: este es el 0 de cada motor.
for m in (hombro, codo, muneca, garra):
    m.reset_angle(0)

print("Escribi 'x' para salir. Rangos: A 0-270, C -180 a 45, B 0-190.")
print("Voltaje inicial:", hub.battery.voltage(), "mV")

origen = pedir_coordenadas(
    "TOMAR OBJETO", "abrir a {} al inicio, cerrar a {} al final".format(GARRA_ABIERTA, GARRA_CERRADA))

if origen is not None:
    if tomar(origen):
        print("Objeto tomado.")
        destino = pedir_coordenadas(
            "DEJAR OBJETO", "cerrada durante el traslado, abrir a {} al llegar".format(GARRA_ABIERTA))
        if destino is not None:
            if dejar(destino):
                print("Objeto dejado.")
            else:
                corte()
    else:
        corte()

print("Voltaje final (motores aun con hold):", hub.battery.voltage(), "mV")
detener_todo()
wait(500)
print("Voltaje final (motores libres):", hub.battery.voltage(), "mV")
print("Programa terminado.")
