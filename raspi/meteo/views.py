# from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
from django.shortcuts import render


# from raspi.meteo.ant10 import AHT10
# from raspi.meteo.bmp180_a import readBmp180

def index(request):
    # m = AHT10(1)
    # data = m.getData()
    temperature = 23.234234 # data[0]
    humidity = 75.223232 # data[1]
    # temp, pressure, altitude = readBmp180()
    press = 758.343434 # pressure / (100.0 * 1.333)
    # return HttpResponse("Temperature: %.2f C " % temperature + "Humidity: %.2f " % humidity + "% " + "Pressure:
    # %.2f mmHg" % press)
    return render(
        request,
        'index.html',
        context={'temperature': temperature, 'humidity': humidity, 'press': press},
    )
