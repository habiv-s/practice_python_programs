user_input = input("Enter anything: ")
index = 0
while index < len(user_input) and user_input[index] == " ":
    index += 1
print(user_input[index:])