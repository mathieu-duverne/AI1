
import numpy as np
import random

class Board:
    def __init__(self, i, j):
        self.hauteur = i
        self.largeur = j
        self.board = np.zeros( (i, j), dtype=str)
    
    def printB(self):
        return print(self.board)

    def isfree(self, height, width):
        return True if self.board[height][width] != ''  else False

    def getPossibleMove(self):
        
        possibleMoves = []
        for x in range(self.hauteur):
            for y in range(self.largeur):
                if self.board[x][y] == "":
                    possibleMoves.append((y))
                                
        return possibleMoves
    
        
    def randomize(self):
        pos = random.sample(range(self.largeur - 1), 1)[0]
        li = self.getPossibleMove()
        if pos in li:
            return pos
        else:
            self.randomize()
    
    def insertLetter(self, letter, pos):
        
            for x in range(self.largeur):
                
                if pos == x:
                    
                    for y in range(self.hauteur):
                        
                        if self.board[y][pos] == "J" or self.board[y][pos] == "R":
                            self.board[y-1][pos] = letter
                            return self.board   
                    
                        elif y == (self.hauteur - 1):
                            self.board[y][pos] = letter
                            return self.board
            
                        
    def winner(self, letter):
        
        for x in range(self.hauteur):
            
            for y in range(self.largeur):
                
                    if self.board[x][y] == letter:
                        
                        if (x + 3) <= (self.hauteur - 1):
                            if self.board[x + 1][y] == letter and self.board[x + 2][y] == letter and self.board[x + 3 ][y] == letter:
                                return letter
                            
                        if (y + 3) <= (self.largeur - 1):
                            if self.board[x][y] == letter and self.board[x][y + 1] == letter and self.board[x][y + 2] == letter and self.board[x][y + 3] == letter:
                                return letter   
                                        
                        if (y + 3) <= (self.largeur - 1) and (x + 3) <= (self.hauteur - 1):
                            if self.board[x][y] == letter and self.board[x + 1][y + 1] == letter and self.board[x + 2][y + 2] == letter and self.board[x + 3][y + 3] == letter:
                                return letter
                            
                        if (y - 3) <= (self.largeur - 1) and (x + 3) <= (self.hauteur - 1):
                            if self.board[x][y] == letter and self.board[x + 1][y - 1] == letter and self.board[x + 2][y - 2] == letter and self.board[x + 3][y - 3] == letter:
                                return letter
        return False
    

    def rules(self):
        letter = "J"
        for x in range(self.hauteur):
            for y in range(self.largeur):
                if self.board[x][y] == letter:

                        if (x - 3) >= 0:
                            # -- regle sur la hauteur si 3 aligné un au dessus
                            if self.board[x][y] == letter and self.board[x - 1][y] == letter and self.board[x - 2][y] == letter:
                                if not self.isfree( (x-3), y ):
                                    return y
                            
                        if (y + 3) <= (self.largeur - 1):
                            if self.board[x][y] == letter and self.board[x][y + 1] == letter and self.board[x][y + 2] == letter:
                                
                                if (x - 1) >= 0:
                                    # si libre la ou on contre et en dessous pas libre sinon next tour opposant win
                                    if not self.isfree( x, (y + 3) ) and self.isfree((x - 1), y) == False:
                                        print("sisi")
                                        return (y+3)
                                else:
                                    if not self.isfree( x, (y + 3) ):
                                        return (y+3)

                        if (y - 1) >= 0 and (y + 2) <= (self.largeur - 1):
                            # -- regle 3 aligné en largeur
                            if self.board[x][y] == letter and self.board[x][y + 1] == letter and self.board[x][y + 2] == letter:
                                if x == (self.hauteur - 1):
                                    # si libre un en arriere et que tout en bas if au dessus
                                    if not self.isfree( x, (y - 1) ):
                                        print("sisi")
                                        return (y-1)
                                else:
                                    # si y - 1 libre tjr et x- 1 pas libre empile et contre sinon pose pas
                                    if not self.isfree( x, (y - 1) ) and self.isfree((x - 1), y):
                                        return (y-1)
        return False
    
    
    def game(self,iter):

        if iter%2==0:
            pos = int(input("Choose number : "))
            letter = 'J'
            self.insertLetter(letter, pos)
            if self.winner(letter) == 'J':
                print("player " + letter + " won")
                self.printB()
                return
            
            self.printB()
            iter += 1
            self.game(iter)
                
        else:
            letter = 'R'
            pos = self.rules()
            if pos != False:
                print("rules")
                self.insertLetter(letter, pos)
            else:
                print("random")
                randomPos = self.randomize()
                self.insertLetter(letter, randomPos)
                
    
            if self.winner(letter) == 'R':
                print("player " + letter + " won")
                return
            pos = self.randomize()
            print(pos)
            
            self.printB()
            iter += 1
            self.game(iter)
                
                
class AI_one(Board):
    
    def __init__(self, i, j):
        self.hauteur = i
        self.largeur = j
        self.board = np.zeros( (i, j), dtype=str)
        self.Game = self.game(iter=2)
        super().__init__(i, j)
    
    
    
    def think(self, board, player):
        pass
        
    
AI_one(5, 10)




        