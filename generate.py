"""
All of this is copied from solver.py
The only thing that's different is there is no print board
Also in lines 17 and 29, there are things related to a random list of numbers 1-9
"""

import random
import terminal_solver as solver

#Create an empty 9x9 grid
board = [[0 for i in range(9)] for j in range(9)]

def main():
    create_random(board)
    solver.print_board(board)
    remove_numbers(board)
    print("---Removed---")
    solver.print_board(board)

def create_random(board):
    nums = list(range(1,10))

    #Seach for the coords of the empty
    find = solver.find_empty(board)
    if not find:
        #If you can't find an empty space, you're done
        return True
    else:
        #Break the empty space into its row and column
        row, column = find

    #Shuffle the list of numbers around each time so we can make sure it's random every time
    random.shuffle(nums)

    #Plug in the random list of 1-9 into the slot
    for i in nums:
        # Validate the position with the current number (i)
        if solver.validate(board, i, row, column):
            #If validated, make the current coords the number that's valid
            board[row][column] = i

            #After validation, re call the solve function again to find the next empty and continue the cycle
            if create_random(board):
                return True
            
            #If at some point, we have to go back, set the current position to empty again (0)
            #This will continue the loop in this position and you will keep going down the numbers
            board[row][column] = 0
    #If none are valid, we return false to the previous, which will continue to loop in that recursion step
    return False

def remove_numbers(board):
    #Set a tally of how many numbers removed
    removed = 0

    #As long as we're not at 64
    while removed != 64:
        row_elim = random.randint(0, 8)
        col_elim = random.randint(0,8)

        #If our current random coord is not equal to 0
        if board[row_elim][col_elim] != 0:
            #Set the coord to 0 and increase removed tally
            board[row_elim][col_elim] = 0
            removed += 1




if __name__ == "__main__":
    main()