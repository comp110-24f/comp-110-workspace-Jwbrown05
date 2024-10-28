"""Something Similar to Wordle"""

__author__: str = "730752946"


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + str(letter) + " in " + str(word))
    x: int = 0
    if letter == word[0]:
        print(letter + " found at index 0")
        x += 1
    if letter == word[1]:
        print(letter + " found at index 1")
        x += 1
    if letter == word[2]:
        print(letter + " found at index 2")
        x += 1
    if letter == word[3]:
        print(letter + " found at index 3")
        x += 1
    if letter == word[4]:
        print(letter + " found at index 4")
        x += 1
    if x > 1: 
        print(str(x) + " instances of " + letter + " found in " + word)
    elif x == 1:
        print(str(x) + " instance of " + letter + " found in " + word)
    else:
        print("No instances of " + str(letter) + " found in " + str(word))


def input_word() -> str:
    Word: str = str(input("Enter a 5-character word: "))
    if len(Word) == 5:
        return(Word)
        """It will find the length of the word and compare it to if it is 5"""
    else:
        print("Error: Word must contain 5 characters.")
        exit()
        """I originally put quit() which seemed to also work"""

def input_letter() -> str:
    letter: str = str(input("Enter a single character: "))
    if len(letter) == 1:
        return(letter)
        """Same as I said for def input_word"""
    else:
        print("Error: Character must be a single character.")
        exit()

def main() -> None:
    contains_char(word=input_word(), letter=input_letter())

if __name__ == "__main__":
    main()


