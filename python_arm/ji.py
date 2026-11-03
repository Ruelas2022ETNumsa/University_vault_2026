from math import sin, cos, atan2, acos, pi

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait, StopWatch

# ji.py = ha.py pero en vez de ANGULOS se ingresan COORDENADAS (cinematica inversa).
#   pide punto de take -> pide punto de left -> take -> [descanso] -> left -> [descanso] -> inicio
#
# Sistema de coordenadas (en cm, origen = eje del HOMBRO = 0,0,0):
#   X = hacia adelante (horizontal)    Z = hacia arriba (altura)
#   Y = NO se pide: el brazo solo tiene hombro/codo/muneca (no hay motor de giro de base),
#       asi que solo se mueve en UN plano vertical (el plano X-Z, con Y = 0).
#
# El brazo se modela como 3 eslabones en ese plano:
#   hombro -> codo (L1), codo -> muneca (L2), muneca -> punta de la garra (L3).
# El punto ingresado es la PUNTA DE LA GARRA; la inclinacion de la garra (ORIENT_GARRA_DEG)
# es una preferencia (por defecto apuntando hacia abajo).
#
# !!! IMPORTANTE: los valores de la seccion GEOMETRIA son PLACEHOLDERS. Hay que medirlos en el
# brazo real (ver instrucciones abajo) y poner CALIBRADO = True. Mientras CALIBRADO = False
# el programa avisa y pide confirmacion antes de seguir.
#
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
# El motor gira (angulo x multiplicador) para que la articulacion se mueva el angulo calculado.
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

# =====================================================================================
# GEOMETRIA DEL BRAZO  (PLACEHOLDERS: MEDIR EN EL BRAZO REAL Y AJUSTAR)
# =====================================================================================
CALIBRADO = False        # poner True cuando los valores de abajo sean los reales

# Longitudes (cm): de eje a eje.
L1 = 12.0                # hombro -> codo
L2 = 12.0                # codo -> muneca
L3 = 8.0                 # muneca -> punta de la garra (donde esta el objeto)

# Convencion de angulos geometricos: medidos en el plano X-Z desde +X (adelante),
# positivos hacia arriba (+Z). Un eslabon horizontal hacia adelante = 0 grados,
# vertical hacia arriba = 90, vertical hacia abajo = -90.
#
# Pose de calibracion (todos los motores en 0 grados, el "home" del brazo):
HOME_TH1 = 90.0          # angulo ABSOLUTO del eslabon 1 (hombro->codo) cuando A = 0
HOME_Q2 = 0.0            # angulo del eslabon 2 RELATIVO al eslabon 1 cuando C = 0
HOME_QW = 0.0            # angulo del eslabon 3 RELATIVO al eslabon 2 cuando B = 0
# Sentido: +1 si al AUMENTAR el angulo de la articulacion el eslabon sube (giro antihorario
# visto desde el lado, de +X hacia +Z); -1 si baja (giro horario).
SIGN_A = -1
SIGN_C = 1
SIGN_B = 1

# Preferencia de inclinacion de la garra (angulo absoluto del eslabon 3): -90 = apuntando abajo.
ORIENT_GARRA_DEG = -90.0
ORIENT_TOL_DEG = 30      # si no hay solucion, prueba inclinaciones hasta +-este valor (paso 5)
# Preferencia de codo: (1, -1) prueba primero un lado del codo, (-1, 1) el otro.
LADO_CODO = (1, -1)

# Como calibrar (una sola vez):
#  1) Con el brazo en home (motores en 0): medir L1, L2, L3 con regla (eje a eje, cm).
#  2) En home, medir el angulo ABSOLUTO del eslabon 1 -> HOME_TH1; el relativo del 2 respecto
#     del 1 -> HOME_Q2; el relativo del 3 respecto del 2 -> HOME_QW.
#  3) Con cero.py mover UNA articulacion unos grados y ver hacia donde se mueve el eslabon
#     (arriba/abajo) para fijar SIGN_A, SIGN_C, SIGN_B.
#  4) Probar puntos conocidos y comparar con la regla.

