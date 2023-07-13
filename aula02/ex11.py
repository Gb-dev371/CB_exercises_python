# 11 - Faça um programa que leia o preço de um produto
# e retorne o seu preço com 5% de desconto
price = float(input("Informe o preço do produto: "))
price_descounted = price - (price * 0.05)
print(f"O preço com desconto de 5% eh {price_descounted}")
