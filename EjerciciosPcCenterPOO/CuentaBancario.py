class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Se han depositado {cantidad} unidades. Saldo actual: {self.saldo}")

    def retirar(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            print(f"Se han retirado {cantidad} unidades. Saldo actual: {self.saldo}")
        else:
            print("Saldo insuficiente.")

    def consultar_saldo(self):
        print(f"Saldo actual de {self.titular}: {self.saldo}")

cuenta = CuentaBancaria("Juan")
cuenta.depositar(1000)
cuenta.retirar(500)
cuenta.consultar_saldo()
