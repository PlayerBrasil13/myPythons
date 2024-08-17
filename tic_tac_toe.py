import random
def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    board_draw = "+-------+-------+-------+\n|       |       |       |\n|",\
                 "   ",\
                 "   |",\
                 "\n|       |       |       |",\
                 "+-------+-------+-------+"
    
    for row in board:
        print(board_draw[0], end="")
        for column in row:
            print (board_draw[1], column, board_draw[2], sep="", end="")
        print(board_draw[3])
    print(board_draw[4])


def enter_move(board):
    # The function accepts the board current status, asks the user about their move, 
    # checks the input and updates the board according to the user's decision.
    move = int(input("Enter your move: ")) - 1
    move = (move // 3), (move % 3) 
    if move in free_fields:
        board[move[0]][move[1]] = "O"
        make_list_of_free_fields(board)
    else: 
        print("This cell is occupied. Try again.")
        enter_move(board)


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    del free_fields[:]
    for row in range(len(board)):
        for cell in range(len(board[row])):
            if board[row][cell] in range(0, 10):
                free_fields.append((row, cell))


def victory_for(board, sign):
    # The function analyzes the board status in order to check if 
    # the player using 'O's or 'X's has won the game
    for row in board:
        if row[0] == row[1] == row[2] == sign:
            return True
    columns = []
    for row in range(3):
        for column in range(3):
            columns.append(board[column][row])
        if columns[0] == columns[1] == columns[2] == sign:
            return True
        del columns[:]

    if board[0][0] == board[1][1] == board[2][2] == sign or \
        board[0][2] == board[1][1] == board[2][0] == sign:
        return True
    return False


def draw_move(board):
    # The function draws the computer's move and updates the board.
    move = random.choice(free_fields)
    board[move[0]][move[1]] = "X"
    make_list_of_free_fields(board)

board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
free_fields = []
make_list_of_free_fields(board)

while len(free_fields) > 0:
    display_board(board)
    enter_move(board)
    display_board(board)
    if victory_for(board, "O"):
        print("You won!")
        break
    draw_move(board)
    display_board(board)
    if victory_for(board, "X"):
        print("You lost!")
        break

if len(free_fields) == 0:
    print("It's a tie!")