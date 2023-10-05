from random import choice

def add_name(words, name):
    print("Nome a ser adicionado ",name)
    words.append(name)
    with open("list.txt", "a", encoding="utf-8") as write_word:
        if(len(words) == 2):  # the reason for two is that when the file is empty, the first line is considered as a value. So we have this first value and the name that we have just added
            write_word.write(words[1])
        else:
            write_word.write("\n"+name)

def remove_name(words, name):
    print(name)
    words.remove(str(name))
    with open("list.txt", "w", encoding="utf-8") as file_write:
        file_write.write("")

    with open("list.txt", "a") as file_append:
        for name in words:
            if name == words[0]:
                continue
            elif name == words[len(words)-1]:
                file_append.write(name)
            else:
                file_append.write(name+"\n")

def get_random_name(words):
    return choice(words)