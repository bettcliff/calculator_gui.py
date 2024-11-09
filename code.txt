def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """Subtract two numbers"""
    return x - y

def multiply(x, y):
    """Multiply two numbers"""
    return x * y

def divide(x, y):
    """Divide two numbers"""
    try:
        return x / y
    except ZeroDivisionError:
        return "Error! Division by zero."

def power(x, y):
    """Calculate x raised to power y"""
    return x ** y

def calculate():
    """Main calculator function"""
    # Display operations menu
    operations = {
        '1': ('Add', add),
        '2': ('Subtract', subtract),
        '3': ('Multiply', multiply),
        '4': ('Divide', divide),
        '5': ('Power', power)
    }
    
    while True:
        print("\n=== Simple Calculator ===")
        print("Select operation:")
        for key, (operation_name, _) in operations.items():
            print(f"{key}. {operation_name}")
        print("q. Quit")

        # Get user choice
        choice = input("\nEnter choice (1/2/3/4/5 or q to quit): ").lower()

        # Check if user wants to quit
        if choice == 'q':
            print("Thanks for using the calculator!")
            break

        # Validate the choice
        if choice not in operations:
            print("Invalid choice! Please select a valid operation.")
            continue

        # Get input numbers
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        # Perform calculation
        operation_name, operation_function = operations[choice]
        result = operation_function(num1, num2)

        # Display result
        print(f"\n{operation_name} Result: {num1} {get_operator(choice)} {num2} = {result}")
        
        # Ask if user wants to perform another calculation
        again = input("\nDo you want to perform another calculation? (y/n): ").lower()
        if again != 'y':
            print("Thanks for using the calculator!")
            break

def get_operator(choice):
    """Return the operator symbol for the selected operation"""
    operators = {
        '1': '+',
        '2': '-',
        '3': '×',
        '4': '÷',
        '5': '^'
    }
    return operators.get(choice, '')

if __name__ == "__main__":
    try:
        calculate()
    except KeyboardInterrupt:
        print("\nCalculator terminated by user.")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
