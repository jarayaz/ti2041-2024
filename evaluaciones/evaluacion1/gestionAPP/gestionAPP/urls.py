from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos', include('productos.urls')),  # Incluye las URLs principales de gestionAPP
    path('', lambda request: redirect('registro_producto')),  # Incluye las URLs de productos
]
