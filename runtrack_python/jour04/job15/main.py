import numpy as np
def maze():
    with open("jour04\job15\maze.mz") as textFile:  
        lines = [line.split() for line in textFile]
    return lines

start = ()
def recursiv(k):
    pass

def bestPath():
    data = maze()
    

def makeMatrix():
    data = maze()
    li = []
    for x in data:
       for i in x:
           print(i[0][0])
makeMatrix()