"""
Chapter 03
Working with list


The list.append() and list.extend() methods add new elements to 
the end of a given list. The list.insert() method allows you to 
place new items at any position by specifying the index

Slicing lists:You can extract “slices” (sub-lists) of a list by using 
list[start:stop]. 
"""
import argparse
import os
from posixpath import join
import sys


def get_every_args():
    """Command Line All types Arguments"""
    parseer = argparse.ArgumentParser(description='Picnic Game',
                                      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    """ Make a Positional Argument"""
    parseer.add_argument('items',
                         metavar='items',
                         nargs='+',
                         help='List of Items')

    parseer.add_argument('-s',
                         '--sorted',
                         help='Whether items are sorted',
                         action='store_true')

    return parseer.parse_args()


def main():
    argss = get_every_args()
    items = argss.items
    sizeOfList = len(items)
    if argss.sorted:
        items.sort()
    
    """Use an empty string to initialize a 
    variable to hold the items we are bringing."""
    intotheList = ' '
    if sizeOfList == 1:
        intotheList = items(0)
    elif sizeOfList == 2:
        intotheList = ' and '.join(items)
    else:
        items[-1] = 'and' + items[-1]
        intotheList = ','.join(items)
    print('You are bringing {}.'.format(intotheList))

if __name__ == '__main__':
    main()
