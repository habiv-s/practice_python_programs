first_number = float(input("Enter a number: "))
for i in range(9):
    numbers_to_minus = float(input("Enter a number: "))
    first_number -= numbers_to_minus
print(f"The result of the first number minus all of the remaining numbers is", first_number)