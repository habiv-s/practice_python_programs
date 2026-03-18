text = input("Enter a string: ")
is_upper = True

for character in text:
    if 'a' <= character <= 'z':
        is_upper = False
        break

print(is_upper)