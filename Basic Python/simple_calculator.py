def simple_calculator(operand1:float,operator:str,operand2:float)->float:
  """Function to perform basic arithmatic operations"""
    match operator:
        case '+':
            return operand1+operand2
        case '-':
            return operand1-operand2
        case '*':
            return operand1*operand2
        case '/':
            if operand2 == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            return operand1/operand2
        case _:
            raise ValueError(f"Unsupported operator : {operator}")


result:float = 0.0

if __name__ == "__main__":
    try : 
        while True : 
            operand1:float = float(input("Enter number : "))
    
            operator:str = input("Enter the operator(+,-,/,* or 'q' to quit) : ")
            if(operator=="q"):
                break
    
            operand2:float = float(input("Enter number : "))

            try:
                result+= simple_calculator(operand1,operator,operand2)
                print(result)
            except (ZeroDivisionError,ValueError) as e:
                print(f"Error : {e}")
    except ValueError:
        print("Invalid Input")
    except KeyboardInterrupt:
        print("\nCalculator terminates by user!")
