'''
Chapter-14
Using regular expressions to create rhyming words

In this program, you will
 Learn to write and use regular expressions
 Use a guard with a list comprehension
 Explore the similarities of list comprehension with a guard to the filter() function
 Entertain ideas of “truthiness” when evaluating Python types in a Boolean context
'''
import argparse
import string
import sys
import re
from typing import Pattern  # Regular Expressions


def get_every_args():
    """Command Line All types Arguments"""
    parseer = argparse.ArgumentParser(description='Make rhyming words',
                                      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    """ Make a Positional Argument"""
    parseer.add_argument('word',
                         metavar='word',
                         help='A word to rhyme')

    return parseer.parse_args()


def main():
    '''Make a jazz noise Here'''
    argss = get_every_args()
    prefixes = list('bcdfghjklmnpqrstvwxyz') + (
        'bl br ch cl cr dr fl fr gl gr pl pr sc '
        'sh sk sl sm sn sp st sw th tr tw thw wh wr '
        'sch scr shr sph spl spr squ str thr').split()
    start, rest = stemmer(argss.word)
    if rest:
        print('\n'.join(sorted([p + rest for p in prefixes if p != start])))
    else:
        print(f'Cannot rhyme "{argss.word}')


def stemmer(word):
    word = word.lower()
    vowels = 'aeiou'
    consonants = ''.join(
        [c for c in string.ascii_lowercase if c not in vowels])
    pattern = (
        '([' + consonants + ']+)?'
        '([' + vowels + '])'
        '(.*)'
    )

    match = re.match(pattern, word)
    if match:
        p1 = match.group(1) or ''
        p2 = match.group(2) or ''
        p3 = match.group(3) or ''
        return (p1, p2+p3)
    else:
        return(word, '')


if __name__ == '__main__':
    main()
