print("=" * 10)
print("     MATHEMATICAL CALCULATOR    ")
print("=" * 10)

while True:

    print()
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Floor Division (//)")
    print("6. Power (^)")
    print("7. Modulus (%)")
    print("8. Clear")
    print("9. OFF")

    choice = int(input("Enter your choice (1-9): "))

    match choice:

        case 1:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Answer =", a + b)

        case 2:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Answer =", a - b)

        case 3:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Answer =", a * b)

        case 4:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if b == 0:
                print("Error! Division by zero is not allowed.")
            else:
                print("Answer =", a / b)

        case 5:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))

            if b == 0:
                print("Error! Division by zero is not allowed.")
            else:
                print("Answer =", a // b)

        case 6:
            a = float(input("Enter the base: "))
            b = float(input("Enter the exponent: "))
            print("Answer =", a ** b)

        case 7:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))

            if b == 0:
                print("Error! Modulus by zero is not allowed.")
            else:
                print("Answer =", a % b)

        case 8:
            print("\n" * 15)
            print("Calculator Cleared.")

        case 9:
            print("Calculator OFF.")
            break

        case _:
            print("Invalid choice! Please select a number between 1 and 9.")