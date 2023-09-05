# 93 - Desenvolva uma classe Bank que gerencia várias contas bancárias. Os métodos devem permitir criar novas contas, 
# fazer transferências entre contas e calcular o saldo total do banco.

# informations = {account}

class Bank:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.show_method()

    def deposit(self):
        try: # Tratando o possível erro do usuário digitar uma string no lugar de um número
            quantity = float(input("How many do you want to deposit? "))
            if quantity < 0:
                print("You cannot to deposit a negative value.")
            else:
                self.balance += quantity
        except ValueError:
            print("Invalid value.")

    def withdraw(self):
        try:  # Tratando o possível erro do usuário digitar uma string no lugar de um número
            quantity = float(input("How many do you want to withdraw from your balance? "))
            if quantity > self.balance:
                print("You cannot to withdraw a balance bigger than you actually have.")
            else:
                self.balance -= quantity
                print(f"You just withdraw {quantity}$. Now you have {self.balance} in your account.")
        except ValueError:
            print("Invalid value.") 

    
    def show_method(self):
        method = input("What do you want to do?\n1 - To withdraw\n2 - To deposit\n3 - To add an account\n4 - Nothing ")
        if method == "1":
            self.withdraw()
        elif method == "2":
            self.deposit()
        elif method == "3":
            Bank.add_account()
        elif method == "4":
            pass
        elif method == "5":
            pass
        else:
            print("Invalid.")

    def transfer(self, amount, account):
        # amount = float("How many do you want to transfer? ")
        # account = 
        self.balance -= amount
        account.balance += amount

    def show_atributes(self):
        print(f"Number account: {self.account_number}, balance: {self.balance}")

    def __add__(self, other):
        account = [self.account_number, other.account_number]
        balance = self.balance + other.balance
        return Bank(account, balance)
    
    # def total_balance(self, other):
    #     return self.balance + other.balance


    @classmethod
    def add_account(cls):
        account_number = int(input("What is the account number? "))
        balance = float(input("What is the balance? "))
        return cls(account_number, balance)
    
account1 = Bank.add_account()
account2 = Bank.add_account()
account1.transfer(1000, account2)
account1.show_atributes()
account2.show_atributes()
total = account1 + account2
print(total.show_atributes())