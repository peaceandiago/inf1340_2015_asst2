#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


#####################
# HELPER FUNCTIONS ##
#####################
def remove_duplicates(l):
    """
    Removes duplicates from l, where l is a List of Lists.
    :param l: a List
    """

    d = {}
    result = []
    for row in l:
        if tuple(row) not in d:
            result.append(row)
            d[tuple(row)] = True

    return result


class MismatchedAttributesException(Exception):
    """
    Raised when attempting set operations with tables that
    don't have the same attributes.
    """
    pass

###############
# FUNCTIONS  ##
##############


def union(table1, table2):
    """
     Perform the union set operation on tables, table1 and table2.

     :param table1: a table (a List of Lists)
     :param table2: a table (a List of Lists)
     :return: the resulting table that contains all unique rows that appear in either table
     :raises: MismatchedAttributesException:
         if tables t1 and t2 don't have the same attributes
    """

    if table1[0] != table2[0]:
        raise MismatchedAttributesException
    union_list = []
    for rows1 in table1:
        union_list.append(rows1)
    for rows2 in table2:
        union_list.append(rows2)
    union_list = remove_duplicates(union_list)

    return union_list


def intersection(table1, table2):
    """
     Perform the intersection set operation on tables, table1 and table2.

     :param table1: a table (a List of Lists)
     :param table2: a table (a List of Lists)
     :return: the resulting table that contains all unique rows that appear in both table
     :raises: MismatchedAttributesException:
         if tables t1 and t2 don't have the same attributes

    """
    if table1[0] != table2[0]:
        raise MismatchedAttributesException
    intersection_list = []
    for rows1 in table1:
        for rows2 in table2:
            if rows1 == rows2:
                intersection_list.append(rows1)

    return intersection_list


def difference(table1, table2):
    """
     Perform the difference set operation on tables, table1 and table2.

     :param table1: a table (a List of Lists)
     :param table2: a table (a List of Lists)
     :return: the resulting table that contains all unique rows that appear in table1 only, not table2
     :raises: MismatchedAttributesException:
         if tables t1 and t2 don't have the same attributes

    """
    if table1[0] != table2[0]:
        raise MismatchedAttributesException
    intersected_list = intersection(table1,table2)
    del intersected_list[0]
    for intersected_row in intersected_list:
        for table1_row in table1:
            if table1_row == intersected_row:
                table1.remove(table1_row)
    return table1


