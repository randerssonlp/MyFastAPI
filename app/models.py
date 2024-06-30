# app/models.py

from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Cliente(Base):
    __tablename__ = "cliente"

    idcliente = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), index=True)
    telefono = Column(String(15))
    direccion = Column(String(200))

class Producto(Base):
    __tablename__ = "producto"

    codproducto = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(20))
    descripcion = Column(String(200))
    precio = Column(Float)
    existencia = Column(Integer)
    id_lab = Column(Integer, ForeignKey('laboratorios.id'))
    id_presentacion = Column(Integer, ForeignKey('presentacion.id'))
    id_tipo = Column(Integer)
    vencimiento = Column(Date)

    laboratorio = relationship("Laboratorio", back_populates="productos")
    presentacion = relationship("Presentacion", back_populates="productos")

class Laboratorio(Base):
    __tablename__ = "laboratorios"

    id = Column(Integer, primary_key=True, index=True)
    laboratorio = Column(String(100), index=True)
    direccion = Column(String(200))

    productos = relationship("Producto", back_populates="laboratorio")

class Presentacion(Base):
    __tablename__ = "presentacion"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    nombre_corto = Column(String(10), nullable=False)

    productos = relationship("Producto", back_populates="presentacion")
