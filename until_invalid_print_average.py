numbers_list = [ ]

while True:
    try:
        number = float(input("Enter number: "))
        numbers_list.append(number)
    except ValueError:
        average = sum(numbers_list) / len(numbers_list)
        print(f"Invalid Input. The average is: {average}")
        break