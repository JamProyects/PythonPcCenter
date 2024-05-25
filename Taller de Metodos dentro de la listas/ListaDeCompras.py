#Supongamos que tienes una lista de compras en la que necesitas agregar, eliminar y marcar elementos como comprados a medida que los adquieres en el supermercado   
class ListaDeCompras:
    def __init__(self):
        self.items = []

    def agregar_item(self, item):
        self.items.append(item)
        print(f"Se ha agregado '{item}' a la lista de compras.")

    def eliminar_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"Se ha eliminado '{item}' de la lista de compras.")
        else:
            print(f"'{item}' no está en la lista de compras.")

    def marcar_comprado(self, item):
        if item in self.items:
            print(f"'{item}' ha sido marcado como comprado.")
        else:
            print(f"'{item}' no está en la lista de compras.")

    def mostrar_lista(self):
        if self.items:
            print("Lista de Compras:")
            for item in self.items:
                print(f"- {item}")
        else:
            print("La lista de compras está vacía.")
    
    def eliminar_item_input(self):
        item = input("Ingrese el producto que desea agregar (o 'fin' para terminar): ")
        if item.lower() == 'fin':
            return False
        self.eliminar_item(item)
        return True

    def agregar_item_input(self):
        item = input("Ingrese el producto que desea eliminar (o 'fin' para terminar): ")
        if item.lower() == 'fin':
            return False
        self.agregar_item(item)
        return True

lista = ListaDeCompras()

continuar = True
while continuar:
    lista.mostrar_lista()
    continuar = lista.eliminar_item_input()
    if continuar:
        continuar = lista.agregar_item_input()