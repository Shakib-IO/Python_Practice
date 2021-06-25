'''
Chapter-13
Twelve Days of Christmas: Algorithm design

In this exercise, you will
 Create an algorithm to generate “The Twelve Days of Christmas” from any given day in the range 1–12
 Reverse a list
 Use the range() function
 Write text to a file or to STDOUT
'''
import argparse
import os
import sys


def get_every_args():
    """Command Line All types Arguments"""
    parseer = argparse.ArgumentParser(description='Twelve Days of Christmas',
                                      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    """ Make a Positional Argument"""
    parseer.add_argument('-n',
                         '--num',
                         metavar='days',
                         help='Number of days to sing',
                         type=int,
                         default=12
                         )

    parseer.add_argument('-o',
                         '--outfile',
                         help='OutFile',
                         metavar='FILE',
                         type=argparse.FileType('wt'),
                         default=sys.stdout
                         )

    argument = parseer.parse_args()

    if argument.num not in range(1, 13):
        parseer.error(f'--num "{argument.num}" must be between 1 and 12')

    return argument


def main():
    '''Make a jazz noise Here'''
    argss = get_every_args()
    verses = map(verse, range(1, argss.num + 1))
    print('\n\n'.join(verses), file=argss.outfile)


def verse(day):
    ordinal = [
        'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth'
    ]
    gifts = [
        'A partridge in a pear tree.',
        'Two turtle doves,',
        'Three French hens,',
        'Four calling birds,',
        'Five gold rings,',
        'Six geese a laying,',
        'Seven swans a swimming,',
        'Eight maids a milking,',
        'Nine ladies dancing,',
        'Ten lords a leaping,',
        'Eleven pipers piping,',
        'Twelve drummers drumming,', ]
    lines = [
        f'On the {ordinal[day - 1]} day of Christmas,',
        'My true love gave to me,'
    ]

    lines.extend(reversed(gifts[:day]))
    if day > 1:
        lines[-1] = 'And ' + lines[-1].lower()

    return '\n'.join(lines)


if __name__ == '__main__':
    main()
