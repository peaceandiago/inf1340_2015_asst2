#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

# Describe your function
# :param : word passed on to the function
# :return: if begins with vowel, add "yay" to the end.
# if begins with consonant, move consonant(s) to end and add "ay"
# :raises: if an integer is entered, raises AttributeError


def pig_latinify(child_talk):
    # convert string to lowercase
    child_talk = child_talk.lower()

    # begins with vowel add yay to end of word
    vowel = ["a", "e", "i", "o", "u"]
    first_letter = child_talk[0]
    if first_letter in vowel:
        return child_talk + "yay"

    # begins with consonant, remove all consonants from beginning, append in end + ay
    elif first_letter not in vowel:
        for i in range(len(child_talk)):
            # Assigning letter_vowel as i
            if child_talk[i] in vowel:
                letter_vowel = i
                break
        # once the vowel is found in child_talk, print the vowel first, move consonants to end, append "ay"
        return child_talk[letter_vowel:] + child_talk[:letter_vowel] + "ay"

    # if entering a non-string, raise AttributeError
    else:
        raise AttributeError
