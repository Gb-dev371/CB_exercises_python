# 66 - Implemente uma função chamada "get_list_element" que recebe uma lista e
# um índice como parâmetros. A função deve retornar o elemento da lista no
# índice especificado. Caso o índice esteja fora do intervalo válido,
# capture a exceção IndexError e retorne uma  mensagem indicando que o índice
# é inválido.

def get_list_element(lista: list[int], index):
    try:
        return lista[index]
    except (IndexError):
        print("O indíce informado não existe na lista.")
