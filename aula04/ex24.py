km = int(input("Informe a distância em km de uma viagem: "))

if km <= 200:
    preco_por_km = float((0.50*km))
else:
    preco_por_km = float((0.45*km))

print(f"O preço total é {preco_por_km}")
