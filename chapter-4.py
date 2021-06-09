'''
Chapter-4: Working with dictionaries

In this exercise, we’ll discuss how to encrypt 
messages using this algorithm, and then we’ll 
see how to use it to decrypt the encrypted messages.

In this chapter, you will learn to
 Create a dictionary
 Use a for loop and a list comprehension to process text, character by character 
 Check if items exist in a dictionary
 Retrieve values from a dictionary
 Print a new string with the numbers substituted with their encoded values

A Python dictionary allows us to relate some thing (a “key”) to 
some other thing (a “value”). An actual dictionary does this. 
If we look up a word like “quirky” in a dictionary , 
we can find a definition. We can think of the word itself 
as the “key” and the defini- tion as the “value.”
'''
import argparse
import os
import sys


def get_every_args():
    """Command Line All types Arguments"""
    parseer = argparse.ArgumentParser(description='Rock Cash Casbah',
                                      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    """ Make a Positional Argument"""
    parseer.add_argument('text',
                         metavar='str',
                         help='Input String')

    return parseer.parse_args()


def main():
    argss = get_every_args()
    jumper = {'1': '9', '2': '8', '3': '7', '4': '6', '5': '0',
              '6': '4', '7': '3', '8': '2', '9': '1', '0': '5'}
    for char in argss.text:
        print(jumper.get(char, char), end='')
    print()


if __name__ == '__main__':
    main()
