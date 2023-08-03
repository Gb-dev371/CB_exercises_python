# 58 - Crie uma função que receba uma lista de números como entrada e retorne
# o maior número presente na lista.

def lista(*args):
    numeros = [*args]
    maior = sorted(numeros, key=int, reverse=True)
    print(f"O maior número é {maior[0]}")


lista(1, 3, 2, 55)
