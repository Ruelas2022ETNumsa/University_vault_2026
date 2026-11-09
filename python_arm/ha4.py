from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait, StopWatch

# ha4.py = ha3.py + ESTADO INICIAL en paralelo + MUNECA A 0 tras agarrar
#
# Cambios respecto a ha3.py:
#   1) ESTADO INICIAL: al iniciar, los motores van a 0 UNO POR UNO (muneca -> codo -> hombro -> garra)
#      sin pedir nada, MIENTRAS el usuario ingresa los angulos (ver INICIO_EN_PARALELO).
#      No se hace reset_angle al arrancar: se usa el cero que el hub ya tiene.
#      Se repite despues de una secuencia abortada (el brazo puede no estar en inicio).
#      Despues de una secuencia completa NO hace falta: el brazo ya esta en 0 y se hace reset_angle(0).
#   2) TAKE: garra abre -> hombro -> codo -> muneca -> garra cierra -> MUNECA A 0
#      (la muneca se retrae para no ARRASTRAR el objeto) -> LEFT lleva el objeto al destino.
#   3) Si pulsas Y antes de que termine el estado inicial, espera a que termine.
#
# Se mantiene: un solo motor energizado a la vez (cada motor se SUELTA con stop() al llegar),
# monitoreo de voltaje con pausa (g/x), inclinacion del hub al inicio y final del ciclo,
# y reinicio automatico al terminar (vuelve a pedir valores).
#
# Cableado (recableado el 8-nov-2026):
#   A = hombro | C = muneca | D = codo | E = garra | F = sensor de color (no se usa aqui) | B = vacio

# Cambiar PrimeHub por tu hub: InventorHub, EssentialHub, CityHub, etc.
hub = PrimeHub()

# Lectura del teclado SIN bloquear (para mover motores mientras se escriben los angulos)
try:
    from usys import stdin
    from uselect import poll
    teclado = poll()
    teclado.register(stdin)
except ImportError:
    teclado = None

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

# True : el estado inicial ocurre mientras escribes los angulos (necesita poder leer el teclado
#        sin bloquear; si tu firmware no lo permite se cambia solo a False)
# False: primero se llevan los motores a 0 y DESPUES se piden los angulos
INICIO_EN_PARALELO = True

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

def inclinacion():
    """Texto con la inclinacion del hub (cabeceo/pitch y balanceo/roll, en grados)."""
    try:
        pitch, roll = hub.imu.tilt()
        return "cabeceo {} deg | balanceo {} deg".format(pitch, roll)
    except Exception:
        return "(no disponible)"


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


# Estadisticas de la corrida (se muestran al final de cada ciclo y al salir)
STATS = {"vmin": 99999, "vmin_en": "-", "imax": 0, "imax_en": "-", "pausas": 0}


def actualizar_stats(etapa, v, i):
    if v < STATS["vmin"]:
        STATS["vmin"] = v
        STATS["vmin_en"] = etapa
    if i > STATS["imax"]:
        STATS["imax"] = i
        STATS["imax_en"] = etapa


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
    actualizar_stats(etapa, v, i)
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


# ---------------- Estado inicial (en paralelo con la entrada de datos) ----------------

# Maquina de estados: se avanza llamando homing_tick() cada ~20 ms mientras se espera el teclado.
# Mueve UN motor a la vez a 0 (muneca -> codo -> hombro -> garra) y lo suelta al llegar.
HOMING = {"activo": False, "i": 0, "arrancado": False, "pausado": False,
          "bajos": 0, "reloj": None, "vmin": 0, "imax": 0}


def homing_iniciar():
    HOMING["activo"] = True
    HOMING["i"] = 0
    HOMING["arrancado"] = False
    HOMING["pausado"] = False


def homing_tick():
    """Un paso del estado inicial. No bloquea."""
    if not HOMING["activo"]:
        return
    nombre, motor, timeout = SECUENCIA_INICIO[HOMING["i"]]

    if not HOMING["arrancado"]:
        HOMING["vmin"] = hub.battery.voltage()
        HOMING["imax"] = hub.battery.current()
        HOMING["bajos"] = 0
        HOMING["reloj"] = StopWatch()
        HOMING["arrancado"] = True
        print("  [inicio] {} -> 0 ...".format(nombre))
        motor.run_target(VELOCIDAD, 0, wait=False)
        return

    v = hub.battery.voltage()
    i = hub.battery.current()
    if v < HOMING["vmin"]:
        HOMING["vmin"] = v
    if i > HOMING["imax"]:
        HOMING["imax"] = i
    actualizar_stats(nombre, v, i)

    if HOMING["pausado"]:
        # espera automatica a que el voltaje se recupere (motor soltado)
        if v >= UMBRAL_AVISO_MV:
            HOMING["pausado"] = False
            HOMING["bajos"] = 0
            print("  [inicio] voltaje recuperado ({} mV), retomando {}".format(v, nombre))
            motor.run_target(VELOCIDAD, 0, wait=False)
            HOMING["reloj"] = StopWatch()
        return

    if v < UMBRAL_MV:
        HOMING["bajos"] += 1
        if HOMING["bajos"] >= MUESTRAS_CORTE:
            motor.stop()
            HOMING["pausado"] = True
            STATS["pausas"] += 1
            print("  [inicio] !! VOLTAJE BAJO: {} mV con {} mA, motor soltado; espero a que se recupere".format(v, i))
        return
    HOMING["bajos"] = 0

    termino = motor.done()
    if not termino and HOMING["reloj"].time() > timeout:
        print("  [inicio] ! timeout en", nombre)
        termino = True
    if termino:
        motor.stop()
        print("  [inicio] {} en {} deg | Vmin {} mV | Imax {} mA | soltado".format(
            nombre, motor.angle(), HOMING["vmin"], HOMING["imax"]))
        HOMING["i"] += 1
        HOMING["arrancado"] = False
        if HOMING["i"] >= len(SECUENCIA_INICIO):
            HOMING["activo"] = False
            print("  [inicio] Estado inicial completo: motores en 0.")


