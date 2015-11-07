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
         [1233, "Piper Chapman", "Prisoner", 31],
         [4383, "Oliver Dart", "Unknown", 23]]

PROFESSORS = [["Number", "Surname", "Age"],
              [7434, "Silva", 33],
              [8374, "Cray", 40],
              [9824, "Darkes", 38]]

BLANK = [["Number", "Surname", "Age"]]


#####################
# HELPER FUNCTIONS ##
#####################
def is_equal(t1, t2):
    return sorted(t1) == sorted(t2)


###################
# TEST FUNCTIONS ##
###################
def test_union():
    """
    Test union operation.
    """

    result = [["Number", "Surname", "Age"],
              [9297, "O'Malley", 56],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38],
              [7274, "Robinson", 37]]

    assert result == union(MANAGERS, GRADUATES)

    result = [["Number", "Surname", "Age"],
              [7434, "Silva", 33],
              [8374, "Cray", 40],
              [9824, "Darkes", 38],
              [7274, "Robinson", 37],
              [7432, "O'Malley", 39]]

    assert result == union(PROFESSORS, GRADUATES)

    result = [['Number', 'Surname', 'Age'],
              [7274, 'Robinson', 37],
              [7432, "O'Malley", 39],
              [9824, 'Darkes', 38],
              [9297, "O'Malley", 56]]

    assert result == union(GRADUATES,MANAGERS)

    try:
        assert result == union(GRADUATES, STAFF)
    except MismatchedAttributesException:
        assert True


def test_intersection():
    """
    Test intersection operation.
    """
    result = [["Number", "Surname", "Age"],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert result == intersection(GRADUATES, MANAGERS)

    result = [["Number", "Surname", "Age"],
              [9824, "Darkes", 38]]

    assert result == intersection(PROFESSORS, MANAGERS)

    assert intersection(GRADUATES, BLANK) is None

    try:
        assert result == intersection(GRADUATES, STAFF)
    except MismatchedAttributesException:
        assert True


def test_difference():
    """
    Test difference operation.
    """

    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37]]

    assert result == difference(GRADUATES, MANAGERS)

    result = [["Number", "Surname", "Age"],
              [9297, "O'Malley", 56],
              [7432, "O'Malley", 39]]

    assert result == difference(MANAGERS, PROFESSORS)

    assert difference(BLANK, GRADUATES) is None

    try:
        assert result == difference(GRADUATES, STAFF)
    except MismatchedAttributesException:
        assert True

