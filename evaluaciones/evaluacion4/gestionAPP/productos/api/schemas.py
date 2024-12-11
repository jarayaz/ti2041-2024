from ninja import Schema
from typing import Optional

class AuthSchema(Schema):
    username: str
    password: str

class CategoriaSchema(Schema):
    id: int
    nombre: str

class MarcaSchema(Schema):
    id: int
    nombre: str

class ProductoBaseSchema(Schema):
    codigo: str
    nombre: str
    precio: float
    marca_id: int
    categoria_id: Optional[int] = None

class ProductoListSchema(ProductoBaseSchema):
    id: int
    marca: MarcaSchema
    categoria: Optional[CategoriaSchema] = None

class ProductoDetailSchema(ProductoListSchema):
    pass

class ProductoUpdateSchema(Schema):
    nombre: Optional[str] = None
    precio: Optional[float] = None
    marca_id: Optional[int] = None
    categoria_id: Optional[int] = None
