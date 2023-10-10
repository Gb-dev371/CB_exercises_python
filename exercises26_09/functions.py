import random

def add_name(words):
    name = input("What name do you want to add? ")
    words.append(name)
    with open("list.txt", "a", encoding="utf-8") as write_word:
        write_word.write("\n"+name)

def remove_name(words):
    name = input("What name do you want to remove? ")

    with open("list.txt", "w") as file_write:
        file_write.write("")

    words.remove(str(name))

    with open("list.txt", "a", encoding="utf-8") as file_append:
        for word in words:
            if(words.index(word) == (len(words)-1)):
                file_append.write(word)
            else:
                file_append.write(word+"\n")



def random_word(words):
    print(f"Palavra selecionada aleatoriamente: {random.choice(words)}")

def separator():
    print("-"*30)

