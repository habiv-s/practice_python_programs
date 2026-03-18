text = input("Enter a string: ")
suffix = input("Enter the suffix to remove: ")

if len(text) >= len(suffix) and text[-len(suffix):] == suffix:
    print(text[:-len(suffix)])
else:
    print(text)