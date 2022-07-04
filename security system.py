from microbit import *
from ultrasonic import Ultrasonic

ultrasonic_sensor = Ultrasonic()
pin0.set_analog_period(20)

while True:
    distance_value = ultrasonic_sensor.measure_distance_cm()

    motion = pin1.read_digital()
    if motion == 1 and distance_value < 15:
        pin1.write_digital(1)
        pin16.write_digital(1)
    else:
        pin16.write_digital(0)
        pin1.write_digital(0)

while True:
    pin0.write_analog(360)
