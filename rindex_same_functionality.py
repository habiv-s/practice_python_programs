text = input("Enter main string: ")
substring = input("Enter substring to find: ")

for i in range(len(text) - len(substring), -1, -1):
    if text[i:i + len(substring)] == substring:
        print(i)
        break
else:
    raise ValueError("Substring not found.")