"Unit testing for lists utils functions."

__author__ = "730435533"

from utils import only_evens, sub, concat


# ONLY_EVENS TESTS
# Edge case:
def test_only_evens_one_even() -> None:
    integer_list: list[int] = []
    assert only_evens(integer_list) == []


def test_only_evens_no_evens() -> None:
    integer_list: list[int] = [3, 7, 11]
    assert only_evens(integer_list) == []


# Usage case
def test_only_evens_with_addition() -> None:
    integer_list: list[int] = [22 + 1, 2 + 3, 1 + 2, 3 + 4, 2 + 2, 5 + 5]
    assert only_evens(integer_list) == [4, 10]


# Usage case
def test_only_evens_with_multiplication() -> None:
    integer_list: list[int] = [2 * 2, 3 * 9, 8 * 7, 10 * 2]
    assert only_evens(integer_list) == [4, 56, 20]


def test_only_evens_all_evens() -> None:
    integer_list: list[int] = [4, 4, 4]
    assert only_evens(integer_list) == [4, 4, 4]


# SUB TESTS
# Usage cases:
def test_sub() -> None:
    # if we wanted to take have one single number in our list:
    list_of_integers: list[int] = [15, 45, 35, 14]
    start_index: int = 1
    end_index: int = 2
    assert sub(list_of_integers, start_index, end_index) == [45]


def test_sub_list_two_items() -> None:
    # if we wanted to use the numbers with a single digit in a list:
    list_of_integers: list[int] = [15, 45, 35, 14, 2, 3, 44, 78, 199, 202]
    start_index: int = 4
    end_index: int = 6
    assert sub(list_of_integers, start_index, end_index) == [2, 3]


# edge cases:
# if someone wanted to have the same list as the return value:
def test_sub_replicated_list() -> None:
    list_of_integers: list[int] = [15, 45, 22, 89, 23, 15, 22]
    start_index: int = 0
    end_index: int = 7
    assert sub(list_of_integers, start_index, end_index) == [15, 45, 22, 89, 23, 15, 22]


def test_sub_negative_start_index() -> None:
    list_of_integers: list[int] = [15, 45, 35, 14, 90, 15, 22]
    start_index: int = -1
    end_index: int = 4
    assert sub(list_of_integers, start_index, end_index) == [15, 45, 35, 14]


def test_sub_end_index_greater_than_length() -> None:
    list_of_integers: list[int] = [99, 95, 34, 88, 2, 22]
    start_index: int = 2
    end_index: int = 10
    assert sub(list_of_integers, start_index, end_index) == [34, 88, 2, 22]


def test_sub_list_length_zero() -> None:
    list_of_integers: list[int] = []
    start_index: int = 2
    end_index: int = 4
    assert sub(list_of_integers, start_index, end_index) == []


def test_sub_start_index_greater_than_length() -> None:
    list_of_integers: list[int] = [2, 4, 5]
    start_index: int = 10
    end_index: int = 4
    assert sub(list_of_integers, start_index, end_index) == []


def test_sub_end_index_negative() -> None:
    list_of_integers: list[int] = [21, 56, 66, 20]
    start_index: int = 2
    end_index: int = -4
    assert sub(list_of_integers, start_index, end_index) == []


def test_sub_end_index_zero() -> None:
    list_of_integers: list[int] = [22, 54, 78, 2]
    start_index: int = 2
    end_index: int = 0
    assert sub(list_of_integers, start_index, end_index) == []


# CONCAT TESTS
# Usage cases:
def tes_concat_two_lists_together() -> None:
    integer_list_one: list[int] = [1, 2, 3, 7, 9]
    integer_list_two: list[int] = [10, 12, 14, 16]
    assert concat(integer_list_one, integer_list_two) == [1, 2, 3, 7, 9, 10, 12, 14, 16]
