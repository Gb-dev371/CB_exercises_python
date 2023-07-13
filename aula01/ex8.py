# 8 - Faça um programa que leia um número que diga se o número é par ou ímpar

num = int(input("Digite um numero: "))

verifica = "par" * (num % 2 == 0) + "impar" * (num % 2 == 1)

print(f"{num} eh {verifica}")
