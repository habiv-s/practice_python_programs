numbers_list = [ ]
unique_numbers_list = [ ]

for i in range(10):
    number = float(input("Enter number: "))
    numbers_list.append(number)

for number in numbers_list:
    if numbers_list.count(number) == 1:
        unique_numbers_list.append(number)

print(unique_numbers_list)