def fibonacci(number:int)->str|list:
    """Fibonacci sequence with first term 0 and second term 1"""
    if number<=0:
        return "Enter valid number of terms."
    
    if number == 1:
        return [0]
    if number == 2:
        return [0,1]
    
    terms = [0,1]
    for i in range(0,number-2):
        terms.append(terms[i]+terms[i+1])
    
    return terms

if __name__ == "__main__":
    try:
        number = int(input("Enter a number : "))
        print(fibonacci(number))
    except ValueError:
        print("Invalid Input")
