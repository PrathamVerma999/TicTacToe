ALL_SPACES = list('123456789')
X, O, BLANK = 'X', 'O', ' '

def main():
    print("Welcome to Tic Tac Toe!")
    gameBoard = getBlankBoard()
    currentPlayer, nextPlayer = X, O

    while True:
        print(getBoardStr(gameBoard)) # display the board to the user
        
        # Keep asking the player until they enter a number 1-9
        move = None
        while not isValidSpace(move, gameBoard):
            move = input(f"What is {currentPlayer}'s move? (1-9)\n")
        updateBoard(gameBoard, move, currentPlayer)
        
        # check if the game is over
        if isWinner(gameBoard, currentPlayer): # checking for victory
            print(getBoardStr(gameBoard))
            print(f"{currentPlayer} has won the game!")
            break
        elif isBoardFull(gameBoard):
            print(getBoardStr(gameBoard))
            print('The game is a tie!')
            break
        currentPlayer, nextPlayer = nextPlayer, currentPlayer # switching turns
    print('Thanks for playing!')

def getBlankBoard():
    # This creates a new tic tac toe board
    board = {}
    for space in ALL_SPACES:
        board[space] = BLANK # all spaces start as blank
    return board

def getBoardStr(board):
    # returns a graphical text representation of the board
    return f'''
      {board['1']}|{board['2']}|{board['3']} 1 2 3
      -+-+-
      {board['4']}|{board['5']}|{board['6']} 4 5 6
      -+-+- 
      {board['7']}|{board['8']}|{board['9']} 7 8 9'''

def isValidSpace(space, board):
    # checks if the space is a valid space number on the board and if it is blank or not
    return space in ALL_SPACES and board[space] == BLANK

def isWinner(board, player):
    # checks for the winner
    return ((board['1'] == board['2'] == board['3'] == player) or # Top Row
            (board['4'] == board['5'] == board['6'] == player) or # Middle Row 
            (board['7'] == board['8'] == board['9'] == player) or # bottom row
            (board['1'] == board['4'] == board['7'] == player) or # first column
            (board['2'] == board['5'] == board['8'] == player) or # second column
            (board['3'] == board['6'] == board['9'] == player) or # third column
            (board['1'] == board['5'] == board['9'] == player) or # diagonal from top left
            (board['3'] == board['5'] == board['7'] == player))   # diagonal from top right

def isBoardFull(board):
    # checks if all the spaces on the board are full
    for space in ALL_SPACES:
        if board[space] == BLANK:
            return False
    return True

def updateBoard(board, space, mark):
    # sets the place on the board to mark and updates the board
    board[space] = mark

main()