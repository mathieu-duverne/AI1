def draw_triangle(height):
    
    x = "/"
    q = "\\"
    w = "_"
    free = " "
    base = free * height
    print(base, x ,q)
    
    h = 1
    for y in range(height - 1):
        
        base = free * (height - h)
        ecart = free * (y + h)
        
        if (h+ 1) == height:
            print(base, x , w * (y + h ), q)
            
        else:
            print(base, x , ecart, q)
        h +=1
    
draw_triangle(4)