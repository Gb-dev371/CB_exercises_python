# Escreva um programa que permita selecionar um aluno aleatório de um arquivo txt. 
# Permita que o programa adicione um aluno a lista. Permita que o programa remova um aluno da lista.

import random


def add_name():
    name = input("What name do you want to add? ")
    with open("list.txt", "a") as write_word:
        write_word.write("\n"+name)
    words.append(name)

def remove_name():
    name = input("What name do you want to remove? ")
    words.remove(str(name))

def palavra_aleatoria():
    print(f"Palavra selecionada aleatoriamente: {random.choice(words)}")


with open("list.txt", "r") as file:
    completed_text = file.read()
    words = list(completed_text.split())

add_name()
remove_name()
palavra_aleatoria()


file_write = open("list.txt", "w")
file_write.write("")

file_append = open("list.txt", "a")
for word in words:
    file_append.write(word+"\n")

# print(words)


