def perfect_number(number:int)->str:
    if number <= 1:
        return f"{number} is not a perfect number."
    
    factors = [1]
    for i in range(2,int(number**0.5)+1):
        if number%i==0:
            factors.append(i)
            if i != number // i:
                factors.append(number // i)
    return f"{number} is {'' if number==sum(factors) else 'not'} perfect "

if __name__ == "__main__":
    try:
        number = int(input("Enter the number : "))
        print(perfect_number(number))
    except ValueError:
        print("Invalid Input")
