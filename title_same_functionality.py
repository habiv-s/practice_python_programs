text = input("Enter a string in an incorrect casing: ")
result = ""
new_word = True

for character in text:
    if character == " ":
        result += " "
        new_word = True
    elif new_word:
        if 'a' <= character <= 'z':
            result += chr(ord(character) - 32)
        else:
            result += character
        new_word = False
        
print(text)