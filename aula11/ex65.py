# 65 - Escreva um programa que leia um valor numérico inteiro do usuário e
# imprima o resultado da raiz quadrada desse valor. Utilize try/except para
# lidar com a possibilidade de o usuário inserir um número negativo.

import math

num = int(input("Informe um número: "))
try:
    print(math.sqrt(num))
except:
    print("Não existe raiz de número negativo.")
