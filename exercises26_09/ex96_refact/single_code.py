import tkinter as tk
from random import choice

with open("list.txt", "r") as file:
    completed_text = file.read()
    words = list(completed_text.split("\n"))

def add_name():
    name = add_entry.get()
    print("Nome a ser adicionado: ", name)
    words.append(name)
    with open("list.txt", "a", encoding="utf-8") as write_word:
        if(len(words) == 2):  # the reason for two is that when the file is empty, the first line is considered as a value. So we have this first value and the name that we have just added
            write_word.write(words[1]+"\n")
            words.remove(words[0])
        else:
            write_word.write("\n"+name)

def remove_name():
    name = remove_entry.get()
    print("Nome a ser removido: ", name)

    words.remove(str(name))

    with open("list.txt", "w", encoding="utf-8") as file_write:
        file_write.write("\n".join(words))

def random_name():
    label_file_explorer.configure(text="Random name: "+ choice(words))

window = tk.Tk() 

add_entry = tk.Entry(window)
add_entry.grid(column=3, row=2)

remove_entry = tk.Entry(window)
remove_entry.grid(column=3, row=4)
    
window.title('Names project') 
window.geometry("700x200") 
window.config(background = "white") 

label_file_explorer = tk.Label(window,  
                            text = "Names project using Tkinter", 
                            width = 100, height = 4,  
                            fg = "blue")
label_file_explorer.grid(column = 3, row = 0) 
    
button_add = tk.Button(window,  
                        text = "Add name",
                        command = add_name)
button_add.grid(column = 3, row = 1)
                     
button_remove = tk.Button(window,  
                    text = "Remove a name", 
                    command = remove_name) 
button_remove.grid(column = 3, row = 3)

button_random = tk.Button(window,  
                        text = "Random name", 
                        command = random_name)
button_random.grid(column = 3,row = 5) 

window.mainloop() 