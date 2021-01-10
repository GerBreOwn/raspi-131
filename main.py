import math
from random import randrange
from time import sleep
import statistics

# wind_count = 17
import gpiozero
from gpiozero import Button

radius_in = 3.0
wind_interval = 5
# wind_speed_sensor = gpiozero.Button(5)
wind_count = 0

store_wind_speeds = []
store_temp = []
store_humidity = []
store_pressure = []

def rain():
    bucket_size = 0.2794

def bme280a():
    port = 1    
    address: int = 0x77
    # bus = smbus2.SMBus(port)
    # bme280.load.calibration_params(bus,address)
    #while True
    for i in range(6):
        #bme280_data = bme280.sample(bus, address)
        temperature = randrange(60, 110) # bme280_data.temperature
        store_temp.append(temperature)
        humidity = randrange(0, 100) # bme280_data.humidity
        store_humidity.append(humidity)
        pressure = randrange(60, 100) # bme280_data.pressure
        store_pressure.append(pressure)
        print("Temp", temperature, "HUM", humidity, "PRES", pressure)
        print("Max T", max(store_temp))
        print("Avg T", statistics.mean(store_temp) )
        print("Max Hu",max(store_humidity))
        print("Max Pre", max(store_pressure))
        print('AVG', avg)
        sleep(1)

def reset_wind():
    wind_count = 0

class Wind():
    def spin(self):
        wind_count += 1
        return wind_count

    def calc_speed(time_sec):
        global wind_count
        global wind_speed
        circfm_in = (2 * math.pi) * radius_in
        rotations = wind_count / 2.0
        dist_in = circfm_in * rotations
        wind_speed = dist_in / time_sec
        return wind_speed

# wind_speed_sensor.when_pressed = Wind.spin()
"""
while True:
    # global wind_count
    wind_count = 0
    sleep(wind_interval)
    print(Wind.calc_speed(wind_interval), wind_speed)
"""
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bme280a()
    Wind()
    rain()