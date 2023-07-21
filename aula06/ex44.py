num = int(input("Escolha um número: "))
for x in range(2, num):
    if (num % x == 0):
        print("{} não é um número primo!".format(num))
        break
else:
    print("{} é um número primo!".format(num))
