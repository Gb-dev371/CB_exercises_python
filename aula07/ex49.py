# 49 - Refaça o desafio da PA mostrando os 20 primeiros termos e pergunte
# ao usuário quantos termos a mais ele quer ver o programa encerra quando
# disser que quer mostrar 0 termos.

primeiro_termo = int(input("Informe o primeiro termo da PA: "))
razao = int(input("Informe a razão da PA "))
termo = primeiro_termo
PA = [primeiro_termo]

for r in range(9):
    termo += razao
    PA.append(termo)

termos_adicionais = int(input("Quantos termos a mais você quer ver?"))
while termos_adicionais > 0:
    for t in range(0, termos_adicionais):
        termo += razao
    termos_adicionais = int(input("Quantos termos a mais você quer ver?"))

print(PA)
print(len(PA))
