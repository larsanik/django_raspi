from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from ant10 import AHT10
m = AHT10(1)

def index(request):
    data = m.getData()
    return HttpResponse("Hello, world. You're at the polls index." + "Temperature: %.2f C" % data[0] + "Humidity: %.2f " % data[1] + "%")
