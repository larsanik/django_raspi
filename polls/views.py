from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from polls.ant10 import AHT10

def index(request):
    m = AHT10(1)
    data = m.getData()
    return HttpResponse("Temperature: %.2f C" % data[0] + "\n" "Humidity: %.2f " % data[1] + "%")
