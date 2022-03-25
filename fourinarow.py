import random

length = 7
height = 6
board = [[]]*length

def conv(ch):
    if ch == 1:
        return 'X'
    else:
        return 'O'

def printBoard():
    
    matrix = [["```"]]
    for i in range(height):
        row = []
        for j in range(length):
            if len(board[j]) > height-i-1:
                ch = conv(board[j][height-i-1])
            else:
                ch = ' '
            row.append(ch)
        matrix.append(row)
        
        row = []
        for i in range(length):
            row.append(" ")
        matrix.append(row)


    row = ["1"]
    for i in range(1,length):
        row.append(chr(ord("1")+i))
    matrix.append(row)

    matrix.append(["```"])

    print("\n".join(["|".join(x) for x in matrix]))
        
def win():
    for row in range(height):
        for col in range(length-4):
            if row < len(board[col]) and row < len(board[col+1]) and row < len(board[col+2]) and row < len(board[col+3]) and board[col][row] == board[col+1][row] and board[col][row] == board[col+2][row] and board[col][row] == board[col+3][row]:
                return True
            
    for col in range(length):
        for row in range(height):
            if len(board[col]) > row+3 and board[col][row] == board[col][row+1] and board[col][row] == board[col][row+2] and board[col][row] == board[col][row+3]:
                return True

    for col in range(length-4):
        for row in range(height-4):
            if len(board[col]) > row and len(board[col+1]) > row+1 and len(board[col+2]) > row+2 and len(board[col+3]) > row+3 and board[col][row] == board[col+1][row+1] and board[col][row] == board[col+2][row+2] and board[col][row] == board[col+3][row+3]:
                return True

    for col in range(3,length):
        for row in range(height-4):
            if len(board[col]) > row and len(board[col-1]) > row+1 and len(board[col-2]) > row+2 and len(board[col-3]) > row+3 and board[col][row] == board[col-1][row+1] and board[col][row] == board[col-2][row+2] and board[col][row] == board[col-3][row+3]:
                return True

    return False

def botMove():
    global board
    cand = []
    for i in range(length):
        if len(board[i]) != height:
            cand.append(i)

    move = random.choice(cand)
    board[move].append(2)

def start():
    global board

    board = [[] for i in range(length)]
    
    if random.randrange(2) == 0:
        print("I go first")
        botMove()
    else:
        print("You go first")
        
    printBoard()

def fullBoard():
    return all([len(x) == height for x in board])
    
def move(content):
    global board

    n = int(content)
    n -= 1
    if n >= len(board) or len(board[n]) == height:
        print("Doesn't work like that")
        return False

    board[n].append(1)
    printBoard()
    
    if win():
        print("You win.")
        return True
    
    if fullBoard():
        print("Draw.")
        return True

    botMove()
    printBoard()

    if win():
        print("I win.")
        return True
    
    if fullBoard():
        print("Draw.")
        return True

    return False

