from django.contrib import admin
from .models import Marca, Categoria, Caracteristica, Producto, ProductoCaracteristica

admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Caracteristica)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'precio', 'marca', 'categoria')
    search_fields = ('codigo', 'nombre', 'marca__nombre', 'categoria__nombre')
    list_filter = ('marca', 'categoria')

@admin.register(ProductoCaracteristica)
class ProductoCaracteristicaAdmin(admin.ModelAdmin):
    list_display = ('producto', 'caracteristica', 'valor')