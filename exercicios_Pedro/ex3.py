# 3 - Crie uma função que receba uma string como parâmetro e retorne
# uma string invertida. Por exemplo, se a função for chamada de inverter_string,
# chamar inverter_string("olá") deve retornar "álO"

def main():
    print(f'Inversao da String: {inversion_string(input("Digite uma palavra: "))}')


def inversion_string(string):
    return string[::-1]


if __name__ == "__main__":
    main()
