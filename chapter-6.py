'''
Chapter-06
Reading files and STDIN, iterating lists, formatting strings

In this chapter, you will
 Learn how to process zero or more positional arguments 
 Validate input files
 Read from files or from standard input
 Use multiple levels of for loops
 Break files into lines, words, and bytes  Use counter variables
 Format string output
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
    parseer.add_argument('file',
                         nargs='*',
                         help='Input file',
                         metavar='FILE',
                         type=argparse.FileType('rt'), 
                         default = sys.stdin )

    return parseer.parse_args()


def main():
    argss = get_every_args()
    


if __name__ == '__main__':
    main()
