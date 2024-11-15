def remove_duplicate_elements(lst:list)->list|str:
    """Function to remove duplicate elements from the list!"""
    if not lst:
        return f"{List} is empty"
    if len(lst)==1:
        return f"{List} has only one element"
    
    new_list = []
    for element in lst:
        if element not in new_list:
            new_list.append(element)
    
    return new_list

if __name__ == "__main__":
    try:
        List = [1,2,3,4,2,3,4]
        print(remove_duplicate_elements(List))
    except ValueError:
        print("Invalid Input")
