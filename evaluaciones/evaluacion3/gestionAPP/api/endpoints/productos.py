from ninja import Router
from typing import List
from ..schemas.productos import ProductoBaseSchema, ProductoDetalleSchema
from ..security import AuthBearer
from ...productos.models import Producto

router = Router()

@router.get("/", response=List[ProductoBaseSchema])
def listar_productos(request, marca_id: int = None, categoria_id: int = None):
    productos = Producto.objects.all()
    if marca_id:
        productos = productos.filter(marca_id=marca_id)
    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)
    return productos

@router.get("/{codigo}", response=ProductoDetalleSchema)
def detalle_producto(request, codigo: str):
    return Producto.objects.get(codigo=codigo)

@router.patch("/{codigo}", auth=AuthBearer())
def actualizar_producto(request, codigo: str, datos: dict):
    producto = Producto.objects.get(codigo=codigo)
    for campo, valor in datos.items():
        setattr(producto, campo, valor)
    producto.save()
    return {"mensaje": "Producto actualizado"}
