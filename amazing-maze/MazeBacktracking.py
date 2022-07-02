# lib
import random
import numpy as np
from rich import print
import sys
# image lib
from tkinter import *
# from PIL import Image, ImageTk
import time
# maximise maximum recursion depth exceeded
sys.setrecursionlimit(10000)


"""
Class Maze Generator
genere un labyrinthe avec l'algorithme backtracking
"""
class MazeGenerator():
    def __init__(self):                                            
        self.size = int(input("choose a number : "))                 
        self.direction = [ [-1, 0], [1, 0], [0, -1], [0, 1] ]           
        self.grid = np.zeros((self.size, self.size), dtype=int)         
        self.ver = [["#."] * self.size + ['#'] for _ in range(self.size)] + [[]]
        self.hor = [["##"] * self.size + ['#'] for _ in range(self.size + 1)]
        self.hor[0][0] = '#.'
        self.hor[-1][-2] = '#.'
        self.generate = self.backtrackingRecursive(0, 0)                
        self.print = self.printMaze()

    def isWall(self, x , y):                                        
        
        if 0 <= x < self.size and 0 <= y < self.size:              
            return x, y                                             
        else: return False

    def selectGoodNeighbors(self, x, y):                           
        
        neighbors = []                                                                                        
        for dir in self.direction:                                 
            if self.isWall((x + dir[0]), (y + dir[1])):           
                if self.grid[(x + dir[0])][(y + dir[1])] == 0:     
                    neighbors.append((x + dir[0], y + dir[1]))     
        return neighbors                                           
    
    def shuffleDirection(self, x, y):                              
        
        liNeighbors = self.selectGoodNeighbors(x, y)              
        if liNeighbors == False:                                   
            return False                                           
        random.shuffle(liNeighbors)                                
        return liNeighbors                                        
        
    def backtrackingRecursive(self, x ,y):                        
        # print(self.grid)                                           
        #                                                                                                        
        # input("continue")                                         
        posRandom = self.shuffleDirection(x, y)                    
        self.grid[x][y] = 1                                        
        for pos in posRandom:                                      
            if self.grid[pos[0]][pos[1]]: continue
            if pos[0] == x: self.hor[max(y, pos[1])][x] = "#."
            if pos[1] == y: self.ver[y][max(x, pos[0])] = ".."                                                      
            self.backtrackingRecursive(pos[0],pos[1])              
            
            #print(pos)                                            
        return x , y                                               
         
    def printMaze(self):                                          
        maze = ""
        for (a, b) in zip(self.hor, self.ver):
            maze += ''.join(a + ['\n'] + b + ['\n'])
        print("Labyrinthe génerée ")
        print("\n")
        # print(maze)

        return maze

"""
Class SolveMazeBacktracking
herite de la Class MazeBacktracking
resoud un labyrinthe avec l'algorithme backtracking o pour le chemin
et * pour les impasses
"""    
class SolveMazeBacktracking(MazeGenerator):
    def __init__(self, debug):
        self.debug = debug                                
        super().__init__()
        self.maze = np.zeros((self.size*2+1, self.size*2+1), dtype=int)
        self.start = (0, 1)
        self.end = (-1, -2)
        self.fillMaze = self.solveMazeRecusrive(self.start[0], self.start[1])
               
    def isLimit(self, x , y):                                             
        if 0 <= x < self.size*2+1 and 0 <= y < self.size*2+1:             
            return x, y                                            
        else: return False

    def fillMatrice(self):
        listChar = []
        for char in self.print:
            if char == "\n": continue
            listChar.append(char)       
        i = 0
        for x in range(len(self.maze)):
            for y in range(len(self.maze)):
                if listChar[i] == '#': self.maze[x][y] = 1
                i += 1

    def selectNeighbors(self, x, y):                                       
        neighbors = []                                                                                       
        for dir in self.direction:                                
            if self.isLimit((x + dir[0]), (y + dir[1])):            
                if self.maze[(x + dir[0])][(y + dir[1])] == 0:    
                    neighbors.append((x + dir[0], y + dir[1]))     
        return neighbors     

    def selectOldNeighbors(self, x, y):                                    
        Oldneighbors = []                                                                                     
        for dir in self.direction:                                
            if self.isLimit((x + dir[0]), (y + dir[1])):          
                if self.maze[(x + dir[0])][(y + dir[1])] != 0 and self.maze[(x + dir[0])][(y + dir[1])] != 1:   
                    Oldneighbors.append((x + dir[0], y + dir[1]))     
        return Oldneighbors     

    def setPath(self, x, y):
        old = self.selectOldNeighbors(x, y)
        if not old:
            self.maze[x][y] = 2
        elif self.maze[old[0][0]][old[0][1]] == -1:
            self.maze[x][y] = self.maze[old[0][0]][old[0][1]] + 3
        else:
            self.maze[x][y] = self.maze[old[0][0]][old[0][1]] + 1

    def findGoodPathRecursive(self, x, y):
        old = self.selectOldNeighbors(x, y)
        for ney in old:
            if (self.maze[x][y] -1) == self.maze[ney[0]][ney[1]]:
                if self.maze[ney[0]][ney[1]] == 2:
                    self.maze[ney[0]][ney[1]] = -7
                self.maze[x][y] = -7
                
                if self.debug == True:
                    # print(self.maze)
                    print(self.beautifulPrint())
                    time.sleep(0.1)
                    # input("Continue Good path ? ")
                self.findGoodPathRecursive(ney[0], ney[1])
        
    def solveMazeRecusrive(self, x, y):
        self.fillMatrice()
        self.setPath(x, y)
        if self.maze[x][y] == self.maze[self.end[0]][self.end[1]]:
            self.end = (x, y)
            self.findGoodPathRecursive(self.end[0], self.end[1])
            return 

        neighbors = self.selectNeighbors(x, y)
        random.shuffle(neighbors)
        
        if self.debug == True:
            # print(self.maze)
            print(self.beautifulPrint())
            time.sleep(0.1)
            # input("Recurse continue  ?")

        for ney in neighbors:
            self.solveMazeRecusrive(ney[0], ney[1])
            
            # if self.debug == True:
            #     print(self.maze)
            #     print(self.beautifulPrint())
            #     input("Backtrack continue ? ")
        
    def beautifulPrint(self):
        mazeString = ''
        for x in range(self.size*2+1):
            for y in range(self.size*2+1):
                if self.maze[x][y] == -7:
                    mazeString += ":green_square:"
                elif self.maze[x][y] == 1:
                    mazeString += ":black_large_square:"
                elif self.maze[x][y] == 0:
                    mazeString += ":white_large_square:"
                else:
                    mazeString += ":red_square:"
            mazeString += "\n"
        
        # print(mazeString)
        return mazeString


S1 = SolveMazeBacktracking(debug=True)
maze = S1.beautifulPrint()
