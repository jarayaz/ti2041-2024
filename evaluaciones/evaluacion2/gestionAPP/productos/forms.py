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
        error_messages = {
            'codigo': {
                'required': 'El código es obligatorio.',
                'unique': 'Este código ya existe.',
            },
            'nombre': {
                'required': 'El nombre es obligatorio.',
            },
            'precio': {
                'required': 'El precio es obligatorio.',
                'invalid': 'Ingrese un precio válido.',
            },
            'marca': {
                'required': 'La marca es obligatoria.',
            },
            'categoria': {
                'required': 'La categoría es obligatoria.',
            },
        }

class ProductoCaracteristicaForm(forms.ModelForm):
    class Meta:
        model = ProductoCaracteristica
        fields = ['caracteristica', 'valor']
        widgets = {
            'caracteristica': forms.Select(attrs={'class': 'form-control'}),
            'valor': forms.TextInput(attrs={'class': 'form-control'}),
        }
        error_messages = {
            'caracteristica': {
                'required': 'La característica es obligatoria.',
            },
            'valor': {
                'required': 'El valor es obligatorio.',
            },
        }

ProductoCaracteristicaFormSet = inlineformset_factory(
    Producto,
    ProductoCaracteristica,
    form=ProductoCaracteristicaForm,
    extra=1,
    can_delete=True
)