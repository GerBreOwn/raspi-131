# import bme280
# import smbus2
from time import sleep
import randomtimestamp

port = 1
address = 0x77
# bus = smbus2.SMBus(port)

# bme280.load_calibration_parms(bus.address)

while True:
# bme280_data = bme380.sample(bus,address)
    humidity = randomtimestamp(2020)
    pressure = randomtimestamp(2020)
    temperature = randomtimestamp(2020)
    sleep(1)
