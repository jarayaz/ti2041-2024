from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', include('productos.urls')),
    path('', lambda request: redirect('registro_producto')),  # Redirige la raíz a la vista de registro de productos
]
