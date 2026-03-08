check_even_numbers = 0
for i in range(10):
    number = int(input("Enter number: "))
    if number % 2 == 0:
        check_even_numbers += 1
print(f"EVEN NUMBERS COUNT: ", check_even_numbers)