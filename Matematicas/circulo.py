class circulo:
    def __init__(self):
        self.resultado = 0

    def multiplicar(self, num):
        self.resultado *= num
    
    
    def dividir(self, num):  
        if num != 0:
            self.resultado /= num
        else:
            print("No se puede divir entre cero")

    def obtener_resultado(self):
        return self.resultado


