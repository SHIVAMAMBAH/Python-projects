def factorial(number:int)->str|int:
    if number<0:
        return "Factorial of negative numbers don't exist."
    if number in (0,1):
        return "1"
    result = 1
    for i in range(2,number+1):
        result*=i
    return result

if __name__ == "__main__":
    try:
        number = int(input("Enter a number :"))
        print(factorial(number))
    except ValueError:
        print("Invalid number input. Please Enter an Integer.")
