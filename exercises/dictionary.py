"""Some Practice with Dictionaries"""

__author__: str = "730752946"

def invert(Dict1: dict[str, str]) -> dict[str, str]:
    dict2: dict[str, str] = {}
    for key in Dict1:
        value = Dict1[key]
        if value in Dict2:
            raise KeyError("error message of your choice here!")
        dict2[value] = key
    return dict2
    
def favorite_color(Color1: dict[str, str]) -> str:
    Color2: dict[str, str] = {}
    Int: int = 0
    FavColor: str = ""
    for key in Color1:
        value = Color1[key]
        if value in Color2:
            Color2[value] += 1
        else:
            Color2[value] = 1
        if Color2[value] > Int:
            Int = Color2[value]
            FavColor = Color1[key]
    return FavColor

def count(list1: list[str]) -> dict[str, int]: 
    list2: dict[str, int] = {}
    for key in list1:
        value = list[key]
        if value in list2:
            list2[value] += 1
        else:
            list2[value] = 1
    return list2

def alphabetizer(list1: list[str]) -> dict[str, list[str]]:
    Dict1: dict[str, list[str]] = {}
    for word in list1:
        Firstletter = word[0].lower()
        if Firstletter in Dict1:
            Dict1[Firstletter].append(word)
        else:
            Dict1[Firstletter] = []
            Dict1[Firstletter].append(word)
    return Dict1

def update_attendance(ATD: dict[str, list[str]], DOTW: str, Student: str) -> None:
    