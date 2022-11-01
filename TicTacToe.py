import random

grid_size = 3

board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]


# Function to print the Tic Tac Toe board
def printBoard(board):
    for i in range(grid_size):
        if 0 < i <= 2:
            print('------', end='')
            print()
        for j in range(grid_size):
            print('|', end='')
            print(board[i][j], end='')
            if j == 2:
                print()


x = 'X'
o = 'O'

# Loop to take in inputs from the user
while True:
    askWhichSymbol = input('Which symbol would you like to play as? (X/O)? ')
    if askWhichSymbol == 'x' or askWhichSymbol == 'X' or askWhichSymbol == 'o' or askWhichSymbol == 'O':
        break
    else:
        print('Please input a valid alphabet, X or O.')


# Function that takes in the user input as an argument, checks if there is a place for it and places it on the board
def playersInput(playerSymbol):
    if playerSymbol == 'x' or playerSymbol == 'X':
        while True:
            userInput = input('Where would you like to put X? (1-9) ')

            if userInput.isnumeric():
                if 0 < int(userInput) < 10:
                    if moveIsValid(board, userInput):
                        match userInput:

                            case '1':
                                board[0][0] = x
                                break

                            case '2':
                                board[0][1] = x
                                break

                            case '3':
                                board[0][2] = x
                                break

                            case '4':
                                board[1][0] = x
                                break

                            case '5':
                                board[1][1] = x
                                break

                            case '6':
                                board[1][2] = x
                                break

                            case '7':
                                board[2][0] = x
                                break

                            case '8':
                                board[2][1] = x
                                break

                            case '9':
                                board[2][2] = x
                                break

                    else:
                        print('Invalid Move!!')
            else:
                print('Please input a valid number from 1-9. ')

    elif playerSymbol == 'o' or playerSymbol == 'O':

        while True:
            userInput = input('Where would you like to put O? (1-9) ')

            if userInput.isnumeric():
                if 0 < int(userInput) < 10:
                    if moveIsValid(board, userInput):
                        match userInput:

                            case '1':
                                board[0][0] = o
                                break

                            case '2':
                                board[0][1] = o
                                break

                            case '3':
                                board[0][2] = o
                                break

                            case '4':
                                board[1][0] = o
                                break

                            case '5':
                                board[1][1] = o
                                break

                            case '6':
                                board[1][2] = o
                                break

                            case '7':
                                board[2][0] = o
                                break

                            case '8':
                                board[2][1] = o
                                break

                            case '9':
                                board[2][2] = o
                                break

                    else:
                        print('Invalid Move!!')

                else:
                    print('Please input a valid number from 1-9. ')


# Function that takes the random number that was generated and places it on the board
def computerPlay(board, position, symbol):
    match position:

        case '1':
            board[0][0] = symbol

        case '2':
            board[0][1] = symbol

        case '3':
            board[0][2] = symbol

        case '4':
            board[1][0] = symbol

        case '5':
            board[1][1] = symbol

        case '6':
            board[1][2] = symbol

        case '7':
            board[2][0] = symbol

        case '8':
            board[2][1] = symbol

        case '9':
            board[2][2] = symbol


# Function that Checks if the board position chosen is available or occupied
def moveIsValid(board, position):
    match position:

        case '1':
            return board[0][0] == ' '

        case '2':
            return board[0][1] == ' '

        case '3':
            return board[0][2] == ' '

        case '4':
            return board[1][0] == ' '

        case '5':
            return board[1][1] == ' '

        case '6':
            return board[1][2] == ' '

        case '7':
            return board[2][0] == ' '

        case '8':
            return board[2][1] == ' '

        case '9':
            return board[2][2] == ' '


# Function used to generate a random number for the computer to place a symbol in
def computerTurn():
    while True:
        computerInput = str(random.randint(1, 9))
        if moveIsValid(board, computerInput):
            print('Computer Plays: ' + computerInput)
            if askWhichSymbol == 'x' or askWhichSymbol == 'X':
                computerPlay(board, computerInput, o)
                break
            elif askWhichSymbol == 'o' or askWhichSymbol == 'O':
                computerPlay(board, computerInput, x)
                break


# Function that checks if the board is completely full or calls another function to determine a winner
def gameFinished(board, userSymbol):
    if userSymbol == 'x' or userSymbol == 'X':
        if whoWins(board, o):
            print('')
            print('Computer Wins!!!')
            return True
        elif whoWins(board, x):
            print('')
            print('You Win!!!')
            return True

    elif userSymbol == 'o' or userSymbol == 'O':
        if whoWins(board, x):
            print('')
            print('Computer Wins')
            return True
        elif whoWins(board, o):
            print('')
            print('You Win!!!')
            return True

    for i in range(grid_size):
        for j in range(grid_size):
            if board[i][j] == ' ':
                return False
    printBoard(board)
    print('')
    print('The game is a tie!!')
    return True


# Function which checks to see if
def whoWins(board, symbol):
    # Checking for 3 in a ROW
    if ((board[0][0] == symbol and board[0][1] == symbol and board[0][2] == symbol) or
            (board[1][0] == symbol and board[1][1] == symbol and board[1][2] == symbol) or
            (board[2][0] == symbol and board[2][1] == symbol and board[2][2] == symbol) or

            # Checking for 3 in a COLUMN
            (board[0][0] == symbol and board[1][0] == symbol and board[2][0] == symbol) or
            (board[0][1] == symbol and board[1][1] == symbol and board[2][1] == symbol) or
            (board[0][2] == symbol and board[1][2] == symbol and board[2][2] == symbol) or

            # Checking for diagonal matches
            (board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol) or
            (board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol)):
        return True

    return False


# Loop to let the player and computer take turns. Stops when there is a winner.
while True:
    playersInput(askWhichSymbol)
    if gameFinished(board, askWhichSymbol):
        printBoard(board)
        quit()

    printBoard(board)

    computerTurn()
    if gameFinished(board, askWhichSymbol):
        printBoard(board)
        quit()

    printBoard(board)
