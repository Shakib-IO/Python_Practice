'''
Chapter-10
Telephone: Randomly mutating strings

In this exercise, you will learn to
 Round numbers
 Use the string module
 Modify strings and lists to introduce random mutations

'''
import argparse
import os
import sys
import random
import string


def get_every_args():
    """Command Line All types Arguments"""
    parseer = argparse.ArgumentParser(description='Telephones',
                                      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    """ Make a Positional Argument"""
    parseer.add_argument('text',
                        metavar='text',
                        help='Input text for file')
    
    parseer.add_argument('-s',
                         '--seed',
                         help='Random Seed',
                         metavar='seed',
                         type=int,
                         default=None)

    parseer.add_argument('-m',
                         '--mutation',
                         help='Percent Mutations',
                         metavar='mutations',
                         type=float,
                         default=0.1)

    argument = parseer.parse_args()

    if not 0 <= argument.mutation <= 1:
        parseer.error(
            f'--mutation "{argument.mutation}" must be between 0 and 1')

    if os.path.isfile(argument.text):
        argument.text = open(argument.text).read().rstrip()

    return argument


def main():
    '''Make a jazz noise Here'''

    argss = get_every_args()
    text = argss.text
    random.seed(argss.seed)
    alpha = ''.join(sorted(string.ascii_letters + string.punctuation))
    len_text = len(text)
    num_mutations=round(argss.mutations*len_text)
    new_text=text

    for i in random.sample(range(len_text), num_mutations):
        new_char=random.choice(alpha.replace(new_text[i], ''))
        new_text=new_text[:i] + new_char + new_text[i + 1:]

    print(f'You said: "{text}"\nI heard : "{new_text}"')

if __name__ == '__main__':
    main()
