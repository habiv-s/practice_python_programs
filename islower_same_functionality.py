text = input("Enter a string: ")
is_lower = True

for character in text:
    if 'A' <= character <= 'Z':
        is_lower = False
        break

if is_lower:
    print(f"{is_lower}. The string is all lowercase.")
else:
    print(f"{is_lower}. The string is NOT all lowercase.")