def reverse_string(string:str)->str:
    """To reverse a string"""
    return string[::-1]

if __name__=="__main__":
    string:str = input("Enter a string : ")
    reversed_string = reverse_string(string)
    print(f"{string} -> {reversed_string}")
