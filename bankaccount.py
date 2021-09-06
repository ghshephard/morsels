class BankAccount:
    id=1001
    accounts = []
    def __init__(self,balance=0):
        if balance < 0:
            raise ValueError(f"Cannot open account with {balance} balance")
        self._balance = balance
        self.number = BankAccount.id
        BankAccount.id += 1
        BankAccount.accounts.append(self)
    @property
    def balance(self):
        return self._balance
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError(f"Can't withdraw {amount}")
        if self.balance - amount < 0:
            raise ValueError(f"Cannot withdraw {amount} with {self.balance} balance")
        self._balance -= amount
    def deposit(self, amount):
        if amount < 0:
            raise ValueError(f"Cannot deposit {amount}")
        self._balance += amount
    def transfer(self, destination, amount):
        if amount < 0:
            raise ValueError(f'Cannot Transfer {amount}')
        self.withdraw(amount)
        destination.deposit(amount)


    def __repr__(self):
        return f'{type(self).__name__}(balance={self.balance})'
    
if __name__ == '__main__':
    a1 = BankAccount()
    a1.deposit(10)
    a1.withdraw(5)
    a2 = BankAccount()
    a1.transfer(a2,2)
    print(BankAccount.accounts)