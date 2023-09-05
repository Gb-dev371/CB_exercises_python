# 1 - Crie uma função que receba um número como parâmetro
# e retorne o seu quadrado. Por exemplo, se a função for
# chamada de quadrado, chamar quadrado(2) deve retornar 4.

def main():
    print(square_number(int(input("Informe um número: "))))


def square_number(n):
    return n ** 2


if __name__ == "__main__":
    main()
