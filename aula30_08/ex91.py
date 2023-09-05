# 91 - Crie uma classe Employee com atributos name, position e salary. Adicione um método apply_raise 
# que aumenta o salário do funcionário em uma determinada porcentagem.

class Employee:
    def __init__(self, name, position, salary):
        self.__name = name
        self.__position = position
        self.__salary = salary

    def apply_raise(self):
        percent = float(input("The salary will be increased by how many percent? "))
        self.__salary = (self.__salary + (self.__salary * percent/100))
        print(f"The salary now is {self.__salary}")

    def show_attributes(self):
        print(f"Name: {self.__name}, position: {self.__position}, salary: {self.__salary}")

    @classmethod
    def get(cls):
        name = input("What is the name of the employee? ")
        position = input("What is the employee position? ")
        salary = float(input("What is the salary of the employee? "))
        return cls(name, position, salary)
    
employee1 = Employee.get()
employee1.apply_raise()
employee1.show_attributes()