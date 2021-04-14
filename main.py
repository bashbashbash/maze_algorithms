class Square:
    def __init__(self, blockType, x, y, color, start_node, end_node):
        self.blockType  = blockType
        self.x          = x
        self.y          = y
        self.color      = color
        self.compass    = [1,1,1,1]
        self.previous   = None
        self.start_node = start_node
        self.end_node   = end_node

def compare_coors(xy1, xy2) :
    return compare_coor(xy1[0], xy2[0]) and compare_coor(xy1[1], xy2[1]) 

def compare_coor(coor_a, coor_b) :
    return True if coor_a == coor_b else False

import pathlib
pathlib.Path().absolute()
def main(start_coor, end_coor) :
    path = str(pathlib.Path().absolute()) + "\maze_algorithms\maze.txt"
    f = open(path , "r")
    fileMap = f.read()
    squares = {}
    y_coor = 0
    x_coor = 0
    file_map_counter = 0
    while(file_map_counter < len(fileMap)) :
        value             = fileMap[file_map_counter]
        file_map_counter += 1
        color             = "blue" if value == "M" else "yellow" 
        if value != 'M' and value != 'O' :
            continue
        elif x_coor != 0 and x_coor % 39 == 0 :
            squares[(x_coor, y_coor)] = Square(value, x_coor, y_coor, color, compare_coors([x_coor, y_coor], start_coor), compare_coors([x_coor, y_coor], end_coor))
            y_coor += 1
            x_coor = 0
            continue
        else :
            squares[(x_coor, y_coor)] = Square(value, x_coor, y_coor, color, compare_coors([x_coor, y_coor], start_coor), compare_coors([x_coor, y_coor], end_coor))
        
        x_coor += 1
    return squares

from termcolor import colored
import os
import time
# print row strings "visual map"
def printMap(squares) :
    os.system('cls')
    for key, value in squares.items():
        print(colored(value.blockType, value.color), end = "")
        if key[0] != 0 and key[0] % 39 == 0 :
            print()
    
    time.sleep(.1)

# start and end coor
start_coor = [2,1]
end_coor   = [8,35]

# load in the file as square objects
squares = main(start_coor, end_coor)

# travel coor
travel_coor = start_coor

# available direction
compass = [1,1,1,1]

# naviage the maze with loop
import sys
try :
    trySquare = squares[(travel_coor[0], travel_coor[1])]
    trySquare.color    = "green"
    trySquare.previous = None
    lastTrailSquare    = None
    while travel_coor != end_coor :
        printMap(squares)

        if 0 in trySquare.compass == False :
            break

        tryRight  = travel_coor[0] + 1
        trySquare = squares[(tryRight, travel_coor[1])]
        if trySquare.blockType == "O" and trySquare.color != "green" and trySquare.compass[0] == 1 :
            trySquare.color      = "green"
            trySquare.compass[0] = 0
            trySquare.previous = squares[(travel_coor[0], travel_coor[1])]
            lastTrailSquare = trySquare.previous
            travel_coor[0]       = tryRight
            continue
        
        tryDown   = travel_coor[1] + 1
        trySquare = squares[(travel_coor[0], tryDown)]
        if trySquare.blockType == "O" and trySquare.color != "green" and trySquare.compass[1] == 1 :
            trySquare.color      = "green"
            trySquare.compass[1] = 0
            trySquare.previous = squares[(travel_coor[0], travel_coor[1])]
            lastTrailSquare = trySquare.previous
            travel_coor[1]       = tryDown
            continue

        tryLeft   = travel_coor[0] - 1
        trySquare = squares[(tryLeft, travel_coor[1])]
        if trySquare.blockType == "O" and trySquare.color != "green" and trySquare.compass[2] == 1 :
            trySquare.color      = "green"
            trySquare.compass[2] = 0
            trySquare.previous = squares[(travel_coor[0], travel_coor[1])]
            lastTrailSquare = trySquare.previous
            travel_coor[0]       = tryLeft
            continue

        tryUp     = travel_coor[1] - 1
        trySquare = squares[(travel_coor[0], tryUp)]
        if trySquare.blockType == "O" and trySquare.color != "green" and trySquare.compass[3] == 1 :
            trySquare.color      = "green"
            trySquare.compass[3] = 0
            trySquare.previous = squares[(travel_coor[0], travel_coor[1])]
            lastTrailSquare = trySquare.previous
            travel_coor[1]       = tryDown
            continue

        backtrack = False
        while trySquare.start_node == False :
            trySquare = lastTrailSquare
            if 0 in trySquare.compass == True :
                backtrack = True
        
        if backtrack :
            continue
        print("failed to find a route!")
        break
except KeyboardInterrupt :
    print('Interrupted')
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)

    
