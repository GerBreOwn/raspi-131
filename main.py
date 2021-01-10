import math
from random import randrange
from time import sleep
import statistics

# wind_count = 17
# import gpiozero
# from gpiozero import Button

radius_in = 3.0
radius_cm = radius_in * 2.5
wind_interval = 5
# wind_speed_sensor = gpiozero.Button(5)
wind_count = 0
secs_in_an_hour = 3600
cm_in_a_km = 100000
in_in_a_mile = 63360

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
        # print("Temp", temperature, "HUM", humidity, "PRES", pressure)
        #print("Total Temps", store_temp)
        #print("Max T", max(store_temp))
        print("Avg T", statistics.mean(store_temp) )
        #print("Max Hu",max(store_humidity))
        #print("Max Pre", max(store_pressure))
        sleep(1)

def reset_wind():
    wind_count = 0

class Wind():
    def spin(self):
        global wind_count
        wind_count += 1
        return wind_count

    def calc_speed(time_sec):
        global wind_count
        global wind_speed
        #circfm_cm = (2 * math.pi) * radius_cm
        circfm_in = (2 * math.pi) * radius_in

        rotations = wind_count / 2.0

        #dist_km = (circfm_cm * rotations) / cm_in_a_km
        dist_mi = circfm_in * rotations / in_in_a_mile

        #km_per_sec = dist_km / time_sec
        #km_per_hr = km_per_sec * secs_in_an_hour

        in_per_sec = dist_mi / time_sec
        mph = in_per_sec * secs_in_an_hour

        #return km_per_hr
        return mph


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