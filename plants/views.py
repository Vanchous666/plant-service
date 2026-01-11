from django.shortcuts import render
from .models import Plant

def plants_list(request):
    plants = Plant.objects.all()
    return render(request, 'plants/list.html', {'plants': plants})

def plant_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    return render(request, 'plants/detail.html', {'plant': plant})
