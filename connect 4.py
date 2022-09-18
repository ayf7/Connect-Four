# FUNCTIONS ------

def printBoard(board):
    ''' printBoard(board) -> None
    prints the board out
    '''
    print("")
    print("0 1 2 3 4 5 6")
    print("-------------")
    for i in range(len(board)):
        row = board[5-i]
        rowString = ""
        for element in row:
            rowString += element + " "
        print(rowString)
    print("-------------")
    print("0 1 2 3 4 5 6")
    print("")
    
def game(startingPlayer, startingSymbol):
    ''' game(player, symbol) -> player name or "tie"
    runs the move and check command in a while loop, switching playerMove bewteen O and X, until a winning move or tie
    '''
    # initializes a variable determining who is moving with the starting parameters
    playerMove = startingPlayer
    symbol = startingSymbol

    # runs move and check commands in a while loop, returning "win" or "tie" once its over, otherwise switching between O and X
    while True:
        coordinate = move(playerMove, symbol)
        status = check(symbol, coordinate[0], coordinate[1])
        # takes the return from status and determines whether to keep going or not
        if status == "win":
            printBoard(board)
            print(playerMove + " wins!")
            return playerMove
        if status == "tie":
            printBoard(board)
            print("It's a tie!")
            return "tie"
        if playerMove is playerX:
            playerMove = playerO
            symbol = "O"
        else:
            playerMove = playerX
            symbol = "X"

def move(player, symbol):
    ''' check(symbol, col, row) -> (int, int)
    prints the board, waits for the player to input a valid move, update the board with the new move, return the coordinate of said move
    '''
    printBoard(board)
    legalMoves = ["0", "1", "2", "3", "4", "5", "6"]

    validMoveFound = False
    while not validMoveFound:
        selectedCol = input(player + ", you're " + symbol + ". What column do you want to play in? ")
        selectedRow = ""
        if selectedCol in legalMoves: # makes sure the input is a number from 0-6
            for row in range(6):
                if validMoveFound:
                    break
                if board[row][int(selectedCol)] == ".": # looking for an empty slot in the selected column
                    board[row][int(selectedCol)] = symbol
                    selectedRow = row
                    validMoveFound = True
    return (int(selectedCol), selectedRow)

def check(symbol, col, row):
    ''' check(symbol, col, row) -> "win", "tie", ""
    determines if the most recent move was a win, tie, or nothing (keep going)
    '''

    # create strings of horizontal, vertical, and the 2 diagonal entries
    horizontal = ""
    vertical = ""
    diagonal1 = ""
    diagonal2 = ""

    # create horizontal string
    for index in board[row]:
        horizontal += index
    
    # create vertical string
    for array in board:
        vertical += array[col]

    # create diagonal string
    startingRow = row
    startingCol = col
    while startingRow > 0 and startingCol > 0:
        startingRow -= 1
        startingCol -= 1
    while startingRow < 6 and startingCol < 7:
        diagonal1 += board[startingRow][startingCol]
        startingRow += 1
        startingCol += 1

    # create other diagonal string
    startingRow = row
    startingCol = col
    while startingRow > 0 and startingCol < 6:
        startingRow -= 1
        startingCol += 1
    while startingRow < 6 and startingCol >= 0:
        diagonal2 += board[startingRow][startingCol]
        startingRow += 1
        startingCol -= 1

    if (symbol*4 in horizontal or symbol*4 in vertical or symbol*4 in diagonal1 or symbol*4 in diagonal2):
        return "win"

    # check if all slots are filled, in case of tie
    emptySlot = False
    for row in board:
        for element in row:
            if element == ".":
                emptySlot = True
    if emptySlot:
       return ""
    return "tie"

# MAIN -----------

# inputs and initial setup
playerX = input("Player X, enter your name: ")
playerO = input("Player O, enter your name: ")

playerXScore = 0
playerOScore = 0

startingPlayer = playerX
startingSymbol = "X"

# game start
nextGame = True
while nextGame:
    # creates empty board
    board = []
    for row in range(6):
        board.append([])
        for column in range(7):
            board[row].append(".")

    # starts the game, with startingPlayer
    winner = game(startingPlayer, startingSymbol)

    # once the game is finished, finds the winner and adds 1 to their score
    if winner is playerX:
        playerXScore += 1
    elif winner is playerO:
        playerOScore += 1
    else:
        playerXScore += 0.5
        playerOScore += 0.5
    print(playerX + "'s score: " + str(playerXScore))
    print(playerO + "'s score: " + str(playerOScore))

    # play again prompt
    validInput = False    
    while not validInput:
        nextGameInput = input("Play again? (y/n) ")
        if nextGameInput == "y":
            validInput = True
            if startingPlayer is playerX:
                startingPlayer = playerO
                startingSymbol = "O"
            else:
                startingPlayer = playerX
                startingSymbol = "X"
        if nextGameInput == "n":
            validInput = True
            nextGame = False
