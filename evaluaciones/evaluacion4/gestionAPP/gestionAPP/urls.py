from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', include('productos.urls')),
    path('api/', include('productos.api.urls')),
    path('', lambda request: redirect('productos:login')),
]
