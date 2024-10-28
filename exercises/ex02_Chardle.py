"""Something Similar to Wordle"""

__author__: str = "730752946"


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + str(letter) + " in " + str(word))
    x: int = 0
    y: int = 0
    """I made a y so that I can use it later to find how many instances of the letter happen"""
    while x < 5:
        """I used a while loop to go over all the indexes so I did not need to write out a full set of if statements"""
        if word[x] == str(letter):
            print (str(letter) + " found at index " + str(x))
            x += 1
            y += 1
        else:
            x += 1 
    if y == 0:
        print("No instances of " + str(letter) + " found in " + str(word))
    elif y == 1:
        print(str(y) + " instance of " + str(letter) + " found in " + str(word))
    else:
        print(str(y) + " instances of " + str(letter) + " found in " + str(word))
        #I did this part so that it would change from instance to instances to match what your text was.

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


