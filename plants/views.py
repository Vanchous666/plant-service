"""
Views for plants app.
"""
from django.http import HttpResponse

def plants_list(request):
    """Список всех растений"""
    html = """
    <h1>🌿 Список растений</h1>
    <ul>
        <li><a href="/plants/1/">Растение #1</a></li>
        <li><a href="/plants/2/">Растение #2</a></li>
        <li><a href="/plants/3/">Растение #3</a></li>
    </ul>
    <p><a href="/">← На главную</a></p>
    """
    return HttpResponse(html)

def plant_detail(request, plant_id):
    """Детальная информация о растении"""
    html = f"""
    <h1>📋 Растение #{plant_id}</h1>
    <p><strong>Название:</strong> Фикус Бенджамина #{plant_id}</p>
    <p><strong>Уход:</strong> Полив 2 раза в неделю</p>
    <p><strong>Освещение:</strong> Яркий рассеянный свет</p>
    <p><a href="/plants/">← К списку растений</a> | <a href="/">На главную</a></p>
    """
    return HttpResponse(html)

def plants_search(request):
    """Поиск растений"""
    return HttpResponse("🔍 Страница поиска растений")

def plant_create(request):
    """Создание нового растения"""
    return HttpResponse("🆕 Форма создания растения")
