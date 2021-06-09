'''
Chapter-06
Reading files and STDIN, iterating lists, formatting strings

In this chapter, you will
 Learn how to process zero or more positional arguments 
 Validate input files
 Read from files or from standard input
 Use multiple levels of for loops
 Break files into lines, words, and bytes  Use counter variables
 Format string output
'''
import argparse
import os
import sys


def get_every_args():
    """Command Line All types Arguments"""
    parseer = argparse.ArgumentParser(description='Rock Cash Casbah',
                                      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    """ Make a Positional Argument"""
    """ Take from file"""
    parseer.add_argument('file',
                         nargs='*',
                         help='Input file',
                         metavar='FILE',
                         type=argparse.FileType('rt'),
                         default=sys.stdin)

    return parseer.parse_args()


def main():
    argss = get_every_args()
    total_lines, total_bytes, total_words = 0, 0, 0
    for fh in argss.file:
        num_line, num_bytes, num_words = 0, 0, 0
        for line in fh:
            num_line += 1
            num_bytes += len(line)
            num_words += len(line.split())

        total_lines += num_line
        total_bytes += num_bytes
        total_words += num_words

        """using {:8} placeholders in the print template to indicate a text field 8 characters wide"""
        print(f'{num_line:8} lines {num_words:8} words {num_bytes:8} bytes {fh.name}')

    if len(argss.file) > 1:
        print(f'{total_lines:8}{total_words:8}{total_bytes:8} total')


if __name__ == '__main__':
    main()
