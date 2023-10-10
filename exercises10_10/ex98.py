# Faça um script que permita o uso de 2 argparsers ("age", "city").
# Se for passado idade/cidade, então printe na tela o valor. Se não,
# printe "Nenhuma mensagem fornecida"

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--age")
parser.add_argument("--city")
args = parser.parse_args()

if(args.age != None and args.city != None):
    print(f"Age: {args.age}\n"+
          f"City: {args.city}")
else:
    print("Age or city was not digited")