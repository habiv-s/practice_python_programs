numbers_list = [ ]

while True:
    try:
        number = float(input("Enter number: "))
        numbers_list.append(number)
    except ValueError:
        numbers_list.sort()
        print("Invalid Input", numbers_list)
        break