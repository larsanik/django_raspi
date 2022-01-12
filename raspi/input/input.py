from raspi.input.ant10 import AHT10
from raspi.input.bmp180_a import readBmp180
# import time
# import random # only for testing

def sensorPolling():
    # while True:
    # time.sleep(3)
    m = AHT10(1)
    data = m.getData()
    #temperature = data[0]
    #humidity = data[1]
    temp, pressure, altitude = readBmp180()
    press = pressure / (100.0 * 1.333)
    temperature_out =  data[0] # random.uniform(-40.0, 40.0)
    humidity_out = data[1] # random.uniform(60.0, 90.0)
    press_out = press # random.uniform(740.0, 780.0)
    # print(temperature, '***', humidity, '***', press)
    return temperature_out, humidity_out, press_out
