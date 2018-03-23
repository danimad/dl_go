from . import gotypes

COLS = 'ABCDEFGHJKLMNOPRQST'
STONE_TO_CHAR = {
    None: '.',
    gotypes.Player.black: 'x',
    gotypes.Player.white: 'o',
}

def print_move(player, move):
    if move.is_pass:
        move_str = 'passes'
    else:
        move_str = '%s%d' % (COLS[move.point.col -1], move.point.row)
    print('%s %s' % (player, move_str))


def print_board(board):
    for row in range(board.num_rows, 0, -1):
        line = []
        for col in range(1, board.num_cols + 1):
            stone = board.get(gotypes.Point(row=row, col=col))
            line.append(STONE_TO_CHAR[stone])
        print('%d %s' % (row, ''.join(line)))
    print('  ' + COLS[:board.num_cols])

# new v1.2
def point_from_coords(coords):
    cols = COLS.index(coords[0]) + 1
    row = int(coords[1])
    return gotypes.Point(row=row, col=col)
