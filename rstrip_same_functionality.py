user_input = input("Enter anything: ")
index = len(user_input) - 1
while index >= 0  and user_input[index] == " ":
    index -= 1
print("'" + user_input[:index + 1] + "'")