#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

Test module for exercise2.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


from exercise2 import find, multi_find


def test_find_basic():
    """
    Test find function.
    """
    assert find("This is an ex-parrot", "parrot", 0, 20) == 14
    assert find("Where is the cookie", "the", 3, 15) == 9
    assert find("ABCDEFFGABCDEFF", "FF", 8, 11) == -1
    try:
        find(239239081, "integers", 0, 20)
    except TypeError:
        assert True
    else:
        assert False

def test_multi_find_basic():
    """
    Test multi_find function.
    """
    assert multi_find("Ni! Ni! Ni! Ni!", "Ni", 0, 20) == [0, 4, 8, 12]
    assert multi_find("ABCDEFFGABCDEFF", "FF", 3, 15) == [5, 13]
    assert multi_find("Ni! Ni! Ni! Ni!", "No", 0, 20) == ""

    try:
        multi_find(12382938293, "asldasd", 0, 15)
    except TypeError:
        assert True
    else:
        assert False
