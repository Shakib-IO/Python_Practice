'''
Chapter-21
Tic-Tac-Toe Exploring state
In this exercise, you will
 Consider how to use elements like strings and lists to represent aspects of a pro- gram’s state
 Enforce the rules of a game in code, such as preventing a player from playing in a cell that has already been taken
 Use a regular expression to validate the initial board
 Use and and or to reduce combinations of Boolean values to a single value
 Use lists of lists to find a winning board
 Use the enumerate() function to iterate a list with the index and value
'''
import argparse
import re  # Regular Expressions


def get_every_args():
    """Command Line All types Arguments"""
    parseer = argparse.ArgumentParser(description='Tic-Tac-Toe',
                                      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    """ Make a Positional Argument"""
    parseer.add_argument('-b',
                         '--board',
                         help='The state of the board',
                         metavar='board',
                         type=str,
                         default='.' * 9)
    parseer.add_argument('-p',
                         '--player',
                         help='Player',
                         choices='XO',
                         metavar='player',
                         type=str,
                         default=None)

    parseer.add_argument('-c',
                         '--cell',
                         help='Cell 1-9',
                         metavar='cell',
                         type=int,
                         choices=range(1, 10),
                         default=None)

    args = parseer.parse_args()
    if any([args.player, args.cell]) and not all([args.player, args.cell]):
        parseer.error('Must provide both --player and --cell')

    if not re.search('^[.XO]{9}$', args.board):
        parseer.error(
            f'--board "{args.board}" must be 9 characters of ., X, O')

    if args.player and args.cell and args.board[args.cell - 1] in 'XO':
        parseer.error(f'--cell "{args.cell}" already taken')

    return args


def main():
    '''Make a jazz noise Here'''
    args = get_every_args()
    board = list(args.board)

    if args.player and args.cell:
        board[args.cell - 1] = args.player

    print(format_board(board))
    winner = find_winner(board)
    print(f'{winner} has won!' if winner else 'No winner.')


def format_board(board):
    cells = [str(i) if c == '.' else c for i, c in enumerate(board, 1)]
    bar = '-------------'
    cells_tmpl = '| {} | {} | {} |'
    return '\n'.join([
        cells_tmpl.format(*cells[:3]), bar,
        cells_tmpl.format(*cells[3:6]), bar,
        cells_tmpl.format(*cells[6:]), bar
    ])


def find_winner(board):
    """Return the winner"""
    winning = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
               [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for player in ['X', 'O']:
        for i, j, k in winning:
            combo = [board[i], board[j], board[k]]
            if combo == [player, player, player]:
                return player


if __name__ == '__main__':
    main()
