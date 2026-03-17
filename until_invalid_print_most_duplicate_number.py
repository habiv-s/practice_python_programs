numbers_list = [ ]

while True:
    try:
        number = float(input("Enter number: "))
        numbers_list.append(number)
    except ValueError:
        most_duplicate = max(numbers_list, key=numbers_list.count)
        print(f"Invalid Input. The number with the most duplicates is {most_duplicate}")
        break