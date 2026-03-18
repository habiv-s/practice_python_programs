text = input("Enter a string: ")
is_upper = True

for character in text:
    if 'a' <= character <= 'z':
        is_upper = False
        break

if is_upper:
    print(f"{is_upper}. The string is all uppercase.")
else:
    print(f"{is_upper}. The string is NOT all uppercase.")