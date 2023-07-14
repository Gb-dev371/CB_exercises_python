birth_year = int(input("Write the year of your birth: "))
current_year = 2023
age = current_year - birth_year

if age < 18:
    print(f"Você precisa se alistar daqui a {18 - age} anos")
elif age == 18:
    print("Você precisa se alistar nesse ano.")
else:
    print(f"Você devia ter se alistado há {age-18} anos")
