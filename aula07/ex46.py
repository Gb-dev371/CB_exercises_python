# 46 - Melhore o jogo de advinhação onde o computador "pensa" em um número.
# Mostre quantos palpites o usuário usou.

import random

num_pc = random.randint(0, 5)
num_usuario = int(input("Escolha um numero de 0 a 5: "))
tentativas = 1


def conta_tentativas(t):
    t += 1


while num_usuario != num_pc:
    conta_tentativas(tentativas)
    num_usuario = int(input("Escolha um numero de 0 a 5: "))

if num_usuario == num_pc:
    print(f"Parabéns! Você acertou e tentou {tentativas} vezes.")
