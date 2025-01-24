def perform_operation(num1,num2,"operation"):
    """performs basic arithematic operations using match statement"""
    match "operation":
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 !=0 :
                return num1/num2
            else:
                print("Error")#return f"we you cant divide {num1} by 0"
        case _:
            return "Error: Invalid operation"

perform_operation(2,0,"divide")

