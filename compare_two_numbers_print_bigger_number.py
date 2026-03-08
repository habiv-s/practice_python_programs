first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

if first_number > second_number:
    print(f"The bigger number is {first_number}.")
elif second_number > first_number:
    print(f"The bigger number is {second_number}.")
else:
    print("The numbers are the same and just equal.")