print("Angelina Masiuk, IT-31")

first_number = float(input("Enter the first number: "))
operation = input("Enter the operation (+, -, *, /, //, %, **): ").strip()
second_number = float(input("Enter the second number: "))

if operation == "+":
    result = first_number + second_number
elif operation == "-":
    result = first_number - second_number
elif operation == "*":
    result = first_number * second_number
elif operation == "/":
    if second_number == 0:
        print("Error: division by zero is not allowed")
    else:
        result = first_number / second_number
elif operation == "//":
    if second_number == 0:
        print("Error: division by zero is not allowed")
    else:
        result = first_number // second_number
elif operation == "%":
    if second_number == 0:
        print("Error: division by zero is not allowed")
    else:
        result = first_number % second_number
elif operation == "**":
    result = first_number ** second_number
else:
    print("Error: unknown operation")
    result = None

if operation in ["+", "-", "*", "/", "//", "%", "**"] and not (
    second_number == 0 and operation in ["/", "//", "%"]
):
    print(f"{first_number} {operation} {second_number} = {result:.4f}")