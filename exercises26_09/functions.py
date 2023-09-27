import random

def add_name(words):
    name = input("What name do you want to add? ")
    with open("list.txt", "a") as write_word:
        write_word.write("\n"+name)
    words.append(name)

def remove_name(words):
    name = input("What name do you want to remove? ")

    with open("list.txt", "w") as file_write:
        file_write.write("")

    with open("list.txt", "a") as file_append:
        for word in words:
            file_append.write(word+"\n")

    words.remove(str(name))

def random_word(words):
    print(f"Palavra selecionada aleatoriamente: {random.choice(words)}")

def separator():
    print("-"*30)

