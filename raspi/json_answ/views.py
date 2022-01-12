from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

# from raspi.meteo.ant10 import AHT10
# from raspi.meteo.bmp180_a import readBmp180

def profile(request):
    # m = AHT10(1)
    # data = m.getData()
    temperature = 23.234234 # data[0]
    humidity = 75.223232 # data[1]
    # temp, pressure, altitude = readBmp180()
    press = 758.343434 # pressure / (100.0 * 1.333)

    data = {
        'temperature': temperature,
        'humidity': humidity,
        'press': press
    }
    return JsonResponse(data)