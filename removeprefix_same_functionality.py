text = input("Enter a string: ")
prefix = input("Enter the prefix to remove: ")

if len(text) >= len(prefix) and text[:len(prefix)] == prefix:
    print(text[len(prefix):])
else:
    print(text)