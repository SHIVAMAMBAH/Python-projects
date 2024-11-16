def vowel_count(string:str)->str:
    """To count the number of vowels in a string"""
    vowels = ['a','e','i','o','u']
    
    count:int = sum(1 for char in string.lower() if char in vowels)
    
    return f"{count} Vowels"

if __name__ == "__main__":
    try:
        string:str = input("Enter a string : ")
        print(vowel_count(string)) 
    except ValueError:
        print("Invalid Input")   
