#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

Test module for exercise3.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from exercise3 import union, intersection, difference, MismatchedAttributesException


###########
# TABLES ##
###########
GRADUATES = [["Number", "Surname", "Age"],
             [7274, "Robinson", 37],
             [7432, "O'Malley", 39],
             [9824, "Darkes", 38]]

MANAGERS = [["Number", "Surname", "Age"],
            [9297, "O'Malley", 56],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38]]

STAFF = [["ID", "Name", "Position", "Age"],
         [7466, "Frank Underwood", "President", 55],
         [5323, "Jeffrey Winger", "Former Lawyer", 40],
         [1233, "Piper Chapman", "Prisoner", 31],
         [4383, "Oliver Dart", "Unknown", 23]]

PROFESSORS = [["Number", "Surname", "Age"],
              [7434, "Silva", 33],
              [8374, "Cray", 40],
              [9824, "Darkes", 38]]


#####################
# HELPER FUNCTIONS ##
#####################
def is_equal(t1, t2):
    return set(map(tuple, t1)) == set(map(tuple, t2))


###################
# TEST FUNCTIONS ##
###################
def test_union():
    """
    Test union operation.
    """

    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37],
              [9297, "O'Malley", 56],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, union(GRADUATES, MANAGERS))

    result = [["Number", "Surname", "Age"],
              [7434, "Silva", 33],
              [8374, "Cray", 40],
              [9824, "Darkes", 38],
              [7274, "Robinson", 37],
              [7432, "O'Malley", 39]]

    assert is_equal(result, union(PROFESSORS, GRADUATES))

    try:
        is_equal(result, difference(GRADUATES, STAFF))
    except MismatchedAttributesException:
        assert True


def test_intersection():
    """
    Test intersection operation.
    """
    result = [["Number", "Surname", "Age"],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, intersection(PROFESSORS, MANAGERS))

    result = [["Number", "Surname", "Age"],
              [9824, "Darkes", 38]]

    assert is_equal(result, intersection(PROFESSORS, MANAGERS))

    try:
        is_equal(result, difference(GRADUATES, STAFF))
    except MismatchedAttributesException:
        assert True


def test_difference():
    """
    Test difference operation.
    """

    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37]]

    assert is_equal(result, difference(GRADUATES, MANAGERS))


    result = [["Number", "Surname", "Age"],
              [9297, "O'Malley", 56],
              [7432, "O'Malley", 39]]

    assert is_equal(result, difference(MANAGERS, PROFESSORS))

    try:
        is_equal(result, difference(GRADUATES, STAFF))
    except MismatchedAttributesException:
        assert True