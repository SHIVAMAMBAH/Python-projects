def check_odd_even(number: int)->str:
    return f"{number} is {'odd' if number&1 else 'even'}"

if __name__ == "__main__":
    try:
        number = int(input("Enter a number:"))
        print(check_odd_even(number))
    except ValueError:
        print("Invalid Input. Pleae enter an integer.")
