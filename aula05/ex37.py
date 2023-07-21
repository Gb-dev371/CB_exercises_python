import random

usuario = int(input("Escolha pedra, papel ou tesoura [0, 1 ou 2]: "))
opcoes = [0, 1, 2]
computador = random.randint(0, 2)

# if (usuario != "pedra" or usuario != "papel"
#    or usuario != "tesoura"):
#     print("Você não escolheu corretamente uma das opções!")

if usuario == 0:
    if computador == 1:
        print("Computador ganhou!")
    elif computador == 2:
        print("Você ganhou")
    elif computador == 0:
        print("Empate!")

elif usuario == 1:
    if computador == 1:
        print("Empate!")
    elif computador == 2:
        print("Computador ganhou!")
    elif computador == 0:
        print("Você ganhou!")

elif usuario == 2:
    if computador == 1:
        print("Você ganhou!")
    elif computador == 2:
        print("Empate!")
    elif computador == 0:
        print("Computador ganhou!")

print(computador)