DEG = 180 / pi           # radianes -> grados
RAD = pi / 180           # grados -> radianes


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


# ---------------- Cinematica ----------------

def a_rango(valor, vmin, vmax):
    """Lleva un angulo (grados) al rango [vmin, vmax] probando +-360, +-720.
    Devuelve None si no entra (tolerancia 0.5 grados)."""
    for k in (0, -360, 360, -720, 720):
        v = valor + k
        if vmin - 0.5 <= v <= vmax + 0.5:
            return min(max(v, vmin), vmax)
    return None


def resolver_plano(x, z, phi_deg):
    """Cinematica inversa plana para la punta en (x, z) con la garra inclinada phi_deg
    (angulo absoluto del eslabon 3). Devuelve {A, C, B} en grados de articulacion o None."""
    p = phi_deg * RAD
    wx = x - L3 * cos(p)         # punto de la muneca
    wz = z - L3 * sin(p)
    cq = (wx * wx + wz * wz - L1 * L1 - L2 * L2) / (2 * L1 * L2)
    if cq > 1 or cq < -1:
        return None              # fuera de alcance
    for signo in LADO_CODO:
        q2 = signo * acos(cq)    # angulo relativo del codo (rad)
        th1 = atan2(wz, wx) - atan2(L2 * sin(q2), L1 + L2 * cos(q2))
        qw = p - (th1 + q2)      # angulo relativo de la muneca (rad)
        a = a_rango((th1 * DEG - HOME_TH1) / SIGN_A, ARTICULACIONES["A"][2], ARTICULACIONES["A"][3])
        c = a_rango((q2 * DEG - HOME_Q2) / SIGN_C, ARTICULACIONES["C"][2], ARTICULACIONES["C"][3])
        b = a_rango((qw * DEG - HOME_QW) / SIGN_B, ARTICULACIONES["B"][2], ARTICULACIONES["B"][3])
        if a is None or c is None or b is None:
            continue             # esta solucion de codo no entra en los rangos de los motores
        return {"A": a, "C": c, "B": b}
    return None


def resolver(x, z):
    """Prueba la inclinacion preferida y luego variantes hasta +-ORIENT_TOL_DEG.
    Devuelve (angulos, phi_usado) o (None, None)."""
    d = 0
    while d <= ORIENT_TOL_DEG:
        for s in (1, -1):
            if d == 0 and s == -1:
                continue
            phi = ORIENT_GARRA_DEG + s * d
            ang = resolver_plano(x, z, phi)
            if ang is not None:
                return ang, phi
        d += 5
    return None, None


def punta(ang):
    """Cinematica directa (comprobacion): posicion (x, z) de la punta para los angulos dados."""
    th1 = (HOME_TH1 + SIGN_A * ang["A"]) * RAD
    th2 = th1 + (HOME_Q2 + SIGN_C * ang["C"]) * RAD
    th3 = th2 + (HOME_QW + SIGN_B * ang["B"]) * RAD
    x = L1 * cos(th1) + L2 * cos(th2) + L3 * cos(th3)
    z = L1 * sin(th1) + L2 * sin(th2) + L3 * sin(th3)
    return x, z


def pedir_numero(texto):
    """Pide un numero. Devuelve None si escribe x."""
    while True:
        t = input(texto).strip().lower()
        if t == "x":
            return None
        try:
            return float(t)
        except ValueError:
            print("Valor no valido, escribi un numero (o 'x' para salir).")


