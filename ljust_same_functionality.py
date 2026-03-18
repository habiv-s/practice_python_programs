text = input("Enter a string: ")
width = int(input("Enter the total width: "))

spaces_to_add = max(0, width - len(text))
result = text + (" " * spaces_to_add)

print(f"Result: '{result}'")