#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"
#"""
 #   Describe your function

  #  :param : word passed on to the function
   # :return:
    #:raises: if an integer is entered, raises AttributeError

   # """
   # result = ""


def pig_latinify(child_talk):

    # convert string to lowercase
    child_talk = child_talk.lower()

    # begins with vowel add yay to end of word
    vowel = ["a", "e", "i", "o", "u"]
    first_letter = child_talk[0]
    if first_letter in vowel:
        print (child_talk + "yay")

    # begins with consonant, remove all consonants from beginning, append in end + ay
    elif first_letter not in vowel:
        for i in range(len(child_talk)):
            # Assigning letter_vowel as i
            if child_talk[i] in vowel:
                letter_vowel = i
                break
        print(child_talk[letter_vowel:] + child_talk[:letter_vowel] + "ay")

    else:
        raise AttributeError


pig_latinify("spoon")
