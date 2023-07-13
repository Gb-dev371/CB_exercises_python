l1 = int(input("Informe o tamanho do primeiro lado: "))
l2 = int(input("Informe o tamanho do segundo lado: "))
l3 = int(input("Informe o tamanho do terceiro lado: "))

if (((abs(l2 - l3)) < l1 < (l2 + l3)) and ((abs(l1 - l3)) < l2 < (l1 + l3))
        and ((abs(l1 - l2)) < l3 < (l1 + l2))):
    print("É possível formar um triângulo!")
else:
    print("Não é possível formar um triângulo!")
