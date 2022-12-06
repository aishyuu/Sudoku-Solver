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