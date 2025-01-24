def perform_operation(num1, num2, operation):
    """Performs basic arithmetic operations using if-elif-else."""
    
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero"
        else:
            return num1 / num2 
    else:
        return "Error: Invalid operation"

# Example call
result = perform_operation(2, 0, "divide")
print(result)  # Output: Error: Division by zero
