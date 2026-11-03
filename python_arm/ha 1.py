from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait, StopWatch

# ha.py = paz.py + DESCANSO entre fases:
#   pide angulos de take -> pide angulos de left -> take -> [descanso] -> left -> [descanso] -> inicio
# El descanso imita lo que pasa cuando corres take.py, left.py e inicio.py por separado:
# al terminar cada programa se llama detener_todo() (se sueltan los 4 motores) y la bateria
# se recupera antes del siguiente. Los angulos de cada motor se conservan (no hay reset).
# Si el voltaje baja del umbral, el programa se PAUSA y espera 'g' + Enter para continuar
# ('x' + Enter aborta la secuencia).

# Cambiar PrimeHub por tu hub: InventorHub, EssentialHub, CityHub, etc.
hub = PrimeHub()

hombro = Motor(Port.A, Direction.CLOCKWISE)
codo = Motor(Port.C, Direction.CLOCKWISE)
muneca = Motor(Port.B, Direction.CLOCKWISE)
garra = Motor(Port.F, Direction.CLOCKWISE)

VELOCIDAD = 200          # grados/segundo del MOTOR (todos los motores)
UMBRAL_MV = 5000         # si el voltaje baja de esto, se PAUSA el programa
PERIODO_MS = 20          # cada cuanto se mide durante el movimiento
TIMEOUT_ART_MS = 10000   # tiempo maximo por movimiento de articulacion
TIMEOUT_GARRA_MS = 3000  # tiempo maximo para la garra
ESPERA_INICIO_MS = 500   # espera antes de volver a inicio (tiempo para alejarse)

# --- Descanso entre fases ---
DESCANSO_FASES_MS = 2000  # tiempo con los motores SUELTOS entre take->left y left->inicio

# --- Monitoreo de voltaje / corriente ---
UMBRAL_AVISO_MV = 5500   # por debajo de esto se imprime un aviso (no pausa)
MUESTRAS_CORTE = 3       # muestras SEGUIDAS bajo UMBRAL_MV para pausar (filtra picos de 1 muestra)
HOLD_MUESTRA_MS = 300    # tras cada movimiento se mide la corriente de sostenimiento (hold)
PAUSA_SOLTAR = False     # False: durante la pausa el motor activo mantiene posicion (hold)
                         # True: se sueltan todos los motores (menos corriente, el brazo puede caer)
# Mitigaciones opcionales (None = valor por defecto del hub/motor):
ACELERACION = None       # grados/s^2 del motor; ej. 300 suaviza arranques (menos pico de corriente)
TORQUE_MAX = None        # mN*m; limita la corriente maxima de cada motor

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


def descanso(etiqueta):
    """Entre fases: suelta los 4 motores (detener_todo) y espera a que la bateria se recupere,
    igual que al terminar un programa y empezar el siguiente por separado."""
    v_antes = hub.battery.voltage()
    i_antes = hub.battery.current()
    detener_todo()
    print("-- Descanso {} ({} ms, motores sueltos) | antes: {} mV, {} mA".format(
        etiqueta, DESCANSO_FASES_MS, v_antes, i_antes))
    wait(DESCANSO_FASES_MS)
    print("   despues: {} mV, {} mA".format(hub.battery.voltage(), hub.battery.current()))


def a_articulacion(motor, mult):
    """Convierte los grados medidos por el motor a grados de la articulacion."""
    return round(motor.angle() / mult, 1)


def nombre_motor(motor):
    if motor is hombro:
        return "A hombro"
    if motor is codo:
        return "C codo"
    if motor is muneca:
        return "B muneca"
    return "F garra"


# Estadisticas globales de la corrida (se muestran al final)
STATS = {"vmin": 99999, "vmin_en": "-", "imax": 0, "imax_en": "-", "pausas": 0}


def pausar(etapa, motor, v, i):
    """Voltaje bajo sostenido: NO termina el programa, espera 'g' + Enter para continuar.
    Devuelve True si se continua, False si el usuario escribe 'x' (abortar)."""
    STATS["pausas"] += 1
    if PAUSA_SOLTAR:
        detener_todo()
    else:
        motor.hold()
    print("  !! VOLTAJE BAJO en {}: {} mV con {} mA".format(etapa, v, i))
    while True:
        texto = input("  PAUSA. 'g' + Enter = continuar | 'x' = abortar: ").strip().lower()
        if texto == "g":
            print("  Continuando... bateria: {} mV, {} mA".format(
                hub.battery.voltage(), hub.battery.current()))
            return True
        if texto == "x":
            detener_todo()
            return False
        print("  Escribi 'g' para continuar o 'x' para abortar.")


