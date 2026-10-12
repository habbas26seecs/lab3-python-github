def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


def check_even_odd(num):
    if num % 2 == 0:
        return f"{num} is Even."
    else:
        return f"{num} is Odd."


def calculate_percentage(part, total):
    if total == 0:
        return "Error: Total cannot be zero for percentage calculation."
    return (part / total) * 100


def main():
    while True:
        print("\n--- Suggested Menu ---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Check Even/Odd")
        print("6. Calculate Percentage")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "7":
            print("Exiting calculator. Goodbye!")
            break

        if choice in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            if choice == "1":
                print(f"Result: {add(num1, num2)}")
            elif choice == "2":
                print(f"Result: {subtract(num1, num2)}")
            elif choice == "3":
                print(f"Result: {multiply(num1, num2)}")
            elif choice == "4":
                print(f"Result: {divide(num1, num2)}")

        elif choice == "5":
            try:
                num = int(input("Enter an integer to check Even/Odd: "))
                print(f"Result: {check_even_odd(num)}")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        elif choice == "6":
            try:
                part = float(input("Enter the part value: "))
                total = float(input("Enter the total value: "))
                print(f"Result: {calculate_percentage(part, total)}%")
            except ValueError:
                print("Invalid input. Please enter numeric values.")

        else:
            print("Invalid choice! Please select a valid option from 1 to 7.")


if __name__ == "__main__":
    main()
