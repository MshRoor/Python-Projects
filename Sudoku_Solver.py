grid_size = 9  # As we have a 9x9 board here

# The sudoku board. 0 means an empty slot.
board = [[0, 2, 7, 1, 9, 4, 6, 3, 8],
         [3, 8, 0, 5, 0, 0, 0, 0, 1],
         [1, 9, 4, 0, 0, 0, 5, 0, 0],
         [8, 0, 0, 7, 6, 0, 4, 0, 5],
         [0, 6, 0, 4, 3, 8, 7, 1, 9],
         [7, 0, 0, 0, 5, 1, 0, 6, 0],
         [0, 7, 8, 0, 2, 0, 0, 5, 4],
         [0, 0, 0, 0, 0, 5, 0, 0, 7],
         [4, 0, 0, 0, 1, 0, 3, 9, 6]]


# Function to print the sudoku board (solved and unsolved)
def printSudokuBoard(board):
    for row in range(grid_size):
        if row % 3 == 0 and row != 0:
            print('-----------')
        for col in range(grid_size):
            if col % 3 == 0 and col != 0:
                print("|", end="")
            print(board[row][col], end="")
        print(" ")


print("Unsolved Board")
print()
printSudokuBoard(board)
print()


# Function to see if a particular number exists within a particular row
def isNumInRow(board, num, row):
    for i in range(grid_size):
        if board[row][i] == num:
            return True  # number exists in that row
    return False  # number does not exist in that row (which is what we want)


# Function to see if a particular number exists within a particular column
def isNumInColumn(board, num, col):  # col is the particular column
    for i in range(grid_size):
        if board[i][col] == num:
            return True  # number exists in that column
    return False  # number does not exist in that column (which is what we want)


# Function to see if a particular number exists within a particular 3x3 section of the sudoku board
def isNumInSmallerGrid(board, num, row, col):
    tinyBoxRow = row - row % 3  # formula to get the top-left row number of a specific 3x3 grid
    tinyBoxCol = col - col % 3  # formula to get the top-left column number of a specific 3x3 grid

    for i in range(tinyBoxRow, tinyBoxRow + 3):
        for j in range(tinyBoxCol, tinyBoxCol + 3):
            if board[i][j] == num:
                return True  # number exists in the smaller 3x3 grid
    return False  # number does not exist in the smaller 3x3 grid (which is what we want)


# Function to run all the functions above and determine a valid number for the board
def isNotOnBoard(board, num, row, col):
    return (not isNumInRow(board, num, row)
            and not isNumInColumn(board, num, col)
            and not isNumInSmallerGrid(board, num, row, col))  # if they all return 'False'(hence will return true
    # because of the not operator) the number can be placed onto the sudoku board


def solveBoard(board):
    for row in range(grid_size):

        for col in range(grid_size):

            if board[row][col] == 0:

                for trialNum in range(1, grid_size + 1):  # TrialNum is the number the computer inputs into the board
                    if isNotOnBoard(board, trialNum, row, col):
                        board[row][col] = trialNum

                        if solveBoard(board):
                            return True
                        else:
                            board[row][col] = 0  # value set to zero if the number is invalid for the board

                return False

    return True


solveBoard(board)

if solveBoard(board):
    print("Board Solved!!")
    print("")
else:
    print("Board not solvable, please enter a valid board")

printSudokuBoard(board)
