class Account:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Cannot withdraw negative amount")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def deposito(self , valor):
        if valor <= 0:
            raise ValueError("valor de deposito invalido")
        
        self.balance += valor

    def transferencia(self , destino , valor):
        if self.balance <= 0:
            raise ValueError("a conta não possui o saldo necessario para a operação")

        if valor <= 0:
            raise ValueError("valor de transferencia invalido")

        self.balance -= valor
        destino.balance += valor


#teste de commit