def main(width, height):
    x = '-'
    y = '|'
    free = ' '
    mur = y + (x * width) + y
    print(mur)
    for i in range(height -2):    
        print(y + ( free * width ) + y)
    print(mur)    
        

if __name__ == "__main__":
    main(10, 3)