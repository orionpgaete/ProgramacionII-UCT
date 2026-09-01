class Animal:

    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso

    def comer(self):
        print(self.nombre, "está comiendo")

    def dormir(self):
        print(self.nombre, "está durmiendo")

    def moverse(self):
        print(self.nombre, "se está moviendo")

    def emitirSonido(self):
        return "Sonido de animal"

class Reptil(Animal):

    def __init__(self, nombre, edad, peso, esVenenoso):
        super().__init__(nombre, edad, peso)

        self.esVenenoso = esVenenoso

    def reptar(self):
        print(self.nombre, "esta reptando")

    def tomarSol(self):
        print(self.nombre, "esta tomando sol")

class Mamimefo(Animal):
    def __init__(self, nombre, edad, peso, viviparo):
        super().__init__(nombre, edad, peso)
        self.viviparo = viviparo

    def amamantar(self):
        print(self.nombre, "esta amamantando")

    def gestar(self):
        print(self.nombre, "se encuentra en gestacion")

class Ornitorrinco(Mamimefo):
    def __init__(self, nombre, edad, peso, viviparo, venenso):
        super().__init__(nombre, edad, peso, viviparo)

    def ponerHuevos(self):
        print(self.nombre, "esta poniendo huevos")

    def nada(self):
        print(self.nombre, "esta nadando")

    def detectarCampoElectrico(self):
        print(self.nombre, "detacta campo electrico")

class Jaula:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.animales = []

    def cantidad_actual(self):
        return len(self.animales)

    def capacidad_restante(self):
        return (self.capacidad - len(self.animales))

    def agregar_animales(self, animal):
        if len(self.animales) < self.capacidad:
            self.animales.append(animal)
            print(animal.nombre, "fue agregado animal")
        else:
            print("NO hay espacio")
        return self.capacidad_restante()

    def liberar_animal(self, nombre):
        for animal in self.animales:
            if animal.nombre == nombre:
                self.animales.remove(animal)

                print(nombre, "fue liberado")
                break
        return self.cantidad_actual()


def main():
    animal1 = Animal("Firulais", 5, 12.5)

    print("Nombre:", animal1.nombre)
    print("Edad:", animal1.edad)
    print("Peso:", animal1.peso)

    animal1.comer()
    animal1.dormir()
    animal1.moverse()
    print(animal1.emitirSonido())

    serpiente = Reptil("Serpiente", 5, 12.5, True)

    serpiente.comer()
    serpiente.dormir()
    serpiente.reptar()
    serpiente.tomarSol()

    perro = Mamimefo("Perro", 5, 12.5, True)
    perro.comer()
    perro.dormir()

    perro.amamantar()
    perro.gestar()

    perry = Ornitorrinco("Perry", 8, 2.5, False, True)

    perry.comer()
    perry.nada()
    perry.ponerHuevos()
    perry.amamantar()

    jaula = Jaula(3)
    print("Capacidad actual", jaula.cantidad_actual())

    jaula.agregar_animales(animal1)
    print("Capacidad actual", jaula.cantidad_actual())

if __name__ == "__main__":
    main()