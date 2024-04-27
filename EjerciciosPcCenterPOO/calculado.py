#hacer una calculadora que sume, reste, multiplique y divida
class Calculadora:
    def __init__(self):
        self.resultado = 0

    def sumar(self, num):
        self.resultado += num

    def restar(self, num):
        self.resultado -= num

    def multiplicar(self, num):
        self.resultado *= num
    
    
    def dividir(self, num):  
        if num != 0:
            self.resultado /= num
        else:
            print("No se puede divir entre cero")

    def obtener_resultado(self):
        return self.resultado

calculadora = Calculadora()

while True:
    print("1. sumar")
    print("2. restar")
    print("3. multiplicar")
    print("4. dividir")

    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        num = float(input("Ingrese un numero para sumar: "))
        calculadora.sumar(num)

    elif opcion == "2":
        num = float(input("ingrese un numero para restar: "))
        calculadora.restar(num)
    elif opcion == "3":
        num = float(input("ingrese un numero para multiplicar: "))
        calculadora.multiplicar(num)
    elif opcion == "4":
        num = float(input("ingrese un numero para restar: "))
        calculadora.dividir(num)
    elif opcion == "5":
        break
    else:
        print("Opcion invalida")

    print("Resultado:", calculadora.obtener_resultado())
    print()
    print("Fin del calculo")

    
