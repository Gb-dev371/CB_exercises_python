import random

num_pc = random.randint(0, 5)
num_usuario = int(input("Escolha um numero de 0 a 5: "))


if 0 < num_usuario > 5:
    if num_usuario == num_pc:
        print("Voce acertou!")
    else:
        print(f"Voce errou. O numero sorteado pelo computador foi {num_pc}")
else:
    print("Digite um número válido")

# try:
# except:
