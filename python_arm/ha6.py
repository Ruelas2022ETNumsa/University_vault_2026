from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait, StopWatch

# ha6.py = ha5.py con el cableado y los nombres del brazo nuevo (13-nov-2026):
#   F = BASE giratoria (rotacional; 360 posibles pero se evita forzarlo por el cable USB)
#   D = HOMBRO (levanta el brazo; rango -120 a 180)  <- era "codo" en ha5.py
#   A = MUNECA (diseno aun no final; gira como rotacional)
#   B = GARRA  (antes estaba en E)
#   C = libre | E = libre (el brazo ya no tiene sensor de color)
#
# Cambios respecto a ha5.py:
#   1) Renombrado: hombro(A) -> base | codo(D) -> hombro
#   2) Garra pasa del puerto E al B
#   3) Rango del hombro (D): -120 a 180 (antes -180 a 45)
#   4) Base pasa del puerto A al F y muneca del C al A (menos tension en los cables)
#   5) Multiplicadores corregidos: hombro (D) x3 (antes x1) y muneca (A) x1 (antes x3)
# Flujos, monitoreo y umbrales: iguales a ha5.py.
#
# Se mantiene: un solo motor energizado a la vez (cada motor se SUELTA con stop() al llegar),
# monitoreo de voltaje con pausa (g/x), inclinacion del hub al inicio y final de cada ciclo,
# y reinicio automatico al terminar (vuelve a pedir valores).
#
# Flujo TAKE : garra abre -> base -> hombro -> muneca -> garra cierra -> muneca a 0 -> hombro a 0
# Flujo LEFT : base -> hombro -> muneca -> garra abre
# Flujo INICIO: muneca -> hombro -> base -> garra, todos a 0
#
# Cableado (13-nov-2026):
#   F = base | D = hombro | A = muneca | B = garra | C = libre | E = libre

# Cambiar PrimeHub por tu hub: InventorHub, EssentialHub, CityHub, etc.
hub = PrimeHub()

base = Motor(Port.F, Direction.CLOCKWISE)
muneca = Motor(Port.A, Direction.CLOCKWISE)
hombro = Motor(Port.D, Direction.CLOCKWISE)
garra = Motor(Port.B, Direction.CLOCKWISE)

VELOCIDAD = 200          # grados/segundo del MOTOR (todos los motores)
UMBRAL_MV = 5500         # si el voltaje baja de esto (3 muestras seguidas), se PAUSA el programa
UMBRAL_AVISO_MV = 6000   # por debajo de esto se imprime un aviso (no pausa)
MUESTRAS_CORTE = 3       # muestras SEGUIDAS bajo UMBRAL_MV para pausar (filtra picos de 1 muestra)
PERIODO_MS = 20          # cada cuanto se mide durante el movimiento
TIMEOUT_ART_MS = 10000   # tiempo maximo por movimiento de articulacion
TIMEOUT_GARRA_MS = 3000  # tiempo maximo para la garra
ESPERA_INICIO_MS = 500   # espera antes de volver a inicio (tiempo para alejarse)
DESCANSO_FASES_MS = 1000 # pausa con motores sueltos entre fases (recupera bateria)

# Inclinacion del hub: False = solo inicio y final de cada ciclo | True = ademas tras cada movimiento
MOSTRAR_INCLINACION_POR_MOVIMIENTO = False

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
    "F": (base, 3, 0, 270),
    "D": (hombro, 3, -120, 180),
    "A": (muneca, 1, 0, 190),
}
ORDEN = ["F", "D", "A"]  # base -> hombro -> muneca
NOMBRES = {"F": "base", "D": "hombro", "A": "muneca"}

# Secuencia de inicio: (nombre, motor, timeout) en orden muneca -> hombro -> base -> garra
SECUENCIA_INICIO = [
    ("A muneca", muneca, TIMEOUT_ART_MS),
    ("D hombro", hombro, TIMEOUT_ART_MS),
    ("F base", base, TIMEOUT_ART_MS),
    ("B garra", garra, TIMEOUT_GARRA_MS),
]


# ---------------- Utilidades comunes ----------------

def inclinacion():
    """Texto con la inclinacion del hub (cabeceo/pitch y balanceo/roll, en grados)."""
    try:
        pitch, roll = hub.imu.tilt()
        return "cabeceo {} deg | balanceo {} deg".format(pitch, roll)
    except Exception:
        return "(no disponible)"


