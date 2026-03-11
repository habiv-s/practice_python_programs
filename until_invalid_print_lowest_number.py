numbers_list = [ ]

while True:
    try:
        number = float(input("Enter number: "))
        numbers_list.append(number)
    except ValueError:
        if numbers_list:
            print(f"Invalid Input. The lowest number among all inputs is ", min(numbers_list))
        else:
            print("Invalid Input. No valid numbers were entered.")
        break