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

vowel = ["a", "e", "i", "o", "u"]

def pig_latinify(word):
    # begins with vowel add yay to end of word
    word = word.lower()
    first_letter = word[0]
    if first_letter in vowel:
        print (word + "yay")

    return

pig_latinify("Orange")
