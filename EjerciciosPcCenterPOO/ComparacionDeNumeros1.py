#Cree una funcion que compare 2 numeros y luego compare 3 numeros con la funcion anterior.
class Comparador:
    def comparar_dos_numeros(self, num1, num2):
        if num1 > num2:
            return f"{num1} es mayor que {num2}"
        elif num1 < num2:
            return f"{num1} es menor que {num2}"
        else:
            return f"{num1} es igual a {num2}"
    
    def comparar_tres_numeros(self, num1, num2, num3):
        resultado1 = self.comparar_dos_numeros(num1, num2)
        resultado2 = self.comparar_dos_numeros(num1, num3)
        resultado3 = self.comparar_dos_numeros(num2, num3)
        return f"Comparacion 1: {resultado1}\nComparacion 2: {resultado2}\nComparacion 3: {resultado3}"

comparador = Comparador()

num1 = float(input("ingrese un numero: "))
num2 = float(input("ingrese un numero: "))
resultado = comparador.comparar_dos_numeros(num1, num2)
print(resultado)

num3 = float(input("ingrese un numero: "))
resultado = comparador.comparar_tres_numeros(num1, num2, num3)
print(resultado)

        

