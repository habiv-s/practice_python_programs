text = input("Enter a string in an incorrect casing: ")
lowercase_text = ""

for character in text:
    if 'A' <= character <= 'Z':
        lowercase_text += chr(ord(character) + 32)
    else:
        lowercase_text += character

print(lowercase_text)