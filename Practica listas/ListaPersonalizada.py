#Ingresar numeros en una lista hasta que el usuario lo dese y luego imprima la lista.

numeros = []


while True:
    numero = input("Ingresa un número (o 'fin' para terminar): ")
    if numero.lower() == 'fin':
        break
    try:
        numero = int(numero)
        numeros.append(numero)  
    except ValueError:
        print("Por favor, ingresa un número válido.")

print("Los números ingresados son:", numeros)
