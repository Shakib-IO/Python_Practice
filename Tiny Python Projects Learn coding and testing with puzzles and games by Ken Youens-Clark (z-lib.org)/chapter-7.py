'''
Chapter-07
Looking items up in a dictionary

In this exercise, you will
 Accept one or more positional arguments that we’ll call letter.
 Accept an optional --file argument, which must be a readable text file. The default value will be 'gashlycrumb.txt' (provided).
 Read the file, find the first letter of each line, and build a data structure that associates the letter to the line of text. (We’ll only be using files where each line starts with a single, unique letter. This program would fail with any other format of text.)
 For each letter provided by the user, either print the line of text for the let- ter if present, or print a message if it isn’t.
 Learn how to “pretty-print” a data structure.
'''
import argparse
import os
import sys


def get_every_args():
    """Command Line All types Arguments"""
    parseer = argparse.ArgumentParser(description='Rock Cash Casbah',
                                      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    """ Make a Positional Argument"""
    """ Take from file"""
    parseer.add_argument('letter',
                         nargs='+',
                         help='Letters',
                         metavar='letter',
                         type=str)

    parseer.add_argument('-f',
                         '--file',
                         nargs='*',
                         help='Input file',
                         metavar='FILE',
                         type=argparse.FileType('rt'),
                         default=sys.stdin)

    return parseer.parse_args()


def main():
    argss = get_every_args()

    # Create a Dictionary
    lookup = {}
    for line in argss.file:
        lookup[line[0].upper()] = line.rstrip()

    for letter in argss.letter:
        if letter.upper() in lookup:
            print(lookup[letter.upper()])
        else:
            print(f'I do not know "{letter}".')


if __name__ == '__main__':
    main()
