'''
33 - A Confederação Nacional de Natação precisa de um programa que
leia o ano de nascimento de um atleta e mostre sua categoria,
de acordo com a idade:
Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JÚNIOR
Até 25 anos: SÊNIOR
Acima de 25 anos: MASTER
'''

birth_year = int(input("What is the year of your birth? "))
current_year = 2023
age = current_year - birth_year

if age < 0:
    print("There is something wrong with the year of your bith")
elif age <= 9:
    print(f"{age}: MIRIM")
elif age <= 14:
    print(f"{age}: INFANTIL")
elif age <= 19:
    print(f"{age}: JÚNIOR")
elif age <= 25:
    print(f"{age}: SÊNIOR")
else:  # age > 25
    print(f"{age}: MASTER")
