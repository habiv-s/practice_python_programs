numbers_list = [ ]

while True:
    try:
        number = float(input("Enter number: "))
        numbers_list.append(number)
    except ValueError:
        numbers_list.sort()
        print(f"Invalid Input. Here's the lowest to highest number inputs: ", numbers_list)
        break