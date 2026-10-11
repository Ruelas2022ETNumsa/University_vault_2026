---
tags: [robotic-arm, pybricks, lego, notas]
project: Robotic_Arm_AI
hardware: LEGO Robot Inventor 51515
created: 2026-10-09
related: "[[arm_todo]]"
---

# arm_pybricks-notas

Resumen de lo aprendido sobre Pybricks, el hub del 51515 y las apps de LEGO. Fuente: sesión del 2026-10-09 con Claude. Lo marcado con (?) no fue confirmado.

## Pybricks
- Firmware alternativo (MicroPython) para el hub del 51515. Reversible: **Restore official LEGO firmware** desde Pybricks Code.
- **Pybricks Code** = web app en code.pybricks.com (Chrome o Edge, Web Bluetooth/USB). "Instalar como app" solo crea un acceso directo y permite uso offline.
- Los proyectos se guardan **en el navegador de cada equipo**. Guardar copias `.py` en carpeta sincronizada.
- No conectar el hub desde los ajustes Bluetooth del sistema: conectar desde la app.
- Instalación del firmware: Pybricks Code > Install Pybricks Firmware > elegir hub > licencias > nombre > modo actualización > conectar.

## Gratis vs. de pago
- **Python = gratis y open source.** Es lo que usamos en el proyecto.
- Bloques = requiere licencia (código anual/vitalicio) o Patreon / GitHub Sponsors. No es necesario.
- En Pybricks Code, crear proyecto con el botón "+" y elegir **Python**. La ventana "Enable block coding" se puede cerrar.

## Programa base
```python
# The main program starts here.
print('Hello, Pybricks!')
```
Mover un motor (de memoria, probar con el hub):
```python
from pybricks.pupdevices import Motor
from pybricks.parameters import Port

motor = Motor(Port.A)
motor.run_angle(200, 90)
```

## Sin hub
- No hay simulador oficial de Pybricks: el programa corre dentro del hub.
- Sí se puede: escribir código, verificar sintaxis, leer docs (docs.pybricks.com), planificar el brazo.
- `pip install pybricks` instala módulos de apoyo (autocompletado/verificación), **no mueve motores**.
- `pybricksdev run ble archivo.py` lanza programas al hub por consola (documentado para Linux, Windows sin confirmar).

## Notepad++ (en vez de VS Code)
- Plugin **NppExec** (Plugins Admin).
- Verificar sintaxis: `npp_save` + `python -m py_compile "$(FULL_CURRENT_PATH)"`.
- Pylint: `pylint "$(FULL_CURRENT_PATH)" --errors-only`.
- Ejecutar el script en la PC fallará o no hará nada útil con el hardware: solo sirve para detectar errores.

## Apps de LEGO
- La app **Robot Inventor** se discontinuó el 1-oct-2026. Paquete Android: `com.lego.retail.mindstorms` (LEGO System A/S, ~542 MB).
- APKMirror tiene la ficha (v10.5.0) pero **no ofrece descarga** (retirada a pedido de LEGO). Aptoide: no recomendado.
- Las apps `Commander` y `EV3 Programmer` son de EV3, **no sirven** para el 51515.
- Alternativa oficial: **SPIKE App** de LEGO Education (Play Store, desarrollador "LEGO Education"). Elegir **Prime** (no Essential).
- SPIKE 2 (Legacy) y SPIKE 3 son **versiones de la app**, no hubs distintos. Requieren firmware distinto en el hub y no son compatibles entre sí.
- El hub del Inventor = **hub grande de SPIKE Prime** (mismo hardware).
- (?) Cuál versión de la app funciona mejor con el 51515: sin confirmar. Probar la instalada (SPIKE 3 probable).
- Al conectar, la app probablemente pedirá actualizar el Hub OS. No importa: Pybricks se instala encima.

## Entorno PC (escritorio)
- Python 3.13.13, pip 26.0.1, `pybricks 4.0.0`, `pylint 4.1.2` instalados.
- `pip` solo falla (lanzador a Python 3.11 inexistente): usar siempre `python -m pip`.
- Archivo `C:\Users\USUARIO\python` sin extensión: vigilar.
- Pendiente repetir en laptop.

Ver también: [[arm_hub-compra-checklist]], [[arm_todo]]
