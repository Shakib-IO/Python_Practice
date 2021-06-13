'''
Chapter-08
Apples and Bananas: Find and replace


Your program is going to need to do the following:
 Take a positional argument that might be some plain text or may name a file
 If the argument is a file, use the contents as the input text
 Take an optional -v or --vowel argument that should default to the letter “a”
 Verify that the --vowel option is in the set of vowels “a,” “e,” “i,” “o,” and “u”
 Replace all instances of vowels in the input text with the specified (or default) --vowel argument
 Print the new text to STDOUT

Methods Like -
str.replace() 
str.translate()
'''
import argparse
import os
import sys


def get_every_args():
    """Command Line All types Arguments"""
    parseer = argparse.ArgumentParser(description='Apples and Bananas',
                                      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    """ Make a Positional Argument"""
    """ Take from file"""
    parseer.add_argument('text',
                         help='Input text or file',
                         metavar='text')

    parseer.add_argument('-v',
                         '--vowel',
                         help='The Vowel Allowed',
                         metavar='vowel',
                         type=str,
                         choices=list('aeiou'),
                         default='a')

    args = parseer.parse_args()
    '''Check if the text argument is file'''
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()
    return args


def main():
    argss = get_every_args()

    # Create a Dictionary
    text = argss.text
    vowel = argss.vowel
    new_text = []
    for char in text:
        if char in 'aeiou':
            new_text.append(vowel)
        elif char in 'AEIOU':
            new_text.append(vowel.upper())
        else:
            new_text.append(char)
    print(''.join(new_text))

if __name__ == '__main__':
    main()
