class PuestoLimonadas:
    def __init__(self):
        self.vasos_disponibles = 100
        self.azucares_disponibles = 80
        self.venta_dia = 0
        self.vasos_consumidos = 0
        self.azucares_consumidos = 0

    def vender_limonada(self, tipo_limonada):
        if tipo_limonada == 1:  # Limonada endulzada
            precio = 0.50
            azucar_consumida = 3
        elif tipo_limonada == 2:  # Limonada sin endulzar
            precio = 0.45
            azucar_consumida = 1
        else:
            print("Opción inválida.")
            return

        if self.vasos_disponibles > 0:
            self.vasos_disponibles -= 1
            self.venta_dia += precio
            self.vasos_consumidos += 1
            if self.azucares_disponibles >= azucar_consumida:
                self.azucares_disponibles -= azucar_consumida
                self.azucares_consumidos += azucar_consumida
                print(f"¡Aquí tiene su limonada! Precio: {precio} centavos.")
            else:
                print("Lo siento, no hay azúcar suficiente para preparar su limonada.")
        else:
            print("Lo siento, no quedan vasos disponibles.")

    def imprimir_totales(self):
        print(f"Total dinero de la venta del día: {self.venta_dia} centavos")
        print(f"Total vasos consumidos: {self.vasos_consumidos}")
        print(f"Total azúcar consumida: {self.azucares_consumidos} cucharadas")

def main():
    puesto = PuestoLimonadas()
    while True:
        print("\nMenú:")
        print("1. Limonada endulzada (0.50 centavos)")
        print("2. Limonada sin endulzar (0.45 centavos)")
        print("3. Imprimir totales")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            puesto.vender_limonada(1)
        elif opcion == '2':
            puesto.vender_limonada(2)
        elif opcion == '3':
            puesto.imprimir_totales()
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()