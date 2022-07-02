def recursiv(k):
    
    if k == 0:
        print(1)
        
    elif k < 0:
        return print(k)
    
    else:
        print(k)
        print("test")
        recursiv(k - 1)
        
    
k = int(input(" choose a number : "))
recursiv(k)