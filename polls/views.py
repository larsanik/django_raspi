from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from polls.ant10 import AHT10

def index(request):
    m = AHT10(1)
    data = m.getData()
    return HttpResponse("Hello, world. You're at the polls index." + "Temperature: %.2f C" % data[0] + "Humidity: %.2f " % data[1] + "%")
