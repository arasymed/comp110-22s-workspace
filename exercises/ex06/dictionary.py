"""Practice with dictionary functions."""

import pytest


def invert(dict_to_invert: dict[str, str]) -> dict[str, str]:
    """Inverts a dictionary of strings."""
    final_dict: dict[str, str] = {}
    for key in dict_to_invert:
        keys: str = dict_to_invert[key]
        final_dict[keys] = key
    return final_dict


def favorite_color(dict_with_colors: dict[str, str]) -> str:
    """Returns the most frequent favorite color."""
    i: int = 0
    dict_with_colors_duplicated: dict[str, str] = dict_with_colors
    list_of_colors: list[str] = []
    color_count_1: int = 0
    color_count_2: int = 0
    color_count_3: int = 0
    index_colors: int = 0 
    color: str = ""
    color_2: str = ""
    color_3: str = ""
    for keys in dict_with_colors_duplicated:
        list_of_colors += dict_with_colors[keys]
    for keys in dict_with_colors:
        while i < len(list_of_colors):
            if keys == list_of_colors[index_colors + i]:
                color += keys
                color_count_1 += 1
                i += 1
            else: 
                i += 1
        i = 0
        while i < len(list_of_colors):
            if keys == list_of_colors[index_colors + i]:
                color_2 += keys
                color_count_2 += 1
                i += 1
            else:
                color_count_2 = 0
                i += 1
        i = 0
        while i < len(list_of_colors):
            if keys == list_of_colors[index_colors + i]:
                color_3 += keys
                color_count_3 += 1
                i += 1
            else: 
                color_count_3 = 0
                i += 1
    if color_count_1 > color_count_2 and color_count_3:
        return color
    else:
        if color_count_2 > color_count_1 and color_count_3:
            return color_2
        else:
            if color_count_3 > color_count_1 and color_count_2:
                return color_3
            else:
                if color_count_1 == color_count_2 or color_count_3:
                    return color


def count(the_list: list[str]) -> dict[str, int]:
    """Creates a dictionary out of a list."""
    my_dictionary: dict[str, int] = {}
