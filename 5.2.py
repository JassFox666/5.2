def calculator():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("Error: Cannot divide by zero.")
                    continue
                result = num1 / num2
            else:
                print("Invalid operator. Please enter +, -, *, or /.")
                continue

            print(f"Result: {result}")

        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        continue_calc = input("Do you want to perform another calculation? (yes/y to continue): ").strip().lower()
        if continue_calc not in ('yes', 'y'):
            print("Exiting calculator. Goodbye!")
            break


calculator()