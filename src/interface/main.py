from src.models.calculator import Calculator

def main():
    operation = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    calculator = Calculator()
    
    if operation == "add":
        result = calculator.add(num1, num2)
    elif operation == "subtract":
        result = calculator.subtract(num1, num2)
    elif operation == "multiply":
        result = calculator.multiply(num1, num2)
    elif operation == "divide":
        result = calculator.divide(num1, num2)
    else:
        print("Invalid operation")
        return
    
    print(f"The result is: {result}")

if __name__ == "__main__":
    main()