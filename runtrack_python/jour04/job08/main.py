import numpy as np

class Board:
    
    def __init__(self, hauteur, largeur):
        self.hauteur = hauteur
        self.largeur = largeur
        self.board = np.zeros( (hauteur, largeur), dtype=str)
    
    def isFree(self):
        for i in range(self.hauteur):
            for j in range(self.largeur):
                
                if self.board[j][i] != 'O' and self.board[j][i] != 'X':
                    return (j, i)

    def isDone(self):
        count = 0
        for x in range(self.hauteur):
            for y in range(self.largeur):
                if self.board[x][y] == "":
                    count += 1
        return count
            
            
    def play(self, k):

        # -- double condition arret function recursive
        if self.isDone() == False:
            print("last state")
            return self.board
        if k == 0:
            return self.board

        # init premiere dame
        if self.board[0][0] != "X":
            self.board[0][0] = "X"
            self.bloque()
            print("FIRST STATE")
            print(self.board)
            print("----------------")
            print("")
            self.play(k)
        

        elif k > 0:
            pos = self.isFree()            
            self.board[pos[0]][pos[1]] = "X"
            self.bloque()
            k = k -1
            print(" ")
            print(self.board)
            print("----------------")
            print(" ")

            self.play(k)
            
    
    def bloque(self):

        liImpossibleMove = []    
        for x in range(self.hauteur):
            for y in range(self.largeur):
                
                if self.board[x][y] == "X":
                    
                    for p in range(self.hauteur):
                        
                        if p == 0:
                            p += 1
                        # remplissage diagonale +1 \ +1
                        if((p + x) <= (self.hauteur-1)) and ((p + y) <= (self.largeur-1)):
                            liImpossibleMove.append( ( (x+p) ,(y+p) ) )
                            self.board[x + p][y + p] = "O"
                            
                        # remplissage diagonale -1 \ -1 
                        if((x - p) >= 0 and (y - p) >= 0):
                            liImpossibleMove.append( ( (x-p) ,(y-p) ) )
                            self.board[(x - p)][(y - p)] = "O"

                        # remplissage diagonale -1 / +1 
                        if((x - p) >= 0 and (y + p) <= (self.largeur-1) ):
                            liImpossibleMove.append( ( (x-p) ,(y+p) ) )
                            self.board[(x - p)][(y + p)] = "O"

                        # remplissage diagonale x +1 / y -1 
                        if((x + p) <= (self.hauteur-1) and (y - p) >= 0):
                            liImpossibleMove.append( ( (x+p) ,(y-p) ) )
                            self.board[(x + p)][(y - p)] = "O"

                        # remplissage par la droite +1 x
                        if ((p + x) <= (self.hauteur -1)):
                            liImpossibleMove.append( ( x+p , y ) )
                            self.board[x+p][y] = "O"
                        
                        # remplissage descente +1 y
                        if ((p+y) <= (self.largeur-1)):
                            liImpossibleMove.append( ( x , y+p ) )
                            self.board[x][y+p] = "O"
                        
                        # remplissage par la droite -1 x
                        if ((x - p) >= 0):
                            liImpossibleMove.append( ( x-p , y ) )
                            self.board[(x-p)][y] = "O"
                        
                        # remplissage monter -1 y
                        if ((y - p) >= 0):
                            liImpossibleMove.append( ( x , y-p ) )
                            self.board[x][(y-p)] = "O"
                        
                        
                   
nbr = int(input('choose a number : '))                
B1 = Board(nbr, nbr)
result = B1.play(k=(nbr))