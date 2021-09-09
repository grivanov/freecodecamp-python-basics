try:
    test = 10/0
    number = int(input("Enter a number:"))
    print(number)
except ZeroDivisionError as err:
    print(err)