def pedir_punto(titulo):
    """Pide X y Z (cm desde el hombro) hasta que el punto sea alcanzable.
    Devuelve {'x','z','phi','ang'} o None si el usuario sale (x)."""
    while True:
        x = pedir_numero("[{}] X adelante del hombro [cm]: ".format(titulo))
        if x is None:
            return None
        z = pedir_numero("[{}] Z altura del hombro [cm]: ".format(titulo))
        if z is None:
            return None
        ang, phi = resolver(x, z)
        if ang is None:
            print("Punto ({}, {}) sin solucion: fuera de alcance o fuera de los rangos de los motores.".format(x, z))
            continue
        return {"x": x, "z": z, "phi": phi, "ang": ang}


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

def resumen_punto(titulo, pt):
    xc, zc = punta(pt["ang"])
    print("{}: punta en X={} cm, Z={} cm (garra inclinada {} deg)".format(
        titulo, pt["x"], pt["z"], round(pt["phi"], 1)))
    for k in ORDEN:
        mult = ARTICULACIONES[k][1]
        print("  {} ({}): {} deg articulacion -> motor {} deg (x{})".format(
            k, NOMBRES[k], round(pt["ang"][k], 1), int(pt["ang"][k] * mult), mult))
    print("  comprobacion (cinematica directa): X={} cm, Z={} cm".format(round(xc, 1), round(zc, 1)))


def mostrar_resumen(pt_take, pt_left):
    print("--- Resumen ---")
    print("(origen = hombro; X adelante, Z arriba; en cm)")
    print("TAKE: garra abre a", GARRA_ABIERTA, "al inicio, cierra a", GARRA_CERRADA, "al final")
    resumen_punto("TAKE", pt_take)
    print("LEFT: garra cerrada durante el traslado, abre a", GARRA_ABIERTA, "al llegar")
    resumen_punto("LEFT", pt_left)
    print("INICIO: vuelve a 0 (B -> C -> A -> garra)")
    print("Descanso entre fases: {} ms con motores sueltos".format(DESCANSO_FASES_MS))


# --- Programa principal ---
print("Geometria: L1={} L2={} L3={} cm | origen = hombro (0,0,0) | plano X-Z".format(L1, L2, L3))
if not CALIBRADO:
    print("!!! ATENCION: la geometria NO esta calibrada (valores de ejemplo).")
    print("!!! El brazo puede ir a una posicion distinta de la ingresada.")
    resp = input("Continuar igual? (s/n): ").strip().lower()
    if resp != "s":
        print("Programa terminado. Calibra la seccion GEOMETRIA y pone CALIBRADO = True.")
        raise SystemExit

# Se asume que el brazo esta en su posicion de calibracion: este es el 0 de cada motor.
# Un solo reset al principio: take, left e inicio comparten las mismas coordenadas.
for m in (hombro, codo, muneca, garra):
    m.reset_angle(0)
    if ACELERACION is not None:
        m.control.limits(acceleration=ACELERACION)
    if TORQUE_MAX is not None:
        m.control.limits(torque=TORQUE_MAX)

print("Bateria en reposo: {} mV, {} mA".format(hub.battery.voltage(), hub.battery.current()))

print("Ingresa puntos en cm desde el hombro. 'x' para salir.")

print("== Punto para TAKE ==")
pt_take = pedir_punto("TAKE")
pt_left = None
if pt_take is not None:
    print("== Punto para LEFT ==")
    pt_left = pedir_punto("LEFT")

salir = pt_take is None or pt_left is None

while not salir:
    mostrar_resumen(pt_take, pt_left)
    cmd = input("Y=iniciar | X=salir | T=reingresar punto take | L=reingresar punto left: ").strip().lower()

    if cmd == "x":
        break
    elif cmd == "t":
        nuevo = pedir_punto("TAKE")
        if nuevo is None:
            break
        pt_take = nuevo
    elif cmd == "l":
        nuevo = pedir_punto("LEFT")
        if nuevo is None:
            break
        pt_left = nuevo
    elif cmd == "y":
        ok = ejecutar_take(pt_take["ang"])
        if ok:
            print("Toma del objeto terminada.")
            descanso("TAKE -> LEFT")
            ok = ejecutar_left(pt_left["ang"])
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
