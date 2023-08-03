# Gerencie um jogador de futebol lendo o nome e quantas partidas ele jogou.
# Depois, leia a quantidade de gols feitas em cada partida. Coloque tudo num
# dicionário incluindo o total de gols durante o período.

nome = input("Informe o nome: ")
partidas = int(input("Quantas partidas jogou? "))
gols = int(input("Informe a quantidade de gols feitos em cada partida: "))

dict_fut = {
    "Nome": nome,
    "Partidas": partidas,
    "Gols totais": gols * partidas
}

print(dict_fut)
