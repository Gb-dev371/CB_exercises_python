# 16 - Leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo. Calcule e mostre o comprimento da
# hipotenusa.

import math
num_co = float(input("Informe o comprimento do cateto oposto: "))
num_ca = float(input("Informe o comprimento do cateto adjacente: "))
hipotenusa = (math.hypot(num_co, num_ca))
print(f"O valor da hipotenusa eh {hipotenusa}")
