"""
Say Hello Program
Using Commad-line text
Chapter 1
"""

import argparse
import os
import sys
"""
The argparse module is a standard module that is always 
installed with Python. It’s widely used because it can 
save us so much time in parsing and validating the arguments 
to our programs. You’ll be using argparse in every pro- gram 
for this book, and you’ll learn how you can use it to convert 
text to numbers, to validate and open files, and much more. 
"""


def get_args():
   
    parser = argparse.ArgumentParser(description='Say Hello')
    parser.add_argument('name', default='world', help='Name to greet')
    return parser.parse_args()


def main():
    args = get_args()
    print("Hello" + args.name + "!")


if __name__ == '__main__':
    main()


def get_every_args():
    """Command Line All types Arguments"""
    parseer = argparse.ArgumentParser(description='Rock Cash Casbah',
                                      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    """ Make a Positional Argument"""
    parseer.add_argument('positional',
                         metavar='str',
                         help='A named string Argument')
    """ Take Sring"""
    parseer.add_argument('-a',
                        '--arg',
                        help='A named string argument',
                        metavar='str',
                        type=str,
                        default='')
    """ Take Integer"""
    parseer.add_argument('-i',
                         '--int',
                         help='A named integer Argument',
                         metavar='int',
                         type=int, default=0)
    """ Take from file"""
    parseer.add_argument('-f',
                         '--file',
                         help='A readable file',
                         metavar='FILE',
                         type=argparse.FileType('r'), default=None)
    parseer.add_argument('-o',
                         '--on',
                         help='A boolean flag',
                         action='store_true')

    return parseer.parse_args()


def main():
    argss = get_every_args()
    str_arg = argss.arg
    int_arg = argss.int
    file_arg = argss.file
    flag_arg = argss.on
    pos_arg = argss.positional

    print(f'str_arg = "{str_arg}"')
    print(f'int_arg = "{int_arg}"')
    print('file_arg = "{}"'.format(file_arg.name if file_arg else '')) 
    print(f'flag_arg = "{flag_arg}"')
    print(f'positional = "{pos_arg}"')


if __name__ == '__main__':
    main()
