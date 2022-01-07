from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
from django.shortcuts import render
from ant10 import AHT10
from bmp180_a import readBmp180

def index(request):
    m = AHT10(1)
    data = m.getData()
    temperature = data[0]
    humidity = data[1]
    temp, pressure, altitude = readBmp180()
    press = pressure / (100.0 * 1.333)
    # return HttpResponse("Temperature: %.2f C " % temperature + "Humidity: %.2f " % humidity + "% " + "Pressure:    %.2f mmHg" % press)
    return render(
        request,
        'index.html',
        context={'temperature': temperature, 'humidity': humidity, 'press': press},
    )
