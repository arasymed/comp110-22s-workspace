""""Practice with if-then-statements."""

choice: int = int(input("Pick a number: "))

# Implement_this_logic 
# A < 25
# B >= 25 and < 50
# C > 75
# D >= 50 and <= 75

if choice < 50:
    if choice < 25:
        print("A")
    else:
        print("B")
else:
    if choice > 75:
        print("C")
    else:
        print("D")


"""Second try"""
choice: int = int(input("Pick a number"))

if choice < 50:
    if choice < 25:
        print("A")
    else:
        print("B")
else:
    if choice > 75:
        print("C")
    else:
        print("D")