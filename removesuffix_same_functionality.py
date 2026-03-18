text = input("Enter a string: ")
suffix = input("Enter the suffix to remove: ")

if text[-len(suffix):] == suffix:
    print(text[:-len(suffix)])