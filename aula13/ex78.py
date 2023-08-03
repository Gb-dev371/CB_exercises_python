# 78 - Classe "Cachorro":
# Crie uma classe chamada "Cachorro" que possua o método __init__ para
# inicializar as propriedades "nome" e "idade" do cachorro. Em seguida, crie
# um objeto da classe "Cachorro" e imprima o nome e a idade do cachorro.

def main():
    class Cachorro:
        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade

    cachorro = Cachorro(get_nome(), get_idade())

    print(f"O nome do cachorro é {cachorro.nome} e a "
          f"idade do cachorro é {cachorro.idade}")


def get_nome():
    return input("Informe o nome do cachorro: ")


def get_idade():
    return int(input("Informe a idade do cachorro: "))


if __name__ == "__main__":
    main()
