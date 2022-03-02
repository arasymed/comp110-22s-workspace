"""Building list utility functions."""

__author__ = "730435533"

# Define a function that takes in a list of integers and returns a list of only even numbers


def only_evens(integer_list: list[int]) -> list[int]:
    even_list: list[int] = list()
    i: int = 0
    while i <= len(integer_list):
        even: int = (integer_list[i] // 2) * 2
        if integer_list[i] != even:
            even_list.pop(integer_list[i])
        else:
            even_list.append(integer_list[i])
    i += 1
    return even_list