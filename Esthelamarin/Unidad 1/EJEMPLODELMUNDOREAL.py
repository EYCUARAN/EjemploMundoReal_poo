class Cliente:
    def __init__(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion

class Cuenta:
    def __init__(self, numero_cuenta, cliente, saldo=0.0):
        self.numero_cuenta = numero_cuenta
        self.cliente = cliente
        self.saldo = saldo

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f'Depositados {monto} en la cuenta {self.numero_cuenta}. Nuevo saldo: {self.saldo}')
        else:
            print('El monto a depositar debe ser positivo.')

    def retirar(self, monto):
        if monto > 0 and monto <= self.saldo:
            self.saldo -= monto
            print(f'Retirados {monto} de la cuenta {self.numero_cuenta}. Nuevo saldo: {self.saldo}')
        else:
            print('Monto insuficiente o inválido.')

    def transferir(self, monto, cuenta_destino):
        if monto > 0 and monto <= self.saldo:
            self.retirar(monto)
            cuenta_destino.depositar(monto)
            print(f'Transferidos {monto} de la cuenta {self.numero_cuenta} a la cuenta {cuenta_destino.numero_cuenta}.')
        else:
            print('Monto insuficiente o inválido para la transferencia.')

# Ejemplo de uso
cliente1 = Cliente("Juan Pérez", "12345678")
cliente2 = Cliente("María López", "87654321")

cuenta1 = Cuenta("001", cliente1, 1000.0)
cuenta2 = Cuenta("002", cliente2, 500.0)

# Depositar dinero en la cuenta 1
cuenta1.depositar(200.0)

# Retirar dinero de la cuenta 2
cuenta2.retirar(100.0)

# Transferir dinero de la cuenta 1 a la cuenta 2
cuenta1.transferir(300.0, cuenta2)