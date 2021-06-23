'''
Chapter-12
Ransom: Randomly capitalizing text

In this chapter, you will
 Learn how to use the random module to figuratively “flip a coin” to decide between two choices
 Explore ways to generate new strings from an existing one, incorporating ran- dom decisions
 Study the similarities of for loops, list comprehensions, and the map() function
'''
import argparse
import os
import random


def get_every_args():
    """Command Line All types Arguments"""
    parseer = argparse.ArgumentParser(description='Random Note',
                                      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    """ Make a Positional Argument"""
    parseer.add_argument('text',
                         metavar='text',
                         help='Input text for file')

    parseer.add_argument('-s',
                         '--seed',
                         help='Random Seed',
                         metavar='int',
                         type=int,
                         default=None)

    argument = parseer.parse_args()

    if os.path.isfile(argument.text):
        argument.text = open(argument.text).read().rstrip()

    return argument

def main():
    '''Make a jazz noise Here'''
    argss = get_every_args()
    text = argss.text
    random.seed(argss.seed)
    ransom = []
    for char in argss.text:
        ransom.append(choose(char))
    print(''.join(ransom))

def choose(char):
    """Randomly choose an upper or lowercase letter to return"""
    return char.upper() if random.choice([0,1]) else char.lower()

def test_choice():
    """Test choose"""
    state = random.getstate()
    random.seed(1)
    assert choose('a') == 'a'
    assert choose('b') == 'b'
    assert choose('c') == 'C'
    assert choose('d') == 'd'
    random.setstate(state)

if __name__ == '__main__':
    main()