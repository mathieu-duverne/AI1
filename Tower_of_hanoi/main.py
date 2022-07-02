def towerOfHanoi(n, start, target, aux):

    if n != 0:
        towerOfHanoi(n - 1, start, aux, target)
        print(str(start) + " -> " + str(target))
        towerOfHanoi(n - 1, aux, target, start)
        

n = int(input("give a number of pieces to move : "))
nbrParam = int(input("give a number of sticks : "))
towerOfHanoi(4, 1, 2, 3)