text = input("Enter a string in an incorrect casing: ")
result = ""
new_word = True

for character in text:
    if character == " ":
        result += " "
        new_word = True

print(text)