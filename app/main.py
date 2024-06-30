from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
from . import models, crud, schemas
from .database import SessionLocal, engine
from typing import List

# Crear las tablas en la base de datos si no existen
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de la Botica Bazar",
    description="""Esta es la API para la Botica Bazar, donde puedes consultar productos, clientes y laboratorios y más.

URL del sistema: [http://localhost/sistema_farmacia/src/](http://localhost/sistema_farmacia/src/)
""",
    version="1.0.0"
)

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rutas para CRUD de cada modelo (Cliente, Producto, Laboratorio, Presentacion) irían aquí

@app.get("/")
def main():
    return RedirectResponse(url="/docs")
@app.get("/")
def read_root():
    return {"Hello": "World"}
# Rutas (endpoints) para Cliente
@app.post("/clientes/", response_model=schemas.Cliente)
def create_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    """
    Crea un nuevo cliente con el nombre, telefono y direccion proporcionados.
    """
    return crud.create_cliente(db=db, nombre=cliente.nombre, telefono=cliente.telefono, direccion=cliente.direccion)

@app.get("/clientes/", response_model=list[schemas.Cliente])
def read_clientes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Obtiene una lista paginada de clientes registrados en la base de datos.
    """
    clientes = crud.get_clientes(db=db)
    return clientes[skip : skip + limit]

@app.get("/clientes/{cliente_id}", response_model=schemas.Cliente)
def read_cliente(cliente_id: int, db: Session = Depends(get_db)):
    """
    Obtiene un cliente específico según su ID.
    """
    db_cliente = crud.get_cliente_by_id(db=db, cliente_id=cliente_id)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente not found")
    return db_cliente

@app.put("/clientes/{cliente_id}", response_model=schemas.Cliente)
def update_cliente(cliente_id: int, cliente: schemas.ClienteUpdate, db: Session = Depends(get_db)):
    """
    Actualiza la información de un cliente específico según su ID.
    """
    db_cliente = crud.update_cliente(db=db, cliente_id=cliente_id, nombre=cliente.nombre, telefono=cliente.telefono, direccion=cliente.direccion)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente not found")
    return db_cliente

@app.delete("/clientes/{cliente_id}", response_model=schemas.Cliente)
def delete_cliente(cliente_id: int, db: Session = Depends(get_db)):
    """
    Elimina un cliente específico según su ID.
    """
    db_cliente = crud.delete_cliente(db=db, cliente_id=cliente_id)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente not found")
    return db_cliente

# Rutas (endpoints) para Producto
@app.post("/productos/", response_model=schemas.Producto)
def create_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):

    """
    Crea un nuevo producto con la información proporcionada.
    """
    return crud.create_producto(db=db, **producto.model_dump())

@app.get("/productos/", response_model=list[schemas.Producto])
def read_productos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Obtiene una lista paginada de productos registrados en la base de datos.
    """
    productos = crud.get_productos(db=db)
    return productos[skip : skip + limit]

@app.get("/productos/{producto_id}", response_model=schemas.Producto)
def read_producto(producto_id: int, db: Session = Depends(get_db)):
    """
    Obtiene un producto específico según su ID.
    """
    db_producto = crud.get_producto_by_id(db=db, producto_id=producto_id)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto not found")
    return db_producto

@app.put("/productos/{producto_id}", response_model=schemas.Producto)
def update_producto(producto_id: int, producto: schemas.ProductoUpdate, db: Session = Depends(get_db)):
    """
    Actualiza la información de un producto específico según su ID.
    """
    db_producto = crud.update_producto(db=db, producto_id=producto_id, **producto.model_dump())
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto not found")
    return db_producto

@app.delete("/productos/{producto_id}", response_model=schemas.Producto)
def delete_producto(producto_id: int, db: Session = Depends(get_db)):
    """
    Elimina un producto específico según su ID.
    """
    db_producto = crud.delete_producto(db=db, producto_id=producto_id)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto not found")
    return db_producto

