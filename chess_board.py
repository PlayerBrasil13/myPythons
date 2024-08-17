EMPTY = " ---- "
ROOK = " ROOK "
PAWN = " PAWN "
KNIGHT = "KNIGHT"
BISHOP = "BISHOP"
QUEEN = "QUEEN "
KING = " KING "
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

board[0][1] = KNIGHT
board[0][6] = KNIGHT
board[7][1] = KNIGHT
board[7][6] = KNIGHT

board[0][2] = BISHOP
board[0][5] = BISHOP
board[7][2] = BISHOP
board[7][5] = BISHOP

board[0][3] = QUEEN
board[0][4] = KING
board[7][3] = QUEEN
board[7][4] = KING


board[1] = [PAWN for i in range(8)]
board[6] = [PAWN for i in range(8)]


for i in board:
    print(i)
