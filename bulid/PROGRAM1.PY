class Calculator:
    def __init__(self, a: float, b: float, operation: str):
        self.a = a
        self.b = b
        self.operation = operation.lower()

    def calculate(self):
        if self.operation == 'addition':
            return self.add()
        elif self.operation == 'subtraction':
            return self.subtract()
        elif self.operation == 'multiplication':
            return self.multiply()
        elif self.operation == 'division':
            return self.divide()
        else:
            return "Invalid operation. Please choose from addition, subtraction, multiplication, or division."

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            return "Error: Division by zero is not allowed."
        return self.a / self.b
    # Example usage
a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))
operation = input("Enter the type of operation (addition, subtraction, multiplication, division): ")

calculator = Calculator(a, b, operation)
result = calculator.calculate()

print(f"The result of the {operation} is: {result}")
