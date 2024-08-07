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

def preguntar_alquilar_otra():
    while True:
        respuesta = input("¿Alquilar otra? (s/n): ").strip().lower()
        if respuesta in ['s', 'n']:
            return respuesta
        else:
            print("Respuesta inválida. Por favor, ingrese 's' o 'n'.")

def solicitar_numero_serie():
    while True:
        try:
            numero_serie = input("Ingrese el número de serie: ")
            if not numero_serie.isalnum():
                raise ValueError("Debe ser alfanumérico.")
            return numero_serie
        except ValueError as e:
            print(f"Error: {e}")

def solicitar_meses_alquilar():
    while True:
        try:
            meses = input("Ingrese meses a alquilar: ")
            if not meses.isdigit() or int(meses) <= 0:
                raise ValueError("Debe ser un número entero positivo.")
            return int(meses)
        except ValueError as e:
            print(f"Error: {e}")

def solicitar_tipo_maquina():
    while True:
        try:
            tipo = input("Tipo de máquina (caliente/fria): ").strip().lower()
            if tipo in ["caliente", "fria"]:
                return tipo
            else:
                raise ValueError("Tipo inválido. Debe ser 'caliente' o 'fria'.")
        except ValueError as e:
            print(f"Error: {e}")

while True:
    numero_serie = solicitar_numero_serie()
    meses = solicitar_meses_alquilar()
    tipo = solicitar_tipo_maquina()

    if tipo == "caliente":
        maquina = MaquinaBebidasCalientes(numero_serie, meses)
    else:
        maquina = MaquinaBebidasFrias(numero_serie, meses)

    generar_factura(maquina)

    if preguntar_alquilar_otra() != 's':
        break
