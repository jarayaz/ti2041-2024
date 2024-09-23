from django.shortcuts import render, redirect

# Lista para almacenar productos temporalmente
productos_registrados = []

def registro_producto(request):
    if request.method == 'POST':
        # Recoger los datos del formulario
        codigo = request.POST['codigo']
        nombre = request.POST['nombre']
        marca = request.POST['marca']
        fecha_vencimiento = request.POST['fecha_vencimiento']

        # Crear un diccionario para representar el producto
        producto = {
            'codigo': codigo,
            'nombre': nombre,
            'marca': marca,
            'fecha_vencimiento': fecha_vencimiento
        }

        # Guardar el producto en la lista de productos
        productos_registrados.append(producto)

        # Redirigir a la pantalla de resultados, pasando el producto como contexto
        return render(request, 'productos/resultado.html', {'producto': producto})

    return render(request, 'productos/registro.html')

def consulta_productos(request):
    # Pasamos la lista de productos al template
    return render(request, 'productos/consulta.html', {'productos': productos_registrados})
