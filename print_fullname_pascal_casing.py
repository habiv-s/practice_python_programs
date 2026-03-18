fullname = input("Enter your fullname in incorrect casing: ")
fixed_proper_casing = fullname.title()
pascal_casing = fixed_proper_casing.replace(" ", "")
print(pascal_casing)