class Producto:

    def __init__(self, nombre):
        self.__nombre = ""

    @property
    def precio(self):
        return self.__precio


        self.set_nombre(nombre)
        self.set_precio(precio)

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        if nuevo_nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío")
        self.__nombre = nuevo_nombre

    def get_precio(self):
        return self.__precio

    def set_precio(self, nuevo_precio):
        if nuevo_precio <= 0:
            raise ValueError("El precio debe ser mayor que cero")
        self.__precio = nuevo_precio

    def mostrar_informacion(self):
        return f"Producto: {self.__nombre} - Precio: ${self.__precio}"

def main():
    p1 = Producto("Teclado", 25000)
    p2 = Producto("Mouse", 15000)

    print(p1.mostrar_informacion())
    print(p2.mostrar_informacion())

    p1.set_nombre("Teclado Mecánico")
    p2.set_precio(18000)

    print(p1.get_nombre())
    print(p2.get_precio())

    try:
        p1.set_precio(-5000)
    except ValueError as error:
        print("Error:", error)

if __name__ == "__main__":
    main()