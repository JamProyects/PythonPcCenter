#Escribe un programa que solicite al usuario ingresar una lista de numeros enteros separados por espacios y luego imprima la lista en orden inverso
entrada = input("Ingresa una lista de números enteros separados por espacios: ")
numeros = list(map(int, entrada.split()))
print("La lista en orden inverso es:", numeros[::-1])