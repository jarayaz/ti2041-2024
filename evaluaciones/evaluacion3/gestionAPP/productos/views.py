from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from django.contrib import messages
from .forms import ProductoForm, ProductoCaracteristicaFormSet
from .models import Producto, ProductoCaracteristica, Marca, Categoria, Caracteristica

def is_admin_products(user):
    return user.groups.filter(name='ADMIN_PRODUCTS').exists() or user.is_superuser

def is_operator(user):
    return user.groups.filter(name='OPERARIOS').exists()

def can_add_products(user):
    return user.groups.filter(name__in=['ADMIN_PRODUCTS', 'OPERARIOS']).exists() or user.is_superuser

@login_required
def registro_producto(request):
    if not can_add_products(request.user):
        messages.error(request, 'No tienes permisos para registrar productos.')
        return redirect('consulta_productos')
    
    productos = Producto.objects.all().order_by('-fecha_ingreso')
    
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        formset = ProductoCaracteristicaFormSet(request.POST)
        
        if form.is_valid() and formset.is_valid():
            try:
                with transaction.atomic():
                    # Guardar el producto
                    producto = form.save()
                    
                    # Guardar las características
                    for caracteristica_form in formset:
                        if caracteristica_form.cleaned_data and not caracteristica_form.cleaned_data.get('DELETE', False):
                            caracteristica = caracteristica_form.cleaned_data.get('caracteristica')
                            valor = caracteristica_form.cleaned_data.get('valor')
                            if caracteristica and valor:
                                ProductoCaracteristica.objects.create(
                                    producto=producto,
                                    caracteristica=caracteristica,
                                    valor=valor
                                )
                
                messages.success(request, 'Producto registrado exitosamente.')
                return redirect('consulta_productos')
            except Exception as e:
                messages.error(request, f'Error al guardar el producto: {str(e)}')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = ProductoForm()
        formset = ProductoCaracteristicaFormSet()
    
    context = {
        'form': form,
        'formset': formset,
        'productos': productos,
        'es_admin': is_admin_products(request.user),
        'es_operario': is_operator(request.user)
    }
    return render(request, 'productos/registro.html', context)

@login_required
def consulta_productos(request):
    productos = Producto.objects.all().order_by('-fecha_ingreso')
    marcas = Marca.objects.all()
    categorias = Categoria.objects.all()
    caracteristicas = Caracteristica.objects.all()
    
    es_admin = is_admin_products(request.user)
    es_operario = is_operator(request.user)
    
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
        'es_admin': es_admin,
        'es_operario': es_operario,
    }
    return render(request, 'productos/consulta.html', context)

@login_required
def editar_producto(request, producto_id):
    if not is_admin_products(request.user):
        messages.error(request, 'No tienes permisos para editar productos.')
        return redirect('consulta_productos')
        
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        formset = ProductoCaracteristicaFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            try:
                with transaction.atomic():
                    producto = form.save()
                    ProductoCaracteristica.objects.filter(producto=producto).delete()
                    for caracteristica_form in formset:
                        if caracteristica_form.cleaned_data and not caracteristica_form.cleaned_data.get('DELETE', False):
                            caracteristica = caracteristica_form.cleaned_data.get('caracteristica')
                            valor = caracteristica_form.cleaned_data.get('valor')
                            if caracteristica and valor:
                                ProductoCaracteristica.objects.create(
                                    producto=producto,
                                    caracteristica=caracteristica,
                                    valor=valor
                                )
                messages.success(request, 'Producto actualizado exitosamente.')
                return redirect('consulta_productos')
            except Exception as e:
                messages.error(request, f'Error al actualizar el producto: {str(e)}')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = ProductoForm(instance=producto)
        formset = ProductoCaracteristicaFormSet(initial=[
            {'caracteristica': pc.caracteristica, 'valor': pc.valor}
            for pc in producto.productocaracteristica_set.all()
        ])
    
    context = {
        'form': form,
        'formset': formset,
        'producto': producto,
        'es_admin': is_admin_products(request.user),
        'es_operario': is_operator(request.user)
    }
    return render(request, 'productos/editar.html', context)

@login_required
def eliminar_producto(request, producto_id):
    if not is_admin_products(request.user):
        messages.error(request, 'No tienes permisos para eliminar productos.')
        return redirect('consulta_productos')
        
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        try:
            producto.delete()
            messages.success(request, 'Producto eliminado exitosamente.')
        except Exception as e:
            messages.error(request, f'Error al eliminar el producto: {str(e)}')
        return redirect('consulta_productos')
    return render(request, 'productos/eliminar.html', {'producto': producto})