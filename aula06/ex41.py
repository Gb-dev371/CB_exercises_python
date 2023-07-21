# 41 - Faça uma tabuada

# for i in range(11):
#     print(f"----- Tabuada de {i} -----")
#     for j in range(11):
#         print(f"{i}*{j} = {i*j}")

num = int(input("Você quer fazer a tabuada de qual número? "))

for i in range(1, 11):
    print(f"{num}*{i} = {num*i}")
