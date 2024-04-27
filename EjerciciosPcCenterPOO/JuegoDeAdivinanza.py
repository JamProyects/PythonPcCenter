import random

class JuegoAdivinanza:
    def __init__(self):
        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0

    def adivinar_numero(self, numero):
        self.intentos += 1
        if numero < self.numero_secreto:
            return "El número a adivinar es mayor."
        elif numero > self.numero_secreto:
            return "El número a adivinar es menor."
        else:
            return f"Felicitaciones! Adivinaste el número en {self.intentos} intento(s)."

juego = JuegoAdivinanza()
while True:
    conjetura = input("Adivina el número entre 1 y 100: ")
    try:
        conjetura = int(conjetura)
        resultado = juego.adivinar_numero(conjetura)
        print(resultado)
        if resultado.startswith("Felicitaciones!"):
            break
    except ValueError:
        print("Por favor, ingresa un número válido.")