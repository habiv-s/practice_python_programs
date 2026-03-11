numbers_list = [ ]
duplicate_numbers_list = [ ]

for i in range(10):
    number = float(input("Enter number: "))
    numbers_list.append(number)

for number in numbers_list:
    if numbers_list.count(number) != 1:
        duplicate_numbers_list.append(number)

print(duplicate_numbers_list)