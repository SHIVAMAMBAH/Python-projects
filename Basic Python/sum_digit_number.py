def sum_of_digits_of_number(number:int)->int:
    """Function to  find the sum of digits of a number"""
    result:int = 0
    while number!=0:
        result+=number%10
        number//=10
    return result

if __name__ == "__main__":
    try:
        number:int = int(input("Enter a number : "))
        print(sum_of_digits_of_number(number))
    except ValueError:
        print("Invalid Input")
