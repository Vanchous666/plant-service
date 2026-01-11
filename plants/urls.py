from django.urls import path
from . import views

urlpatterns = [
    path('', views.plants_list, name='plants_list'),
    path('<int:plant_id>/', views.plant_detail, name='plant_detail'),
]