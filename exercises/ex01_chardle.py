"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730435533"

user_word: str = (input("Enter a 5-character word: "))
user_word_characters: int = (len(user_word))
if user_word_characters != 5:
    print("Error: Word must contain 5 characters")
    exit()

single_character: str = (input("Enter a single chracter: "))
single_character_characters: int = (len(single_character))
if single_character_characters != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + single_character + " in " + user_word)


if single_character == (user_word[0] + user_word[1] + user_word[2] + user_word[3] + user_word[4]):
    print(single_character + " found at index 0")
    print(single_character + " found at index 1")
    print(single_character + " found at index 2")
    print(single_character + " found at index 3")
    print(single_character + " found at index 4")
    print("4 instances of " + single_character + " found in " + user_word)
else: 
    if single_character == (user_word[0] + user_word[1] + user_word[2] + user_word[3]):
        print(single_character + " found at index 0")
        print(single_character + " found at index 1")
        print(single_character + " found at index 2")
        print(single_character + " found at index 3")
        print("4 instances of " + single_character + " found in " + user_word)
    else: 
        if single_character == (user_word[0] + user_word[1] + user_word[2]):
            print(single_character + " found at index 0")
            print(single_character + " found at index 1")
            print(single_character + " found at index 2")
            print("3 instances of " + single_character + " found in " + user_word)
        else: 
            if single_character == (user_word[0] + user_word[1]):
                print(single_character + " found at index 0")
                print(single_character + " found at index 1")
                print("2 instances of " + single_character + " found in " + user_word)
            else: 
                if single_character == user_word[0]:
                    print(single_character + " found at index 0")
                    print("1 instance of " + single_character + " found in " + user_word)
                else:
                    if single_character == (user_word[1] + user_word[2] + user_word[3] + user_word[4]):
                        print(single_character + " found at index 1")
                        print(single_character + " found at index 2")
                        print(single_character + " found at index 3")
                        print(single_character + " found at index 4")
                        print("4 instances of " + single_character + " found in " + user_word)
                    else:
                        if single_character == (user_word[1] + user_word[2] + user_word[3]):
                            print(single_character + " found at index 1")
                            print(single_character + " found at index 2")
                            print(single_character + " found at index 3")
                            print("3 instances of " + single_character + " found in " + user_word)
                        else:
                            if single_character == (user_word[1] + user_word[2]):
                                print(single_character + " found at index 1")
                                print(single_character + " found at index 2")
                                print("2 instances of " + single_character + " found in " + user_word)
                            else: 
                                if single_character == user_word[1]:
                                    print(single_character + " found at index 1")
                                    print("1 instance of " + single_character + " found in " + user_word)
                                else:
                                    if single_character == (user_word[2] + user_word[3] + user_word[4]):
                                        print(single_character + " found at index 2")
                                        print(single_character + " found at index 3")
                                        print(single_character + " found at index 4")
                                        print("3 instances of " + single_character + " found in " + user_word)
                                    else:
                                        if single_character == (user_word[2] + user_word[3]):
                                            print(single_character + " found at index 2")
                                            print(single_character + " found at index 3")
                                            print("2 instances of " + single_character + " found in " + user_word)
                                        else:
                                            if single_character == user_word[2]:
                                                print(single_character + " found at index 2")
                                                print("1 instance of " + single_character + " found in " + user_word)
                                            else:
                                                if single_character == (user_word[3] + user_word[4]):
                                                    print(single_character + " found at index 3")
                                                    print(single_character + " found at index 4")
                                                    print("2 instances of " + single_character + " found in " + user_word)
                                                else:
                                                    if single_character == user_word[3]:
                                                        print(single_character + " found at index 3")
                                                        print("1 instance of " + single_character + " found in " + user_word)
                                                    else:
                                                        if single_character == user_word[4]:
                                                            print(single_character + " found in index 4")
                                                            print("1 instance of " + single_character + " found in " + user_word)
                                                        else:
                                                            print("No instances of " + single_character + " found in " + user_word)