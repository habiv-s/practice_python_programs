numbers_list = [ ]

while True:
    try:
        number = float(input("Enter number: "))
        if number not in numbers_list:
            numbers_list.append(number)
            print("Unique")
        else:
            numbers_list.append(number)
            print("Duplicate")
    except ValueError:
        print("Invalid Input")
        break