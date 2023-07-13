# 19 - Agora, sorteie uma ordem aleatória de 4 alunos.
# Leia o nome dos alunos e mostre a ordem aleatória.

import random

st1 = input("Digite o nome do primeiro aluno: ")
st2 = input("Digite o nome do segundo aluno: ")
st3 = input("Digite o nome do terceiro aluno: ")
st4 = input("Digite o nome do quarto aluno: ")
students_list = [st1, st2, st3, st4]
random.shuffle(students_list)
print(students_list)
