from django.contrib import admin
from .models import Marca, Categoria, Caracteristica, Producto, ProductoCaracteristica

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Caracteristica)
class CaracteristicaAdmin(admin.ModelAdmin):
    list_display = ('tipo',)
    search_fields = ('tipo',)

class ProductoCaracteristicaInline(admin.TabularInline):
    model = ProductoCaracteristica
    extra = 1

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'precio', 'marca', 'categoria')
    list_filter = ('marca', 'categoria')
    search_fields = ('codigo', 'nombre')
    inlines = [ProductoCaracteristicaInline]
    
    # Campos en el formulario de edición
    fieldsets = (
        (None, {
            'fields': ('codigo', 'nombre', 'precio')
        }),
        ('Clasificación', {
            'fields': ('marca', 'categoria')
        }),
    )

@admin.register(ProductoCaracteristica)
class ProductoCaracteristicaAdmin(admin.ModelAdmin):
    list_display = ('producto', 'caracteristica', 'valor')
    list_filter = ('caracteristica',)
    search_fields = ('producto__nombre', 'caracteristica__tipo', 'valor')
