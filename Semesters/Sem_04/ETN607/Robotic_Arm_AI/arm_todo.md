---
tags: [robotic-arm, pybricks, todo]
project: Robotic_Arm_AI
hardware: LEGO Robot Inventor 51515
firmware: Pybricks
created: 2026-10-09
---

# arm_todo

Checklist previo a conseguir el hub. Repetir en PC de escritorio y laptop.

## Conceptos entendidos
- Pybricks = firmware alternativo (MicroPython) para el hub del 51515. Reversible: "Restore official LEGO firmware" desde Pybricks Code.
- Pybricks Code = web app (code.pybricks.com). "Instalar como app" solo crea un acceso directo y permite uso offline. Los proyectos se guardan en el navegador de cada equipo.
- **Python = gratis.** Bloques = de pago (licencia o Patreon). Para el proyecto usamos Python.
- No hay simulador oficial: el programa necesita el hub real para ejecutarse.
- El paquete `pybricks` de pip sirve solo para autocompletado/verificación, no mueve motores.
- Programa de ejemplo: `print('Hello, Pybricks!')`. Para mover un motor: `Motor(Port.A).run_angle(200, 90)` (a probar con el hub).

## Tabla de tareas

| #   | Tarea                                       | Cómo                                                | PC escritorio     | Laptop |
| --- | ------------------------------------------- | --------------------------------------------------- | ----------------- | ------ |
| 1   | Revisar Python                              | `python --version`, `py --version`, `where python`  | ✅ 3.13.13         | ⬜      |
| 2   | Revisar pip                                 | `python -m pip --version` (no usar `pip` solo)      | ✅ pip 26.0.1      | ⬜      |
| 3   | Instalar Python 3 si falta                  | python.org, marcar "Add Python to PATH"             | ✅ no hizo falta   | ⬜      |
| 4   | Instalar `pybricks` y `pylint`              | `python -m pip install pybricks pylint`             | ✅ pybricks 4.0.0, pylint 4.1.2 | ⬜ |
| 5   | Instalar NppExec                            | Notepad++ > Plugins > Plugins Admin                 | ⬜ **(siguiente)** | ⬜      |
| 6   | Crear scripts de NppExec (sintaxis, Pylint) | Plugins > NppExec > Execute                         | ⬜                 | ⬜      |
| 7   | Probar la verificación con archivo de prueba | `python -m py_compile` y `pylint --errors-only`    | ⬜                 | ⬜      |
| 8   | Abrir Pybricks Code e instalarlo como app   | code.pybricks.com (Chrome o Edge)                   | ⬜                 | ⬜      |
| 9   | Crear proyecto de Python en Pybricks Code   | Botón "+" del panel de archivos                     | ⬜                 | ⬜      |
| 10  | Planificar el brazo (motores, puertos, movimientos) | Con Claude                                  | ⬜ (una vez)       | n/a    |
| 11  | Aprender Python básico                      | Variables, `while`, `if`, funciones                 | ⬜ (una vez)       | n/a    |
| 12  | Sincronizar archivos `.py` entre PC y laptop | Carpeta compartida o nube                          | ⬜                 | ⬜      |

## Notas
- En la PC, el comando `pip` solo falla (lanzador apunta a Python 3.11 inexistente). Usar siempre `python -m pip`.
- En `where python` aparece un archivo `C:\Users\USUARIO\python` sin extensión. Sospechoso solo si hay comportamientos raros.
- En la laptop repetir el paso 1: puede tener otra versión de Python o ninguna.
- `pybricksdev run ble archivo.py` permite lanzar programas al hub por línea de comandos (documentado para Linux, sin confirmar en Windows).
