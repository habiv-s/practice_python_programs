text = input("Enter a string in an incorrect casing: ")
uppercase_text = ""

for character in text:
    if 'a' <= character <= 'z':
        uppercase_text += chr(ord(character) - 32)
    else:
        uppercase_text += character

print(uppercase_text)