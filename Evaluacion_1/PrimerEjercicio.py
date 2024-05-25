
n = int(input("Introduce un número entero positivo: "))


if n <= 0:
    print("El número debe ser un entero positivo.")
else:
    for i in range(2, n + 1):
        if i % 2 == 0:
            print(i)