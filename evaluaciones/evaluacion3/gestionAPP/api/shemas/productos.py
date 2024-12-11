from ninja import Schema
from typing import List, Optional

class CaracteristicaSchema(Schema):
    tipo: str
    valor: str

class ProductoBaseSchema(Schema):
    codigo: str
    nombre: str
    precio: float

class ProductoDetalleSchema(ProductoBaseSchema):
    marca: str
    categoria: Optional[str]
    caracteristicas: List[CaracteristicaSchema]
