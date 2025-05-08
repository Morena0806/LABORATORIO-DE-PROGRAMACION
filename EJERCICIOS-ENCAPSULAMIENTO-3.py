class CuentaBancaria:
    def __init__(self, titular, saldo, numero_cuenta):
        self.__titular = titular
        self.__saldo = saldo if saldo >= 0 else 0.0
        self.__numero_cuenta = numero_cuenta

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def get_numero_c(self):
        return self.__numero_cuenta

    def set_titular(self, nuevo_titular):
        self.__titular = nuevo_titular

        return nuevo_titular

    def set_saldo(self, nuevo_saldo):
        if nuevo_saldo >= 0:
            self.__saldo = nuevo_saldo

        else:
            print("Saldo invalido")

        return nuevo_saldo

    def set_numero_c(self, nuevo_numero_c):
        self.__numero_cuenta = nuevo_numero_c

    def depositar_dinero(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Se depositaron {cantidad} en la cuenta {self.__numero_cuenta}.")

        else:
            print("La cantidad a depositar debe ser mayor a 0.")


    def retirar_dinero(self, cantidad):
        if 0 < cantidad <=self.__saldo:
            self.__saldo -= cantidad
            print(f"Se retiraron {cantidad} de la cuenta {self.__numero_cuenta}.")

        else:
            print("Se debe retirar una cantidad mayor a 0 y no puede exceder el saldo disponible.")

    def mostrar_saldo(self):
        return self.__saldo

    
if __name__ == "__main__":
    cuenta1 = CuentaBancaria("Maria", 0.0, "1234567890")

    print(f"Saldo inicial: {cuenta1.mostrar_saldo()}")
    cantidad = 0

    print("Ingrese la cantidad de dinero que quiere depositar:")
    
    cantidad = float(int(input()))
    cuenta1.depositar_dinero(cantidad)
    print(f"Cantidad de dinero luego del deposito: {cuenta1.mostrar_saldo()}")

    print("Ingrese la cantidad de dinero que quiere retirar:")

    cantidad = float(int(input()))
    cuenta1.retirar_dinero(cantidad)
    print(f"Cantidad de dinero luego del retiro: {cuenta1.mostrar_saldo()}")
