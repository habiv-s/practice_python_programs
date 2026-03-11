while True:
    try:
        number = float(input("Enter number: "))
    except ValueError:
        print("Invalid Input")
        break