from django.db import models

class Plant(models.Model):
    CATEGORY_CHOICES = [
        ('INDOOR', 'Комнатное'),
        ('OUTDOOR', 'Садовое'),
        ('SUCCULENT', 'Суккулент'),
        ('HERB', 'Трава'),
    ]
    
    name = models.CharField('Название', max_length=200)
    latin_name = models.CharField('Латинское название', max_length=200, blank=True)
    description = models.TextField('Описание', blank=True)
    category = models.CharField('Категория', max_length=20, choices=CATEGORY_CHOICES, default='INDOOR')
    watering_frequency = models.CharField('Полив', max_length=100, default='1 раз в неделю')
    sunlight = models.CharField('Освещение', max_length=100, default='Яркий рассеянный свет')
    created_at = models.DateTimeField('Дата добавления', auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Растение'
        verbose_name_plural = 'Растения'