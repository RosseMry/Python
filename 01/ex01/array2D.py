from typing import List

def slice_me(family: list, start: int, end: int) -> list:

    #if is not list 
    if not isinstance (family, list):
        raise TypeError("Family is not a list \n")

    #if is empty
    if len(family) == 0:
        return[]
    
    #check row in Tuple family
    for row in family:
        if not isinstance(row, list):
                raise TypeError("Internal elements must be a list\n")
    
    #size check
    len_row = len(family[0]);
    for row in family:
        if len(row) != len_row :
            raise ValueError("List are not the same size\n")
    
    for row in family:
        for i in row:
            if not isinstance(i, (int, float)) or isinstance(i, bool):
                raise TypeError(f"Value {i} should be a number\n")

    #finding shape
    num_row = len(family)
    num_column = len_row
    print(f"My shape is : ({num_row}, {num_column})")

    #new list
    truncate_family = family[start : end]
    new_row = len(truncate_family)
    print(f"My new shape is : ({new_row}, {num_column})")
    return truncate_family




    
    
    
