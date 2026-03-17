numbers_list = [ ]

while True:
    try:
        number = float(input("Enter number: "))
        numbers_list.append(number)
    except ValueError:
        print("Invalid Input")
        break