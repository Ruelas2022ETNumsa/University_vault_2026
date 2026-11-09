from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait, StopWatch

# ha2.py = take.py + left.py + inicio, pensado para AHORRAR CORRIENTE por USB:
#   - UN solo motor alimentado a la vez.
#   - Cuando un motor llega a su destino se hace stop() (se SUELTA, sin hold), asi esa corriente
#     queda libre para el siguiente motor. Se confia en la resistencia propia de los motores.
#   - Flujo: pide angulos de TAKE -> pide angulos de LEFT -> take -> [descanso] -> left -> [descanso] -> inicio
#   - Si el voltaje baja del umbral, se PAUSA y espera 'g' + Enter ('x' + Enter aborta).
#
# Cableado actual (recableado el 8-nov-2026):
#   A = hombro | C = muneca | D = codo | E = garra | F = sensor de color (no se usa aqui) | B = vacio

# Cambiar PrimeHub por tu hub: InventorHub, EssentialHub, CityHub, etc.
hub = PrimeHub()

hombro = Motor(Port.A, Direction.CLOCKWISE)
muneca = Motor(Port.C, Direction.CLOCKWISE)
codo = Motor(Port.D, Direction.CLOCKWISE)
garra = Motor(Port.E, Direction.CLOCKWISE)

VELOCIDAD = 200          # grados/segundo del MOTOR (todos los motores)
UMBRAL_MV = 5500         # si el voltaje baja de esto (3 muestras seguidas), se PAUSA el programa
UMBRAL_AVISO_MV = 6000   # por debajo de esto se imprime un aviso (no pausa)
MUESTRAS_CORTE = 3       # muestras SEGUIDAS bajo UMBRAL_MV para pausar (filtra picos de 1 muestra)
PERIODO_MS = 20          # cada cuanto se mide durante el movimiento
TIMEOUT_ART_MS = 10000   # tiempo maximo por movimiento de articulacion
TIMEOUT_GARRA_MS = 3000  # tiempo maximo para la garra
ESPERA_INICIO_MS = 500   # espera antes de volver a inicio (tiempo para alejarse)
DESCANSO_FASES_MS = 1000 # pausa con motores sueltos entre fases (recupera bateria)

# True : la garra tambien se SUELTA al cerrar (maximo ahorro; el objeto podria resbalar)
# False: la garra queda en hold sosteniendo el objeto durante el traslado (gasta algo de corriente)
SOLTAR_GARRA_CERRADA = True

# Mitigaciones opcionales (None = valor por defecto del hub/motor):
ACELERACION = None       # grados/s^2 del motor; ej. 300 suaviza arranques (menos pico de corriente)
TORQUE_MAX = None        # mN*m; limita la corriente maxima de cada motor

GARRA_ABIERTA = 90
GARRA_CERRADA = 0

# clave = PUERTO del motor: (motor, multiplicador, minimo, maximo) -> rangos en grados de la ARTICULACION
# El motor gira (angulo x multiplicador) para que la articulacion se mueva el angulo ingresado.
ARTICULACIONES = {
    "A": (hombro, 3, 0, 270),
    "D": (codo, 1, -180, 45),
    "C": (muneca, 3, 0, 190),
}
ORDEN = ["A", "D", "C"]  # hombro -> codo -> muneca
NOMBRES = {"A": "hombro", "D": "codo", "C": "muneca"}

# Secuencia de inicio: (nombre, motor, timeout) en orden muneca -> codo -> hombro -> garra
SECUENCIA_INICIO = [
    ("C muneca", muneca, TIMEOUT_ART_MS),
    ("D codo", codo, TIMEOUT_ART_MS),
    ("A hombro", hombro, TIMEOUT_ART_MS),
    ("E garra", garra, TIMEOUT_GARRA_MS),
]


# ---------------- Utilidades comunes ----------------

def detener_todo(incluir_garra=True):
    """Suelta los motores (stop = sin alimentacion)."""
    for m in (hombro, codo, muneca):
        m.stop()
    if incluir_garra:
        garra.stop()


def descanso(etiqueta):
    """Entre fases: todo suelto y espera a que la bateria se recupere."""
    v_antes = hub.battery.voltage()
    i_antes = hub.battery.current()
    detener_todo(SOLTAR_GARRA_CERRADA)
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
        return "D codo"
    if motor is muneca:
        return "C muneca"
    return "E garra"


# Estadisticas globales de la corrida (se muestran al final)
STATS = {"vmin": 99999, "vmin_en": "-", "imax": 0, "imax_en": "-", "pausas": 0}


