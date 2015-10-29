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

  #  :param :
   # :return:
    #:raises:

   # """
   # result = ""


def pig_latinify(word):

    # convert string to lowercase
    childtalk = word.lower()

    # begins with vowel add yay to end of word
    vowel = ["a", "e", "i", "o", "u"]
    first_letter = childtalk[0]
    if first_letter in vowel:
        print (childtalk + "yay")

    # begins with consonant, remove all consonants from beginning, append in end + ay
    if first_letter not in vowel:
        for i in range(len(childtalk)):
            if childtalk[i] in vowel:
                letter_vowel = i
                break

        print(childtalk[letter_vowel:] + childtalk[:letter_vowel] + "ay")


pig_latinify("scratch")
