from circulo import circulo

calculadora = circulo()

while True:
    print("1. multiplicar")
    print("2. dividir")

    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        num = float(input("ingrese un numero para multiplicar: "))
        calculadora.multiplicar(num)
    elif opcion == "2":
        num = float(input("ingrese un numero para restar: "))
        calculadora.dividir(num)
    elif opcion == "3":
        break
    else:
        print("Opcion invalida")

    print("Resultado:", circulo.obtener_resultado())
    print()
    print("Fin del calculo")

    