def pausar(etapa, motor, v, i):
    """Voltaje bajo sostenido: SUELTA el motor activo y espera 'g' + Enter para continuar.
    Devuelve True si se continua, False si el usuario escribe 'x' (abortar)."""
    STATS["pausas"] += 1
    motor.stop()
    print("  !! VOLTAJE BAJO en {}: {} mV con {} mA (motor soltado)".format(etapa, v, i))
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
    Devuelve 0 = normal | 1 = hubo pausa y el usuario continuo (g) | 2 = abortar (x)."""
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


def mover(motor, objetivo, timeout_ms, mantener=False):
    """Mueve al angulo absoluto del MOTOR vigilando voltaje y corriente.
    Al terminar (llegada, timeout o aborto) el motor se SUELTA con stop(), salvo mantener=True (hold).
    Devuelve (ok, minimo_mV). ok=False solo si el usuario aborta ('x') durante una pausa."""
    etapa = nombre_motor(motor)
    st = {"vmin": hub.battery.voltage(), "imax": hub.battery.current(), "bajos": 0, "avisado": False}
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
            print("  ! timeout en", etapa)
            break
        wait(PERIODO_MS)

    # Llego (o termino el tiempo): se corta la alimentacion de este motor
    if mantener and ok:
        motor.hold()
    else:
        motor.stop()
    print("  mon {}: Vmin {} mV | Imax mov {} mA | {}".format(
        etapa, st["vmin"], st["imax"], "hold" if (mantener and ok) else "soltado"))
    return ok, st["vmin"]


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
    """Mueve hombro -> codo -> muneca, UNO A LA VEZ, soltando cada uno al llegar."""
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
    """Garra abre -> A -> D -> C -> garra cierra."""
    ok, minimo = mover(garra, GARRA_ABIERTA, TIMEOUT_GARRA_MS)
    print("Garra abierta | minimo:", minimo, "mV")
    if not ok:
        return False

    if not mover_articulaciones(angulos):
        return False

    ok, minimo = mover(garra, GARRA_CERRADA, TIMEOUT_GARRA_MS, mantener=not SOLTAR_GARRA_CERRADA)
    print("Garra cerrada | minimo:", minimo, "mV")
    return ok


def ejecutar_left(angulos):
    """A -> D -> C -> garra abre (suelta el objeto)."""
    if not mover_articulaciones(angulos):
        return False

    ok, minimo = mover(garra, GARRA_ABIERTA, TIMEOUT_GARRA_MS)
    print("Garra abierta | minimo:", minimo, "mV")
    return ok


def ejecutar_inicio():
    """C -> D -> A -> garra, todos a 0 (posicion de calibracion)."""
    wait(ESPERA_INICIO_MS)
    for nombre, motor, timeout in SECUENCIA_INICIO:
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
    print("LEFT: traslado y la garra abre a", GARRA_ABIERTA, "al llegar")
    for k in ORDEN:
        mult = ARTICULACIONES[k][1]
        print("  L{} ({}): {} deg articulacion -> motor {} deg (x{})".format(
            k, NOMBRES[k], ang_left[k], int(ang_left[k] * mult), mult))
    print("INICIO: vuelve a 0 (C -> D -> A -> garra)")
    print("Cada motor se suelta al llegar. Descanso entre fases: {} ms".format(DESCANSO_FASES_MS))


def pedir_set(titulo):
    """Pide A, D, C para una fase. Devuelve el dict o None si el usuario sale."""
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
print("Puertos: A hombro | D codo | C muneca | E garra | F sensor color (sin uso)")
print("Escribi 'x' para salir. Rangos: A 0-270, D -180 a 45, C 0-190.")

print("== Angulos para TAKE ==")
ang_take = pedir_set("TAKE")
ang_left = None
if ang_take is not None:
    print("== Angulos para LEFT ==")
    ang_left = pedir_set("LEFT")

salir = ang_take is None or ang_left is None

while not salir:
    mostrar_resumen(ang_take, ang_left)
    cmd = input("Y=iniciar | X=salir | TA/TD/TC o LA/LD/LC=reingresar: ").strip().lower()

    if cmd == "x":
        break
    elif cmd in ("ta", "td", "tc"):
        valor = pedir_angulo("TAKE", cmd[1].upper())
        if valor is None:
            break
        ang_take[cmd[1].upper()] = valor
    elif cmd in ("la", "ld", "lc"):
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
