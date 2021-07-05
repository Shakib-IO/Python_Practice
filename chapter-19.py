'''
Chapter-19
Workout of the Day: Parsing CSV files, creating text table output
In this exercise, you will
 Parse delimited text files using the csv module  Coerce text values to numbers
 Print tabular data using the tabulate module  Handle missing and malformed data
'''
import argparse
import csv
import io
import re  # Regular Expressions
import sys
import random
from tabulate import tabulate


def get_every_args():
    """Command Line All types Arguments"""
    parseer = argparse.ArgumentParser(description='Create Workout Of (the) Day (WOD)',
                                      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    """ Make a Positional Argument"""
    parseer.add_argument('-f',
                         '--file',
                         help='CSV input file of exercises',
                         metavar='FILE',
                         type=argparse.FileType('rt'),
                         default='exercises.csv')

    parseer.add_argument('-s',
                         '--seed',
                         help='Random seed',
                         metavar='seed',
                         type=int,
                         default=None)

    parseer.add_argument('-n',
                         '--num',
                         help='Number of exercises',
                         metavar='exercises',
                         type=int,
                         default=4)

    parseer.add_argument('-e',
                         '--easy',
                         help='Halve the reps',
                         action='store_true')

    args = parseer.parse_args()
    if args.num < 1:
        parseer.error(f'--num "{args.num}" must be greater than 0')

    return args


def main():
    '''Make a jazz noise Here'''
    args = get_every_args()
    random.seed(args.seed)
    wod = []
    exercises = read_csv(args.file)

    for name, low, high in random.sample(exercises, k=args.num):
        reps = random.randint(low, high)
    if args.easy:
        reps = int(reps / 2)
    wod.append((name, reps))


def read_csv(fh):
    """Read the CSV input"""
    exercises = []
    for row in csv.DictReader(fh, delimiter=','):
        low, high = map(int, row['reps'].split('-'))
        exercises.append((row['exercise'], low, high))
    return exercises


if __name__ == '__main__':
    main()
