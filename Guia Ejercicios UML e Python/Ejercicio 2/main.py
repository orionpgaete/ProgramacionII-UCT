class SensorTemperatura:

    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, valor):
        if valor < -273.15:
            raise ValueError(
                "Temperatura inferior al cero absoluto"
            )
        self.__celsius = valor

    @property
    def fahrenheit(self):
        return self.__celsius * 9 / 5 + 32

def main():
    sensor = SensorTemperatura(25)

    print("Celsius:", sensor.celsius)
    print("Fahrenheit:", sensor.fahrenheit)

    sensor.celsius = 0

    print("Celsius:", sensor.celsius)
    print("Fahrenheit:", sensor.fahrenheit)

if __name__ == "__main__":
    main()