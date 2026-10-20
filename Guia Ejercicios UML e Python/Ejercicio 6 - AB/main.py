from abc import ABC, abstractmethod

class MetodoPago(ABC):
    @property
    @abstractmethod
    def nombre(self) -> str:
        pass

    @abstractmethod
    def pagar(self, monto: float)->bool:
        pass

class TarjetaCredito(MetodoPago):
    def __init__(self, cupo):
        if cupo < 0:
            raise ValueError("Cupo Insuficiente")
        self.__cupo = cupo

    @property
    def nombre(self):
        return "Tarjeta Credito"

    @property
    def cupo(self):
        return self.__cupo

    def pagar(self, monto: float)->bool:
        if monto <= 0:
            raise ValueError("Monto Insuficiente")
        if monto > self.__cupo:
            return False
        self.__cupo -= monto
        return True

class Trasnferencia(MetodoPago):
    def __init__(self, saldo):
        if saldo < 0:
            raise ValueError("Saldo insuficiente")
        self.__saldo = saldo

    @property
    def nombre(self):
        return "Trasnferencia"

    @property
    def saldo(self):
        return self.__saldo
    def pagar(self, monto: float)->bool:
        if monto <= 0:
            raise ValueError("Monto Insuficiente")
        if monto > self.__saldo:
            return False
        self.__saldo -= monto
        return True

def procesar(
            carrito: list[float],
            metodo : MetodoPago
    ):
        total = sum(carrito)
        print(f"\nMedio de Pago: {metodo.nombre}")
        print(f"Total de Pago: $ {total:.2f}")

        if total <= 0:
            print("Carro Vacio")
            return
        resultado = metodo.pagar(total)

        if resultado:
            print("Pago exitoso")
        else:
            print("Pago rechazado")

def main():
    carrito = [
        25000,
        15000,
        10000
    ]

    tarjeta = TarjetaCredito(100000)
    transferencia = Trasnferencia(30000)

    procesar(carrito, tarjeta)
    procesar(carrito, transferencia)

    print("\n--Status")
    print("Cupo TC: ", tarjeta.cupo)
    print("Saldo CTA: ", transferencia.saldo)

if __name__ == "__main__":
    main()

