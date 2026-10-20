from abc import ABC, abstractmethod
import math

class Figura(ABC):

    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        if radio <= 0:
            raise ValueError("Radio invalido")
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio**2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

class Rectangulo(Figura):
    def __init__(self, base, altura):
        if base <= 0 or altura <= 0:
            raise ValueError("Dimensiones invalido")
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

def main():

    figuras = [
        Rectangulo(10,5),
        Circulo(4),
        Rectangulo(3,8)
    ]

    for figura in figuras:
        print("Figura :", type(figura).__name__)
        print("Area :", round(figura.calcular_area(), 2))
        print("Perimetro :", round(figura.calcular_perimetro(), 2))
        print("------------------------")

if __name__ == "__main__":
    main()