text = input("Enter a string: ")
width = int(input("Enter the total width: "))

spaces_to_add = max(0, width - len(text))

print(text)