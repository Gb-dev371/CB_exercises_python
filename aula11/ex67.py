# 67 - Crie um programa que solicite ao usuário que digite um valor
# numérico inteiro. Em seguida, tente encontrar o fatorial desse número.
# Utilize try/except para tratar a inserção de valores não inteiros e números negativos.

def main():
    num = int(input("Informe um valor: "))
    try:
        print(fat(num))
    except:
        print("Não existe fatorial de números negativos ou não-inteiros")

def fat(n):
    f = 1
    if n < 0:
        raise ValueError
    for i in range(2, n+1):
        f *= i
    return f


main()
