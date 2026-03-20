text = input("Enter a string: ")
beginning = input("Enter the beginning: ")

if text[:len(beginning)] == beginning:
    print(f"The string starts with '{beginning}'.")
else:
    print(f"The string does NOT start with '{beginning}'.")