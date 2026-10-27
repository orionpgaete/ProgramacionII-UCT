from sqlalchemy import text
from conexion import engine
from decimal import Decimal
from conexion import Session
from modelos import *
import crear_tabla
from inserta import inserta_producto

def conexion():
    with engine.connect() as conexion:
        print("Conexión SQLite exitosa")
    conexion = engine.connect()
    return conexion

def insertar(nombre, precio, stock):
    with Session.begin() as session:
        producto = Producto(
            nombre=nombre,
            precio=Decimal(str(precio)),
            stock=stock
        )
        session.add(producto)
    print("Producto registrado")

def main():
    print("Sistema Inventario")
    inserta_producto()

if __name__ == "__main__":
    main()