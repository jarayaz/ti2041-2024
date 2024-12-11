from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..auth.decorators import admin_products_required
from .models import Producto
from .forms import ProductoForm, ProductoCaracteristicaFormSet

@login_required
def consulta_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/consulta.html', {'productos': productos})

@login_required
@admin_products_required
def registro_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos:consulta')
    else:
        form = ProductoForm()
    return render(request, 'productos/registro.html', {'form': form})

# ... resto de las vistas
