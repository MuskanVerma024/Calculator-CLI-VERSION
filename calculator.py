# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b  # Use / instead of // for float result

while True:
    print("\n====== Python CLI Calculator ======")
    print("1 - ADD")
    print("2 - SUBTRACTION")
    print("3 - MULTIPLICATION")
    print("4 - DIVISION")
    print("5 - EXIT")

    try:
        option = int(input("Choose an operation (1-5): "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 5.")
        continue

    if option == 5:
        print("Exiting the calculator. Goodbye!")
        break

    if option in [1, 2, 3, 4]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
            continue

        if option == 1:
            result = add(num1, num2)
        elif option == 2:
            result = subtract(num1, num2)
        elif option == 3:
            result = multiply(num1, num2)
        elif option == 4:
            result = divide(num1, num2)

        print("🧮 Result: {:.2f}".format(result) if isinstance(result, float) else f"🧮 Result: {result}")
    else:
        print("Invalid operation entered. Please try again.")
