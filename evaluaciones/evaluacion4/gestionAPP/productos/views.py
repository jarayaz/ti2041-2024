from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required  # Añadimos permission_required
from django.contrib import messages
from django.db import transaction
from .models import Producto, Marca, Categoria, ProductoCaracteristica
from .forms import ProductoForm, ProductoCaracteristicaFormSet

@login_required(login_url='productos:login')
def consulta_productos(request):
    try:
        productos = Producto.objects.all()
        marcas = Marca.objects.all()
        categorias = Categoria.objects.all()
        
        marca_id = request.GET.get('marca')
        categoria_id = request.GET.get('categoria')
        
        if marca_id:
            productos = productos.filter(marca_id=marca_id)
        if categoria_id:
            productos = productos.filter(categoria_id=categoria_id)
        
        context = {
            'productos': productos,
            'marcas': marcas,
            'categorias': categorias,
        }
        return render(request, 'productos/consulta.html', context)
    except Exception as e:
        messages.error(request, str(e))
        return render(request, 'productos/consulta.html', {'error': str(e)})

@login_required(login_url='productos:login')
@permission_required('productos.add_producto', raise_exception=True)
def registro_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        formset = ProductoCaracteristicaFormSet(request.POST)
        
        if form.is_valid() and formset.is_valid():
            try:
                with transaction.atomic():
                    producto = form.save()
                    formset.instance = producto
                    formset.save()
                messages.success(request, 'Producto registrado exitosamente.')
                return redirect('productos:consulta_productos')
            except Exception as e:
                messages.error(request, f'Error al registrar el producto: {str(e)}')
    else:
        form = ProductoForm()
        formset = ProductoCaracteristicaFormSet()
    
    return render(request, 'productos/registro.html', {
        'form': form,
        'formset': formset,
        'titulo': 'Registrar Producto'
    })

@login_required(login_url='productos:login')
@permission_required('productos.change_producto', raise_exception=True)
def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        formset = ProductoCaracteristicaFormSet(request.POST, instance=producto)
        
        if form.is_valid() and formset.is_valid():
            try:
                with transaction.atomic():
                    form.save()
                    formset.save()
                messages.success(request, 'Producto actualizado exitosamente.')
                return redirect('productos:consulta_productos')
            except Exception as e:
                messages.error(request, f'Error al actualizar el producto: {str(e)}')
    else:
        form = ProductoForm(instance=producto)
        formset = ProductoCaracteristicaFormSet(instance=producto)
    
    return render(request, 'productos/editar.html', {
        'form': form,
        'formset': formset,
        'producto': producto,
        'titulo': 'Editar Producto'
    })

@login_required(login_url='productos:login')
@permission_required('productos.delete_producto', raise_exception=True)
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    
    if request.method == 'POST':
        try:
            producto.delete()
            messages.success(request, 'Producto eliminado exitosamente.')
            return redirect('productos:consulta_productos')
        except Exception as e:
            messages.error(request, f'Error al eliminar el producto: {str(e)}')
    
    return render(request, 'productos/eliminar.html', {
        'producto': producto
    })
