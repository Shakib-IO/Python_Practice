'''
Chapter-16
The scrambler: Randomly reordering the middles of words

In this chapter you will
 Use a regular expression to split text into words
 Use the random.shuffle() function to shuffle a list
 Create scrambled versions of words by shuffling the middle letters while leaving the first and last letters unchanged
'''
import argparse
import os
import re  # Regular Expressions
import random


def get_every_args():
    """Command Line All types Arguments"""
    parseer = argparse.ArgumentParser(description='Scramble the letters of words',
                                      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    """ Make a Positional Argument"""
    parseer.add_argument('text',
                         metavar='text',
                         help='Input text or file')

    parseer.add_argument('-s',
                         '--seed',
                         help='Seed',
                         metavar='seed',
                         type=int,
                         default=None)

    argu = parseer.parse_args()

    if os.path.isfile(argu.text):
        argu.text = open(argu.text).read().rstrip()
    return argu


def main():
    '''Make a jazz noise Here'''
    argss = get_every_args()
    random.seed(argss.seed)
    splitter = re.compile("([a-zA-Z](?:[a-zA-Z']*[a-zA-Z])?)")
    for line in argss.text.splitlines():
        ''' Use the splitter to break the line 
        into a new list that map() will feed 
        into the scramble() function. Join 
        the resulting list on the empty string 
        to create a new str to print.'''
        print(''.join(map(scramble, splitter.split(line))))


def scramble(word):
    if len(word) > 3 and re.match(r'\w+', word):
        middle = list(word[1:-1])
        random.shuffle(middle)
        word = word[0] + ''.join(middle)+word[-1]
    return word


def test_scramble():
    """Test scramble : The test for the scramble() function"""
    random.seed(1)
    assert scramble("a") == "a"
    assert scramble("ab") == "ab"
    assert scramble("abc") == "abc"
    assert scramble("abcd") == "acbd"
    assert scramble("abcde") == "acbde"
    assert scramble("abcdef") == "aecbdf"
    assert scramble("abcde'f") == "abcd'ef"
    random.seed(None)


if __name__ == '__main__':
    main()
