text = input("Enter a string: ")
is_lower = True
has_lowercase = False

for character in text:
    if 'a' <= character <= 'z':
        has_lowercase = True
    elif 'A' <= character <= 'Z':
        is_lower = False
        break

result = is_lower and has_lowercase

if result:
    print(f"{result}. The string is all lowercase.")
else:
    print(f"{result}. The string is NOT all lowercase.")