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
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'marca': forms.Select(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }

class ProductoCaracteristicaForm(forms.ModelForm):
    class Meta:
        model = ProductoCaracteristica
        fields = ['caracteristica', 'valor']
        widgets = {
            'caracteristica': forms.Select(attrs={'class': 'form-control'}),
            'valor': forms.TextInput(attrs={'class': 'form-control'}),
        }

ProductoCaracteristicaFormSet = inlineformset_factory(
    Producto,
    ProductoCaracteristica,
    form=ProductoCaracteristicaForm,
    extra=1,
    can_delete=True
)