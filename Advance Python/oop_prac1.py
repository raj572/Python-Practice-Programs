
class Calculator:
    def add(self, numbers):
        return sum(numbers)

    def subtract(self, numbers):
        result = numbers[0]
        for num in numbers[1:]:
            result -= num
        return result

    def multiply(self, numbers):
        result = 1
        for num in numbers:
            result *= num
        return result

    def divide(self, numbers):
        if 0 in numbers[1:]:
            return "Division by zero is not allowed."
        result = numbers[0]
        for num in numbers[1:]:
            result /= num
        return result

calculator = Calculator()

while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'quit' to end the program")

    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input in ["add", "subtract", "multiply", "divide"]:
        num_count = int(input("Enter the number of values: "))
        numbers = []
        for _ in range(num_count):
            num = float(input("Enter a number: "))
            numbers.append(num)

        if user_input == "add":
            print(f"Result: {calculator.add(numbers)}")
        elif user_input == "subtract":
            print(f"Result: {calculator.subtract(numbers)}")
        elif user_input == "multiply":
            print(f"Result: {calculator.multiply(numbers)}")
        elif user_input == "divide":
            print(f"Result: {calculator.divide(numbers)}")
    else:
        print("Invalid input. Please try again.")