"""Demostrate defining a module imported elsewhere."""


THE_ANSWER: int = 42


def main() -> None:
    print(powerful(2, 10))
    print("helpers.py run as a module")


def powerful(x: float, n: float) -> float:
    """Raise x to the power of n."""
    return x ** n


# idiom for making a module able to run as a program 
# or have its global definition imported elsewhere if it is false and name is actually the name of the module "lessons.helpers" and not "main"
if __name__ == "__main__":
    main()
else:
    # this is not idiomatic to have an else branch. 
    print(f"helpers.py was imported: {__name__}")
