from django.contrib import admin
from django.urls import path, include
from ninja import NinjaAPI
from productos.api.endpoints import auth, productos

api = NinjaAPI()
api.add_router("/auth", auth.router)
api.add_router("/productos", productos.router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
    path('', include('productos.auth.urls')),
    path('productos/', include('productos.productos.urls')),
]
