'''
Chapter-14
The scrambler: Randomly reordering the middles of words

In this chapter you will
 Use a regular expression to split text into words
 Use the random.shuffle() function to shuffle a list
 Create scrambled versions of words by shuffling the middle letters while leaving the first and last letters unchanged
'''
import argparse
import os
import re  # Regular Expressions


def get_every_args():
    """Command Line All types Arguments"""
    parseer = argparse.ArgumentParser(description='Southern fry text',
                                      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    """ Make a Positional Argument"""
    parseer.add_argument('text',
                         metavar='text',
                         help='Input text or file')

    argu = parseer.parse_args()
    if os.path.isfile(argu.text):
        argu.text = open(argu.text).read()
    return argu


def main():
    '''Make a jazz noise Here'''
    argss = get_every_args()
    for line in argss.text.splitlines():
        print(''.join(map(fry, re.split(r'(\W+)', line.rstrip()))))


def fry(word):
    ing_word = re.search('(.+)ing$', word)
    you = re.match('([Yy])ou$', word)

    if ing_word:
        prefix = ing_word.group(1)
        if re.search('[aeiouy]', prefix, re.IGNORECASE):
            return prefix + "in'"
    elif you:
        return you.group(1) + "'all"
    return word


if __name__ == '__main__':
    main()
