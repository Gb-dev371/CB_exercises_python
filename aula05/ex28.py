# 28 - Escreva um programa para aprovar o empréstimo bancária para
# a compra de uma casa. Pergunte o valor da casa, o salário de comprador e
# em quantos anos ele vai pagar. A prestação mensal não pode exceder 30%
# do salário ou o empréstimo será negado.

house_value = int(input("What is the value of the house? "))
salary = int(input("What is your salary? "))
years = int(input("Do you would like to pay in how many years? "))
installments = house_value / years

if installments > 0.3 * salary:
    print("You cannot afford this loan")
else:
    print("You will get the loan")
