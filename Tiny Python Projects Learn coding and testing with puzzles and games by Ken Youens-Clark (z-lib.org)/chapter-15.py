'''
Chapter-15
The Kentucky Friar: More regular expressions
 Learn more about using regular expressions
 Use both re.match() and re.search() to find patterns anchored to the beginning of a string or anywhere in the string, respectively
 Learn how the $ symbol in a regex anchors a pattern to the end of a string
 Learn how to use re.split() to split a string
 Explore how to write a manual solution for finding two-syllable “-ing” words or the word “you”
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
