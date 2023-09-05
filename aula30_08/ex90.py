# 90 - Desenvolva uma classe Book com atributos title, author e year. 
# Implemente um método get_age que retorna quantos anos o livro tem desde o ano atual.

from datetime import date
data = date.today()
CURRENT_YEAR = data.year

class Book:
    def __init__(self, title, author, year):
        self.__title = title
        self.__author = author
        self.__year = year

    def get_age(self):
        return CURRENT_YEAR - self.__year
    
    @classmethod
    def get(cls):
        title = input("What is the title of the book? ")
        author = input("What is the name of the author? ")
        while True:
            try:
                year = int(input("What is the publishing year? "))
                if year > CURRENT_YEAR:
                    raise ValueError
            except ValueError:
                print("Invalid year.")
            else:
                break
        return cls(title, author, year)


book1 = Book.get()
print(f"{book1.get_age()} years ago the book was released")
