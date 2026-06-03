class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
    
    def __str__(self):
        return f"${self.__balance}"
    
    def detailed(self):
        return f"Account Owner: {self.owner} | Account Balance: {self.__balance}"
    
    def __eq__(self, another):
        return self.__balance == another.__balance
    
    def __lt__(self, another):
        return self.__balance < another.__balance
    
    def __gt__(self, another):
        return self.__balance > another.__balance
    
    def __add__(self, another):
        total = self.__balance + another.__balance
        return BankAccount("Combined", total)
    
    def __sub__(self, another):
        total = self.__balance - another.__balance
        if total <0:
            raise ValueError ("Total of subtraction can't be negative")
        else:
            return BankAccount("Difference", total)

a1 = BankAccount("Jenny", 600)
a2 = BankAccount("Bob", 400)

print(a1+a2)
print(a1.detailed())
    
    

    