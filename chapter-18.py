'''
Chapter-18
Gematria: Numeric encoding of text using ASCII values
In this exercise, you will
 Learn about the ord() and chr() functions
 Explore how characters are organized in the ASCII table
 Understand character ranges used in regular expressions
 Use the re.sub() function
 Learn how map() can be written without lambda
 Use the sum() function and see how that relates to using reduce() 
 Learn how to perform case-insensitive string sorting'''

import argparse
import os
import re  # Regular Expressions
import sys


def get_every_args():
    """Command Line All types Arguments"""
    parseer = argparse.ArgumentParser(description='Gematria',
                                      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    """ Make a Positional Argument"""
    parseer.add_argument('text',
                         metavar='text',
                         help='Input file or text')

    argu = parseer.parse_args()
    if os.path.isfile(argu.text):
        argu.text = open(argu.text).read().rstrip()
    return argu


def main():
    '''Make a jazz noise Here'''
    argss = get_every_args()

    for line in argss.text.splitlines():
        print(' '.join(map(word2num, line.split())))


def word2num(word):
    return str(sum(map(ord, re.sub('[^A-Za-z0-9]', '', word))))


def test_word2num():
    """Test word2num"""


assert word2num("a") == "97"
assert word2num("abc") == "294"
assert word2num("ab'c") == "294"
assert word2num("4a-b'c,") == "346"

if __name__ == '__main__':
    main()
