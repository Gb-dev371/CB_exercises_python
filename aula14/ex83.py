# 83 - Crie uma classe de "Estudante". A classe deve conter os atributos "name", "age" e "grade".
# Depois, instancie um objeto a esta classe e por fim crie um método para printar na tela esses atributos criados.

class Student:
    def __init__(self, name:str, age:int, grade:float):
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self) -> str:
        return f"Nome: {self.name}, age: {self.age}, grade: {self.grade}"
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        age = int(input("Age: "))
        grade = float(input("Grade: "))
        return cls(name, age, grade)

std1 = Student.get()
print(std1)
