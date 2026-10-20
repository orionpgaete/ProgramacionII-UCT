class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = ""
        self.__edad = 0

        self.set_nombre(nombre)
        self.set_edad(edad)

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        if nuevo_nombre.strip() == "":
            raise ValueError("El nombre debe ser valido")
        self.__nombre = nuevo_nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, nueva_edad):
        if not isinstance(nueva_edad, int) or nueva_edad < 0:
            raise ValueError("El edad debe ser positivo")
        self.__edad = nueva_edad

    def presentarse(self):
        return f"Soy {self.__nombre} y tengo {self.__edad} años "

class Estudiante(Persona):
    def __init__(self, nombre, edad, matricula):
        super().__init__(nombre, edad)
        self.__matricula = matricula

    def get_matricula(self):
        return self.__matricula

    def estudiar(self, asignatura):
        return f"{self.get_nombre()} esta estudiando {asignatura}"

def main():
    persona = Persona("Pablo", 40)

    estudiante = Estudiante("Camila", 30, "2026001")

    print(persona.presentarse())
    print(estudiante.presentarse())

    estudiante.set_edad(22)

    print(estudiante.presentarse())

    print(
        estudiante.estudiar("Programacion")
    )



if __name__ == "__main__":
    main()