# 59 - Escreva uma função que receba uma lista de palavras como entrada e
# retorne uma lista apenas com as palavras que tem mais de 5 letras.

def lista_palavras(*args):
    l_p = [*args]
    l_p_5 = []

    for i in l_p:
        if len(i) > 5:
            l_p_5.append(i)
    print(l_p_5)


lista_palavras('maçã', 'banana', 'abacaxi', 'laranja')
