# 43 - Leia o primeiro termo e a razão de uma PA.
# Depois, mostre os 20 primeiros termos.

primeiro_termo = int(input("Informe o primeiro termo da PA: "))
razao = int(input("Informe a razão da PA "))
termo = primeiro_termo
PA = [primeiro_termo]

for r in range(19):
    termo += razao
    PA.append(termo)

print(PA)
print(len(PA))
