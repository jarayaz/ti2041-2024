# productos/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'productos'

urlpatterns = [
    # URLs de autenticación
    path('login/', LoginView.as_view(template_name='productos/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='productos:login'), name='logout'),
    
    # URLs de productos
    path('', views.consulta_productos, name='consulta_productos'),
    path('registro/', views.registro_producto, name='registro_producto'),
    path('editar/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
]
