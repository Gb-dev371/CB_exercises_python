import tkinter as tk
from general_functions import *

with open("list.txt", "r") as file:
    completed_text = file.read()
    words = list(completed_text.split("\n"))

def on_add_button_click():
    name = add_entry.get()
    add_name(words, name)
    add_entry.delete(0, tk.END)

def on_remove_button_click():
    name = remove_entry.get()
    remove_name(words, name)
    remove_entry.delete(0, tk.END)

def on_random_button_click():
    random_name = get_random_name(words)
    random_label.configure(text="Name: " + random_name)

def create_interface():
    global add_entry, remove_entry, general_label, random_label  # Declarando as variáveis como globais

    window = tk.Tk()

    add_entry = tk.Entry(window)
    add_entry.grid(column=3, row=2)

    remove_entry = tk.Entry(window)
    remove_entry.grid(column=3, row=4)

    general_label = tk.Label(window,
                                  text="Names project using Tkinter",
                                  width=100, height=4,
                                  fg="blue")
    general_label.grid(column=3, row=0)

    button_add = tk.Button(window,
                           text="Add name",
                           command=on_add_button_click)
    button_add.grid(column=3, row=1)

    button_remove = tk.Button(window,
                              text="Remove a name",
                              command=on_remove_button_click)
    button_remove.grid(column=3, row=3)

    button_random = tk.Button(window,
                              text="Random name",
                              command=on_random_button_click)
    button_random.grid(column=3, row=5)

    random_label = tk.Label(window,
                                  text="Name:",
                                  width=100, height=2,
                                  fg="blue")
    random_label.grid(column=3, row=6)

    window.mainloop()