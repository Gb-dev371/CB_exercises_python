# 45 - Leia o peso de 5 pessoas e mostre o naior e o menor peso digitado

peso1 = float(input("Informe o primeiro peso: "))
peso2 = float(input("Informe o segundo peso: "))
peso3 = float(input("Informe o terceiro peso: "))
peso4 = float(input("Informe o quarto peso: "))
peso5 = float(input("Informe o quinto peso: "))
peso = [peso1, peso2, peso3, peso4, peso5]
maior = peso1
menor = peso1

for x in range(len(peso)):
    if peso[x] > maior:
        maior = peso[x]
    if peso[x] < menor:
        menor = peso[x]

print(f"O maior peso é {maior}kg e o menor peso é {menor}kg")
