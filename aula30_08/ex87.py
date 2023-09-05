# 87 - Desenvolva uma classe Rectangle com atributos width e height. Implemente um método calculate_area para 
# calcular e retornar a área do retângulo.

class Rectangle:
    def __init__(self, width:float, height:float):
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        return self.width * self.height
    
    @classmethod
    def get(cls):
        width = float(input("What is the value of the width? "))
        height = float(input("What is the value of the height? "))
        return cls(width, height)
    
rectangle1 = Rectangle.get()
print(f"The area is: {rectangle1.calculate_area()} u.a")