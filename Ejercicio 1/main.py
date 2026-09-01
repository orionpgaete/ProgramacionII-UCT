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

def main():
    animal1 = Animal("Firulais", 5, 12.5)

    print("Nombre:", animal1.nombre)
    print("Edad:", animal1.edad)
    print("Peso:", animal1.peso)

    animal1.comer()
    animal1.dormir()
    animal1.moverse()

    print(animal1.emitirSonido())

if __name__ == "__main__":
    main()