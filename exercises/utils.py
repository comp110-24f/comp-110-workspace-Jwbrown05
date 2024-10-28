"""Utils or something"""

__author__: str = "730752946"

def only_evens(input: list[int]) -> list[int]:
    """Takes an input and gets rid of odd numbers using mod"""
    list2: list[int] = []
    for idx in range(0, len(input)):
        if input[idx] % 2 == 0: #only odd numbers are mod 2 == 1
            list2.append(input[idx])
    return list2

def sub(list1: list[int], startidx: int, endidx: int) -> list[int]:
    """takes a list and makes it starts at the start index and ends at the end index"""
    if startidx < 0: #If it is negative make it start at the start or 0. These are both for edge case.
        startidx = 0
    if endidx > len(list1): #if it is greater then the length make it start at the length.
        endidx = len(list1)
    list2: list[int] = []
    for idx in range(startidx, endidx):
            list2.append(list1[idx])
    return list2 

def add_at_index(lista: list[int], elem: int, index: int) -> None:
    """Adds the element at the index you choose"""
    listb: list[int] = []
    if (index < 0) or (index > len(lista)):
        raise IndexError("Index is out of bounds for the input list")
    for idx in range(0, len(lista)): #Makes modified list with element in the right index
        if idx == index:
            listb.append(elem)
        listb.append(lista[idx])
    for idx in range(0, len(listb)): #Makes lista turn into the new modified list with the element in the right index
        if len(listb) > len(lista):
            lista.append(0)
        lista[idx] = listb[idx]
    

