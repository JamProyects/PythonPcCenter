def contar_vocales(cadena):
    recuento_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    cadena = cadena.lower()
    for caracter in cadena:
        if caracter in recuento_vocales:
            recuento_vocales[caracter] += 1
    return recuento_vocales

cadena = input("Introduce una cadena de texto: ")


recuento = contar_vocales(cadena)


print("Resultado:")
for vocal, cantidad in recuento.items():
    print(f"{vocal}: {cantidad}")