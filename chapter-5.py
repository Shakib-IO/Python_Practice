'''
Chapter 5: Working with files and STDOUT

In this exercise, you will learn to
 Accept text input from the command line or from a file
 Change strings to uppercase
 Print output either to the command line or to a file that needs to be created  Make plain text behave like a file handle

'''

import argparse
import os
import sys


def get_every_args():
    """Command Line All types Arguments"""
    parseer = argparse.ArgumentParser(description='Howler',
                                      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    """ Make a Positional Argument"""
    parseer.add_argument('text',
                         metavar='str',
                         help='Input String or File')
    
    parseer.add_argument('-o',
                         '--outfile',
                         help='Output filename',
                         metavar='str',
                         type= str,
                         default='')

    args = parseer.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


def main():
    argss = get_every_args()
    out_fh = open(argss.outfile, 'wt') if argss.outfile else sys.stdout
    out_fh.write(argss.text.upper() + '\n')
    out_fh.close()



if __name__ == '__main__':
    main()
