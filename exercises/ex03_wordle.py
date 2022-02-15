"""Structure Wordle using concepts from Lesson 12 through 14"""

__author__ = "730435533"

# Definition of first function which will check indeces of our word


def contains_char(word: str, single_character: str) -> bool:
    """Given two strings, returns True if character of second string is found anywhere in second string"""
    assert len(single_character) == 1 
# making sure that the length is 1 for this character
    i: int = 0
    found: bool = (False)
    counting_characters: int = len(word) 
    while i < counting_characters and found == (False):
        if single_character == word[i]:
            found = (True)
        else:
            i += 1
    return found 
# returning the result of code


def emojified(guess: str, secret: str) -> str: 
    # defining second function which gives emojis according to characters
    """Assigns emoji according to Wordle game"""
    assert len(guess) == len(secret)
    color_coding: int = 0
    emoji: str = ""
    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"
    while color_coding < len(secret): 
        # assigning green emoji
        if secret[color_coding] == guess[color_coding]:
            emoji += green_box
            color_coding += 1
        else:
            if contains_char(secret, guess[color_coding]) == (False): 
                # assigning white emoji
                emoji += white_box
                color_coding += 1
            else:
                if contains_char(secret, guess[color_coding]) == (True): 
                    # assigning yellow emoji
                    emoji += yellow_box
                    color_coding += 1
    return emoji 
    # returning result

# defining third function which controls number of characters


def input_guess(expected_length: int) -> str:
    """Asks for correct number of characters"""
    numbers: int = expected_length
    characters: str = input(f"Enter a {numbers} character word: ")
    while numbers != len(characters):
        characters = input(f"That wasn't {numbers} chars! Try again: ")
    return characters
    # returning result after writing parameters and conditions

# definiting function which controls the game 


def main() -> None:
    """The entrypoint of the program and main game loop"""
    turns: int = 1
    secret: str = "codes"
    # our secret word
    guess: str = ""
    # loop repeats 6 times
    while turns <= 6 and secret != guess:
        print(f"===Turn {turns}/6 ===")
        # using other functions in order to run the game
        guess = input_guess(5)
        print(emojified(guess, secret)) 
        turns += 1
    if secret == guess:
        turns -= 1
        print(f"You won in {turns}/6 turns!")
    if secret != guess:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()        