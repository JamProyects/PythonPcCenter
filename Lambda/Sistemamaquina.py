class Maquina:
    def __init__(self, numero_serie, meses_alquilar):
        self.__numero_serie = numero_serie
        self.__meses_alquilar = meses_alquilar

    @property
    def numero_serie(self):
        return self.__numero_serie

    @property
    def meses_alquilar(self):
        return self.__meses_alquilar

    def calcular_alquiler(self):
        raise NotImplementedError("Este método debe ser sobrescrito en las clases derivadas")

class MaquinaBebidasCalientes(Maquina):
    __costo_alquiler = 500.00

    def calcular_alquiler(self):
        return self.meses_alquilar * self.__costo_alquiler

class MaquinaBebidasFrias(Maquina):
    __costo_alquiler = 700.00

    def calcular_alquiler(self):
        return self.meses_alquilar * self.__costo_alquiler

def validar_numero_serie(numero_serie):
    return numero_serie.isalnum()

def validar_meses_alquilar(meses_alquilar):
    return meses_alquilar.isdigit() and int(meses_alquilar) > 0

def generar_factura(maquina):
    alquiler_total = maquina.calcular_alquiler()
    factura = (
        f"Número de Serie: {maquina.numero_serie}\n"
        f"Meses a Alquilar: {maquina.meses_alquilar}\n"
        f"Alquiler Total: B/ {alquiler_total:.2f}\n"
    )
    print(factura)
    with open("factura_respaldo.txt", "a") as file:
        file.write(factura + "\n")

def main():
    while True:
        try:
            numero_serie = input("Ingrese el número de serie de la máquina: ")
            if not validar_numero_serie(numero_serie):
                raise ValueError("El número de serie debe ser alfanumérico.")

            meses_alquilar = input("Ingrese la cantidad de meses a alquilar: ")
            if not validar_meses_alquilar(meses_alquilar):
                raise ValueError("Los meses a alquilar deben ser un entero positivo.")

            meses_alquilar = int(meses_alquilar)
            tipo_maquina = input("Ingrese el tipo de máquina (caliente/fria): ").strip().lower()

            if tipo_maquina == "caliente":
                maquina = MaquinaBebidasCalientes(numero_serie, meses_alquilar)
            elif tipo_maquina == "fria":
                maquina = MaquinaBebidasFrias(numero_serie, meses_alquilar)
            else:
                raise ValueError("Tipo de máquina inválido. Debe ser 'caliente' o 'fria'.")

            generar_factura(maquina)

        except ValueError as e:
            print(f"Error: {e}")
            print("Por favor, intente de nuevo.")
            continue

        repetir = input("¿Desea alquilar otra máquina? (s/n): ").strip().lower()
        if repetir != 's':
            break

if __name__ == "__main__":
    main()
