fullname = input("Enter your fullname in incorrect casing: ")
fixed_lowercase = fullname.lower()
snake_casing = fixed_lowercase.replace(" ", "_")
print(snake_casing)