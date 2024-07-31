from functools import reduce

def main():
    numeros = [1, 2, 3, 4, 5, 6]
 
    cuadrados = list(map(lambda x: x**2, numeros))
    print("Cuadrados:", cuadrados)  

    pares = list(filter(lambda x: x % 2 == 0, numeros)) 
    print("Números pares:", pares)   

    puntos = [(1, 2), (3, 1), (5, -1), (0, 0)]

    puntos_ordenados = sorted(puntos, key=lambda punto: punto[1])
    print("Puntos ordenados por coordenada y:", puntos_ordenados)  

    suma_total = reduce(lambda x, y: x + y, numeros)
    print("Suma total:", suma_total)  

    maximo = lambda a, b: a if a > b else b
    print("Máximo entre 10 y 20:", maximo(10, 20))  

if __name__ == "__main__":
    main()