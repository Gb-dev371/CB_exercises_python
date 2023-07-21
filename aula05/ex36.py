# 36 - Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

normal_price = float(input("What is the normal price of the product? "))
payment_condition = int((input("Inform how you would like to pay: \n"
                               "À vista no dinheiro/cheque (escolha 1) \n"
                               "À vista no cartão (escolha 2) \n"
                               "Até 2x no cartão (escolha 3) \n"
                               "3x ou mais no cartão (escolha 4) \n")))

if payment_condition == 1:
    new_price = normal_price - normal_price * 0.1
    print(f"Você ganhou 10% de desconto. Agora o preço é {new_price}R$")
elif payment_condition == 2:
    new_price = normal_price - normal_price * 0.05
    print(f"Você ganhou 5% de desconto. Agora o preço é {new_price}R$")
elif payment_condition == 3:
    print(f"Para essa opção de pagamento não há desconto."
          f"O preço continua o mesmo: {normal_price}R$")
elif payment_condition == 4:
    new_price = normal_price + normal_price * 0.2
    print(f"Para essa opção de pagamento tem um juros de 20%."
          f"Agora o preço é {new_price}R$")
