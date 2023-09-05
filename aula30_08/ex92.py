# 92 - Defina uma classe TemperatureConverter com métodos para converter de Celsius para 
# Fahrenheit e vice-versa. Mantenha os atributos e métodos privados.

class TemperatureConverter:
    def __init__(self, name, temperature):
        self.name = name
        self.temperature = temperature

    def converter(self):
        if self.name == "Fahrenheit":
            return ((self.temperature-32)*5)/9
        elif self.name == "Celsius":
            return ((self.temperature*9/5)+32)

    @classmethod
    def get(cls):
        while True:
            name = input("The temperature is in Celsius or Fahrenheit? ").capitalize()
            if name == "Celsius" or name == "Fahrenheit":
                break
            else:
                print("Name invalid")
        
        while True:
            try:
                temperature = int(input("What is the temperature? "))
            except ValueError:
                print("Temperature invalid")
            else:
                break
        return cls(name, temperature)
    
temperature1 = TemperatureConverter.get()
print(f"{temperature1.name} convertido eh: {temperature1.converter()}")
