text = input("Enter a string: ")
width = int(input("Enter the total width: "))

spaces_to_add = max(0, width - len(text))
left_space = spaces_to_add // 2
right_space = spaces_to_add - left_space

print(f"'", " " * left_space + text + " " * right_space, "'")