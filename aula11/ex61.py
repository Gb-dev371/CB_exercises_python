# 61 - Escreva um programa que peça ao usuário para digitar um número inteiro
# e, em seguida, imprima o dobro desse número. Utilize try/except para lidar
# com a possibilidade de o usuário inserir um valor não numérico.

while True:
    try:
        num = int(input("Digite um numero: "))
        print(num)
        break
    except ValueError:
        print("Valor inválido! Tente novamente.")
