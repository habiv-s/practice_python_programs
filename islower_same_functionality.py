text = input("Enter a string: ")
is_lower = True

for character in text:
    if 'A' <= character <= 'Z':
        is_lower = False
        break

print(is_lower)