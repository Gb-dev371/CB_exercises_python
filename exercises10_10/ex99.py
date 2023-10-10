# Crie um script que permita o uso de 3 opções:
# Opções: A (comprimento), B (quantidade de espaços), C (soma dos números)
# Exemplo: "python main.py -o A/B/C -m 'mensagem' "
# Em que a opção A retorne o tamanho/comprimento da mensagem,
# a opção B retorne a quantidade de espaços e a opção C 
# retorne a soma dos números fornecidos

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-o", choices=["A", "B", "C"])
parser.add_argument("-m")
args = parser.parse_args()

choice = args.o
message = args.m
if choice == "A":
    print(f"Comprimento: {len(message)} caracteres")
elif choice == "B":
    print(f"Quantidade de espaços: {message.count(' ')}")
elif choice == "C":
    try:
        numeros = [int(n) for n in message.split()]
    except:
        print("Numbers invalid")
    else:
        print(f"Sum: {sum(numeros)}")
else:
    print("Invalid argument for -o parameter")