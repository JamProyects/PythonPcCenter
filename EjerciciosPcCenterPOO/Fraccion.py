from math import gcd   

class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
        self.simplificar()

    def simplificar(self):
        comun_divisor = gcd(self.numerador, self.denominador)
        self.numerador = self.numerador // comun_divisor
        self.denominador = self.denominador // comun_divisor

    def __add__(self, other):
        nuevo_numerador = self.numerador * other.denominador + other.numerador * self.denominador
        nuevo_denominador = self.denominador * other.numerador
        return f"{self.numerador}/{self.denominador}"
    
    def __str__(self):
        return f"{self.numerador}/{self.denominador}"
    
f1 = Fraccion(1,2)
f2 = Fraccion(3,4)

f3 = f1 + f2
print(f"Suma: {f3}")