def recursiv(k):
    
    if k == 0:
        print(1)
        return
    if k == 1:
        print(2)
        return
    
    if k > 0:
        print(2)
        recursiv(k -1)
        
        
        



k = int(input('choose a number : '))
recursiv(k)