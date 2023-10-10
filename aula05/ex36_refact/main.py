# 36 - Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros
from utils import *

def main():
    normal_price = float(input("What is the normal price of the product? "))
    payment_condition = get_payment_condition()
    calculate_discount(normal_price, payment_condition)


if __name__ == "__main__":
    main()