def detener_todo(incluir_garra=True):
    """Suelta los motores (stop = sin alimentacion)."""
    for m in (base, hombro, muneca):
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
    if motor is base:
        return "F base"
    if motor is hombro:
        return "D hombro"
    if motor is muneca:
        return "A muneca"
    return "B garra"


# Estadisticas de la corrida (se muestran al final de cada ciclo y al salir)
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
    if MOSTRAR_INCLINACION_POR_MOVIMIENTO:
        print("  inclinacion hub: " + inclinacion())
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
    """Mueve base -> hombro -> muneca, UNO A LA VEZ, soltando cada uno al llegar."""
    for k in ORDEN:
        motor, mult, vmin, vmax = ARTICULACIONES[k]
        objetivo = int(angulos[k] * mult)
        ok, minimo = mover(motor, objetivo, TIMEOUT_ART_MS)
        print("{} -> {} deg articulacion (motor {} deg) | minimo: {} mV".format(
            k, a_articulacion(motor, mult), motor.angle(), minimo))
        if not ok:
            return False
    return True


def llevar_a_cero():
    """A -> D -> F -> garra, todos a 0 (posicion de calibracion), uno por uno.
    Devuelve False si el usuario aborta ('x') durante una pausa por voltaje."""
    for nombre, motor, timeout in SECUENCIA_INICIO:
        ok, minimo = mover(motor, 0, timeout)
        print("{} -> {} deg | minimo: {} mV".format(nombre, motor.angle(), minimo))
        if not ok:
            return False
    return True


# ---------------- Fases ----------------

def ejecutar_take(angulos):
    """Garra abre -> F -> D -> A -> garra cierra -> muneca a 0 -> hombro a 0 (no arrastrar el objeto)."""
    ok, minimo = mover(garra, GARRA_ABIERTA, TIMEOUT_GARRA_MS)
    print("Garra abierta | minimo:", minimo, "mV")
    if not ok:
        return False

    if not mover_articulaciones(angulos):
        return False

    ok, minimo = mover(garra, GARRA_CERRADA, TIMEOUT_GARRA_MS, mantener=not SOLTAR_GARRA_CERRADA)
    print("Garra cerrada | minimo:", minimo, "mV")
    if not ok:
        return False

    # Con el objeto tomado, muneca y hombro vuelven a 0: el objeto no se arrastra durante el traslado
    ok, minimo = mover(muneca, 0, TIMEOUT_ART_MS)
    print("A muneca -> 0 (retirada) | motor {} deg | minimo: {} mV".format(muneca.angle(), minimo))
    if not ok:
        return False

    ok, minimo = mover(hombro, 0, TIMEOUT_ART_MS)
    print("D hombro -> 0 (retirada) | motor {} deg | minimo: {} mV".format(hombro.angle(), minimo))
    return ok


def ejecutar_left(angulos):
    """F -> D -> A -> garra abre (suelta el objeto)."""
    if not mover_articulaciones(angulos):
        return False

    ok, minimo = mover(garra, GARRA_ABIERTA, TIMEOUT_GARRA_MS)
    print("Garra abierta | minimo:", minimo, "mV")
    return ok


def ejecutar_inicio():
    """A -> D -> F -> garra, todos a 0 (tras una espera para alejarse del objeto)."""
    wait(ESPERA_INICIO_MS)
    return llevar_a_cero()


def ejecutar_secuencia(ang_take, ang_left):
    """TAKE -> descanso -> LEFT -> descanso -> INICIO. Devuelve True si completo todo."""
    ok = ejecutar_take(ang_take)
    if ok:
        print("Toma del objeto terminada.")
        descanso("TAKE -> LEFT")
        ok = ejecutar_left(ang_left)
    if ok:
        print("Objeto soltado.")
        descanso("LEFT -> INICIO")
        ok = ejecutar_inicio()
    return ok


# ---------------- Interfaz ----------------

def mostrar_resumen(ang_take, ang_left):
    print("--- Resumen ---")
    print("TAKE: garra abre a", GARRA_ABIERTA, "al inicio, cierra a", GARRA_CERRADA,
          "y luego muneca y hombro vuelven a 0")
    for k in ORDEN:
        mult = ARTICULACIONES[k][1]
        print("  T{} ({}): {} deg articulacion -> motor {} deg (x{})".format(
            k, NOMBRES[k], ang_take[k], int(ang_take[k] * mult), mult))
    print("LEFT: traslado y la garra abre a", GARRA_ABIERTA, "al llegar")
    for k in ORDEN:
        mult = ARTICULACIONES[k][1]
        print("  L{} ({}): {} deg articulacion -> motor {} deg (x{})".format(
            k, NOMBRES[k], ang_left[k], int(ang_left[k] * mult), mult))
    print("INICIO: vuelve a 0 (A muneca -> D hombro -> F base -> B garra)")
    print("Cada motor se suelta al llegar. Descanso entre fases: {} ms".format(DESCANSO_FASES_MS))


