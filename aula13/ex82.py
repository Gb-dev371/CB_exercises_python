# 82 - Classe "Pessoa":
# Crie uma classe chamada "Pessoa" que possua o método __init__ para
# inicializar as propriedades "nome", "idade" e "profissão" da pessoa.
# Em seguida, crie um objeto da classe "Pessoa" e  imprima todas as status
# informações (nome, idade e profissão).

class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao


def main():
    pessoa1 = Pessoa(get_nome(), get_idade(), get_profissao())
    print(f"Nome: {pessoa1.nome} \nIdade: {pessoa1.idade} \nProfissão: "
          f"{pessoa1.profissao}")


def get_nome():
    return input("Digite o nome: ")


def get_idade():
    return int(input("Digite a idade: "))


def get_profissao():
    return input("Informe a profissão: ")


if __name__ == "__main__":
    main()
