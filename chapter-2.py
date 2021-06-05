"""
Chapter 02
- Create a program that accepts a positional argument and produces usage documentation
- Create a new output string depending on the inputs to the program
- Run a test suite

Your program should be called chapter-2.py. It will accept a single 
positional argu- ment and will print the given argument inside 
the “Ahoy” bit, along with the word “a” or “an” depending on 
whether the argument starts with a consonant or a vowel.

That is, if given “narwhal,” it should do this:
$ ./chapter-2.py narwhal
Ahoy, Captain, a narwhal off the larboard bow!
And if given “octopus,”
$ ./chapter-2.py octopus
Ahoy, Captain, an octopus off the larboard bow!

"""

import argparse
import os
import sys


def get_every_args():
    """Command Line All types Arguments"""
    parseer = argparse.ArgumentParser(description='Rock Cash Casbah',
                                      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    """ Make a Positional Argument"""
    parseer.add_argument('word',
                         metavar='object',
                         help='A named string Argument')
    return parseer.parse_args()


def main():
    argss = get_every_args()
    word = (argss.word).lower()
    if word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u':
        article = 'an'
    else:
        article = 'a'
    print(f'Ahoy, Captain, {article} {word} off the larboard bow!')


if __name__ == '__main__':
    main()