# app/schemas.py

from pydantic import BaseModel

# Cliente Schemas
class ClienteBase(BaseModel):
    nombre: str
    telefono: str
    direccion: str

class ClienteCreate(ClienteBase):
    pass

class ClienteUpdate(ClienteBase):
    pass

class Cliente(ClienteBase):
    idcliente: int

    class Config:
        orm_mode = True

# Producto Schemas
class ProductoBase(BaseModel):
    codigo: str
    descripcion: str
    precio: float
    existencia: int
    id_lab: int
    id_presentacion: int
    id_tipo: int
    vencimiento: str

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(ProductoBase):
    pass

class Producto(ProductoBase):
    codproducto: int

    class Config:
        orm_mode = True

# Laboratorio Schemas
class LaboratorioBase(BaseModel):
    laboratorio: str
    direccion: str

class LaboratorioCreate(LaboratorioBase):
    pass

class LaboratorioUpdate(LaboratorioBase):
    pass

class Laboratorio(LaboratorioBase):
    id: int

    class Config:
        orm_mode = True

# Presentacion Schemas
class PresentacionBase(BaseModel):
    nombre: str
    nombre_corto: str

class PresentacionCreate(PresentacionBase):
    pass

class PresentacionUpdate(PresentacionBase):
    pass

class Presentacion(PresentacionBase):
    id: int

    class Config:
        orm_mode = True