def pedir_set(titulo):
    """Pide F, D, A para una fase. Devuelve el dict o None si el usuario sale."""
    angulos = {}
    for k in ORDEN:
        valor = pedir_angulo(titulo, k)
        if valor is None:
            return None
        angulos[k] = valor
    return angulos


def mostrar_monitoreo():
    if STATS["vmin_en"] != "-":
        print("=== Monitoreo (acumulado) ===")
        print("Voltaje minimo: {} mV en {}".format(STATS["vmin"], STATS["vmin_en"]))
        print("Corriente maxima: {} mA en {}".format(STATS["imax"], STATS["imax_en"]))
        print("Pausas por voltaje bajo: {}".format(STATS["pausas"]))
        print("Bateria: {} mV".format(hub.battery.voltage()))


# --- Programa principal ---
# Limites opcionales (una sola vez)
for m in (base, hombro, muneca, garra):
    if ACELERACION is not None:
        m.control.limits(acceleration=ACELERACION)
    if TORQUE_MAX is not None:
        m.control.limits(torque=TORQUE_MAX)

necesita_inicio = True   # True al arrancar y tras una secuencia abortada
ciclo = 0
salir = False

while not salir:
    ciclo += 1
    print("===== Ciclo {} =====".format(ciclo))
    print("Bateria en reposo: {} mV, {} mA".format(hub.battery.voltage(), hub.battery.current()))
    print("Inclinacion hub INICIAL: " + inclinacion())
    print("Puertos: F base | D hombro | A muneca | B garra | C y E libres")

    if necesita_inicio:
        # Estado inicial: todos los motores a 0, uno por uno, sin pedir nada.
        print("Estado inicial: motores a 0 (muneca -> hombro -> base -> garra)...")
        if not llevar_a_cero():
            print("Calibracion abortada por el usuario (x) tras voltaje bajo -> motores detenidos.")
            break
        print("Calibracion completa: todos los motores en 0.")

    # El brazo esta en inicio (calibrado o fin de una secuencia completa): esa posicion es el nuevo 0.
    for m in (base, hombro, muneca, garra):
        m.reset_angle(0)

    # Se espera un ENTER antes de mostrar la entrada de angulos
    cmd = input("Presiona Enter para ingresar los angulos (x = salir): ").strip().lower()
    if cmd == "x":
        break

    print("Escribi 'x' para salir. Rangos: F 0-270, D -120 a 180, A 0-190.")

    print("== Angulos para TAKE ==")
    ang_take = pedir_set("TAKE")
    ang_left = None
    if ang_take is not None:
        print("== Angulos para LEFT ==")
        ang_left = pedir_set("LEFT")

    if ang_take is None or ang_left is None:
        break

    while True:
        mostrar_resumen(ang_take, ang_left)
        cmd = input("Y=iniciar | X=salir | TF/TD/TA o LF/LD/LA=reingresar: ").strip().lower()

        if cmd == "x":
            salir = True
            break
        elif cmd in ("tf", "td", "ta"):
            valor = pedir_angulo("TAKE", cmd[1].upper())
            if valor is None:
                salir = True
                break
            ang_take[cmd[1].upper()] = valor
        elif cmd in ("lf", "ld", "la"):
            valor = pedir_angulo("LEFT", cmd[1].upper())
            if valor is None:
                salir = True
                break
            ang_left[cmd[1].upper()] = valor
        elif cmd == "y":
            ok = ejecutar_secuencia(ang_take, ang_left)
            detener_todo()
            necesita_inicio = not ok
            if ok:
                print("Brazo en posicion inicial. Secuencia completa.")
            else:
                print("Secuencia abortada por el usuario (x) tras voltaje bajo -> motores detenidos.")
                print("En el siguiente ciclo los motores volveran a 0 (calibracion).")
            print("Inclinacion hub FINAL: " + inclinacion())
            mostrar_monitoreo()
            break
        else:
            print("Comando no valido.")

detener_todo()
print("Inclinacion hub al salir: " + inclinacion())
mostrar_monitoreo()
print("Programa terminado.")
