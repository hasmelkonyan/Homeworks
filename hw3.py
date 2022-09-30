import random


def input_sum():
    sum = 0
    for i in range(5):
        num = input("Input any number: ")
        if num.isnumeric():
            sum += float(num)
        else:
            print("Invalid input!")
            return input_sum()
    return sum


def is_valid_phone_number():
    phone_number = input("Enter a phone number: ")
    lst = phone_number.split("-")
    for each in lst:
        if not each.isnumeric():
            print("Invalid")
            return
    if len(lst) == 3 and len(lst[0]) == 3 and len(lst[1]) == 3 and len(lst[2]) == 4:
        print("Valid")
    elif len(lst) == 4 and lst[0] == "1" and len(lst[1]) == 3 and len(lst[2]) == 3 and len(lst[3]) == 4:
        print("Valid")
    else:
        print("Invalid")


# Use a list comprehension to produce a list that consists of all palindromic numbers between 100 and 1000.
def is_pal(num):
    if num == int(str(num)[::-1]):
        return True
    return False


def pal_numbers():
    return [num for num in range(100, 1000) if is_pal(num)]


def product_names_and_prices():
    products = {}
    while True:
        product = input("New product name: ")
        if product == "":
            while True:
                product_name = input("Input product name: ")
                if product_name in products.keys():
                    print(f"{product_name}: {products[product_name]}")
                else:
                    print("There is no such product!")
                if product_name == "":
                    break
            break
        price = input("Product's price: ")
        products[product] = price


def dict_parse(lst):
    print([each["name"] for each in lst if each["phone"][-1] == "8"], "phone number ends in an 8")
    print([each["name"] for each in lst if each["email"] == ""], "don’t have an email address listed")


di = [{'name': 'Todd', 'phone': '555-1414', 'email': 'todd@mail.net'},
      {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
      {'name': 'Princess', 'phone': '555-3141', 'email': ''},
      {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@mail.net'}]


def dct_from_lst():
    dct = {}
    lst = [[random.randint(1, 5) for i in range(5)] for j in range(5)]
    print(f"We have a list:\n{lst}")
    for each in lst:
        for i in each:
            if i not in dct.keys():
                dct[i] = 1
            else:
                dct[i] += 1
    print(f"There is a dictionary, whose keys are the numbers and whose values are the how many times the number "
          f"occurs:\n{dct}")
    sorted_lst = sorted(dct.items(), key=lambda t: t[1])
    print(f"Three most common numbers are:\n{sorted_lst[-1][0]} - {sorted_lst[-1][1]} times\n"
          f"{sorted_lst[-2][0]} - {sorted_lst[-2][1]} times\n{sorted_lst[-3][0]} - {sorted_lst[-3][1]} times")



dct_from_lst()
