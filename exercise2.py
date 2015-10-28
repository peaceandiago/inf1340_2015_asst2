#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

This module converts performs substring matching for DNA sequencing

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

#substring matching - determine whether a shorter string (substring) is
#contained within the longer string

def find(input_string, substring, start, end):
    """
#NOT FIND FUNCTION
#Write a function that  behaves exactly like find string method
#Write a loop for letter by letter comparison
#not a string method, string to search is an argument

    :param :
    :return:
    :raises:

    """
DNA = "GAATGTCCTTTCTCTAAGTCCTAAG"
#search = DNA.find("GTCC",0, len(DNA))
#The above is the result they want to achieve w/o the find function
#Refer above to know what answer they want

wanted_DNA = "GTC"
if wanted_DNA in DNA:
    index = DNA.index(wanted_DNA) #DOES THE SAME AS ABOVE
    print(index)
else:
    print ("-1")

#for index in range (0, len(wanted_DNA)):
#    search = DNA["GAAT"]
#    print(search)

#if search != -1:
#    print("String found")
#else:
 #  return = -1

#def multi_find(input_string, substring, start, end):
 #   """
 #   Describe your function

  #  :param :
   # :return:
    #:raises:

   # """
   # result = ""

    #return result

