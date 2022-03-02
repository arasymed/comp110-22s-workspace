"""Building list utility functions."""

__author__ = "730435533"

# Define a function that takes in a list of integers and returns a list of only even numbers


def only_evens(integer_list: list[int]) -> list[int]:
    """Give a list of integers function returns only the even numbers."""
    even_list: list[int] = []
    # in order to append we need to place the item that we want to append
    i: int = 0 
    for item in integer_list:
        # Checking the items in the list to see if they are even numbers
        even: int = (item // 2) * 2
# If after the multiplication (*2) the number is still the same it means that it is even
        if even == item:
            even_list.append(integer_list[i])
        i += 1
    return even_list


def sub(list_of_integers: list[int], start_index: int, end_index: int) -> list[int]:
    subset_list: list[int] = []
    i: int = start_index
    if start_index > 0:
        if end_index < len(list_of_integers):
            while i >= start_index and i < end_index:
                subset_list.append(list_of_integers[i])
                i += 1
            return subset_list
        if end_index > len(list_of_integers):
            while i >= start_index and i <= len(list_of_integers) - 1:
                subset_list.append(list_of_integers[i])
                i += 1
        return subset_list
    if start_index < 0:
        i = 0
        while i >= start_index and i < end_index:
            subset_list.append(list_of_integers[i])
            i += 1
        return subset_list
    if start_index == 0:
        while i >= start_index and i < end_index:
            subset_list.append(list_of_integers[i])
            i += 1
        return subset_list
    if len(list_of_integers) == 0 or start_index > len(list_of_integers) or end_index <= 0:
        return subset_list


def concat(integer_list_one: list[int], integer_list_two: list[int]) -> list[int]:
    list_with_all: list[int] = []
    for item in integer_list_one:
        list_with_all.append(item)
    for item_list_two in integer_list_two:
        list_with_all.append(item_list_two)
    return list_with_all
