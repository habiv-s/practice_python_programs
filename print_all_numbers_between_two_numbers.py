first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

if first_number < second_number:
    for i in range(first_number+1, second_number):
        print(i, end=" ")
elif second_number < first_number:
    for i in range(second_number+1, first_number):
        print(i, end=" ")
else:
    print("The numbers you entered are just the same, so it does not have numbers in between.")