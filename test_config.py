import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.conf import settings

print("=== Проверка конфигурации ===")
print(f"ROOT_URLCONF: {settings.ROOT_URLCONF}")
print(f"INSTALLED_APPS: {[app for app in settings.INSTALLED_APPS if 'plants' in app]}")
try:
    from plants import views
    print("✅ Приложение plants загружается")
except ImportError as e:
    print(f"❌ Ошибка загрузки plants: {e}")