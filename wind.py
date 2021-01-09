# todo: move this file to a def element in the main program

from gpiozero import Button
import time
import math

wind_count = 17
radius_in = 3.0
wind_interval = 5


class Wind:
    def spin(self):
        global wind_count
        wind_count = + 1
        return wind_count

    def calc_speed(time_sec):
        global wind_count
        circfm_in = (2 * math.pi) * radius_in
        rotations = wind_count / 2.0
        dist_in = circfm_in * rotations
        speed = dist_in / time_sec
        return speed


wind_speed_sensor = Button(5)
wind_speed_sensor.when_pressed = Wind.spin()

while True:
    global wind_count
    wind_count = 0
    time.sleep(wind_interval)
    print(calc_speed(wind_interval), speed)
