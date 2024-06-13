class Volador:
    def volar(self):
        print("Estoy volando")


class Nadador:
    def nadar(self):
        print("Estoy nadando")


class Pato(Volador, Nadador ):
    pass

pato = Pato()
pato.volar() 
pato.nadar()