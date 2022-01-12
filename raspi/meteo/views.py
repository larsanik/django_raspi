# from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
from django.shortcuts import render
from raspi.input.input import sensorPolling


def index(request):
    temperature, humidity, press = sensorPolling()
    return render(
        request,
        'index.html',
        context={'temperature': temperature, 'humidity': humidity, 'press': press},
    )
