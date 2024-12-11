from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('', views.consulta_productos, name='consulta'),
    path('registro/', views.registro_producto, name='registro'),
    path('editar/<int:producto_id>/', views.editar_producto, name='editar'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar'),
]