def esperar_homing():
    """Bloquea hasta que termine el estado inicial (si sigue en curso)."""
    if HOMING["activo"]:
        print("Esperando a que termine el estado inicial...")
    while HOMING["activo"]:
        homing_tick()
        wait(PERIODO_MS)


def leer(prompt):
    """Como input(), pero mientras el estado inicial sigue en curso NO bloquea:
    avanza los motores y lee el teclado caracter a caracter."""
    if not HOMING["activo"] or teclado is None:
        return input(prompt)
    print(prompt, end="")
    buffer = ""
    while True:
        homing_tick()
        while teclado.poll(0):
            ch = stdin.read(1)
            if not ch:
                continue
            if ch == "\n" or ch == "\r":
                if buffer != "":
                    return buffer
            else:
                buffer += ch
        wait(PERIODO_MS)


# ---------------- Entrada de angulos ----------------

def pedir_angulo(titulo, clave):
    """Pide el angulo de una articulacion hasta que este en rango. Devuelve None si escribe X."""
    motor, mult, vmin, vmax = ARTICULACIONES[clave]
    while True:
        texto = leer("[{}] {} ({}) [{} a {}]: ".format(
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
    """Garra abre -> A -> D -> C -> garra cierra -> MUNECA A 0 (no arrastrar el objeto)."""
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

    # La muneca vuelve a 0 para que el objeto no se arrastre durante el traslado
    ok, minimo = mover(muneca, 0, TIMEOUT_ART_MS)
    print("C muneca -> 0 (retirada) | motor {} deg | minimo: {} mV".format(muneca.angle(), minimo))
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
    print("TAKE: garra abre a", GARRA_ABIERTA, "al inicio, cierra a", GARRA_CERRADA, "y la muneca vuelve a 0")
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


def mostrar_monitoreo():
    if STATS["vmin_en"] != "-":
        print("=== Monitoreo (acumulado) ===")
        print("Voltaje minimo: {} mV en {}".format(STATS["vmin"], STATS["vmin_en"]))
        print("Corriente maxima: {} mA en {}".format(STATS["imax"], STATS["imax_en"]))
        print("Pausas por voltaje bajo: {}".format(STATS["pausas"]))
        print("Bateria: {} mV".format(hub.battery.voltage()))


# --- Programa principal ---
# Limites opcionales (una sola vez)
for m in (hombro, codo, muneca, garra):
    if ACELERACION is not None:
        m.control.limits(acceleration=ACELERACION)
    if TORQUE_MAX is not None:
        m.control.limits(torque=TORQUE_MAX)

paralelo = INICIO_EN_PARALELO and teclado is not None
if INICIO_EN_PARALELO and teclado is None:
    print("! No se pudo leer el teclado sin bloquear: el estado inicial se hara ANTES de pedir angulos.")

necesita_inicio = True   # True al arrancar y tras una secuencia abortada
ciclo = 0
salir = False

while not salir:
    ciclo += 1
    print("===== Ciclo {} =====".format(ciclo))
    print("Bateria en reposo: {} mV, {} mA".format(hub.battery.voltage(), hub.battery.current()))
    print("Inclinacion hub INICIAL: " + inclinacion())
    print("Puertos: A hombro | D codo | C muneca | E garra | F sensor color (sin uso)")

    if necesita_inicio:
        # Estado inicial: todos los motores a 0, uno por uno, sin pedir nada.
        # No hay reset_angle: se usa el cero que el hub ya tiene.
        print("Estado inicial: motores a 0 (muneca -> codo -> hombro -> garra).")
        homing_iniciar()
        if not paralelo:
            esperar_homing()
        else:
            print("(ocurre mientras ingresas los angulos)")
    else:
        # Secuencia anterior completa: el brazo esta en inicio, esa posicion es el nuevo 0.
        for m in (hombro, codo, muneca, garra):
            m.reset_angle(0)

    print("Escribi 'x' para salir. Rangos: A 0-270, D -180 a 45, C 0-190.")

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
        cmd = leer("Y=iniciar | X=salir | TA/TD/TC o LA/LD/LC=reingresar: ").strip().lower()

        if cmd == "x":
            salir = True
            break
        elif cmd in ("ta", "td", "tc"):
            valor = pedir_angulo("TAKE", cmd[1].upper())
            if valor is None:
                salir = True
                break
            ang_take[cmd[1].upper()] = valor
        elif cmd in ("la", "ld", "lc"):
            valor = pedir_angulo("LEFT", cmd[1].upper())
            if valor is None:
                salir = True
                break
            ang_left[cmd[1].upper()] = valor
        elif cmd == "y":
            esperar_homing()   # el estado inicial debe haber terminado antes de la secuencia
            ok = ejecutar_secuencia(ang_take, ang_left)
            detener_todo()
            necesita_inicio = not ok
            if ok:
                print("Brazo en posicion inicial. Secuencia completa.")
            else:
                print("Secuencia abortada por el usuario (x) tras voltaje bajo -> motores detenidos.")
                print("En el siguiente ciclo los motores volveran a 0 (estado inicial).")
            print("Inclinacion hub FINAL: " + inclinacion())
            mostrar_monitoreo()
            break
        else:
            print("Comando no valido.")

HOMING["activo"] = False
detener_todo()
print("Inclinacion hub al salir: " + inclinacion())
mostrar_monitoreo()
print("Programa terminado.")
