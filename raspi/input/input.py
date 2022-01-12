# from ant10 import AHT10
# from bmp180_a import readBmp180
#import time
import random

def sensorPolling():
    #while True:
    #time.sleep(3)
    # m = AHT10(1)
    # data = m.getData()
    # temperature = data[0]
    # humidity = data[1]
    # temp, pressure, altitude = readBmp180()
    # press = 758.343434 # pressure / (100.0 * 1.333)
    temperature_out = random.uniform(-40.0, 40.0)
    humidity_out = random.uniform(60.0, 90.0)
    press_out = random.uniform(740.0, 780.0)
    #print(temperature, '***', humidity, '***', press)
    return temperature_out, humidity_out, press_out
