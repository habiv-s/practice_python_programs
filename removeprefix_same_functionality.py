text = input("Enter a string: ")
prefix = input("Enter the prefix to remove: ")

if text[:len(prefix)] == prefix:
    print(text[len(prefix):])