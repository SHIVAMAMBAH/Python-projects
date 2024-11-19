import math

def is_prime(number:int)->str|bool:
    """Checks if a number is prime or not."""
    if number <= 1:
        return False
    if number in (2, 3):
        return True
    if number % 2 == 0:
        return False
    
    sqrt_number:int = int(math.sqrt(number))
    for i in range(3,sqrt_number+1,2):
        if number%i==0:
            return f"{number} is not prime"
    
    return f"{number} is prime"

if __name__ == "__main__":
    try:
        number:int = int(input("Enter a number : "))
        print(is_prime(number))
    except ValueError:
        print("Invalid Input")
