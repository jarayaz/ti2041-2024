from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('registro/', login_required(views.registro_producto), name='registro_producto'),
    path('consulta/', login_required(views.consulta_productos), name='consulta_productos'),
    path('editar/<int:producto_id>/', login_required(views.editar_producto), name='editar_producto'),
    path('eliminar/<int:producto_id>/', login_required(views.eliminar_producto), name='eliminar_producto'),
]