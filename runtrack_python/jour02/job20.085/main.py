import numpy as np

class Board:
    def __init__(self, i, j):
        self.hauteur = i
        self.largeur = j
        self.board = np.zeros( (i, j), dtype=str)
         
    def createBoard(self, i, j):
        board = []
        for x in range(i):
            board.append("O")
            for y in range(j):
                board.append("X")
        return board
    
    
    def getPossibleMove(self):
        possibleMoves = []
        for x in range(self.hauteur):
            for y in range(self.largeur):
                if self.board[x][y] == "":
                    possibleMoves.append((x, y))
        return possibleMoves
    
    
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
                        
                        
    def printB(self):
        return print(self.board)
    
    def game(self,iter):
        
        pos = int(input("Choose number : "))
        
        if iter%2==0:
            letter = 'J'
            self.insertLetter(letter, pos)
            self.printB()
            iter += 1
            self.game(iter)
        else:
            letter = 'R'
            self.insertLetter(letter, pos)
            self.printB()
            iter += 1
            self.game(iter)

        
        
B1 = Board(5, 11)
# p = B1.getPossibleMove()
p =  B1.game(iter=2)
print("------------------------")
print("------------------------")
print(p)
