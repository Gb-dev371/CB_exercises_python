# 88 - Crie uma classe Student com atributos name, age e grades (uma lista). 
# Adicione métodos para adicionar notas, calcular a média das notas e exibir as informações do aluno.

class Student:
    def __init__(self, name:str, age:int, grades:list = []):
        self.__name = name
        self.__age = age
        self.__grades = grades

    def add_grades(self):
        try:  # Tratando o possível erro do usuário digitar um dado não-inteiro
            quantity_of_grades = int(input("How many grades do you want to add? "))
            if quantity_of_grades <= 0:
                print("You cannot add this quantity of grades")
            else:
                for i in range(quantity_of_grades):
                    grade = float(input(f"What is the grade {i+1}? "))
                    self.__grades.append(grade)
        except ValueError:
            print("Invalid value.")

    def average_grades(self):
        average_grades = ((sum(self.__grades)) / (len(self.__grades)))
        return average_grades
    
    def show_attributes(self):
        print(f"Name: {self.__name}, age: {self.__age}, grades: {self.__grades}")

    
    @classmethod
    def get(cls):
        name = input("What is the name of the student? ")
        age = int(input("How old is the student? "))
        return cls(name, age)
    
student1 = Student.get()
student1.add_grades()
print(f"Average of grades: {student1.average_grades()}")
student1.show_attributes()

        