board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def main():
    print_board(board)
    print(find_empty(board))

def solve(board):
    #Seach for the coords of the empty
    find = find_empty(board)
    if not find:
        #If you can't find an empty space, you're done
        return True
    else:
        #Break the empty space into its row and column
        row, column = find

    #Plug in 1-9 one a a time into the empty space
    for i in range(1,10):
        # Validate the position with the current number (i)
        if validate(board, i, row, column):
            #If validated,
            board[row][column] = i

            if solve(board):
                return True
            
            board[row][column] = 0

def validate(board, num, pos_row, pos_col):
    for i in range(len(board[0])):
        if board[pos_row][i] == num and pos_col != i:
            return False

    for i in range(len(board)):
        if board[i][pos_col] == num and pos_row != i:
            return False

    box_x = pos_col // 3
    box_y = pos_row // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != (pos_col, pos_row):
                return False
    
    return True

def print_board(board):
    """
    print the current sudoku board

    :param board: 9x9 matrix of sudoku board
    :type board: list
    """
    for row in range(len(board)):
        # Divide the board horizontally into rows of 3
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - - - - ")
        
        # Go through every element of each row
        for column in range(len(board[0])):
            # Divide the board vertically into 3's
            if column % 3 == 0 and column != 0:
                print(" | ", end="")
            # If you reach the end, print with newline at end
            if column == 8:
                print(board[row][column])
            #If not at end, print with no new line
            else:
                print(str(board[row][column]) + " ", end="")

def find_empty(board):
    """
    Find the coordinates of the first empty cell (0) you find.

    :param board: 9x9 matrix of sudoku board
    :type board: list
    """
    # Go down each row
    for row in range(len(board)):
        for column in range(len(board)):
            if board[row][column] == 0:
                return row, column

if __name__ == "__main__":
    main()