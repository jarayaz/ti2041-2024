from ninja import NinjaAPI
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from typing import List
from .schemas import *
from .auth import AuthBearer, create_token
from ..models import Categoria, Marca, Producto

api = NinjaAPI(auth=AuthBearer())

@api.post("/token", auth=None)
def login(request, payload: AuthSchema):
    user = authenticate(username=payload.username, password=payload.password)
    if user:
        token = create_token(user)
        return {"access_token": token}
    return {"error": "Invalid credentials"}

@api.get("/categorias", response=List[CategoriaSchema])
def listar_categorias(request):
    return Categoria.objects.all()

@api.get("/marcas", response=List[MarcaSchema])
def listar_marcas(request):
    return Marca.objects.all()

@api.get("/productos", response=List[ProductoListSchema])
def listar_productos(request, marca_id: int = None, categoria_id: int = None):
    productos = Producto.objects.all()
    if marca_id:
        productos = productos.filter(marca_id=marca_id)
    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)
    return productos

@api.get("/productos/{codigo}", response=ProductoDetailSchema)
def detalle_producto(request, codigo: str):
    return get_object_or_404(Producto, codigo=codigo)

@api.put("/productos/{codigo}", response=ProductoDetailSchema)
def actualizar_producto_completo(request, codigo: str, payload: ProductoBaseSchema):
    producto = get_object_or_404(Producto, codigo=codigo)
    for attr, value in payload.dict().items():
        setattr(producto, attr, value)
    producto.save()
    return producto

@api.patch("/productos/{codigo}", response=ProductoDetailSchema)
def actualizar_producto_parcial(request, codigo: str, payload: ProductoUpdateSchema):
    producto = get_object_or_404(Producto, codigo=codigo)
    for attr, value in payload.dict(exclude_unset=True).items():
        setattr(producto, attr, value)
    producto.save()
    return producto
