numbers_list = [ ]

for i in range(10):
    number = float(input("Enter number: "))
    if number not in numbers_list:
        numbers_list.append(number)

print(numbers_list)