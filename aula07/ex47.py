num1 = int(input("Escolha um número: "))
num2 = int(input("Escolha outro número: "))
operacao = input("Qual operação você quer fazer? Somar, subtrair, dividir ou multiplicar [S, s, d ou m]?")

def main():
    if operacao == "S":
        print(f"O valor da soma é {somar(num1, num2)} ")
    elif operacao == "s":
        print(f"O valor da subtração é {subtrair(num1, num2)} ")
    elif operacao == "d":
        print(f"O valor da divisão é {dividir(num1, num2)} ")
    elif operacao == "m":
        print(f"O valor da multiplicação é {multiplicar(num1, num2)} ")

# Funções para as operações
def somar(a, b):
    return a+b

def subtrair(a, b):
    return a-b

def dividir(a, b):
    return a/b

def multiplicar(a, b):
    return a*b

main()