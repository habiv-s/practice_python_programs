text = input("Enter main string: ")
substring = input("Enter substring to count: ")

count = 0
substring_length = len(substring)

for i in range(len(text) - substring_length + 1):
    if text[i:i + substring_length] == substring:
        count += 1

print(count)