from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from raspi.input.input import sensorPolling

def profile(request):
    temperature, humidity, press = sensorPolling()
    data = {
        'temperature': temperature,
        'humidity': humidity,
        'press': press
    }
    return JsonResponse(data)