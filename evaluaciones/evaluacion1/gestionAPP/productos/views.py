from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from django.urls import reverse
from .forms import ProductoForm, ProductoCaracteristicaFormSet
from .models import Producto, ProductoCaracteristica, Marca, Categoria, Caracteristica

def registro_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        formset = ProductoCaracteristicaFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            with transaction.atomic():
                producto = form.save()
                for caracteristica_form in formset:
                    if caracteristica_form.cleaned_data:
                        ProductoCaracteristica.objects.create(
                            producto=producto,
                            caracteristica=caracteristica_form.cleaned_data['caracteristica'],
                            valor=caracteristica_form.cleaned_data['valor']
                        )
            return redirect('consulta_productos')
    else:
        form = ProductoForm()
        formset = ProductoCaracteristicaFormSet()
    return render(request, 'productos/registro.html', {'form': form, 'formset': formset})

def consulta_productos(request):
    productos = Producto.objects.all()
    marcas = Marca.objects.all()
    categorias = Categoria.objects.all()
    caracteristicas = Caracteristica.objects.all()

    marca_id = request.GET.get('marca')
    categoria_id = request.GET.get('categoria')
    caracteristica_id = request.GET.get('caracteristica')

    if marca_id:
        productos = productos.filter(marca_id=marca_id)
    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)
    if caracteristica_id:
        productos = productos.filter(caracteristicas__id=caracteristica_id)

    context = {
        'productos': productos,
        'marcas': marcas,
        'categorias': categorias,
        'caracteristicas': caracteristicas,
    }
    return render(request, 'productos/consulta.html', context)

def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        formset = ProductoCaracteristicaFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            with transaction.atomic():
                producto = form.save()
                # Eliminar características existentes
                ProductoCaracteristica.objects.filter(producto=producto).delete()
                # Crear nuevas características
                for caracteristica_form in formset:
                    if caracteristica_form.cleaned_data and not caracteristica_form.cleaned_data.get('DELETE', False):
                        caracteristica = caracteristica_form.cleaned_data['caracteristica']
                        valor = caracteristica_form.cleaned_data['valor']
                        ProductoCaracteristica.objects.create(
                            producto=producto,
                            caracteristica=caracteristica,
                            valor=valor
                        )
            return redirect('consulta_productos')
    else:
        form = ProductoForm(instance=producto)
        caracteristicas_iniciales = [
            {'caracteristica': pc.caracteristica, 'valor': pc.valor}
            for pc in producto.productocaracteristica_set.all()
        ]
        formset = ProductoCaracteristicaFormSet(initial=caracteristicas_iniciales)
    return render(request, 'productos/editar.html', {'form': form, 'formset': formset, 'producto': producto})

def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('consulta_productos')
    return render(request, 'productos/eliminar.html', {'producto': producto})