text = input("Enter main string: ")
substring = input("Enter substring to count: ")
count = 0

for i in range(len(text) - len(substring) + 1):
    if text[i:i + len(substring)] == substring:
        count += 1

print(count)