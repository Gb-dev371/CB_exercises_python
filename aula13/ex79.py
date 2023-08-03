# 79 - Classe "Retângulo":
# Crie uma classe chamada "Retângulo" que possua o método
# __init__ para inicializar as propriedades "largura" e "altura"
# do retângulo. Em seguida, crie um objeto da classe "Retângulo"
# e calcule e imprima a área do retângulo.

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura


largura = float(input("Informe o tamanho da largura: "))
altura = float(input("Informe o tamanho da altura: "))

retangulo = Retangulo(largura, altura)

area = retangulo.largura * retangulo.altura

print(f"A área do retângulo é {area}")
