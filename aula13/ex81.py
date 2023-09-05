# 81 - Classe "Círculo":
# Crie uma classe chamada "Círculo" que possua o método __init__
# para inicializar a propriedade "raio" do círculo.
# Em seguida, crie um objeto da classe "Círculo" e calcule e
# imprima a área do círculo.

import math


class Circulo:
    def __init__(self, raio):
        self.raio = raio


def main():
    circulo = Circulo(get_raio())
    area = ((circulo.raio ** 2) * math.pi)
    print(f'Área do círculo: {area:.4f}')


def get_raio():
    return float(input("Informe o valor do raio: "))


if __name__ == "__main__":
    main()
