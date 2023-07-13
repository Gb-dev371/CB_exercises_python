# Exercício 14 - Faça um programa que leia a quantidade de
# dias e km rodados por um carro alugado, depois calcule o valor do contrato
# sabendo que cada dia custa 60 reais e cada km custa 15 centavos
days = int(input("Por quantos dias voce dirigiu?"))
km = float(input("Quantos kilometros voce rodou"))
valor_contrato = days*60 + km*0.15
print(f"O valor do contrato eh {valor_contrato}R$")
