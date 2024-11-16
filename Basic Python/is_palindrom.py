def is_palindrom(string:str)->str:
    """Checks if the given string or numeric string is a palindrome."""
    if string.isdigit():
        return string == string[::-1]
    
    return string == string[::-1]

if __name__ == "__main__":
    try:
        string:str = input("Enter a string :").strip()
        if is_palindrom(string):
            print(f"{string} is a palindrom")
        else:
            print(f"{string} is not a palindrom")
    except ValueError:
        print("Ivalid Input!")
