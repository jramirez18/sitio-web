from django import forms
from .models import Instrumento

class PostForm(forms.ModelForm):
    class Meta:
        model = Instrumento
        fields = ('nombre', 'marca', 'categoria', 'precio', 'descripcion', 'imagen_instrumento',)
