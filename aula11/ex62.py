# 62 - Crie uma função chamada "divide_numbers" que recebe dois parâmetros
# numéricos (a e b) e retorna a divisão de a por b. Utilize try/except para
# tratar a divisão por zero.


def main():
    num1 = float(input("Informe um número: "))
    num2 = float(input("Informe outro número: "))
    print(f"A divisão de {num1} por {num2} é {divide_numbers(num1, num2)}")


def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Não é possível realizar essa operação.")


main()
