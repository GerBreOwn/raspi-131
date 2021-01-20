#! /usr/bin/python3.7

import math
import statistics
from random import randrange
from time import sleep

# import bme280
import psycopg2
#import connect

# from gpiozero import Button

radius_in = 3.0
radius_cm = radius_in * 2.5
#wind_interval = 5
# wind_speed_sensor = Button(5)
# rain_sensor = Button(6)
wind_count = 0
secs_in_an_hour = 3600
cm_in_a_km = 100000
in_in_a_mile = 63360
store_record = list(range(7))

while True:

    class Rain:
        store_rain = []
        print("Rain")
        for i in range(11):
            #def bucket_tipped(self):
            rain_count = randrange(0, 50)  # 0
            bucket_size = 0.2794
        #global rain_count
        # rain_count += 1.0
        # print("Rain", rain_count * bucket_size)
        #return rain_count
            s = rain_count * bucket_size
            store_rain.append(s)

        rainfall = round(statistics.mean(store_rain), 2)
        store_record[6] = rainfall
    #rain_sensor.when_pressed = bucket_tipped()


    class Bme280:
        print("bme280")
        store_temp = []
        store_humidity = []
        store_pressure = []
        port = 1
        address: int = 0x77
    # bus = smbus2.SMBus(port)
    # bme280.load.calibration_params(bus,address)

        for i in range(11):
            # bme280_data = bme280.sample(bus, address)
            temperature = randrange(60, 110)  # bme280_data.temperature
            store_temp.append(temperature)
            temper = round(statistics.mean(store_temp), 2)

            humidity = randrange(0, 100)  # bme280_data.humidity
            store_humidity.append(humidity)
            humid = round(statistics.mean(store_humidity), 2)

            pressure = randrange(60, 100)  # bme280_data.pressure
            store_pressure.append(pressure)
            press = round(statistics.mean(store_pressure), 2)

#       sleep(1)

            store_record[0] = temper
            store_record[1] = press
            store_record[2] = humid
#print("Rec =", store_record)
# def reset_wind(self):
    #    wind_count = 0


    class Wind:
        store_wind_speeds = []
        store_wind_direct = []
        store_wind_gust = []
        print("Wind")
        for i in range(11):
            def spin(self):
                global wind_count
                wind_count += 1

        for j in range(11):
            def calc_speed(self):
                global wind_count
        # global wind_speed
        # circfm_cm = (2 * math.pi) * radius_cm
            circfm_in = (2 * math.pi) * radius_in
            wind_count = randrange(0, 50)
            rotations = wind_count / 2.0
            # dist_km = (circfm_cm * rotations) / cm_in_a_km
            dist_mi = circfm_in * rotations / in_in_a_mile
        # km_per_sec = dist_km / time_sec
        # km_per_hr = km_per_sec * secs_in_an_hour
        # in_per_sec = dist_mi / time_sec
        #mph: Union[int, Any] = in_per_sec * secs_in_an_hour
            wind_speed = randrange(0, 100)
            store_wind_speeds.append(wind_speed)

            wind_direct = randrange(0, 359)
            store_wind_direct.append(wind_direct)

            wind_gust = randrange(50, 125)
            store_wind_gust.append(wind_gust)

            speed = round(statistics.mean(store_wind_speeds), 2)
            direct = round(statistics.mean(store_wind_direct), 2)
            gust = round(statistics.mean(store_wind_gust), 2)

            store_record[3] = direct
            store_record[4] = speed
            store_record[5] = gust
        # return km_per_hr
        # return mph


    class WriteData:
        conn = psycopg2.connect("user=gerald dbname=weather host=192.168.1.142 password=CasC#373")
        #    except:
        #       print("Unable to connect to the database.")

        conn.autocommit = True
        cursor = conn.cursor()

        sql_command = """
            insert into
            wx
            (temperature, 
            pressure, 
            humidity, 
            wind_direction, 
            wind_speed, 
            wind_gust, 
            rainfall)
            values
            (%s,%s,%s,%s,%s,%s,%s)
            """

        cursor.execute(sql_command, (store_record[0],
                                     store_record[1],
                                     store_record[2],
                                     store_record[3],
                                     store_record[4],
                                     store_record[5],
                                     store_record[6]
                                     ))
        print("rec wrote", store_record)

    sleep(10.0)

# wind_speed_sensor.when_pressed = Wind.spin()
#if __name__ == '__main__':
#    i = 0
#    while True:
#        print("Starting", i)
#        i += 1
#        Bme280()
#        Wind()
#        Rain()
#        print("Write data")
#        WriteData()
#        print("Wrote data")
#        sleep(5.0)
