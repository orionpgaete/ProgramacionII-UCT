from encodings import search_function


class Fraccion:

    def __init__(self, nun, den):
        self.num = nun
        self.den = den

    def imprime(self):
        print(self.num, "/", self.den)

    def multiplicacion(self, b):
        n = self.num * b.num
        d = self.den * b.den
        r = Fraccion(n,d)
        return r

    def sumar(self, b):
        n = self.num * b.den + b.num * self.den
        d = self.den * b.den

        r= Fraccion(n,d)
        return r

def main():
    a = Fraccion(5, 8)
    b = Fraccion(4, 5)
    print("Fraccion A")
    a.imprime()

    print("Fraccion B")
    b.imprime()

    print("\nMultiplicacion")
    r = a.multiplicacion(b)
    r.imprime()

    print("\nSumar")
    r = a.sumar(b)
    r.imprime()

if __name__ == "__main__":
    main()