# Rutas (endpoints) para Laboratorio
@app.post("/laboratorios/", response_model=schemas.Laboratorio)
def create_laboratorio(laboratorio: schemas.LaboratorioCreate, db: Session = Depends(get_db)):
    """
    Crea un nuevo laboratorio con la información proporcionada.
    """
    return crud.create_laboratorio(db=db, **laboratorio.model_dump())

@app.get("/laboratorios/", response_model=list[schemas.Laboratorio])
def read_laboratorios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Obtiene una lista paginada de laboratorios registrados en la base de datos.
    """
    laboratorios = crud.get_laboratorios(db=db)
    return laboratorios[skip : skip + limit]

@app.get("/laboratorios/{laboratorio_id}", response_model=schemas.Laboratorio)
def read_laboratorio(laboratorio_id: int, db: Session = Depends(get_db)):
    """
    Obtiene un laboratorio específico según su ID.
    """
    db_laboratorio = crud.get_laboratorio_by_id(db=db, id=laboratorio_id)
    if db_laboratorio is None:
        raise HTTPException(status_code=404, detail="Laboratorio not found")
    return db_laboratorio

@app.put("/laboratorios/{laboratorio_id}", response_model=schemas.Laboratorio)
def update_laboratorio(laboratorio_id: int, laboratorio: schemas.LaboratorioUpdate, db: Session = Depends(get_db)):
    """
    Actualiza la información de un laboratorio específico según su ID.
    """
    db_laboratorio = crud.update_laboratorio(db=db, laboratorio_id=laboratorio_id, **laboratorio.model_dump())
    if db_laboratorio is None:
        raise HTTPException(status_code=404, detail="Laboratorio not found")
    return db_laboratorio

@app.delete("/laboratorios/{laboratorio_id}", response_model=schemas.Laboratorio)
def delete_laboratorio(laboratorio_id: int, db: Session = Depends(get_db)):
    """
    Elimina un laboratorio específico según su ID.
    """
    db_laboratorio = crud.delete_laboratorio(db=db, id=laboratorio_id)
    if db_laboratorio is None:
        raise HTTPException(status_code=404, detail="Laboratorio not found")
    return db_laboratorio

# Rutas (endpoints) para Presentacion
@app.get("/presentaciones/", response_model=List[schemas.Presentacion])
def read_presentaciones(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Obtiene una lista paginada de presentaciones registradas en la base de datos.
    """
    presentaciones = crud.get_presentaciones(db=db)
    return presentaciones[skip: skip + limit]

@app.get("/presentaciones/{presentacion_id}", response_model=schemas.Presentacion)
def read_presentacion(presentacion_id: int, db: Session = Depends(get_db)):
    """
    Obtiene una presentación específica según su ID.
    """
    db_presentacion = crud.get_presentacion_by_id(db=db, presentacion_id=presentacion_id)
    if db_presentacion is None:
        raise HTTPException(status_code=404, detail="Presentacion not found")
    return db_presentacion

@app.post("/presentaciones/", response_model=schemas.Presentacion)
def create_presentacion(presentacion: schemas.PresentacionCreate, db: Session = Depends(get_db)):
    """
    Crea una nueva presentación con la información proporcionada.
    """
    return crud.create_presentacion(db=db, nombre=presentacion.nombre, nombre_corto=presentacion.nombre_corto)

@app.put("/presentaciones/{presentacion_id}", response_model=schemas.Presentacion)
def update_presentacion(presentacion_id: int, presentacion: schemas.PresentacionUpdate, db: Session = Depends(get_db)):
    """
    Actualiza la información de una presentación específica según su ID.
    """
    return crud.update_presentacion(db=db, id=presentacion_id, nombre=presentacion.nombre, nombre_corto=presentacion.nombre_corto)

@app.delete("/presentaciones/{presentacion_id}", response_model=schemas.Presentacion)
def delete_presentacion(presentacion_id: int, db: Session = Depends(get_db)):
    """
    Elimina una presentación específica según su ID.
    """
    return crud.delete_presentacion(db=db, id=presentacion_id)

