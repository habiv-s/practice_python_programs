check_odd_numbers = 0
for i in range(10):
    number = int(input("Enter number: "))
    if number % 2 != 0:
        check_odd_numbers += 1
print(f"ODD NUMBERS COUNT: ", check_odd_numbers)