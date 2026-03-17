numbers_list = [ ]

while True:
    try:
        number = float(input("Enter number: "))
        numbers_list.append(number)
    except ValueError:
        print(f"Invalid Input. The highest number among all inputs is ", max(numbers_list))
        break