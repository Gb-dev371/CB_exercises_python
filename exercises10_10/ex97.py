# Crie um programa para rodar "python main.py --nome (nome)" em que o argumento
# seja obrigatório (ou requerido)

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--nome", help= "Name to be digited", required=True)
args = parser.parse_args()

print("Hello, "+ args.nome)