'''
Chapter-09
Generating random insults from lists of words

In this exercise, you will learn to
 Use parser.error() from argparse to throw errors
 Control randomness with random seeds
 Take random choices and samples from Python lists
 Iterate an algorithm a specified number of times with a for loop 
 Format output strings

'''
import argparse
import os
import sys
import random


def get_every_args():
    """Command Line All types Arguments"""
    parseer = argparse.ArgumentParser(description='Apples and Bananas',
                                      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    """ Make a Positional Argument"""
    """ For the Number of Adjectives """
    parseer.add_argument('-a'
                        '--adjectives',
                         help='Number of adjectives',
                         metavar='adjectives',
                         type = int,
                         default= 2)

    parseer.add_argument('-n',
                         '--number',
                         help='Number of adjectives',
                         metavar='adjectives',
                         type=int,
                         default=3)

    parseer.add_argument('-s',
                         '--seed',
                         help='Random Seed',
                         metavar='seed',
                         type=int,
                         default = None)

    argument = parseer.parse_args()
    '''Check that args.adjectives is greater than 0. If there is a problem, 
    call parser.error() with the error message.'''
    if argument.adjectives < 1:
        parseer.error('--adjectives "{}" must be > 0'.format(argument.adjectives))
    
    if argument.number < 1:
        parseer.error('--number "{}" must be > 0'.format(argument.number))
    
    return argument

def main():
    argss = get_every_args()
    random.seed(argss.seed)
    adjectives = """ bankrupt base caterwauling corrupt cullionly detestable 
    dishonest false filthsome filthy foolish foul 
    gross heedless indistinguishable infected insatiate 
    irksome lascivious lecherous loathsome lubbery 
    old peevish rascaly rotten ruinous scurilous scurvy 
    slanderous sodden-witted thin-faced toad-spotted 
    unmannered vile wall-eyed """.strip().split()
    
    nouns = """ Judas Satan ape ass barbermonger beggar 
    block boy braggart butt carbuncle coward coxcomb 
    cur dandy degenerate fiend fishmonger fool gull 
    harpy jack jolthead knave liar lunatic maw milksop 
    minion ratcatcher recreant rogue scold slave 
    swine traitor varlet villain worm """.strip().split()

    for _ in range(argss.number):
        adjs = ','.join(random.sample(adjectives, k=argss.adjectives)) 
        print(f'You {adjs} {random.choice(nouns)}!')


if __name__ == '__main__':
    main()
