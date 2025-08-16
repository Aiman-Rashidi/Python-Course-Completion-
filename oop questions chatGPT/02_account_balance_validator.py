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
            raise ValueError("negative balance not allowed.")
        self._balance = value

# # Default value check
# account = BankAccount()
# print(account.balance)

# # Input value check
# account = BankAccount(4000)
# print(account.balance)

# Setter use check(valid one)
account = BankAccount(4000)
print(account.balance)
account.balance = 100
print(account.balance)

# # Setter use check(invalid one)
# account = BankAccount(4000)
# print(account.balance)
# account.balance = -100
# print(account.balance)

# # Setter use check(invalid one)
# account = BankAccount(-4000)
# print(account.balance)
# account.balance = -100
# print(account.balance)