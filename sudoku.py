table = []
valid_values = [str(i) for i in range(1, 10)]
def build_table(): # Builds the table based on 9 input lines, checks if all lines are valid and calls check_table
    for column in range(9):
        table.append(list(input()))
        if len(table[-1]) != 9:
            return False
        for row in range(9):
            if table[column][row] not in valid_values:
                return False
    return check_table(0)

def check_table(iteration): # Checks if the table is valid, row by row, and calls the next function depending on the iteration, on it's last, returns true
    for column in range(9):
        for value in valid_values:
            if value not in table[column]:
                return False
    if iteration == 0: 
        return rotate_table()
    elif iteration == 1:
        return square_table()
    else:
        return True

def rotate_table(): # Transforms each row in a column and vice versa, then calls check_table again
    global table
    rotated_table = [[str(0) for i in range(1, 10)] for j in range(9)]
    for column in range(9):
        for row in range(9):
            rotated_table[row][column] = table[column][row]
    table = rotated_table[:]
    return check_table(1)

def square_table(): # Transforms 9 square subdivisions into rows for further checking by check_table
    global table
    squared_table = [[str(0) for i in range(1, 10)] for j in range(9)]
    for column in range(3):
        for subcolumn in range(3):
            for row in range(3):
                for subrow in range(3):
                    squared_table[column*3 + subcolumn][row*3+subrow] = table[row + column*3][subrow + subcolumn*3]
    table = squared_table[:]
    return check_table(2)

if build_table():   print("Yes")
else:               print("No")