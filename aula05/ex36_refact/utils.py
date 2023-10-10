def separator():
    print("-"*30)


def get_payment_condition():
    try:
        payment_condition = int((input("Inform how you would like to pay: \n"
                                "Cash/check (choose 1) \n"
                                "Cash on card (choose 2) \n"
                                "Up to 2x on card (choose 3) \n"
                                "3x or more on the card (choose 4) \n")))
        separator()
    except TypeError:
        print("Error! Enter a valid number.")
        get_payment_condition()
    else:
        return payment_condition


def calculate_discount(normal_price, payment_condition):
    if payment_condition == 1:
        new_price = normal_price - normal_price * 0.1
        print(f"You got 10% discount. Now the price is {new_price}R$")
    elif payment_condition == 2:
        new_price = normal_price - normal_price * 0.05
        print(f"You got 5% discount. Now the price is {new_price}R$")
    elif payment_condition == 3:
        print(f"There is no discount for this payment option.."
            f"The price remains the same: {normal_price}R$")
    elif payment_condition == 4:
        new_price = normal_price + normal_price * 0.2
        print(f"This payment option has an interest of 20%."
            f"Now the price is {new_price}R$")