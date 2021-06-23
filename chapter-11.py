'''
Chapter-11
 Bottles of Beer Song: Writing and testing functions

In this exercise, you will
 Learn how to produce a list of numbers decreasing in value
 Write a function to create a verse of the song, using a test to verify when the verse is correct
 Explore how for loops can be written as list comprehensions, which in turn can be written with the map() function
'''
import argparse


def get_every_args():
    """Command Line All types Arguments"""
    parseer = argparse.ArgumentParser(description='Telephones',
                                      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    """ Make a Positional Argument"""
    parseer.add_argument('text',
                         metavar='text',
                         help='Input text for file')

    parseer.add_argument('-n',
                         '--num',
                         help='How Many Bottles',
                         metavar='number',
                         type=int,
                         default=10)

    argument = parseer.parse_args()

    if argument.num < 1:
        parseer.error(f'--num "{argument.num}" must be greater than 0')

    return argument


def verse(bottle):
    """Define a function that can create a single verse()."""
    next_bottle = bottle-1
    a1 = '' if bottle == 1 else 's'
    a2 = '' if next_bottle == 1 else 's'
    num_next = 'No more' if next_bottle == 0 else next_bottle
    return '\n'.join([
        f'{bottle} bottle{a1} of beer on the wall,',
        f'{bottle} bottle{a1} of beer,',
        f'Take One down pass it around,',
        f'{num_next} bottle{a2} of beer on the wall,',
    ])


"""Define a unit test called test_verse() 
for the verse() function. The test_ prefix 
means that the pytest module will find this 
function and execute it."""


def test_verse():
    """Test verse"""
    last_verse = verse(1)
    assert last_verse == '\n'.join([
        '1 bottle of beer on the wall,', '1 bottle of beer,',
        'Take one down, pass it around,',
        'No more bottles of beer on the wall!'
    ])
    two_bottles = verse(2)
    assert two_bottles == '\n'.join([
        '2 bottles of beer on the wall,', '2 bottles of beer,',
        'Take one down, pass it around,', '1 bottle of beer on the wall!'
    ])


def main():
    '''Make a jazz noise Here'''
    argss = get_every_args()
    print('\n\n'.join(map(verse, range(argss.num, 0, -1))))


if __name__ == '__main__':
    main()
