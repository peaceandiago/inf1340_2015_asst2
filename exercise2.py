#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

This module converts performs substring matching for DNA sequencing

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

# substring matching - determine whether a shorter string (substring) is
# contained within the longer string


def find(input_string, substring, start, end):
    """
NOT FIND FUNCTION
Write a function that  behaves exactly like find string method
Write a loop for letter by letter comparison
not a string method, string to search is an argument

    :param : input_string, substring, start, end
    :return: index number
    :raises: if string not found, return -1

    """

    # split_string stores the input string that's been sliced
    split_string = input_string[start:end]
    if substring in split_string:
        index = input_string.index(substring,start,end)
        return index
    else:
        return -1


def multi_find(input_string, substring, start, end):
    """
Write a function to find all substring in the input_string and add the index number in a list

    :param : input_string, substring, start, end
    :return: list of index number in a list
    :raises: if string is not found, return empty

    """
    # found_list is a blank list  and an index number is added to it each time a substring is found
    found_list = []
    split_string2 = input_string[start:end]
    if substring in split_string2:
        for index in range(start, end):
            search = find(input_string, substring, index, end)
            if search == index:
                found_list.append(search)
    if len(found_list) > 0:
        return found_list
    else:
        return ""
