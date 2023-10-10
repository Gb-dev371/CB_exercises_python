from tkinter import *
import tkinter as tk
from random import choice

with open("list.txt", "r") as file:
    completed_text = file.read()
    words = list(completed_text.split("\n"))


def add_name():
    name = add_entry.get()
    print("Nome a ser adicionado ",name)
    words.append(name)
    with open("list.txt", "a", encoding="utf-8") as write_word:
        if(len(words) == 2):  # the reason for two is that when the file is empty, the first line is considered as a value. So we have this first value and the name that we have just added
            write_word.write(words[1])
        else:
            write_word.write("\n"+name)
    add_entry.delete(0, tk.END)

def remove_name():
    name = remove_entry.get()
    print("Nome a ser removido: ",name)


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


    remove_entry.delete(0, tk.END)

def random_name():
    label_random.configure(text="Name: "+(choice(words)))


window = tk.Tk() 

    
window.title('Names project') 

window.geometry("700x200") 

window.config(background = "white") 


label_file_explorer = Label(window,  
                            text = "Names project using Tkinter", 
                            width = 100, height = 4,  
                            fg = "blue") 
label_file_explorer.pack()

    
button_add = tk.Button(window,  
                        text = "Add name",
                        command = add_name)
button_add.pack()

add_entry = tk.Entry(window)
add_entry.pack()
                         

button_remove = Button(window,  
                    text = "Remove a name", 
                    command = remove_name) 
button_remove.pack()

remove_entry = tk.Entry(window)
remove_entry.pack()


button_random = Button(window,  
                        text = "Random name", 
                        command = random_name) 
button_random.pack()

label_random = Label(window,  
                            text = "Name:", 
                            width = 100, height = 4,  
                            fg = "blue") 
label_random.pack()


window.mainloop() 