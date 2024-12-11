# productos/forms.py
from django import forms
from django.forms import inlineformset_factory
from .models import Producto, ProductoCaracteristica

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo', 'nombre', 'precio', 'marca', 'categoria']
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'marca': forms.Select(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }

# Crear el formset para las características
ProductoCaracteristicaFormSet = inlineformset_factory(
    Producto,
    ProductoCaracteristica,
    fields=['caracteristica', 'valor'],
    extra=1,
    widgets={
        'caracteristica': forms.Select(attrs={'class': 'form-control'}),
        'valor': forms.TextInput(attrs={'class': 'form-control'}),
    }
)
