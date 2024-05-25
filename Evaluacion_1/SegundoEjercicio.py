
contactos = []


def agregar_contacto(nombre, telefono):
    contacto = {"nombre": nombre, "telefono": telefono}
    contactos.append(contacto)
    print(f"Contacto {nombre} agregado exitosamente.")


def mostrar_contactos():
    if not contactos:
        print("No hay contactos en la lista.")
    else:
        print("Lista de contactos:")
        for contacto in contactos:
            print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}")


def buscar_contacto(nombre):
    for contacto in contactos:
        if contacto['nombre'].lower() == nombre.lower():
            print(f"Contacto encontrado: Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}")
            return
    print("Contacto no encontrado.")

def main():
    while True:
        print("\nGestión de Contactos")
        print("1. Agregar contacto")
        print("2. Mostrar todos los contactos")
        print("3. Buscar contacto por nombre")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            nombre = input("Introduce el nombre del contacto: ")
            telefono = input("Introduce el número de teléfono del contacto: ")
            agregar_contacto(nombre, telefono)
        elif opcion == '2':
            mostrar_contactos()
        elif opcion == '3':
            nombre = input("Introduce el nombre del contacto a buscar: ")
            buscar_contacto(nombre)
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor selecciona una opción correcta.")


if __name__ == "__main__":
    main()