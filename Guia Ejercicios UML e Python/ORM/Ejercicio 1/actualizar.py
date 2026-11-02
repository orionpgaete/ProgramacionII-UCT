from decimal import Decimal
from conexion import Session
from modelos import Producto

def actualizar_producto(in_id_prod, in_nombre, in_precio, in_stock):
    with Session.begin() as session:
        #Buscar producto con ID
        producto = session.get(Producto, in_id_prod)

        if producto is None:
            print("Producto no encontrado")
            return

        #Actualizar los atributos
        producto.nombre = in_nombre
        producto.precio = Decimal(str(in_precio))
        producto.stock = in_stock

    print("Producto actulizado")
