# productos/models.py
from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Caracteristica(models.Model):
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo

class Producto(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    marca = models.ForeignKey('Marca', on_delete=models.CASCADE)
    categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True, blank=True)
    caracteristicas = models.ManyToManyField('Caracteristica', through='ProductoCaracteristica')

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

class ProductoCaracteristica(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    caracteristica = models.ForeignKey(Caracteristica, on_delete=models.CASCADE)
    valor = models.CharField(max_length=100)

    class Meta:
        unique_together = ('producto', 'caracteristica')

    def __str__(self):
        return f"{self.producto.nombre} - {self.caracteristica.tipo}: {self.valor}"
