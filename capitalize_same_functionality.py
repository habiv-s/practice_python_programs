text = input("Enter a string in an incorrect casing: ")
result = ""

for index in range(len(text)):
    if index == 0 and 'a' <= text[index] <= 'z':
        result += chr(ord(text[index]) -32 )

print(text)