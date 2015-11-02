#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

Test module for exercise1.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


from exercise1 import pig_latinify


def test_pig_latinify():
    """
    Basic test cases from assignment hand out
    """
    assert pig_latinify("dog") == "ogday"
    assert pig_latinify("scratch") == "atchscray"
    assert pig_latinify("is") == "isyay"
    assert pig_latinify("apple") == "appleyay"

    # Testing words with uppercase
    assert pig_latinify("Almond") == "almondyay"
    assert pig_latinify("Phone") == "onephay"
    assert pig_latinify("wHaT") == "atwhay"
    assert pig_latinify("PHarmAcy") == "armacyphay"


# Test function for input error using integer
def test_input_error():
    try:
        pig_latinify(22)
    except AttributeError:
        assert True



