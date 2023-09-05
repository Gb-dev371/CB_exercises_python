# 86 - Defina uma classe BankAccount com atributos privados balance e account_number. 
# Crie métodos deposit e withdraw para manipular o saldo.

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self):
        try: # Tratando o possível erro do usuário digitar uma string no lugar de um número
            quantity = float(input("How many do you want to deposit?"))
            if quantity < 0:
                print("You cannot to deposit a negative value.")
            else:
                self.__balance += quantity
        except ValueError:
            print("Invalid value.")

    def withdraw(self):
        try:  # Tratando o possível erro do usuário digitar uma string no lugar de um número
            quantity = float(input("How many do you want to withdraw from your balance?"))
            if quantity > self.__balance:
                print("You cannot to withdraw a balance bigger than you actually have.")
            else:
                self.__balance -= quantity
                print(f"You just withdraw {quantity}$. Now you have {self.__balance} in your account.")
        except ValueError:
            print("Invalid value.")
            

    def show_atributes(self):
        print(f"Number account: {self.__account_number}, balance: {self.__balance}")


    @classmethod
    def get(cls):
        account_number = int(input("What is the account_number? "))
        balance = float(input("What is the balance? "))
        return cls(account_number, balance)

conta1 = BankAccount.get()
conta1.deposit()
conta1.show_atributes()

conta2 = BankAccount.get()
conta2.withdraw()
conta2.show_atributes()

