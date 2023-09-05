# 84 - Bank Account. Crie uma classe "BankAccount" que inicialize com "account_number" e "balance". Depois crie
# um método para sacar e outro para depositar. Após isso, teste criando 2 objetos em que um saca e o outro deposita certos valores.
# No fim, mostre a mudança na tela.

class BankAccount:
    def __init__(self, account_number:int, balance:float):
        self.account_number = account_number
        self.balance = balance

    def withdraw(self):
        try:
            quantity = float(input("How many do you want to withdraw? "))
        except ValueError:
            print("You must to enter a valid number")

        if quantity > self.balance:
            print("You don't have enough funds")
        else:
            self.balance -= quantity
            print(f"You just withdraw {quantity}$ ")

    
    def deposit(self):
        while True:
            try:
                quantity = float(input("How many do you want to deposit? "))
            except ValueError:
                print("You must to enter a valid number")
            else:
                break
        self.balance += quantity
        print(f"You just deposited {quantity}$ ")
    
    @classmethod
    def get(cls):
        account_number = int(input("What is the account number? "))
        balance = float(input("What is the balance? "))
        return cls(account_number, balance)
    
    
    def __str__(self) -> str:
        return f"Account_number: {self.account_number}, balance: {self.balance}"
    

account1 = BankAccount.get()
account1.withdraw()
print(account1)
account2 = BankAccount.get()
account2.deposit()
print(account2)