def muestrear(st, etapa, motor):
    """Lee voltaje (mV) y corriente (mA) del hub y actualiza minimos/maximos.
    Devuelve 0 = normal | 1 = hubo pausa por voltaje bajo y el usuario continuo (g) | 2 = abortar (x)."""
    v = hub.battery.voltage()
    i = hub.battery.current()
    if v < st["vmin"]:
        st["vmin"] = v
    if i > st["imax"]:
        st["imax"] = i
    if v < STATS["vmin"]:
        STATS["vmin"] = v
        STATS["vmin_en"] = etapa
    if i > STATS["imax"]:
        STATS["imax"] = i
        STATS["imax_en"] = etapa
    if v < UMBRAL_AVISO_MV and not st["avisado"]:
        st["avisado"] = True
        print("  ! aviso {}: {} mV con {} mA".format(etapa, v, i))
    if v < UMBRAL_MV:
        st["bajos"] += 1
        if st["bajos"] >= MUESTRAS_CORTE:
            st["bajos"] = 0
            if pausar(etapa, motor, v, i):
                return 1
            return 2
    else:
        st["bajos"] = 0
    return 0


def mover(motor, objetivo, timeout_ms):
    """Mueve al angulo absoluto del MOTOR vigilando voltaje y corriente.
    Devuelve (ok, minimo_mV). ok=False solo si el usuario aborta ('x') durante una pausa.
    Si el voltaje baja, se pausa y al escribir 'g' se retoma el movimiento.
    Si se agota el tiempo, se frena el motor y se continua (ok=True).
    Imprime: Vmin, Imax durante el movimiento e Imax en hold (corriente de sostenimiento)."""
    etapa = nombre_motor(motor)
    v0 = hub.battery.voltage()
    st = {"vmin": v0, "imax": hub.battery.current(), "bajos": 0, "avisado": False}
    sh = {"vmin": v0, "imax": 0, "bajos": 0, "avisado": False}
    ok = True
    reloj = StopWatch()
    motor.run_target(VELOCIDAD, objetivo, wait=False)
    while not motor.done():
        r = muestrear(st, etapa, motor)
        if r == 2:
            ok = False
            break
        if r == 1:
            # tras la pausa se retoma el movimiento y se reinicia el timeout
            motor.run_target(VELOCIDAD, objetivo, wait=False)
            reloj = StopWatch()
            continue
        if reloj.time() > timeout_ms:
            motor.hold()
            print("  ! timeout en", etapa)
            break
        wait(PERIODO_MS)
    if ok:
        reloj = StopWatch()
        while reloj.time() < HOLD_MUESTRA_MS:
            r = muestrear(sh, etapa, motor)
            if r == 2:
                ok = False
                break
            if r == 1:
                motor.run_target(VELOCIDAD, objetivo, wait=False)
                reloj = StopWatch()
                continue
            wait(PERIODO_MS)
    minimo = min(st["vmin"], sh["vmin"])
    print("  mon {}: Vmin {} mV | Imax mov {} mA | Imax hold {} mA".format(
        etapa, minimo, st["imax"], sh["imax"]))
    return ok, minimo


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
    """Mueve A -> C -> B a los angulos indicados. Devuelve False si el usuario aborto."""
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
    print("Descanso entre fases: {} ms con motores sueltos".format(DESCANSO_FASES_MS))


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
    if ACELERACION is not None:
        m.control.limits(acceleration=ACELERACION)
    if TORQUE_MAX is not None:
        m.control.limits(torque=TORQUE_MAX)

print("Bateria en reposo: {} mV, {} mA".format(hub.battery.voltage(), hub.battery.current()))

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
            descanso("TAKE -> LEFT")
            ok = ejecutar_left(ang_left)
        if ok:
            print("Objeto soltado.")
            descanso("LEFT -> INICIO")
            ok = ejecutar_inicio()
        if ok:
            print("Brazo en posicion inicial. Secuencia completa.")
        else:
            print("Secuencia abortada por el usuario (x) tras voltaje bajo -> motores detenidos.")
        break
    else:
        print("Comando no valido.")

detener_todo()
if STATS["vmin_en"] != "-":
    print("=== Monitoreo ===")
    print("Voltaje minimo: {} mV en {}".format(STATS["vmin"], STATS["vmin_en"]))
    print("Corriente maxima: {} mA en {}".format(STATS["imax"], STATS["imax_en"]))
    print("Pausas por voltaje bajo: {}".format(STATS["pausas"]))
    print("Bateria final: {} mV".format(hub.battery.voltage()))
print("Programa terminado.")
