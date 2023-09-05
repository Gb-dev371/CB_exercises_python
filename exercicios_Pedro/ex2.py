# 2 - Crie uma função que receba dois números como parâmetro e retorne
# a soma deles. Por exemplo, se a função for chamada de adicionar,
# chamar adicionar(1, 2) deve retornar 3.

def main():
    n1 = float(input("Informe um número: "))
    n2 = float(input("Informe outro número: "))
    print(f"A soma é {soma(n1, n2)}")


def soma(a, b):
    return (a + b)


if __name__ == "__main__":
    main()
