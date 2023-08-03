# 63 - Escreva um programa que solicite ao usuário que digite seu nome e sua
# idade. Em seguida, tente converter a idade em um número inteiro. Se a
# conversão falhar, informe ao usuário que a idade digitada é
# inválida e continue o programa. Caso contrário, exiba uma mensagem com o
# nome e a idade.

name = input("What is your name? ")
age = input("How old are you? ")

try:
    age_int = int(age)
except ValueError:
    print("Invalid age entered.")
else:
    print(f"Name: {name}\nAge: {age}")
