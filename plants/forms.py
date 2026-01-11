from django import forms
from .models import Plant

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'scientific_name', 'description', 'category', 
                  'watering_frequency', 'sunlight', 'temperature', 'difficulty', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }