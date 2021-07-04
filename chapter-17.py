'''
Chapter-17
Mad Libs: Using regular expressions

In this exercise, you will
 Learn to use sys.exit() to halt your program and indicate an error status  Learn about greedy matching with regular expressions
 Use re.findall() to find all matches for a regex
 Use re.sub() to replace found patterns with new text
 Explore ways to write the solution without using regular expressions
'''
import argparse
import os
import re  # Regular Expressions
import sys


def get_every_args():
    """Command Line All types Arguments"""
    parseer = argparse.ArgumentParser(description='Mad Libs',
                                      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    """ Make a Positional Argument"""
    parseer.add_argument('file',
                         metavar='FILE',
                         type=argparse.FileType('rt'),
                         help='Input file')

    parseer.add_argument('-i',
                         '--inputs',
                         help='Inputs (for testing)',
                         metavar='input',
                         type=str,
                         nargs='*')

    return parseer.parse_args()


def main():
    '''Make a jazz noise Here'''
    argss = get_every_args()
    inputs = argss.inputs
    text = argss.file.read().rstrip()
    blanks = re.findall('(<([^<>]+)>)', text)

    if not blanks:
        sys.exit(f'"{argss.file.name}" has no placeholders.')

    tmpl = 'Give me {} {}: '
    for placeholder, pos in blanks:
        article = 'an' if pos.lower()[0] in 'aeiou' else 'a'
        answer = inputs.pop(0) if inputs else input(tmpl.format(article, pos))
        text = re.sub(placeholder, answer, text, count=1)
    print(text)


if __name__ == '__main__':
    main()
