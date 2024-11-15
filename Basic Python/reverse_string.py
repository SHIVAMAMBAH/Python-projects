def reverse_string(string:str)->str:
    return string[::-1]

if __name__=="__main__":
    string = input("Enter a string : ")
    reversed_string = reverse_string(string)
    print(f"{string} -> {reversed_string}")
