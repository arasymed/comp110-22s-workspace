""""Tests for dictionary functions."""

from dictionary import invert, favorite_color, count


# Use cases
def test_invert_long_list() -> None:
    """Tests for inverted dictionary that has greetings as keys and parting statements as values."""
    dict_greetings: dict[str, str] = {"bye": "hello", "adios": "hola", "good night": "good morning"}
    assert invert(dict_greetings) == {"hello": "bye", "hola": "adios", "good morning": "good night"}


def test_invert_prices() -> None:
    """Tests for name of items as keys and price of item as values."""
    dict_shopping: dict[str, str] = {"1.5 dollars": "lettuce", "3 dollars": "Avocado", "0.45 dollars": "Banana"}
    assert invert(dict_shopping) == {"lettuce": "1.5 dollars", "Avocado": "3 dollars", "Banana": "0.45 dollars"}


# Edge case
def test_invert_empty() -> None:
    """Test for invertion of a dictionary that is empty."""
    dict_empty: dict[str, str] = {}
    assert invert(dict_empty) == {}


# use case
def test_favorite_color_friends() -> None:
    """Test for the most frequent favorite color between friends."""
    dict_colors: dict[str, str] = {"Gabi": "Red", "Sofi": "Green", "Tami": "Green"}
    favorite_color(dict_colors) == "Green"


def test_favorite_color_random() -> None:
    """Test for most frequent favorite color of random people."""
    dict_colors_random: dict[str, str] = {"Person_1": "Black", "Person_2": "Yellow", "Person_3": "Yellow"}
    assert favorite_color(dict_colors_random) == "Yellow"


# edge case
def test_favorite_color_tie() -> None:
    """Returns the first color in dictionary if there is a tie."""
    dict_colors_tie: dict[str, str] = {"Ana": "Orange", "Morgan": "Orange", "Sofi": "Orange"}
    assert favorite_color(dict_colors_tie) == "Orange"
    while 