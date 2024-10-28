"""The Word game of WORDLE"""

__author__: str = "730752946"

def main(secret: str) -> None:
    """MAIN FUNTION"""
    N: int = 1
    A: bool = True
    # I set this as one because it shouldn't ask you === Turn 0/6 === 
    while (N < 7) and (A == True):
        #I set this as 7 bc N starts at 1
        print("=== Turn " + str(N) + "/6 ===")
        Guess: str = input_guess(secret_word_len= len(secret))
        #I made this variable to not only check if the length is 5 or whatever you change it to, but also establish the Guess Local variable
        print(emojified(guess= Guess, secret= secret))
        if Guess == secret:
            print("You won in " + str(N) + "/6 turns!")
            A = False
        else:
            N += 1
    if A == True:
        print("X/6 - Sorry, try again tomorrow!")
    #I added this at the end and not in the loop bc once N = 7 (which is when the loop ends) you lose


def input_guess(secret_word_len: int) -> str:
    """Asks for a word and returns if it is the right length"""
    Y: bool = False
    Word: str = (input("Enter a " + str(secret_word_len) + " character word: "))
    while Y == False:
        if secret_word_len == len(Word):
            return Word
            Y = True 
            #This stops the loop because Y is true
        else:
            Word = (input("That wasn't " + str(secret_word_len) + " chars! Try again: "))
    return Word 
    

def contains_char(Secret_Word: str, Single_Char: str) -> bool:
    """figures out if a single character is in the word, used to find if the character is yellow"""
    assert len(Single_Char) == 1
    x: int = 0
    while x < len(Secret_Word):
        if Single_Char == Secret_Word[x]:
            return True
            #named this z because y was already being used for input_guess 
            #and it confused me bc they are both bools
        x += 1
    return False

def emojified(guess: str, secret: str) -> str:
    """Prints out the green, yellow, and white boxes to show player how close there word was to the secret word"""
    assert len(guess) == len(secret)
    Wordle: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    x: int = 0
    """I used x instead of index"""
    while x < len(guess):
        if secret[x] == guess[x]:
            Wordle += (GREEN_BOX)
            """This appends each of the strs together. It takes an empty string and adds new strs into it"""
        elif (secret[x] != guess[x]) and (contains_char(Single_Char= guess[x], Secret_Word= secret) == True):
            Wordle += (YELLOW_BOX)
        else:
            Wordle += (WHITE_BOX)
        x += 1
    return Wordle

if __name__ == "__main__":
    main(secret="codes")
         
            

