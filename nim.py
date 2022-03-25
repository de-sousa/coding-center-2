import random

board = []
length = 0

help = "Send `;N M` where M is the quantity you want to remove from pile N."

def printBoard():
    response = ["```"]
    for i,val in enumerate(board):
        response.append(f"{i+1}) {val}")
    response.append("```")
    
    print("\n".join(response))

def win():
    return all([x==0 for x in board])

def botMove():
    global board
    cand = []
    for i in range(length):
        if board[i] != 0:
            cand.append(i)
    move = random.choice(cand)
    quan = random.randrange(1,board[move]+1)
    board[move] -= quan
    
def start():
    global length,board
    
    length = random.randrange(1,6)
    print(f"The size of the game is {length}")
    board = [random.randrange(1,21) for i in range(length)]
    print("This is the board:")     
    printBoard()

    if random.randrange(2) == 0:
        print("I go first")
        botMove()
    else:
        print("You go first")
        
    printBoard()

def move(content):
    global board
    content = list(map(int,content.split(" ")))
    
    if len(content) != 2 or content[0] < 1 or content[0] > length or content[1] < 1 or content[1] > board[content[0]-1]:
        print("Doesn't work like that.")
        return

    pile = content[0]-1
    quan = content[1]

    board[pile] -= quan
    printBoard()
            
    if win():
        print("You win.")
        return True
            
    botMove()
    printBoard()
            
    if win():
        print("I win.")
        return True

    return False
            
        
                
