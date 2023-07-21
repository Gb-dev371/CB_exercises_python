# 34 - Refaça o desafio 035 dos triângulos, acrescentando o recurso de
# mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes

l1 = int(input("Informe o tamanho do primeiro lado: "))
l2 = int(input("Informe o tamanho do segundo lado: "))
l3 = int(input("Informe o tamanho do terceiro lado: "))

if (((abs(l2 - l3)) < l1 < (l2 + l3)) and ((abs(l1 - l3)) < l2 < (l1 + l3))
        and ((abs(l1 - l2)) < l3 < (l1 + l2))):
    print("É possível formar um triângulo!")
    if l1 == l2 == l3:
        print("E esse triângulo é equilátero.")
    elif (l1 == l2 or l1 == l3 or l2 == l3):
        print("E esse triângulo é isósceles.")
    else:
        print("E esse triângulo é escaleno.")
else:
    print("Não é possível formar um triângulo!")
