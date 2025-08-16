class BankAccount:
    def __init__(self, balance=0):
        print("constructor called")
        self.balance = balance

    @property 
    def balance(self):
        print("balance property called")
        return self._balance
    
    @balance.setter
    def balance(self, value):
        print("balance setter called")
        if value < 0:
            raise ValueError("balance can not be negative")
        self._balance = value

    def deposite(self, amount):
        print("deposite method called")
        if not isinstance(amount, int):
            raise ValueError("invalid amount entered")
        if amount <= 0:
            raise ValueError("amount can not be negative or zero.")
        self.balance += amount

    def withdraw(self, amount):
        print("withdraw method called")
        if not isinstance(amount, int):
            raise ValueError("invalid amount entered")
        if amount <= 0:
            raise ValueError("amount can not be negative or zero")
        if amount > self.balance:
            raise ValueError("entered withdraw amount can't be bigger than balance")
        self.balance -= amount

# # default value check
# acc1 = BankAccount()
# print(acc1.balance)
# acc1.deposite(100)
# print(acc1.balance)
# acc1.withdraw(50)
# print(acc1.balance)

# input value check(valid one)
acc1 = BankAccount(100)
print(acc1.balance)
acc1.deposite(100)
print(acc1.balance)
acc1.withdraw(50)
print(acc1.balance)

# # input value check(invalid one)
# acc1 = BankAccount()
# print(acc1.balance)
# # acc1.deposite(-100)
# print(acc1.balance)
# # acc1.withdraw("60")
# print(acc1.balance)