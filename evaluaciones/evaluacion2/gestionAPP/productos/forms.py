from django import forms
from .models import Producto, ProductoCaracteristica, Caracteristica

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo', 'nombre', 'precio', 'marca', 'categoria']

class CaracteristicaForm(forms.Form):
    caracteristica = forms.ModelChoiceField(queryset=Caracteristica.objects.all())
    valor = forms.CharField(max_length=100)

ProductoCaracteristicaFormSet = forms.formset_factory(CaracteristicaForm, extra=1)