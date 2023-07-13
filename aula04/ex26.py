salary = float(input("Informe o salário: "))

if salary > 1250.0:
    aumento = salary + salary*0.15
    num_aumento = 15
else:
    aumento = salary + salary*0.10
    num_aumento = 10

print(f"Você ganhou um aumento de {num_aumento}%."
      f"Seu salário agora é {aumento}R$.")
