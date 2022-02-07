""" Some examples of tender, loving function definitions."""


def love(name: str) -> str:
    """Given a name as a paraneter, returns a loving string."""
    return f"I love you {name} !"


# name: str = input("Give me a name: ")
# x: str = love(name)
# print(x)
print(love("Tamara"))


def spread_love(to: str, n: int) -> str:
    """Generates a string that repeats a loving message n times. """
    love_note: str = ""
    i: int = 0
    while i < n:
        love_note = love_note + love(to) + "\n"
        i = i + 1
    return love_note


print(spread_love("Tamara", 100))