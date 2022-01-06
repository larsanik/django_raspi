from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from polls.ant10 import AHT10
from polls.bmp180_a import readBmp180

def index(request):
    m = AHT10(1)
    data = m.getData()
    temp, pressure, altitude = readBmp180()
    return HttpResponse("Temperature: %.2f C " % data[0] + "Humidity: %.2f " % data[1] + "% " + "Pressure:    %.2f mmHg" % (pressure / (100.0 * 1.333)))
