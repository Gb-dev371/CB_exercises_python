# 55 - Agora faça o exercício acima aceitar vários jogadores, inclua um
# sistema para vizualizar detalhes do aproveitamento de cada jogador.

numero_de_jogadores = int(input("Quantos jogadores você quer cadastrar? "))
nomes_lista = []
partidas_lista = []
gols_lista = []
gols_totais_lista = []

for i in range(numero_de_jogadores):
    nome = input("Informe o nome: ")
    nomes_lista.append(nome)

    partidas = int(input("Quantas partidas jogou? "))
    partidas_lista.append(partidas)

    gols = int(input("Informe a quantidade de gols feitos em cada partida: "))
    gols_lista.append(gols)

    gols_totais = gols * partidas
    gols_totais_lista.append(gols_totais)

    dict_fut = {
    "Nome": nome,
    "Partidas": partidas,
    "Gols totais": gols * partidas
}





print(dict_fut)
