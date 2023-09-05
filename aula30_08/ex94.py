# Crie uma classe Shape com um método abstrato calculate_area. Em seguida, defina classes derivadas Circle e Triangle que herdam de Shape e 
# implementam esse método para calcular suas respectivas áreas.

class Shape:
    def __init__(self, color):
        self.color = color

    def display_color(self):
        print(f"This shape is {self.color}.")

    @abstractmethod
    def calculate_area(self):
        print("Implementação do método abstrato")


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2



class Triangle(Shape):
    def __init__(self, color, base, height):
        super().__init__(color)
        self.base = base
        self.height = height

    def area(self):
        return ((self.base * self.height) / 2)


# Create instances of Circle and Triangle
circle = Circle("red", 5)
triangle = Triangle("blue", 10, 5)
print(f"Área do círculo: {circle.area()}")
print(f"Área do triângulo: {triangle.area()}")
