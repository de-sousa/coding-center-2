import random
import tictactoe as t
import nim as n
import fourinarow as f

midgame = False
midttt = False
midnim = False
midfir = False

def on_message():
    cont = input().lower()
    global midgame, midttt, midnim, midfir
    
    if cont[0] == ';':            
        
        if not midgame:
            if ";play" in cont:
                if "tictactoe" in cont:
                    midgame = True
                    midttt = True
                    t.start()
                    return
                if "nim" in cont:
                    midgame = True
                    midnim = True
                    n.start()
                    return
                if "fourinarow" in cont:
                    midgame = True
                    midfir = True
                    f.start()
                    return

        if midgame:
            
            if ";help" in cont:
                if midttt:
                    t.helper()
                    return
                if midnim:
                    n.helper()
                    return

            if ";end" in cont:
                midgame = False
                midttt = False
                midnim = False
                return

            cont = cont[1:]
            if midttt:
                over = t.move(cont)
                if over:
                    midgame = False
                    midttt = False
            if midnim:
                over = n.move(cont)
                if over:
                    midgame = False
                    midnim = False
            if midfir:
                over = f.move(cont)
                if over:
                    midgame = False
                    midfir = False

while True:
    on_message()
