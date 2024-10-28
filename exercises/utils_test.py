"""TEST THAT STUFF BABY"""

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest

def test_only_even1() -> None:
    """A list of integers, containing only the even elements of the input parameter. (Return list)"""
    a: list[int] = [9,4,0]
    assert only_evens(a) == [4,0]

def test_only_even2() -> None:
    """A list of integers, containing only the even elements of the input parameter. (Edge Case)"""
    b: list[int] = []
    assert only_evens(b) == []

def test_only_even3() -> None:
    """A list of integers, containing only the even elements of the input parameter. (Mutates List)"""
    c: list[int] = [1, 4, 5, 6]
    only_evens(c)
    assert c == [1, 4, 5, 6]

def test_sub1() -> None:
    """A list of integers, containing only the the numbers within the range of the start and end index. (Return Case)"""
    a: list[int] = [1,2,3,4]
    assert sub(a, 1, 3) == [2,3]

def test_sub2() -> None:
    """A list of integers, containing only the the numbers within the range of the start and end index (Edge Case)"""
    a: list[int] = [1,2,3,4]
    assert sub(a, -1, 6) == [1,2,3,4]

def test_sub3() -> None:
    """A list of integers, containing only the the numbers within the range of the start and end index. (Mutates List)"""
    a: list[int] = [1,2,3,4]
    sub(a, 0, 3) 
    assert a == [1,2,3,4]

def test_add_at_index1() -> None:
    """A list of integers, That includes an int element at an index. (Mutate Case)"""
    a: list[int] = [1,2,3,5]
    add_at_index(a, 4, 3) 
    assert a == [1,2,3,4,5]

def test_add_at_index2() -> None:
    """A list of integers, That includes an int element at an index. (Edge Case)"""
    a: list[int] = []
    with pytest.raises(IndexError):
        add_at_index(a, 4, 3) 

def test_add_at_index3() -> None:
    """A list of integers, That includes an int element at an index. (Return Case)"""
    a: list[int] = [1,2,3]
    assert add_at_index(a, 1, 1) == None