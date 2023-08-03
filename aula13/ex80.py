# 80 - Classe "Aluno":
# Crie uma classe chamada "Aluno" que possua o método __init__
# para inicializar as propriedades "nome" e "nota" do aluno.
# Em seguida, crie dois objetos da classe "Aluno" e verifique qual dos dois
# obteve a maior nota.


def main():
    class Aluno:
        def __init__(self, nome, nota):
            self.nome = nome
            self.nota = nota

    aluno1 = Aluno(get_nome(), get_nota())
    aluno2 = Aluno(get_nome(), get_nota())

    if aluno1.nota > aluno2.nota:
        print("{} é o aluno com maior nota.".format(aluno1.nome))
    elif aluno2.nota > aluno1.nota:
        print("{} é o aluno com maior nota".format(aluno2.nome))
    else:
        print("Os dois alunos tem a mesma nota.")


def get_nome():
    return input("Informe o nome do aluno: ")


def get_nota():
    return float(input("Informe a nota do aluno "))


if __name__ == "__main__":
    main()
