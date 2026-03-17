numbers_list = [ ]

while True:
    try:
        number = float(input("Enter number: "))
        numbers_list.append(number)
    except ValueError:
        numbers_list.sort(reverse=True)
        print(f"Invalid Input. Here's the highest to lowest number inputs: ", numbers_list)
        break