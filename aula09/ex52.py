# Crie um programa onde 4 jogadores jogam um dado. Guarde esses resultados
# em um dicionário. No final, coloque esse dicionário em ordem (1º, 2º...)

# import random

# list = []

# for num in range(4):
#     num_dado = random.randint(1, 6)
#     list.append(num_dado)

# print(list)

# list = sorted(list, key=int, reverse=True)
# print(list)

# dict_dados = {k + 1: v for k, v in enumerate(list)}
# print(dict_dados)

# # Crie um programa onde 4 jogadores jogam um dado. Guarde esses resultados
# # em um dicionário. No final, coloque esse dicionário em ordem (1º, 2º...)

# import random

# lista_decrescente = []

# # for num in range(4):
# #     num_dado = random.randint(1, 6)
# #     list.append(num_dado)

# jogador1 = random.randint(1, 6)
# jogador2 = random.randint(1, 6)
# jogador3 = random.randint(1, 6)
# jogador4 = random.randint(1, 6)

# # print(list)

# lista_decrescente = sorted(lista_decrescente, key=int, reverse=True)
# # print(lista_decrescente)

# dict_dados = {
#     "Jogador 1": jogador1,  
# }

# # {k + 1: v for k, v in enumerate(lista_decrescente)}
# # print(dict_dados)

import random

dict_dado = {
    "Jogador 1": random.randint(1, 6),
    "Jogador 2": random.randint(1, 6),
    "Jogador 3": random.randint(1, 6),
    "Jogador 4": random.randint(1, 6)
}

print(dict_dado)

dict_dado_ordenado = {k: v for k, v in sorted(dict_dado.items(), key=lambda item: item[1], reverse=True)}

print(dict_dado_ordenado)
