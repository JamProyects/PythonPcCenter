class Maquina:
    def __init__(self, numero_serie, meses_alquilar):
        self.numero_serie = numero_serie
        self.meses_alquilar = meses_alquilar

    def calcular_alquiler(self):
        raise NotImplementedError("Sobrescribir en clases derivadas")

class MaquinaBebidasCalientes(Maquina):
    def calcular_alquiler(self):
        return self.meses_alquilar * 500

class MaquinaBebidasFrias(Maquina):
    def calcular_alquiler(self):
        return self.meses_alquilar * 700

def generar_factura(maquina):
    factura = (f"Número de Serie: {maquina.numero_serie}\n"
               f"Meses a Alquilar: {maquina.meses_alquilar}\n"
               f"Alquiler Total: B/ {maquina.calcular_alquiler():.2f}\n")
    print(factura)
    with open("factura_respaldo.txt", "a") as file:
        file.write(factura + "\n")

while True:
    try:
        numero_serie = input("Ingrese el número de serie: ")
        if not numero_serie.isalnum():
            raise ValueError("Debe ser alfanumérico.")
        meses = input("Ingrese meses a alquilar: ")
        if not meses.isdigit() or int(meses) <= 0:
            raise ValueError("Debe ser un número entero positivo.")
        meses = int(meses)
        tipo = input("Tipo de máquina (caliente/fria): ").strip().lower()
        if tipo == "caliente":
            maquina = MaquinaBebidasCalientes(numero_serie, meses)
        elif tipo == "fria":
            maquina = MaquinaBebidasFrias(numero_serie, meses)
        else:
            raise ValueError("Tipo inválido.")
        generar_factura(maquina)
    except ValueError as e:
        print(f"Error: {e}")
    if input("¿Alquilar otra? (s/n): ").strip().lower() != 's':
        break
