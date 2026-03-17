numbers_list = [ ]

while True:
    try:
        number = float(input("Enter number: "))
        numbers_list.append(number)
    except ValueError:
        if numbers_list:
            max_count = max(numbers_list.count(numbers) for numbers in numbers_list)

            most_duplicates = []
            for numbers in numbers_list:
                if numbers_list.count(numbers) == max_count and numbers not in most_duplicates:
                    most_duplicates.append(numbers)

            print(f"Invalid Input. Number(s) with the most duplicates: {most_duplicates}")
        else:
            print("Invalid Input. No valid numbers were entered.")
        break