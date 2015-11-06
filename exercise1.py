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

vowel = ["a", "e", "i", "o", "u"]


def pig_latinify(word):
    # convert input to lowercase
    word = word.lower()

    # convert input to string
    word = str(word)

    letter_vowel_index = -1

    # searches for vowel
    for i in range(len(word)):
        # Assigning letter_vowel as i
        if word[i] in vowel:
            letter_vowel_index = i
            break

    # if word begins with vowel, add yay to end of word
    first_letter = word[0]
    if first_letter in vowel:
        return word + "yay"

    # begins with consonant, remove all consonants from beginning, append in end + ay
    elif first_letter not in vowel and letter_vowel_index == -1:
        return word + "ay"

    # if word does not have vowels, return original word + ay
    elif first_letter not in vowel and letter_vowel_index != -1 and letter_vowel_index != 0:
        return word[letter_vowel_index:] + word[0:letter_vowel_index] + "ay"

    # if entering a non-string, raise AttributeError
    else:
        raise AttributeError


print(pig_latinify("hhpay"))
