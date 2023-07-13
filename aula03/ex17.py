# 17 - Leia um ângulo qualquer e mostre na tela o valor do
# seno, cosseno e tangente desse ângulo
import math
ang = float(input("Informe o valor do ângulo: "))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print(sen)
print(cos)
print(tan)

# print(round(sen, 2))
# print(round(cos, 2))
# print(round(tan, 2))
