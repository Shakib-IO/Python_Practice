'''
Chapter-20
Password strength: Generating a secure and memorable password
In this exercise, you will
 Take a list of one or more input files as positional arguments  Use a regular expression to remove non-word characters
 Filter words by some minimum length requirement
 Use sets to create unique lists
'''
import argparse
import re  # Regular Expressions
import string
import random


def get_every_args():
    """Command Line All types Arguments"""
    parseer = argparse.ArgumentParser(description='Password maker',
                                      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    """ Make a Positional Argument"""
    parseer.add_argument('file',
                         metavar='FILE',
                         type=argparse.FileType('rt'),
                         nargs='+',
                         help='Input file(s)')
    parseer.add_argument('-n',
                         '--num',
                         metavar='num_passwords',
                         type=int,
                         default=3,
                         help='Number of passwords to generate')
    parseer.add_argument('-w',
                         '--num_words',
                         metavar='num_words',
                         type=int,
                         default=4,
                         help='Number of words to use for password')
    parseer.add_argument('-m',
                         '--min_word_len',
                         metavar='minimum',
                         type=int,
                         default=3,
                         help='Minimum word length')
    parseer.add_argument('-x',
                         '--max_word_len',
                         metavar='maximum',
                         type=int,
                         default=6,
                         help='Maximum word length')
    parseer.add_argument('-s',
                         '--seed',
                         metavar='seed',
                         type=int,
                         help='Random seed')
    parseer.add_argument('-l',
                         '--l33t',
                         action='store_true',
                         help='Obfuscate letters')
    return parseer.parse_args()


def main():
    '''Make a jazz noise Here'''
    args = get_every_args()
    random.seed(args.seed)
    words = set()

    def word_len(word):
        return args.min_word_len <= len(word) <= args.max_word_len

    for fh in args.file:
        for line in fh:
            for word in filter(word_len, map(clean, line.lower().split())):
                words.add(word.title())

    words = sorted(words)
    passwords = [
        ''.join(random.sample(words, args.num_words)) for _ in range(args.num)
    ]
    if args.l33t:
        passwords = map(l33t, passwords)

    print('\n'.join(passwords))


def clean(word):
    return re.sub('[^a-zA-Z]', '', word)


def l33t(text):
    text = ransom(text) 
    xform = str.maketrans({
        'a': '@', 'A': '4', 'O': '0', 't': '+', 'E': '3', 'I': '1', 'S': '5'})
    return text.translate(xform) + random.choice(string.punctuation)


def ransom(text):
    return ''.join(
        map(lambda c: c.upper() if random.choice([0, 1]) else c.lower(), text))


if __name__ == '__main__':
    main()
