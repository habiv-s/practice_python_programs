text = input("Enter a string: ")
is_upper = True
has_uppercase = False

for character in text:
    if 'A' <= character <= 'Z':
        has_uppercase = True
    if 'a' <= character <= 'z':
        is_upper = False
        break

result = is_upper and has_uppercase

if result:
    print(f"{result}. The string is all uppercase.")
else:
    print(f"{result}. The string is NOT all uppercase.")