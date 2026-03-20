text = input("Enter a string: ")
width = int(input("Enter the total width: "))

zeros_to_add = max(0, width - len(text))
result = ("0" * zeros_to_add) + text

print(f"Result: '{result}'")