# 89 - Defina uma classe Car com atributos make, model e year. 
# Crie um método start_engine que imprime uma mensagem indicando que o motor foi iniciado.

class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    def start_engine():
        print("The engine was initialized.")
        