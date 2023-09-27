# Escreva um programa que permita selecionar um aluno aleatório de um arquivo txt. 
# Permita que o programa adicione um aluno a lista. Permita que o programa remova um aluno da lista.

from functions import *

def main():
    with open("list.txt", "r") as file:
        completed_text = file.read()
        words = list(completed_text.split())
    
    user_choice(words)
    separator()


def user_choice(words):
    while(True):
        choose = input("What do you want to do?\n1 - To return a random word from the file\n2 - To add a name\n3 - To remove a name\n4 - To exit\n")
        if(choose == "1"):
            random_word(words)
            separator()
        elif(choose == "2"):
            add_name(words)
            separator()
        elif(choose == "3"):
            remove_name(words)
            separator()
        elif(choose == "4"):
            print("Bye bye!")
            break
        else:
            print("Invalid answer")

if __name__ == "__main__":
    main()



