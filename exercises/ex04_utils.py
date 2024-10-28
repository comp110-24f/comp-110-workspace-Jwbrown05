"""List Utility Functions"""

__author__: str = "730752946"

def all(listx: list[int], intx: int) -> bool:
    """Returns True if all of the ints in list[int] are the same as intx"""
    if len(listx) == 0:
        return False
    for elem in listx:
        if elem != intx: #Checks all of the elem in list and sees if any of them do not equal the int
            return False
    return True

def max(input: list[int]) -> int:
    """Finds the max int in a list"""
    Max: int = input[0]
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    for elem in input:
        if elem > Max: #When the new element is bigger then Max it makes Max = to elem then the next elem it does the same
            Max = elem
    return Max   
    
def is_equal(list1: list[int], list2: list[int]) -> bool:
    """when two list are equal in all of their number it returns true otherwise it returns false"""
    idx: int = 0
    if len(list1) + len(list2) == 0: #when they both are zero then it is the same list so return True
        return True
    if len(list1) == 0: #when either of them is empty but not both it should return false as not the same list
        return False
    if len(list2) == 0:
        return False
    if len(list1) != len(list2):
        return False
    for idx in range(0, len(list1)):
        if list1[idx] != list2[idx]: #uses the index to check if each of the numbers are equal
            return False
    return True
        
def extend(lista: list[int], listb: list[int]) -> None:
    """Adds the other list to the first list to make a extended list"""
    lista += listb #appending the two lists together
    print(lista)

