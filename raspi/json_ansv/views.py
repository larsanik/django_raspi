from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
def profile(request):
    data = {
        'name': 'Raghav',
        'location': 'India',
        'is_active': False,
        'count': 28
    }
    return JsonResponse(data)