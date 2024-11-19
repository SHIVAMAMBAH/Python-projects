def check_odd_even(number: int)->str:
    """Checks if a number is odd or not using bitwise operations."""
    return f"{number} is {'odd' if number&1 else 'even'}"

if __name__ == "__main__":
    try:
        number:int = int(input("Enter a number:"))
        print(check_odd_even(number))
    except ValueError:
        print("Invalid Input. Pleae enter an integer.")
