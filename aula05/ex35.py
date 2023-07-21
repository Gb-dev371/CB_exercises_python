# 35 - Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu índice de Massa Corporal (IMC) e mostre seu status,
# de acordo com a tabela abaixo:
# IMC abaixo de 18,5: Abaixo do peso
# Entre 18,5 e 25: Peso Ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida

weight = float(input("How much do you weight? "))
height = float(input("How tall are you? "))
IMC = weight / height ** 2

if IMC < 18.5:
    print(f"{IMC}: Underweight")
elif 18.5 <= IMC <= 25:
    print("{:.2f}: Normal weight".format(IMC))
elif 25 < IMC <= 30:
    print("{:.2f}: Overweight".format(IMC))
elif 30 < IMC <= 40:
    print("{:.2f}: Obesity".format(IMC))
else:
    print("{:.2f}: Morbid obesity".format(IMC))
