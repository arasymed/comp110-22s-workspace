"""Unit testing for lists utils functions."""

__author__ = "730435533"

from utils import only_evens, sub, concat


# ONLY_EVENS TESTS
# Edge case:
def test_only_evens_one_even() -> None:
    """Tests for an empty list and returns no even numbers."""
    integer_list: list[int] = []
    assert only_evens(integer_list) == []


def test_only_evens_no_evens() -> None:
    """Tests a list with no even numbers and returns no even numbers."""
    integer_list: list[int] = [3, 7, 11]
    assert only_evens(integer_list) == []


# Usage case
def test_only_evens_with_addition() -> None:
    """Checks for even numbers in a list with addition operations."""
    integer_list: list[int] = [22 + 1, 2 + 3, 1 + 2, 3 + 4, 2 + 2, 5 + 5]
    assert only_evens(integer_list) == [4, 10]


# Usage case
def test_only_evens_with_multiplication() -> None:
    """Checks for even numbers in a list with multiplication operations."""
    integer_list: list[int] = [2 * 2, 3 * 9, 8 * 7, 10 * 2]
    assert only_evens(integer_list) == [4, 56, 20]


def test_only_evens_all_evens() -> None:
    """Looks for even numbers in a list full of even numbers."""
    integer_list: list[int] = [4, 4, 4]
    assert only_evens(integer_list) == [4, 4, 4]


# SUB TESTS
# Usage cases:
def test_sub() -> None:
    """Creates a subset list out of one given list accordibg to start and end index."""
    # if we wanted to take have one single number in our list:
    list_of_integers: list[int] = [15, 45, 35, 14]
    start_index: int = 1
    end_index: int = 2
    assert sub(list_of_integers, start_index, end_index) == [45]


def test_sub_list_two_items() -> None:
    """Creates a subset list by taking out only 2 consecutive numbers."""
    # if we wanted to use the numbers with a single digit in a list:
    list_of_integers: list[int] = [15, 45, 35, 14, 2, 3, 44, 78, 199, 202]
    start_index: int = 4
    end_index: int = 6
    assert sub(list_of_integers, start_index, end_index) == [2, 3]


# edge cases:
# if someone wanted to have the same list as the return value:
def test_sub_replicated_list() -> None:
    """Creates a subset list that is a replicated list of the given list to the parameter."""
    list_of_integers: list[int] = [15, 45, 22, 89, 23, 15, 22]
    start_index: int = 0
    end_index: int = 7
    assert sub(list_of_integers, start_index, end_index) == [15, 45, 22, 89, 23, 15, 22]


def test_sub_replicated_list2() -> None:
    """Creates a subset list starting from the index 0 to the index 1."""
    list_of_integers: list[int] = [1, 2, 3]
    start_index: int = 0
    end_index: int = 2
    assert sub(list_of_integers, start_index, end_index) == [1, 2]


def test_sub_negative_start_index() -> None:
    """Creates a subset list starting from a negative index."""
    list_of_integers: list[int] = [15, 45, 35, 14, 90, 15, 22]
    start_index: int = -1
    end_index: int = 4
    assert sub(list_of_integers, start_index, end_index) == [15, 45, 35, 14]


def test_sub_end_index_greater_than_length() -> None:
    """Creates a subset list with an end index that is greater than the length of the input list."""
    list_of_integers: list[int] = [99, 95, 34, 88, 2, 22]
    start_index: int = 2
    end_index: int = 10
    assert sub(list_of_integers, start_index, end_index) == [34, 88, 2, 22]


def test_sub_list_length_zero() -> None:
    """Creates a subset empty list because the start and end index are our of range."""
    list_of_integers: list[int] = []
    start_index: int = 2
    end_index: int = 4
    assert sub(list_of_integers, start_index, end_index) == []


def test_sub_start_index_greater_than_length() -> None:
    """Creates a subset empty list because the start index is creater than the length of the list."""
    list_of_integers: list[int] = [2, 4, 5]
    start_index: int = 10
    end_index: int = 4
    assert sub(list_of_integers, start_index, end_index) == []


def test_sub_end_index_negative() -> None:
    """Creates a subset list with a negative end index."""
    list_of_integers: list[int] = [21, 56, 66, 20]
    start_index: int = 2
    end_index: int = -4
    assert sub(list_of_integers, start_index, end_index) == []


def test_sub_end_index_zero() -> None:
    """Creates a subset wirh an end index of zero."""
    list_of_integers: list[int] = [22, 54, 78, 2]
    start_index: int = 2
    end_index: int = 0
    assert sub(list_of_integers, start_index, end_index) == []


# CONCAT TESTS
# Usage cases:
# If we wanted to concatenate two lists with different lengths:
def test_concat_random_numbers() -> None:
    """Tests for concatenation of two lists with different lengths."""
    integer_list_one: list[int] = [4, 6, 2, 9, 15]
    integer_list_two: list[int] = [25, 99, 76, 44, 88, 102, 146]
    assert concat(integer_list_one, integer_list_two) == [4, 6, 2, 9, 15, 25, 99, 76, 44, 88, 102, 146]


# If we wanted to concat two lists with consecutive numbers:
def test_concat_consecutive_numbers() -> None:
    """Test for concatenation of lists with consecutive numbers."""
    integer_list_one: list[int] = [1, 2, 3, 4, 5]
    integer_list_two: list[int] = [6, 7, 8, 9, 10]
    assert concat(integer_list_one, integer_list_two) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Edge case:
# If we wanted to concatenate two empty lists:
def test_concat_empty_lists() -> None:
    """Tests for concatenation of two emoty lists."""
    integer_list_one: list[int] = []
    integer_list_two: list[int] = []
    assert concat(integer_list_one, integer_list_two) == []