text = input("Enter a string: ")
ending = input("Enter the ending: ")

if text[-len(ending):] == ending:
    print(f"The string ends with '{ending}'.")
else:
    print(f"The string does NOT end with '{ending}'.")