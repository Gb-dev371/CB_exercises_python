height_Wall = float(input("Informe a altura da parede: "))
weight_Wall = float(input("Informe a largura da parede: "))
area_Wall = (height_Wall * weight_Wall)
litros = area_Wall/2
print(f"A area da parede eh {area_Wall}m2 "
      f"e sera necessario {litros} litros para pintar a parede")
