"""
URL configuration for plant_service project.
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# ===== ТЕСТОВЫЕ VIEW =====
def test_view(request):
    """Тестовая страница для проверки URL"""
    return HttpResponse("🎉 УРА! Django работает правильно! Тест пройден!")

def home_view(request):
    """Главная страница"""
    return HttpResponse("🌱 Добро пожаловать в Plant Service! <br><a href='/plants/'>Перейти к растениям</a>")

def about_view(request):
    """Страница "О нас" """
    return HttpResponse("📖 Plant Service - система учета растений")

# ===== ОСНОВНЫЕ URL =====
urlpatterns = [
    # 1. ТЕСТ (должен работать первым!)
    path('test/', test_view, name='test'),
    
    # 2. ГЛАВНАЯ СТРАНИЦА
    path('', home_view, name='home'),
    
    # 3. О НАС
    path('about/', about_view, name='about'),
    
    # 4. ПРИЛОЖЕНИЕ PLANTS (все маршруты plants/)
    path('plants/', include('plants.urls')),
    
    # 5. АДМИНКА
    path('admin/', admin.site.urls),
]

print("=== core/urls.py загружен ===")
