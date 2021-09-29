#!/usr/bin/python3
import random
import pickle

def next_move(posx, posy, board):
    dirty_pos = []
    dis = []
    for i,a in enumerate(board):
        for j,b in enumerate(a):
            if b == "d":
                dirty_pos.append((i,j))
                dis.append(abs(i-posx) + abs(j-posy))
    try:
        with open('data.pickle', 'rb') as f:
            dirty_pos_old = pickle.load(f)
        dirty_pos = list(set(dirty_pos_old + dirty_pos))
    except:
        pass
    
    if board[posx][posy] == "d":
        dirty_pos.remove((posx, posy))
    
    with open('data.pickle', 'wb') as f:
        pickle.dump(dirty_pos, f)

    if board[posx][posy] == "d":
        print("CLEAN")
    else:
        cango =[]
        if dis == []:
            if dirty_pos == []:
                for j,b in enumerate(board[posx]):
                    if b =="o":
                        if posy-j < 0:
                            cango.append('RIGHT')
                        if posy-j > 0:
                            cango.append('LEFT') 
                for i,a in enumerate(list(map(list, zip(*board)))[posy]):
                    if a =="o":
                        if posx-i < 0:
                            cango.append('DOWN')
                        if posx-i > 0:
                            cango.append('UP')      
            
                print(random.choice(cango))
                return
            else:
                for i,j in dirty_pos:
                    dis.append(abs(i-posx) + abs(j-posy))                   
                    
        if dis != []:                
            closest_pos = dirty_pos[dis.index(min(dis))]
            
        drp, dcp = closest_pos[0] - posx, closest_pos[1] - posy
        if abs(drp)>abs(dcp):
            if drp<0:
                s = 'UP'
            else:
                s= 'DOWN'
        else:
            if dcp<0:
                s = 'LEFT'
            else:
                s= 'RIGHT'
        print(s)

if __name__ == "__main__": 
    pos = [int(i) for i in input().strip().split()] 
    board = [[j for j in input().strip()] for i in range(5)]  
    next_move(pos[0], pos[1], board)