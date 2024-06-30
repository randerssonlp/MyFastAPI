# app/crud.py

from sqlalchemy.orm import Session
from app.models import Cliente, Producto, Laboratorio, Presentacion
from typing import List

# Funciones CRUD para Cliente
def get_clientes(db: Session) -> List[Cliente]:
    return db.query(Cliente).all()

def get_cliente_by_id(db: Session, cliente_id: int) -> Cliente:
    return db.query(Cliente).filter(Cliente.idcliente == cliente_id).first()

def create_cliente(db: Session, nombre: str, telefono: str, direccion: str) -> Cliente:
    db_cliente = Cliente(nombre=nombre, telefono=telefono, direccion=direccion)
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

def update_cliente(db: Session, cliente_id: int, nombre: str, telefono: str, direccion: str) -> Cliente:
    db_cliente = db.query(Cliente).filter(Cliente.idcliente == cliente_id).first()
    if db_cliente:
        db_cliente.nombre = nombre
        db_cliente.telefono = telefono
        db_cliente.direccion = direccion
        db.commit()
        db.refresh(db_cliente)
    return db_cliente

def delete_cliente(db: Session, cliente_id: int) -> Cliente:
    db_cliente = db.query(Cliente).filter(Cliente.idcliente == cliente_id).first()
    if db_cliente:
        db.delete(db_cliente)
        db.commit()
    return db_cliente

# Funciones CRUD para Producto
def get_productos(db: Session) -> List[Producto]:
    return db.query(Producto).all()

def get_producto_by_id(db: Session, producto_id: int) -> Producto:
    return db.query(Producto).filter(Producto.codproducto == producto_id).first()

def create_producto(db: Session, codigo: str, descripcion: str, precio: float, existencia: int, id_lab: int, id_presentacion: int, id_tipo: int, vencimiento: str) -> Producto:
    db_producto = Producto(codigo=codigo, descripcion=descripcion, precio=precio, existencia=existencia, id_lab=id_lab, id_presentacion=id_presentacion, id_tipo=id_tipo, vencimiento=vencimiento)
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

def update_producto(db: Session, producto_id: int, codigo: str, descripcion: str, precio: float, existencia: int, id_lab: int, id_presentacion: int, id_tipo: int, vencimiento: str) -> Producto:
    db_producto = db.query(Producto).filter(Producto.codproducto == producto_id).first()
    if db_producto:
        db_producto.codigo = codigo
        db_producto.descripcion = descripcion
        db_producto.precio = precio
        db_producto.existencia = existencia
        db_producto.id_lab = id_lab
        db_producto.id_presentacion = id_presentacion
        db_producto.id_tipo = id_tipo
        db_producto.vencimiento = vencimiento
        db.commit()
        db.refresh(db_producto)
    return db_producto

def delete_producto(db: Session, producto_id: int) -> Producto:
    db_producto = db.query(Producto).filter(Producto.codproducto == producto_id).first()
    if db_producto:
        db.delete(db_producto)
        db.commit()
    return db_producto

# Funciones CRUD para Laboratorio
def get_laboratorios(db: Session) -> List[Laboratorio]:
    return db.query(Laboratorio).all()

def get_laboratorio_by_id(db: Session, id: int) -> Laboratorio:
    return db.query(Laboratorio).filter(Laboratorio.id == id).first()

def create_laboratorio(db: Session, laboratorio: str, direccion: str) -> Laboratorio:
    db_laboratorio = Laboratorio(laboratorio=laboratorio, direccion=direccion)
    db.add(db_laboratorio)
    db.commit()
    db.refresh(db_laboratorio)
    return db_laboratorio

def update_laboratorio(db: Session, id: int, laboratorio: str, direccion: str) -> Laboratorio:
    db_laboratorio = db.query(Laboratorio).filter(Laboratorio.id == id).first()
    if db_laboratorio:
        db_laboratorio.laboratorio = laboratorio
        db_laboratorio.direccion = direccion
        db.commit()
        db.refresh(db_laboratorio)
    return db_laboratorio

def delete_laboratorio(db: Session, id: int) -> Laboratorio:
    db_laboratorio = db.query(Laboratorio).filter(Laboratorio.id == id).first()
    if db_laboratorio:
        db.delete(db_laboratorio)
        db.commit()
    return db_laboratorio

# Funciones CRUD para Presentacion
def get_presentaciones(db: Session) -> List[Presentacion]:
    return db.query(Presentacion).all()

def get_presentacion_by_id(db: Session, presentacion_id: int) -> Presentacion:
    return db.query(Presentacion).filter(Presentacion.id == presentacion_id).first()

def create_presentacion(db: Session, nombre: str, nombre_corto: str) -> Presentacion:
    db_presentacion = Presentacion(nombre=nombre, nombre_corto=nombre_corto)
    db.add(db_presentacion)
    db.commit()
    db.refresh(db_presentacion)
    return db_presentacion

def update_presentacion(db: Session, id: int, nombre: str, nombre_corto:str) -> Presentacion:
    db_presentacion = db.query(Presentacion).filter(Presentacion.id == id).first()
    if db_presentacion:
        db_presentacion.nombre = nombre
        db_presentacion.nombre_corto = nombre_corto
        db.commit()
        db.refresh(db_presentacion)
    return db_presentacion

def delete_presentacion(db: Session, id: int) -> Presentacion:
    db_presentacion = db.query(Presentacion).filter(Presentacion.id == id).first()
    if db_presentacion:
        db.delete(db_presentacion)
        db.commit()
    return db_presentacion
