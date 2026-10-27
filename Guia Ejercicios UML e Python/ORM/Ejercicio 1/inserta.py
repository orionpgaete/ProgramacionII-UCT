from decimal import Decimal
from conexion import Session
from modelos import *

def inserta_producto():
    with Session.begin() as session:
        session.add_all([
            Producto(nombre="teclado", precio=Decimal("35000"), stock=10),
            Producto(nombre="mouse ", precio=Decimal("14500"), stock=15),
            Producto(nombre="monitor", precio=Decimal("125000"), stock=5)
        ])
    print("Productos registrados")