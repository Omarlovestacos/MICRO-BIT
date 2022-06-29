from microbit import *
from ssd1306 import initialize, clear_oled
from ssd1306_text import add_text
from ultrasonic import Ultrasonic

ultrasonic_sensor = Ultrasonic()

initialize()
clear_oled()

while True:
    distance_value = ultrasonic_sensor.measure_distance_cm()
    #display.scroll(str(int(distance_value)))
    motion = pin1.read_digital()
    if motion == 1 and distance_value < 15:
        add_text(0, 0, "motion detected")
        pin0.write_digital(1)
        pin16.write_digital(1)
    else:
        pin16.write_digital(0)
        add_text(0, 0, "no motion detected")
        pin0.write_digital(0)


