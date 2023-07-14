num = int(input("Write a number: "))
base = int(input("Do you would like to convert the number to which base:"
                 "binary, octal or hexadecimal? (1, 2 or 3): "))

if base == 1:
    print(f"{num} converted to the binary base is {bin(num)[2:]}")
elif base == 2:
    print(f"{num} converted to the octadecimal base is {oct(num)[2:]}")
elif base == 3:
    print(f"{num} converted to the hexadecimal base is {hex(num)[2:]}")
else:
    print("Probally you made something wrong.")
