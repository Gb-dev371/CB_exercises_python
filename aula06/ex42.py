# 42 - Crie um programa que receba 5 valores int e no final
# mostre a soma apenas dos pares

num1 = int(input("Informe um número "))
num2 = int(input("Informe um número "))
num3 = int(input("Informe um número "))
num4 = int(input("Informe um número "))
num5 = int(input("Informe um número "))
num = [num1, num2, num3, num4, num5]
pares = []
soma_pares = 0

for i in num:
    if (i % 2 == 0):
        pares.append(i)

for j in range(len(pares)):
    soma_pares += pares[j]

print(soma_pares)
