import random

board = []

wins = []
wins.append([0,1,2])
wins.append([3,4,5])
wins.append([6,7,8])
wins.append([0,3,6])
wins.append([1,4,7])
wins.append([2,5,8])
wins.append([0,4,8])
wins.append([2,4,6])

help = []
help.append("```")
help.append(" 1 | 2 | 3 ")
help.append("---+---+---")
help.append(" 4 | 5 | 6 ")
help.append("---+---+---")
help.append(" 7 | 8 | 9 ")
help.append("```")
help = "\n".join(help)

def conv(x):
    if x==0:
        return ' '
    elif x==1:
        return 'X'
    else:
        return 'O'

def printBoard():
    b = []
    b.append("```")
    b.append(f" {conv(board[0])} | {conv(board[1])} | {conv(board[2])} ")
    b.append(f"---+---+---")
    b.append(f" {conv(board[3])} | {conv(board[4])} | {conv(board[5])} ")
    b.append(f"---+---+---")
    b.append(f" {conv(board[6])} | {conv(board[7])} | {conv(board[8])} ")
    b.append("```")
    print('\n'.join(b))

def win():
    check = lambda x,y,z: not 0 in [board[x],board[y],board[z]] and board[x] == board[y] and board[y] == board[z]
    return any([check(x,y,z) for x,y,z in wins])

def botMove():
    global board
    
    cands = []
    for i in range(9):
        if board[i] == 0:
            cands.append(i)
    board[random.choice(cands)] = 2
    return

def fullBoard():
    return all([x!=0 for x in board])

def start():
    global board
    board = [0]*9
    if random.randrange(2) == 0:
        print("You start")
    else:
        print("I start")
        botMove()
        
    tmp = "You play by sending `;N` where N is the position you want to fill"
    tmp += ". Send `;help` for more information"
    print(tmp)
    printBoard()

def move(cont):
    
    n = int(cont)
    n -= 1
    if n < 0 or n > 8 or board[n] != 0:
        print("Number not valid. Try again")
        return False
    
    board[n] = 1
    printBoard()
    if win():
        print("You win")
        return True
    if fullBoard():
        print("Draw")
        return True
    botMove()
    printBoard()
    if win():
        print("I win")
        return True
    if fullBoard():
        print("Draw")
        return True
    return False

def helper():
    print(help)
