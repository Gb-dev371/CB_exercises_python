# 48 - Mostre o fatorial de um número enviado
# pelo usuário (ex: 5x4x3x2x1) = 120

num = int(input("Informe um número: "))

def main():
    if num < 0:
        print("Não existe fatorial de número negativo!")
    elif num == 0:
        print("O fatorial é 1")
    else:
        print(f"O fatorial de {num} é {calcula_fatorial(num)}")

def calcula_fatorial(x):
    fatorial = 1
    for i in range(2, x+1):
        fatorial = fatorial * i
    return fatorial

main()
