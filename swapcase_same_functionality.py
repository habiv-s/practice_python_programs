text = input("Enter a string in an incorrect casing: ")
swap_casing_text = ""

for character in text:
    if 'A' <= character <= 'Z':
        swap_casing_text += chr(ord(character) + 32)
    elif 'a' <= character <= 'z':
        swap_casing_text += chr(ord(character) - 32)
    else:
        swap_casing_text += character

print(swap_casing_text)