import math

import statistics
from datetime import time

from random import randrange
from time import sleep

import bme280
import smbus2
from gpiozero import Button

# wind_count = 17
radius_in = 3.0
wind_interval = 5

store_wind_speeds = []

def rain():
    bucket_size = 0.2794

def bme280a():
    port = 1    
    address: int = 0x77
    bus = smbus2.SMBus(port)
    bme280.load.calibration_params(bus,address)
    while True
        bme280_data = bme280.sample(bus, address)
        temperature = randrange(60, 110, 0.3) # bme280_data.temperature
        humidity = randrange(0, 100, 0.3) # bme280_data.humidity
        pressure = randrange(60, 100, 0.3) # bme280_data.pressure
        sleep(1)

def reset_wind():
    global wind_count
    wind_count = 0

class Wind():
    def spin(self):
        global wind_count
        wind_count += 1
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
    # global wind_count
    wind_count = 0
    sleep(wind_interval)
    print(calc_speed(wind_interval), speed)






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bme280a()
    Wind()
    rain()