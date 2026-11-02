from sqlalchemy import text
from conexion import engine
from decimal import Decimal, InvalidOperation
from conexion import Session
from modelos import *
import crear_tabla
from inserta import inserta_producto
from consultar import consultar_productos
from actualizar import actualizar_producto
from eliminar import eliminar_producto

def conexion():
    with engine.connect() as conexion:
        print("Conexión SQLite exitosa")
    conexion = engine.connect()
    return conexion

#Mostrar Menu
def mostrar_menu():
    print("\n=========================")
    print("       INVENTARIO        ")
    print("===========================")
    print("1. Crear producto")
    print("2: Consultar productos")
    print("3: Actualizar productos")
    print("4: Eliminar productos")
    print("0. Salir")
    print("===========================")

#Solictar Datos e insertar producto
def ingresa_prodcuto():
    print("\n---------REGISTRO PRODUCTO---------")

    nombre = input("Ingrese el nombre del producto: ").strip()
    try:
        precio = Decimal(input("Ingrese el precio del producto: "))
        stock = int(input("Ingrese el stock del producto: "))

        if not nombre:
            print("ERROR: debe ingresar un nombre")
            return
        if not precio.is_finite()  or precio < 0 or stock < 0:
            print("ERROR: precio y stco deben ser validos y no negativos")
            return
        #LLAMDA a la funcion insertar.py
        inserta_producto(nombre, precio, stock)

    except (ValueError, InvalidOperation):
        print("ERROR : ingrese valor nuemrico validos")

def insertar(nombre, precio, stock):
    with Session.begin() as session:
        producto = Producto(
            nombre=nombre,
            precio=Decimal(str(precio)),
            stock=stock
        )
        session.add(producto)
    print("Producto registrado")

def modificar_producto():
    print("\n---------MODIFICAR PRODUCTO---------")

    try:
        in_id_prod = int(input("Ingrese el id del producto: "))
        in_nombre = input("Nuevo nombre del producto: ")
        in_precio = Decimal(input("Nuevo precio del producto: "))
        in_stock = int(input("Nuevo stock del producto: "))

        if in_id_prod <= 0 or not in_nombre:
            print("ERROR : debe ingresar un ID o nombre valido")
            return

        if not in_precio.is_finite() or in_precio < 0 or in_stock < 0:
            print("ERROR precio y stock deben ser validos y no negativos")
            return

        actualizar_producto(in_id_prod, in_nombre, in_precio, in_stock)

    except (ValueError, InvalidOperation):
        print("ERROR : se esperan datos validos y no negativos")


def eliminar_prodcuto():
    print("\n---------ELIMINAR PRODUCTO---------")

    try:
        in_id_producto = int(input("Ingrese el id del producto: "))

        if in_id_producto <= 0 :
            print("ERROR : debe ingresar un ID valido")
            return

        confirmar = input("Confirmar el producto (S/N): ")

        if confirmar.strip().upper() == "S" :
            eliminar_producto(in_id_producto)
        else:
            print("ERROR : Eliminacion cancelado")

    except (ValueError, InvalidOperation):
        print("ERROR : se esperan datos validos y no negativos")

def main():
    conexion()
    while True:
        mostrar_menu()
        opcion = input("Selecciones Opcion: ")

        if opcion == "1":
            ingresa_prodcuto()
        elif opcion == "2":
            consultar_productos()
        elif opcion == "3":
            modificar_producto()
        elif opcion == "4":
            eliminar_prodcuto()
        elif opcion == "0":
            print("Saliendio del sistema")
            break
        else:
            print("Opcion invalida")

if __name__ == "__main__":
    main()