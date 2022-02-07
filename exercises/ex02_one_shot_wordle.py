"""One shot Wordle using concepts from Lessons 9 and 10."""

__author__ = "730435533"

# Assigning variables
index_guess: int = 0
emoji: str = ""
white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"
secret: str = ("python")
guess: str = input(f"What is your {len(secret)}-letter guess? ")
index_yellow: bool = False
alternate_indeces: int = 0
# Checking lenght 
while len(guess) != len(secret):
    guess = str = input(f"That was not {len(secret)} letters! Try again: ")
while index_guess < len(secret):
    if guess[index_guess] == secret[index_guess]:
        emoji += green_box
        index_guess += 1
# checking for good placement
    else:
        while index_yellow == (not(True)) and alternate_indeces < len(secret):
            if secret[alternate_indeces] == guess[index_guess]:
                index_yellow = True
                # Iteration, looking at every letter and checking it according to if then statements 
            else:
                alternate_indeces = alternate_indeces + 1
        if index_yellow == (not(False)):
            emoji += yellow_box
            # Assigning yellow emoji when the letter exists but not in right place
        else:
            emoji += white_box
            # Assigning white emoji when letter does not match at all
        index_guess += 1
        index_yellow = False
        alternate_indeces = 0
        # Going over the program again
print(emoji)
if secret != guess:
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")
