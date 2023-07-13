# 18 - Faça um programa que leia o nome de 4 alunos e escreva na
# tela o nome do escolhido para apagar o quadro

import random

st1 = input("Digite o nome do primeiro aluno: ")
st2 = input("Digite o nome do segundo aluno: ")
st3 = input("Digite o nome do terceiro aluno: ")
st4 = input("Digite o nome do quarto aluno: ")

students_list = [st1, st2, st3, st4]

print(random.choice(students_list))
