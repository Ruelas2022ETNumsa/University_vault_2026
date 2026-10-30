from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait

# Motor conectado al puerto A
motor = Motor(Port.A, Direction.CLOCKWISE)

# Girar a 500 grados/segundo durante 2 segundos
motor.run(500)
wait(2000)

# Detener el motor
motor.stop()

# Alternativas:
# motor.run_angle(500, 360)    # gira 360 grados y se detiene
# motor.run_time(500, 2000)    # gira 2000 ms y se detiene
# motor.run_target(500, 90)    # va al angulo absoluto 90
