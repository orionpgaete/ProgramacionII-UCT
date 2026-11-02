from conexion import Session
from modelos import Producto

def eliminar_producto(in_id_producto):
    with Session.begin() as session:
        producto = session.get(Producto, in_id_producto)

        if producto is None:
            print("Producto no encontrado")
            return
    #Eliminar el producto
        session.delete(producto)

    print("Producto eliminado")