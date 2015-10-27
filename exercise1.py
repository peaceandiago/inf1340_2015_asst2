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

def pig_latinify(childtalk):
    #begins with vowel add yay to end of word
    vowel = ["a", "e", "i", "o", "u"]
    first_letter = childtalk[0]
    if first_letter in vowel:
        print (childtalk + "yay")
    #begins with consonant, remove consonant from beginning, append in end + ay
    else:
        print (childtalk[1:] + first_letter + "ay")

pig_latinify("dagro")
