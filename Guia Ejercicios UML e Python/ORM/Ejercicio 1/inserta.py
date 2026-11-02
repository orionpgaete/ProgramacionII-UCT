from decimal import Decimal
from conexion import Session
from modelos import *

def inserta_producto(nombre, precio, stock):
    with Session.begin() as session:
        producto= Producto(
            nombre =nombre,
            precio = Decimal(str(precio)),
            stock =  stock
        )
        session.add(producto)


    print("Productos registrados")